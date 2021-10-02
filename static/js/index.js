const expireDaysInput = document.querySelector('#customRange1');

expireDaysInput.addEventListener('change', (event) => {
    document.querySelector('#outputDays').innerHTML = event.target.value;
})