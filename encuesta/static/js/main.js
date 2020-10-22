const createInput = (nro) => `
    <div class="option">
        <label for="option-${nro}">Opción ${nro}:</label>
        <input id="option-${nro}" name="opcion_${nro}" type="text" />
    </div>`

const handleOptions = () => {
    const options = [createInput(1), createInput(2)]
    const optionsCont = document.querySelector('.options-cont')
    const addOptionButton = document.querySelector('.opcion-boton')
    const nroOpciones = document.querySelector('#nro_opciones')
    if (!optionsCont || !addOptionButton || !nroOpciones) return
    optionsCont.innerHTML = options.join('')
    addOptionButton.addEventListener('click', () => {
        options.push(createInput(options.length + 1))
        nroOpciones.setAttribute('value', options.length)
        optionsCont.innerHTML = options.join('')
    })
}

const setShowForm = (open) => {
    const form = document.querySelector('#votar-form')
    const showButtonCont = document.querySelector('#votar-button')
    if (!form || !showButtonCont) return
    if (open) {
        form.style.display = 'block'
        showButtonCont.style.display = 'none'
        return
    }
    form.style.display = 'none'
    showButtonCont.style.display = 'block'
}
const handleForm = () => {
    const showButton = document.querySelector('#show-form')
    const hideButton = document.querySelector('#hide-form')
    if (!showButton || !hideButton) return
    showButton.addEventListener('click', () => setShowForm(true))
    hideButton.addEventListener('click', () => setShowForm(false))
}

window.addEventListener('DOMContentLoaded', () => {
    handleOptions()
    handleForm()
    setShowForm(false)
})
