const puppeteer = require("puppeteer");

async function checkEthiopiaCustoms(chassisNumber) {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();

  try {
    console.log(`Connecting to Ethiopia Customs Portal...`);
    // The URL for the vehicle verification module
    await page.goto("https://customs.erca.gov.et/trade/app/vehicle/search", {
      waitUntil: "networkidle2",
    });

    // 1. Locate the input field for Chassis Number/VIN
    // Note: You must inspect the page to get the exact ID (e.g., #chassisNo)
    const selector = 'input[name="chassisNumber"]';
    await page.waitForSelector(selector);
    await page.type(selector, chassisNumber);

    // 2. Click the Search/Verify Button
    await page.click("#searchButtonId"); // Replace with the actual ID from DevTools

    // 3. Wait for the results table to appear
    await page.waitForSelector(".results-table", { timeout: 10000 });

    // 4. Extract the data
    const vehicleData = await page.evaluate(() => {
      return {
        model: document.querySelector(".model-name")?.innerText,
        engineCC: document.querySelector(".engine-capacity")?.innerText,
        year: document.querySelector(".mfg-year")?.innerText,
        status: document.querySelector(".status-badge")?.innerText,
      };
    });

    console.log("Vehicle Found:", vehicleData);
    return vehicleData;
  } catch (error) {
    console.error("Could not retrieve data. The portal might require a login or the VIN is not in the system.");
  } finally {
    await browser.close();
  }
}

// Try your BYD VIN
checkEthiopiaCustoms("LGXCE4CC9R0026989");
