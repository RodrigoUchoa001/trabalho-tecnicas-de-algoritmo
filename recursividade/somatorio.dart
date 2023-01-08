void main() {
  print(somatorio(5));
}

int somatorio(int numero) {
  if (numero == 1) {
    return 1;
  } else {
    return numero + somatorio(numero - 1);
  }
}
