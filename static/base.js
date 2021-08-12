window.onload = function countMenuItems() {
    /*
    * Count the number of menu items depending on
    * whether the user is logged in or not
    */
    let amountElements = document.getElementsByClassName('menu-item').length
    document.body.style.setProperty('--items', amountElements.toString())
}