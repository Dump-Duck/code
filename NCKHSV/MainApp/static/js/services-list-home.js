
document.addEventListener('DOMContentLoaded', function () {
const foodBtns = document.querySelectorAll('.home-menu-about button')
const foodList = document.querySelectorAll('.home-item')

foodBtns.forEach((btn) => {
	btn.addEventListener('click', (e) => {
		const type = e.target.getAttribute('type-home')

		// remove and set active fpr button
		document
			.querySelector('.home-menu-about button.active')
			.classList.remove('active')
		e.target.classList.add('active')

		// filter elements
		foodList.forEach((item) => {
			if (type == 'all' || item.getAttribute('type-home') == type)
				item.classList.remove('hide')
			else item.classList.add('hide')
		})
	})
})
})