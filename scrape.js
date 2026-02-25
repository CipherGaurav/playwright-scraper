const { chromium } = require('playwright');

const urls = [
  'https://tools.datasci.study/seed-72/',
  'https://tools.datasci.study/seed-73/',
  'https://tools.datasci.study/seed-74/',
  'https://tools.datasci.study/seed-75/',
  'https://tools.datasci.study/seed-76/',
  'https://tools.datasci.study/seed-77/',
  'https://tools.datasci.study/seed-78/',
  'https://tools.datasci.study/seed-79/',
  'https://tools.datasci.study/seed-80/',
  'https://tools.datasci.study/seed-81/'
];

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  let grandTotal = 0;
  
  for (const url of urls) {
    console.log(`Scraping: ${url}`);
    await page.goto(url, { waitUntil: 'networkidle' });
    const numbers = await page.$$eval('table td, table th', cells => {
      return cells.map(cell => {
        const num = parseFloat(cell.innerText.trim());
        return isNaN(num) ? 0 : num;
      }).filter(n => n !== 0);
    });
    const pageSum = numbers.reduce((a, b) => a + b, 0);
    grandTotal += pageSum;
  }
  
  console.log(`GRAND TOTAL: ${grandTotal}`);
  await browser.close();
})();
