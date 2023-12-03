#!/usr/bin/python3

import os
import requests
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style
from os import name, system

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

class PHPUnitChecker:
    def __init__(self):
        self.user_agent = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0"
        }
        self.vendor_paths = [
            "/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/api/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/yii/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/laravel/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/laravel52/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/lib/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/zend/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/assets/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/asset/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/dist/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/public/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/tests/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/plugin/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/admin/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/dashboard/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/administrator/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/api1/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/home/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/bower/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/data/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/vendors/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/local/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/test/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/shop/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/wp-content/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/system/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/inc/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/core/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/includes/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/libs/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/app/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/application/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/sys/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/www/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/src/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/cms/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/web/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/site/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/config/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/plugins/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/temp/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/modules/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/ext/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/includes/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/webroot/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/shared/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/wwwroot/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/uploads/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/media/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/blog/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/cgi-bin/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/tools/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/scripts/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/backup/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/assets/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/temp/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/includes/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/core/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/modules/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/temp/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/app/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/web/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/public/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/site/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/config/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/temp/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/plugins/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/api/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/libs/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/ext/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/includes/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/system/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/application/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/webroot/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/modules/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/shared/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/wwwroot/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/uploads/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/media/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/www/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/blog/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/cgi-bin/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/data/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/tools/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/scripts/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/backup/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/includes/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/assets/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/core/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/modules/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/temp/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/app/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/web/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/public/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/site/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/config/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/temp/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/plugins/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/api/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/libs/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/ext/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/includes/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/system/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/application/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/webroot/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/modules/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/shared/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/wwwroot/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/uploads/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/media/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/www/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/blog/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/cgi-bin/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/data/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/tools/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/scripts/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/backup/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/includes/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/assets/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/core/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/modules/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/temp/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/app/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/web/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/public/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/site/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/config/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/temp/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/plugins/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/api/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/libs/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/ext/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/includes/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/system/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/application/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/webroot/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/modules/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/shared/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/wwwroot/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/uploads/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/media/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/www/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/blog/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/cgi-bin/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/data/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/tools/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/scripts/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/backup/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/includes/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/assets/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/core/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/modules/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/temp/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/app/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/web/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/public/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/site/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/config/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/temp/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/plugins/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/api/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/libs/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/ext/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/includes/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/system/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/application/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/webroot/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/modules/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/shared/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/wwwroot/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/uploads/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/media/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/www/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/blog/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/cgi-bin/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/data/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/tools/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/scripts/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/backup/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/includes/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/laravel/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/admin/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/app/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/application/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/dashboards/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/api/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/test/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/shop/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/author/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/index/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/main/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php"
        ]

    def clear_screen(self):
        if name == "nt":
            system("cls")
        else:
            system("clear")

    def check_phpunit(self, website):
        try:
            for vendor_path in self.vendor_paths:
                url = f"{website}{vendor_path}"
                response = requests.get(url, timeout=10, headers=self.user_agent, verify=False)
                if response.status_code == 200 and not response.text.strip():
                    full_path = f"{website}{vendor_path}"
                    print(Fore.GREEN + f"[!] {website} => PHPUNIT FOUND! [ {full_path} ]" + Style.RESET_ALL)
                    result_path = os.path.join("results", "phpunit.txt")
                    with open(result_path, "a") as ap:
                        ap.write(full_path + "\n")
                    break  # No need to check other paths if PHPUnit is found
            else:
                print(f"[!] {website} PHPUNIT NOT FOUND!")
        except requests.RequestException:
            pass

    def main(self):
        print("PHPUNIT CHECKER [ MadExploits ]")
        lists = input("LIST : ")
        with open(lists, "r") as file:
            websites = filter(None, map(str.strip, file))
            with ThreadPoolExecutor(max_workers=120) as executor:
                executor.map(self.check_phpunit, websites)

if __name__ == "__main__":
    phpunit_checker = PHPUnitChecker()
    phpunit_checker.clear_screen()

    # Ensure the "results" folder exists
    if not os.path.exists("results"):
        os.makedirs("results")

    phpunit_checker.main()
