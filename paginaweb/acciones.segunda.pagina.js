function sumar() {
    const n1 = parseFloat(document.getElementById('num1').value);
    const n2 = parseFloat(document.getElementById('num2').value);
    if (isNaN(n1) || isNaN(n2)) {
        document.getElementById('resultado').textContent = "Introduce ambos números";
    } else {
        document.getElementById('resultado').textContent = "Resultado: " + (n1 + n2);
    }
}
