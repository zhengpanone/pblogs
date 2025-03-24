const { chromium } = require('playwright');

(async () => {
    const browser = await chromium.launch();
    const page = await browser.newPage();
    await page.goto('https://www.baidu.com');
    await page.fill('#kw', "Playwright")
    await page.click('#su')
    await page.screenshot({path:"./baidu.png"})
    console.log(await page.title());
    await browser.close();
})();