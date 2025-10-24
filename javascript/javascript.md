## Querying elements

### Query all list items of parent
```javascript
// Get the parent element
const parentElement = document.getElementById("myParent"); 

// Query all list items within the parent
const listItems = parentElement.querySelectorAll("li");

// Iterate over the list items and do something with them
listItems.forEach(item => {
  console.log(item.textContent); // Example: Log the text content of each list item
});
```

### Get parent element by selector
https://stackoverflow.com/questions/14234560/how-to-get-parent-element-by-selector

https://developer.mozilla.org/en-US/docs/Web/API/Element/closest

```javascript
var div = document.querySelector('div#myDiv');
div.closest('div[someAtrr]');
```


## Return values

### Returning two values from a function
While a JavaScript function can only directly return a single value, you can achieve the effect of returning multiple values through the following methods:
1. Using an Array:
```javascript

function getValues() {
  let x = 5;
  let y = 10;
  return [x, y]; // Return an array containing both values
}

let [a, b] = getValues(); // Destructure the array to get individual values
console.log(a); // 5
console.log(b); // 10
```


2. Using an Object:

```javascript
function getPersonDetails() {
  let name = "John";
  let age = 30;
  return { name, age }; // Return an object with properties
}

let person = getPersonDetails();
console.log(person.name); // John
console.log(person.age); // 30 
```


## NodeList
https://developer.mozilla.org/en-US/docs/Web/API/NodeList


### How can I reorder/sort a NodeList in JavaScript?
https://stackoverflow.com/questions/4760080/how-can-i-reorder-sort-a-nodelist-in-javascript

Convert to array first: 
```javascript
var foods = xmlDoc.getElementsByTagName("food");
var foodsArray = Array.prototype.slice.call(foods, 0);
```

Then sort: 
```javascript
foodsArray.sort(function(a,b) {
    var aCat = a.getElementsByTagName("category")[0].childNodes[0].nodeValue;
    var bCat = b.getElementsByTagName("category")[0].childNodes[0].nodeValue;
    if (aCat > bCat) return 1;
    if (aCat < bCat) return -1;
    return 0;
});
```


## String formatting

### Template strings
https://stackoverflow.com/questions/610406/javascript-equivalent-to-printf-string-format
```javascript
let soMany = 10;
console.log(`This is ${soMany} times easier!`);
// "This is 10 times easier!"
```