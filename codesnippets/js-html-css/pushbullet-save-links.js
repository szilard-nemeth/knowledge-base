var script = document.createElement('script');
script.src = "https://code.jquery.com/jquery-3.4.1.min.js";
document.getElementsByTagName('head')[0].appendChild(script);
$$ = null;
//$ = null;
//$ = jQuery;

copy($(".pushbubble").map(function() {
	var e = $(this),
	textPart = e.find(".text-part")
	divs = textPart.children()
	title = $(divs[0]).text()
	link = $(divs[1]).text()
	result = `${title}: ${link}`
	//console.log(result)
	return result
}).get().join("\n"))