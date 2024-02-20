from appium import webdriver
from appium.options.common.base import AppiumOptions

options = AppiumOptions()
options.load_capabilities({
	"platformName": "Android",
	"appium:deviceName": "디바이스종류", #예)GM-GXXX 
	"appium:udid": "device uuid번호", #예)cexxxxxxxx
	"appium:appPackage":"com.sec.android.app.popupcalculator",
	"appium:appActivity":"com.sec.android.app.popupcalculator.Calculator",
})

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)