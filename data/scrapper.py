# from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from pathlib import Path
import os
import random
import sys


def getData(contents):
    # list items
    items = contents.findAll(
        "div",
        {"class": "ui-organism-intersection__element intersection-card-container"},
    )

    data = []
    for item in items:
        # print("halo", item)

        # get content wrapper
        wrapper = item.find("div", {"class": "card-featured__middle-section"})

        # to get item type
        badge = wrapper.find(
            "div", {"class": "card-featured__middle-section__header-badge"}
        ).findAll("div", recursive=False)

        if len(badge) == 2:
            type = badge[0].text
            status = badge[1].text
        else:
            type = badge[0].text
            status = ""

        price = wrapper.find("strong").text
        instalment = wrapper.find("em").text

        house_name = wrapper.find("h2").text

        location = wrapper.findAll("span")[1].text

        # get all the attributes
        features_wrapper = wrapper.find(
            "div", {"class": "card-featured__middle-section__attribute"}
        ).findAll("div")

        room_div = features_wrapper[0]

        # Find the main container div (adjust selector if needed)
        list_items = room_div.findAll(
            "div", {"class": "relative ui-molecules-list__item"}
        )

        # Initialize variables with default values (can be modified)
        bedroom_count = 0
        bathroom_count = 0
        carport_count = 0

        """
        <svg height="16px" viewbox="0 0 16 16" width="16px"><use fill="#677E8C" xlink:href="#rui-icon-bed-small"></use></svg>
        """

        # Loop through each list item
        for item in list_items:
            # Try to find the svg element within the item
            svg_element = item.find("svg")

            if svg_element:
                if "bed" in str(svg_element):
                    bedroom_count = int(
                        item.find("span", class_="attribute-text").text.strip()
                    )
                elif "bath" in str(svg_element):
                    bathroom_count = int(
                        item.find("span", class_="attribute-text").text.strip()
                    )
                elif "car" in str(svg_element):
                    carport_count = int(
                        item.find("span", class_="attribute-text").text.strip()
                    )

        land_area_info = features_wrapper[-2]
        building_area_info = features_wrapper[-1]

        land_area = land_area_info.find("span").text.strip()
        building_area = building_area_info.find("span").text.strip()

        data.append(
            (
                [
                    type,
                    status,
                    price,
                    instalment,
                    house_name,
                    location,
                    bedroom_count,
                    bathroom_count,
                    carport_count,
                    land_area,
                    building_area,
                ]
            )
        )
    return data


def scraper(url):
    try:
        # Configure WebDriver to use headless Firefox
        options = Options()
        options.add_argument("-headless")
        driver = webdriver.Firefox(options=options)

        # Get the URL given
        driver.get(url)

        try:
            wait = WebDriverWait(driver, timeout=15)
            wait.until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "ui-search-page__content")
                )
            )
        except:
            raise LookupError("There is no element specified")

        # BeautifulSoup will parse the URL
        content = driver.page_source
        soup = BeautifulSoup(content, "html.parser")

        data = getData(soup)

        # Close the WebDriver
        driver.quit()

        return data

    except Exception as e:
        # Print the error message
        print("An error occurred: ", e)

        # Close the WebDriver
        driver.quit()


def scrape_and_save(url, file_path):
    """
    Scrapes data from a single page, creates a DataFrame, and saves it to a CSV file.
    """
    try:
        data = scraper(url)
        df = pd.DataFrame(data)
        df.to_csv(file_path, index=False, header=False, mode="a", sep=",")
    except:
        if KeyboardInterrupt:
            # force stop
            sys.exit(0)
        else:
            pass


if __name__ == "__main__":
    # save results
    data_dir = Path("data")
    data_dir.mkdir(parents=True, exist_ok=True)

    results_dir = data_dir / "results"
    results_dir.mkdir(parents=True, exist_ok=True)

    results_dir = Path("data") / "results"

    results_dir.mkdir(parents=True, exist_ok=True)

    file_path = os.path.join(results_dir, "results.csv")

    # set first page index
    first_page = 1
    # set last page index

    results = []

    regions = [
        "andir",
        "astanaanyar",
        "antapani",
        "arcamanik",
        "babakanciparay",
        "bandung-kulon",
        "bandung-wetan",
        "batununggal",
        "bojongloa-kaler",
        "bojongloa-kidul",
        "buah-batu",
        "cibeunying-kaler",
        "cibeunying-kidul",
        "cibiru",
        "cicendo",
        "cidadap",
        "cinambo",
        "coblong",
        "gede-bage",
        "kiaracondong",
        "lengkong",
        "mandalajati",
        "panyileukan",
        "rancasari",
        "regol",
        "sukajadi",
        "sukasari",
        "sumurbandung",
        "ujungberung",
    ]

    for region in regions:
        # set random
        end_page = random.randint(10, 20)
        for page in range(first_page, end_page + 1):
            base_url = f"https://www.rumah123.com/jual/bandung/{region}/rumah/"
            # Define the URL
            url = f"{base_url}?page={page}"

            # scrape data and save
            scrape_and_save(url, file_path)

            print(f"Scraped page {page}. Data appended to {file_path}")
