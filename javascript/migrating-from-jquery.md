## You might not need JQuery
https://youmightnotneedjquery.com/



## Writing jQuery find() in Pure Javascript
https://usefulangle.com/post/43/jquery-find-function-in-pure-vanilla-javascript

### Complex Case - When Outer Selector is a Collection of Elements

```javascript
<div class="post">
	<div class="thumb"><div>
	<div class="thumb"><div>
<div>
<div class="post">
	<div class="thumb"><div>
	<div class="thumb"><div>
<div>
```


JQuery code:
```javascript
// This will give all 4 inner elements with class "thumb"
$(".post").find(".thumb")
```


Vanilla JS: 
```javascript
// Final found elements
var found_elements = [];

// Find all the outer matched elements
var outers = document.querySelectorAll('.post');

for(var i=0; i<outers.length; i++) {
	var elements_in_outer = outers[i].querySelectorAll(".thumb");

	// document.querySelectorAll() returns an "array-like" collection of elements
	// convert this "array-like" collection to an array
	elements_in_outer = Array.prototype.slice.call(elements_in_outer);
	
	found_elements = found_elements.concat(elements_in_outer);
}

// The final 4 elements
console.log(found_elements);

```