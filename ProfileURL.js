const linkElement = document.evaluate("/html/body/div[1]/div[7]/div[1]/div/div[3]/a", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
if (linkElement) {
	const url = linkElement.href;
	window.location.href = url;
} else {
	console.error("Link element not found using the provided XPath.");
}