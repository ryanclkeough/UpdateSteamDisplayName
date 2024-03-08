const value = document.evaluate('/html/body/div[1]/div[7]/div[4]/div/div[2]/div/div/div[3]/div[3]/div[2]/form/div[3]/div[2]/div[1]/label/div[2]/input', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.value;

if (value) {
  console.log("Textbox value:", value);
} else {
  console.warn("Textbox not found using the provided XPath expression.");
}