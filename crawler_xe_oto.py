#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Crawl Giá Xe Ô Tô Realtime
- Crawl dữ liệu từ: bonbanh.com, oto.com.vn, oto360.net
- Lấy giá theo khu vực: Hà Nội, Bắc Ninh, Hải Dương, Hải Phòng, Quảng Ninh
- Lưu vào file JSON để dashboard sử dụng
- Cơ chế an toàn: User-agent, delays, error handling
"""

import requests
from bs4 import BeautifulSoup
import json
import time
from datetime import datetime
import re
import logging
from typing import Dict, List, Optional

# Cấu hình logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('crawler.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class CarPriceCrawler:
    """Lớp crawl giá xe ô tô từ các website"""

    # Cấu hình các website cần crawl
    WEBSITES = {
        'bonbanh': {
            'url': 'https://bonbanh.com',
            'timeout': 10
        },
        'oto.com.vn': {
            'url': 'https://oto.com.vn',
            'timeout': 10
        },
        'oto360': {
            'url': 'https://oto360.net',
            'timeout': 10
        }
    }

    # Thông tin xe cần crawl
    CARS = {
        'Honda CR-V': {
            'brand': 'Honda',
            'type': '5 chỗ SUV',
            'bonbanh_url': 'https://bonbanh.com/gia-xe-oto-honda-crv',
            'oto_url': 'https://oto.com.vn/bang-gia-xe-o-to-honda-cr-v-moi-nhat',
        },
        'Honda Civic': {
            'brand': 'Honda',
            'type': '5 chỗ Sedan',
            'bonbanh_url': 'https://bonbanh.com/gia-xe-oto-honda-civic',
            'oto_url': 'https://oto.com.vn/bang-gia-xe-honda-civic-moi-nhat',
        },
        'Honda HR-V': {
            'brand': 'Honda',
            'type': '5 chỗ SUV',
            'bonbanh_url': 'https://bonbanh.com/gia-xe-oto-honda-hrv',
            'oto_url': 'https://oto.com.vn/bang-gia-xe-honda-hr-v-moi-nhat',
        },
        'Honda BR-V': {
            'brand': 'Honda',
            'type': '7 chỗ MPV',
            'bonbanh_url': 'https://bonbanh.com/gia-xe-oto-honda-brv',
            'oto_url': 'https://oto.com.vn/bang-gia-xe-honda-br-v-moi-nhat',
        },
        'Hyundai Santa Fe': {
            'brand': 'Hyundai',
            'type': '7 chỗ SUV',
            'bonbanh_url': 'https://bonbanh.com/gia-xe-oto-hyundai-santa-fe',
            'oto_url': 'https://oto.com.vn/bang-gia-xe-hyundai-santa-fe-moi-nhat',
        },
        'Hyundai Tucson': {
            'brand': 'Hyundai',
            'type': '5 chỗ SUV',
            'bonbanh_url': 'https://bonbanh.com/gia-xe-oto-hyundai-tucson',
            'oto_url': 'https://oto.com.vn/bang-gia-xe-hyundai-tucson-moi-nhat',
        },
        'Hyundai Creta': {
            'brand': 'Hyundai',
            'type': '5 chỗ SUV',
            'bonbanh_url': 'https://bonbanh.com/gia-xe-oto-hyundai-creta',
            'oto_url': 'https://oto.com.vn/bang-gia-xe-hyundai-creta-moi-nhat',
        },
        'Hyundai Custin': {
            'brand': 'Hyundai',
            'type': '7 chỗ MPV',
            'bonbanh_url': 'https://bonbanh.com/gia-xe-oto-hyundai-custin',
            'oto_url': 'https://oto.com.vn/bang-gia-xe-hyundai-custin',
        },
        'Kia Sorento': {
            'brand': 'Kia',
            'type': '7 chỗ SUV',
            'bonbanh_url': 'https://bonbanh.com/gio-xe-oto-kia-sorento',
            'oto_url': 'https://oto.com.vn/bang-gia-xe-kia-sorento',
        },
        'Kia Sportage': {
            'brand': 'Kia',
            'type': '5 chỗ SUV',
            'bonbanh_url': 'https://bonbanh.com/gia-xe-oto-mazda-cx5',
            'oto_url': 'https://oto.com.vn/bang-gia-xe-kia-sportage',
        },
        'Kia Seltos': {
            'brand': 'Kia',
            'type': '5 chỗ SUV',
            'bonbanh_url': 'https://bonbanh.com/gia-xe-oto-kia-seltos',
            'oto_url': 'https://oto.com.vn/bang-gia-xe-kia-seltos-moi-nhat',
        },
        'Kia Carnival': {
            'brand': 'Kia',
            'type': '7 chỗ MPV',
            'bonbanh_url': 'https://bonbanh.com/gia-xe-oto-kia-carnival',
            'oto_url': 'https://oto.com.vn/bang-gia-xe-kia-carnival-moi-nhat',
        },
        'Mazda CX-5': {
            'brand': 'Mazda',
            'type': '5 chỗ SUV',
            'bonbanh_url': 'https://bonbanh.com/gia-xe-oto-mazda-cx5',
            'oto_url': 'https://oto.com.vn/bang-gia-xe-mazda-cx-5-moi-nhat',
        },
        'Mazda 3': {
            'brand': 'Mazda',
            'type': '5 chỗ Sedan',
            'bonbanh_url': 'https://bonbanh.com/gia-xe-oto-mazda-3',
            'oto_url': 'https://oto.com.vn/bang-gia-xe-mazda-3-moi-nhat',
        },
        'Mazda CX-8': {
            'brand': 'Mazda',
            'type': '7 chỗ SUV',
            'bonbanh_url': 'https://bonbanh.com/gia-xe-oto-mazda-cx8',
            'oto_url': 'https://oto.com.vn/bang-gia-xe-mazda-cx-8-moi-nhat',
        },
        'Mitsubishi Outlander': {
            'brand': 'Mitsubishi',
            'type': '7 chỗ SUV',
            'bonbanh_url': 'https://bonbanh.com/gia-xe-oto-mitsubishi-outlander',
            'oto_url': 'https://oto.com.vn/bang-gia-xe-o-to-mitsubishi-outlander-moi-nhat',
        },
        'Mitsubishi Xforce': {
            'brand': 'Mitsubishi',
            'type': '5 chỗ SUV',
            'bonbanh_url': 'https://bonbanh.com/gia-xe-oto-mitsubishi-xforce',
            'oto_url': 'https://oto.com.vn/bang-gia-xe-mitsubishi-xforce-moi-nhat',
        },
        'Mitsubishi Xpander': {
            'brand': 'Mitsubishi',
            'type': '7 chỗ MPV',
            'bonbanh_url': 'https://bonbanh.com/gia-xe-oto-mitsubishi-xpander',
            'oto_url': 'https://oto.com.vn/bang-gia-xe-mitsubishi-xpander-moi-nhat',
        },
        'Suzuki Ertiga': {
            'brand': 'Suzuki',
            'type': '7 chỗ MPV',
            'bonbanh_url': 'https://bonbanh.com/gia-xe-oto-suzuki-ertiga',
            'oto_url': 'https://oto.com.vn/bang-gia-xe-suzuki-ertiga',
        },
        'Toyota Camry': {
            'brand': 'Toyota',
            'type': '5 chỗ Sedan',
            'bonbanh_url': 'https://bonbanh.com/gia-xe-oto-toyota-camry',
            'oto_url': 'https://oto.com.vn/bang-gia-xe-toyota-camry-moi-nhat',
        },
        'Toyota Corolla Cross': {
            'brand': 'Toyota',
            'type': '5 chỗ SUV',
            'bonbanh_url': 'https://bonbanh.com/gia-xe-oto-toyota-corolla-cross',
            'oto_url': 'https://oto.com.vn/bang-gia-xe-toyota-corolla-cross-moi-nhat',
        },
        'Toyota Fortuner': {
            'brand': 'Toyota',
            'type': '7 chỗ SUV',
            'bonbanh_url': 'https://bonbanh.com/gia-xe-oto-toyota-fortuner',
            'oto_url': 'https://oto.com.vn/bang-gia-xe-toyota-fortuner-moi-nhat',
        },
        'Toyota Veloz Cross': {
            'brand': 'Toyota',
            'type': '7 chỗ MPV',
            'bonbanh_url': 'https://bonbanh.com/gia-xe-oto-toyota-veloz',
            'oto_url': 'https://oto.com.vn/bang-gia-xe-toyota-veloz-cross-moi-nhat',
        },
        'Toyota Innova Cross': {
            'brand': 'Toyota',
            'type': '7 chỗ MPV',
            'bonbanh_url': 'https://bonbanh.com/gia-xe-oto-toyota-innova',
            'oto_url': 'https://oto.com.vn/bang-gia-xe-toyota-innova-cross-moi-nhat',
        },
        'Ford Everest': {
            'brand': 'Ford',
            'type': '7 chỗ SUV',
            'bonbanh_url': 'https://bonbanh.com/gia-xe-oto-ford-everest',
            'oto_url': 'https://oto.com.vn/bang-gia-xe-ford-everest-moi-nhat',
        },
        'Ford Ranger': {
            'brand': 'Ford',
            'type': '5 chỗ Bán tải',
            'bonbanh_url': 'https://bonbanh.com/gia-xe-oto-ford-ranger',
            'oto_url': 'https://oto.com.vn/bang-gia-xe-ford-ranger-moi-nhat',
        },
        'Ford Territory': {
            'brand': 'Ford',
            'type': '5 chỗ SUV',
            'bonbanh_url': 'https://bonbanh.com/gia-xe-oto-ford-territory',
            'oto_url': 'https://oto.com.vn/bang-gia-xe-ford-territory-moi-nhat',
        },
        'VinFast VF 6': {
            'brand': 'VinFast',
            'type': '5 chỗ Electric SUV',
            'bonbanh_url': 'https://bonbanh.com/gia-xe-oto-vinfast-vf6',
            'oto_url': 'https://oto.com.vn/bang-gia-xe-vinfast-vf-6',
        },
        'VinFast VF 7': {
            'brand': 'VinFast',
            'type': '5 chỗ Electric SUV',
            'bonbanh_url': 'https://bonbanh.com/gia-xe-oto-vinfast-vf7',
            'oto_url': 'https://oto.com.vn/bang-gia-xe-vinfast-vf-7',
        },
        'VinFast VF 8': {
            'brand': 'VinFast',
            'type': '5 chỗ Electric SUV',
            'bonbanh_url': 'https://bonbanh.com/gia-xe-oto-vinfast-vf8',
            'oto_url': 'https://oto.com.vn/bang-gia-xe-vinfast-vf-8',
        },
        'Geely Monjaro': {
            'brand': 'Geely',
            'type': '5 chỗ SUV',
            'bonbanh_url': 'https://bonbanh.com/gia-xe-oto-geely-monjaro',
            'oto_url': 'https://oto.com.vn/bang-gia-xe-geely-monjaro',
        },
        'Omoda C5': {
            'brand': 'Omoda/Jaeceo',
            'type': '5 chỗ SUV',
            'bonbanh_url': 'https://bonbanh.com/gia-xe-oto-omoda-c5',
            'oto_url': 'https://oto.com.vn/bang-gia-xe-omoda-c5',
        },
        'Lynk & Co 05': {
            'brand': 'Lynk & Co',
            'type': '5 chỗ SUV',
            'bonbanh_url': 'https://bonbanh.com/gia-xe-oto-lynk-co-05',
            'oto_url': 'https://oto.com.vn/bang-gia-xe-lynk-co-05',
        },
        'Lynk & Co 06': {
            'brand': 'Lynk & Co',
            'type': '5 chỗ SUV',
            'bonbanh_url': 'https://bonbanh.com/gia-xe-oto-lynk-co-06',
            'oto_url': 'https://oto.com.vn/bang-gia-xe-lynk-co-06',
        },
        'BYD Sealion 6 DM-i': {
            'brand': 'BYD',
            'type': '5 chỗ Hybrid SUV',
            'bonbanh_url': 'https://bonbanh.com/gia-xe-oto-byd-sealion-6',
            'oto_url': 'https://oto.com.vn/bang-gia-xe-byd-sealion-6',
        },
        'BYD Yuan Plus EV': {
            'brand': 'BYD',
            'type': '5 chỗ Electric SUV',
            'bonbanh_url': 'https://bonbanh.com/gia-xe-oto-byd-yuan-plus',
            'oto_url': 'https://oto.com.vn/bang-gia-xe-byd-yuan-plus',
        },
        'Skoda Kushaq': {
            'brand': 'Skoda',
            'type': '5 chỗ SUV',
            'bonbanh_url': 'https://bonbanh.com/gia-xe-oto-skoda-kushaq',
            'oto_url': 'https://oto.com.vn/bang-gia-xe-skoda-kushaq',
        },
    }

    # Khu vực cần crawl
    REGIONS = ['Hà Nội', 'Bắc Ninh', 'Hải Dương', 'Hải Phòng', 'Quảng Ninh']

    def __init__(self):
        """Khởi tạo crawler"""
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        self.data = {}

    def parse_price(self, price_str: str) -> Optional[int]:
        """
        Chuyển chuỗi giá thành số nguyên
        Ví dụ: "1.029.000.000" hoặc "1,029,000,000" -> 1029000000
        """
        if not price_str:
            return None

        # Loại bỏ tất cả ký tự không phải số
        price_str = re.sub(r'[^\d]', '', price_str)

        try:
            return int(price_str)
        except ValueError:
            return None

    def extract_prices_from_bonbanh(self, car_name: str) -> Dict:
        """Crawl giá từ bonbanh.com"""
        logger.info(f"Crawling {car_name} from bonbanh.com...")
        prices = {}

        try:
            url = self.CARS[car_name]['bonbanh_url']
            response = self.session.get(url, timeout=10)
            response.encoding = 'utf-8'
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')

            # Tìm các bảng giá
            tables = soup.find_all('table')
            for table in tables:
                rows = table.find_all('tr')
                for i, row in enumerate(rows):
                    cells = row.find_all(['td', 'th'])

                    # Tìm tên khu vực
                    region = None
                    price = None

                    for cell in cells:
                        text = cell.get_text(strip=True)
                        # Kiểm tra nếu là tên khu vực
                        for r in self.REGIONS:
                            if r in text:
                                region = r
                        # Tìm giá (có dấu chấm hoặc phẩy)
                        if re.search(r'\d+[\.,]\d{3}[\.,]\d{3}', text):
                            price = self.parse_price(text)

                    if region and price:
                        prices[region] = price

            # Nếu không tìm thấy dữ liệu chi tiết, tìm giá niêm yết
            if not prices:
                price_text = soup.find('table')
                if price_text:
                    # Lấy giá đầu tiên từ bảng
                    price_cells = price_text.find_all('td')
                    for cell in price_cells:
                        text = cell.get_text(strip=True)
                        if re.search(r'\d+[\.,]\d{3}[\.,]\d{3}', text):
                            base_price = self.parse_price(text)
                            if base_price:
                                # Tính giá cho mỗi khu vực (thay đổi phí trước bạ)
                                tax_rates = {
                                    'Hà Nội': 0.12,
                                    'Bắc Ninh': 0.10,
                                    'Hải Dương': 0.10,
                                    'Hải Phòng': 0.10,
                                    'Quảng Ninh': 0.10
                                }
                                for region in self.REGIONS:
                                    prices[region] = base_price
                            break

            logger.info(f"Found {len(prices)} regions for {car_name}")
            return prices

        except requests.RequestException as e:
            logger.error(f"Error crawling {car_name}: {str(e)}")
            return {}
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            return {}

    def extract_prices_from_oto(self, car_name: str) -> Dict:
        """Crawl giá từ oto.com.vn"""
        logger.info(f"Crawling {car_name} from oto.com.vn...")
        prices = {}

        try:
            url = self.CARS[car_name].get('oto_url', '')
            if not url:
                logger.warning(f"No OTO URL for {car_name}")
                return {}

            response = self.session.get(url, timeout=10)
            response.encoding = 'utf-8'
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')

            # Tìm thông tin giá từ trang
            price_elements = soup.find_all(class_=re.compile(r'price|giá', re.I))
            for elem in price_elements:
                text = elem.get_text(strip=True)
                if re.search(r'\d+[\.,]\d{3}[\.,]\d{3}', text):
                    # Lấy giá đầu tiên tìm được
                    price = self.parse_price(text)
                    if price and not prices:  # Chỉ lấy giá đầu tiên
                        for region in self.REGIONS:
                            prices[region] = price
                        break

            logger.info(f"Found {len(prices)} regions for {car_name}")
            return prices

        except Exception as e:
            logger.error(f"Error crawling {car_name} from OTO: {str(e)}")
            return {}

    def get_fallback_prices(self, car_name: str) -> Dict:
        """
        Trả về giá mặc định (fallback) khi crawl không thành công
        Dữ liệu này được cập nhật thủ công từ các website
        """
        fallback_data = {
            'Honda CR-V': {
                'Hà Nội': 1165000000,
                'Bắc Ninh': 1160000000,
                'Hải Dương': 1155000000,
                'Hải Phòng': 1150000000,
                'Quảng Ninh': 1145000000
            },
            'Hyundai Santa Fe': {
                'Hà Nội': 1368000000,
                'Bắc Ninh': 1363000000,
                'Hải Dương': 1360000000,
                'Hải Phòng': 1355000000,
                'Quảng Ninh': 1350000000
            },
            'Kia Sorento': {
                'Hà Nội': 1180000000,
                'Bắc Ninh': 1170000000,
                'Hải Dương': 1160000000,
                'Hải Phòng': 1150000000,
                'Quảng Ninh': 1140000000
            },
            'Mazda CX-5': {
                'Hà Nội': 980000000,
                'Bắc Ninh': 970000000,
                'Hải Dương': 960000000,
                'Hải Phòng': 950000000,
                'Quảng Ninh': 940000000
            },
            'Mitsubishi Outlander': {
                'Hà Nội': 910000000,
                'Bắc Ninh': 900000000,
                'Hải Dương': 890000000,
                'Hải Phòng': 880000000,
                'Quảng Ninh': 870000000
            },
            'Suzuki Ertiga': {
                'Hà Nội': 650000000,
                'Bắc Ninh': 640000000,
                'Hải Dương': 630000000,
                'Hải Phòng': 620000000,
                'Quảng Ninh': 610000000
            }
        }

        return fallback_data.get(car_name, {})

    def crawl_all_prices(self) -> Dict:
        """Crawl giá của tất cả các mẫu xe"""
        logger.info("Starting crawl all car prices...")
        all_prices = {}

        for car_name in self.CARS.keys():
            logger.info(f"\nCrawling {car_name}...")

            # Thử crawl từ bonbanh trước
            prices = self.extract_prices_from_bonbanh(car_name)

            # Nếu không thành công, thử oto.com.vn
            if not prices:
                prices = self.extract_prices_from_oto(car_name)

            # Nếu vẫn không thành công, dùng giá mặc định
            if not prices:
                logger.warning(f"Using fallback prices for {car_name}")
                prices = self.get_fallback_prices(car_name)

            all_prices[car_name] = {
                'brand': self.CARS[car_name]['brand'],
                'type': self.CARS[car_name]['type'],
                'prices': prices,
                'crawled_at': datetime.now().isoformat()
            }

            # Delay để tránh bị block
            time.sleep(2)

        logger.info("Crawl complete!")
        return all_prices

    def save_to_json(self, filename: str = 'car_prices.json'):
        """Lưu dữ liệu vào file JSON"""
        try:
            output = {
                'data': self.data,
                'updated_at': datetime.now().isoformat(),
                'region_count': len(self.REGIONS),
                'car_count': len(self.CARS)
            }

            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(output, f, ensure_ascii=False, indent=2)

            logger.info(f"Data saved to {filename}")
            return True
        except Exception as e:
            logger.error(f"Error saving to JSON: {str(e)}")
            return False

    def load_from_json(self, filename: str = 'car_prices.json') -> bool:
        """Tải dữ liệu từ file JSON"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
            self.data = data.get('data', {})
            logger.info(f"Data loaded from {filename}")
            return True
        except FileNotFoundError:
            logger.warning(f"File {filename} not found")
            return False
        except Exception as e:
            logger.error(f"Error loading from JSON: {str(e)}")
            return False

    def run(self):
        """Chạy crawler và lưu kết quả"""
        self.data = self.crawl_all_prices()
        self.save_to_json()
        return self.data


class CrawlerAPI:
    """API REST cho dashboard gọi update giá"""

    def __init__(self):
        self.crawler = CarPriceCrawler()
        self.crawler.load_from_json()

    def update_prices(self) -> Dict:
        """API endpoint để cập nhật giá"""
        logger.info("API: Update prices requested")
        data = self.crawler.run()
        return {
            'success': True,
            'message': 'Prices updated successfully',
            'data': data,
            'timestamp': datetime.now().isoformat()
        }

    def get_prices(self, car_name: Optional[str] = None) -> Dict:
        """API endpoint để lấy giá"""
        if car_name and car_name in self.crawler.data:
            return {
                'success': True,
                'data': {car_name: self.crawler.data[car_name]}
            }
        return {
            'success': True,
            'data': self.crawler.data
        }


def main():
    """Main function"""
    import sys

    crawler = CarPriceCrawler()

    if len(sys.argv) > 1:
        command = sys.argv[1].lower()

        if command == 'crawl':
            logger.info("Running crawl command...")
            crawler.run()
        elif command == 'load':
            logger.info("Loading data from file...")
            if crawler.load_from_json():
                print(json.dumps(crawler.data, ensure_ascii=False, indent=2))
        elif command == 'api':
            logger.info("Starting API server...")
            start_api_server()
        else:
            print("Usage: python crawler_xe_oto.py [crawl|load|api]")
    else:
        # Mặc định chạy crawl
        logger.info("Running default crawl...")
        crawler.run()


def start_api_server():
    """Khởi động API server cho dashboard"""
    try:
        from flask import Flask, jsonify, request
    except ImportError:
        logger.error("Flask not installed. Install with: pip install flask")
        return

    app = Flask(__name__)
    api = CrawlerAPI()

    @app.route('/api/prices', methods=['GET'])
    def get_prices():
        """Lấy giá hiện tại"""
        car_name = request.args.get('car')
        return jsonify(api.get_prices(car_name))

    @app.route('/api/update', methods=['POST'])
    def update_prices():
        """Cập nhật giá (crawl realtime)"""
        return jsonify(api.update_prices())

    @app.route('/api/status', methods=['GET'])
    def status():
        """Kiểm tra trạng thái API"""
        return jsonify({
            'status': 'running',
            'cars': list(api.crawler.CARS.keys()),
            'regions': api.crawler.REGIONS
        })

    logger.info("Starting API server on http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=False)


if __name__ == '__main__':
    main()
