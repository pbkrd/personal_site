function changeCat(button, section) {
    const parent = button.parentNode;
    const parents = document.querySelectorAll(".card-category-wrap");
	for (let p of parents) {
	    p.classList.remove('active');
	}
	parent.classList.add('active');

    const tabPanels = document.querySelectorAll(".posts-scrollbar-wrap");
    for (let tap of tabPanels) {
        tap.classList.remove('active-data');
	}
    section.classList.add('active-data');
}
