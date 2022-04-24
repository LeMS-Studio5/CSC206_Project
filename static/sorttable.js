var cPrev=-1;
function sortBy(c) {
    rows = document.getElementById("sortable").rows.length; // num of rows
    columns = document.getElementById("sortable").rows[0].cells.length; // num of columns
    arrTable = [...Array(rows)].map(e => Array(columns)); // create an empty 2d array
    for (ro=0; ro<rows; ro++) { // cycle through rows
        for (co=0; co<columns; co++) { // cycle through columns
            // assign the value in each row-column to a 2d array by row-column
            arrTable[ro][co] = document.getElementById("sortable").rows[ro].cells[co].innerHTML;
        }
    }
    th = arrTable.shift(); // remove the header row from the array, and save it
    if (c !== cPrev) { // different column is clicked, so sort by the new column
        arrTable.sort(
            function (a, b) {
                if (a[c] === b[c]) {
                    return 0;
                } else {
                    return (a[c] < b[c]) ? -1 : 1;
                }
            }
        );
		clearFormat();
    } else { // if the same column is clicked then reverse the array
        arrTable.reverse();
    }
	document.getElementById(c).classList.toggle("up");
    cPrev = c; // save in previous c
    arrTable.unshift(th); // put the header back in to the array
    for (ro=0; ro<rows; ro++) {// cycle through rows-columns placing values from the array back into the html table
        for (co=0; co<columns; co++) {
            document.getElementById("sortable").rows[ro].cells[co].innerHTML = arrTable[ro][co];
        }
    }
}
function clearFormat(){
    if (cPrev > -1) document.getElementById(cPrev).classList.remove("up");
}