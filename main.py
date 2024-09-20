import time, random
import asyncio
from playwright.async_api import async_playwright, expect

with open('useragent.txt') as f:
    user_agents = []
    user_agents = f.readlines()

with open('proxy.txt') as f:
    proxy = []
    proxy = f.readlines()

with open('emails.txt') as f:
    emails = []
    emails = f.readlines()

EXTENTION_PATH = 'C:\\Users\\tblud\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Extensions\\caacbgbklghmpodbdafajbgdnegacfmo\\1.0.5_0'
#caacbgbklghmpodbdafajbgdnegacfmo

async def main(proxy, user_agent, email):
    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(
            '',
            headless=False,
            proxy={'server': f'http://{proxy.strip()}',
                   'username': 'vNuNjA5W',
                   'password': 'HmxyeHtB'},
            user_agent=user_agent.strip(),
            args=[
                f"--disable-extensions-except={EXTENTION_PATH}",
                f"--load-extension={EXTENTION_PATH}",

            ],
        )



        # if len(context.background_pages) == 0:
        #     await asyncio.sleep(1)
        #
        #     background_page = await context.wait_for_event('serviceworker')
        # else:
        #     background_page = context.background_pages[0]

        # titles = [await p.title() for p in context.pages]
        # while 'Gradient Network Dashboard' not in titles:
        #     titles = [await p.title() for p in context.pages]



        page = await context.new_page()
        await page.goto('https://app.gradient.network/')
        await page.bring_to_front()
        await page.wait_for_load_state()
        page1 = context.pages[0]
        await page1.close()
        page1 = context.pages[1]
        await page1.close()

        await asyncio.sleep(random.randint(2, 6))
        inputs = page.get_by_placeholder("Enter Email")
        await expect(inputs).to_be_visible()
        await inputs.type(email.strip())
        inputs2 = page.get_by_placeholder("Enter Password")
        await expect(inputs2).to_be_visible()
        await inputs2.type("20042004")
        await asyncio.sleep(random.randint(2, 6))
        button = page.locator('//html/body/div[1]/div[2]/div/div/div/div[4]/button[1]')
        await expect(button).to_be_visible()
        await button.click()
        await asyncio.sleep(3)
        await page.keyboard.press('Escape')
        await asyncio.sleep(3)
        page2 = await context.new_page()
        await page2.goto("chrome-extension://caacbgbklghmpodbdafajbgdnegacfmo/popup.html")
        await asyncio.sleep(3)
        await page2.keyboard.press('Escape')
        await asyncio.sleep(10**100)

if __name__ == '__main__':
    asyncio.run(main(proxy[0], user_agents[0], emails[0]))

