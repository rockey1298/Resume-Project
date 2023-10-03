import requests
import csv
from bs4 import BeautifulSoup


# url = "https://secure.runescape.com/m=hiscore_oldschool/overall?table=0#headerHiscores"

# page = requests.get(url).text

# soup = BeautifulSoup(page, "html.parser")

# # print(soup.prettify)

# soup_anchors = soup.find_all("a")

# # soup_anchors.select('a[href*=hiscorepersonal?user1]')

# user_links = soup.find_all(
#     "a", href=lambda href: href and href.startswith("hiscorepersonal?user1=")
# )

# user_data = []

# page_number = 1

# base_url = "https://secure.runescape.com/m=hiscore_oldschool/overall?table=0&page="

# while page_number < 10:
#     url = base_url + str(page_number)
#     page = requests.get(url)
#     soup = BeautifulSoup(page, "html.parser")
#     user_links = soup.find_all(
#         "a", href=lambda href: href and href.startswith("hiscorepersonal?user1=")
#     )
#     for user_link in user_links:
#         user_url = (
#             "https://secure.runescape.com/m=hiscore_oldschool/" + user_link["href"]
#         )
#         username = user_link.text
#         print("Username:", username)
#         print("User URL:", user_url)
#         next_page_arrow = soup.find(
#             "a", class_="personal-hiscores__pagination-arrow--down"
#         )

#         if next_page_arrow:
#             page_number += 1
#         else:
#             break
#     with open("user_data.csv", mode="w", newline="") as file:
#         writer = csv.writer(file)
#         writer.writerow(["Username", "User URL"])  # Write header
#         writer.writerows(user_data)

import requests
from bs4 import BeautifulSoup
import csv

# Define the base URL
base_url = "https://secure.runescape.com/m=hiscore_oldschool/overall?table=0&page="

# Initialize a counter for the page number
page_number = 1

# Create a list to store the scraped data
all_data = []

while page_number < 10:
    # Construct the URL for the current page
    url = base_url + str(page_number)

    # Fetch the page content
    page = requests.get(url).text
    soup = BeautifulSoup(page, "html.parser")

    # Check if there's a "Next Page" arrow
    next_page_arrow = soup.find("a", class_="personal-hiscores__pagination-arrow--down")

    # Find and extract user data from the current page
    user_links = soup.find_all(
        "a", href=lambda href: href and href.startswith("hiscorepersonal?user1=")
    )

    for user_link in user_links:
        user_url = (
            "https://secure.runescape.com/m=hiscore_oldschool/" + user_link["href"]
        )
        username = user_link.text

        # Fetch the user's page
        user_page = requests.get(user_url).text
        user_soup = BeautifulSoup(user_page, "html.parser")

        # Extract skill-related and minigame-related information
        skill_data = user_soup.select(
            ".personal-hiscores__row--content .personal-hiscores__row__column"
        )
        minigame_data = user_soup.select(".activity-feed__row")

        # Process and extract skill data
        skills = []
        for skill in skill_data:
            skill_name = skill.find(
                "div", class_="personal-hiscores__row__column--gutter"
            ).text.strip()
            skill_rank = skill.find(
                "div", class_="personal-hiscores__row__column--gutter-skill"
            ).text.strip()
            skill_level = skill.find(
                "div", class_="personal-hiscores__row__column--gutter-level"
            ).text.strip()
            skill_xp = skill.find(
                "div", class_="personal-hiscores__row__column--gutter-xp"
            ).text.strip()
            skills.append((skill_name, skill_rank, skill_level, skill_xp))

        # Process and extract minigame data
        minigames = []
        for minigame in minigame_data:
            minigame_name = minigame.find(
                "div", class_="activity-feed__row__column"
            ).text.strip()
            minigame_rank = minigame.find(
                "div", class_="activity-feed__row__column--score"
            ).text.strip()
            minigame_score = minigame.find(
                "div", class_="activity-feed__row__column--points"
            ).text.strip()
            minigames.append((minigame_name, minigame_rank, minigame_score))

        # Combine all data for the user
        user_data = (username, user_url, skills, minigames)
        all_data.append(user_data)

    if next_page_arrow:
        # Increment the page number and continue to the next page
        page_number += 1
    else:
        # Break the loop if there's no "Next Page" arrow
        break

# Save the scraped data to a CSV file
with open("user_data.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    # Update the CSV header to include skill and minigame columns
    writer.writerow(["Username", "User URL", "Skills", "Minigames"])
    writer.writerows(all_data)
