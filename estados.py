class EstadoPedido:
    def __init__(self):
        # Estado inicial
        self.estado_actual = "Procesando"  # Estado inicial

    def siguiente_estado(self):
        """Transición al siguiente estado según la secuencia definida."""
        if self.estado_actual == "Procesando":
            self.estado_actual = "Preparación"
        elif self.estado_actual == "Preparación":
            self.estado_actual = "Enviado"
        elif self.estado_actual == "Enviado":
            self.estado_actual = "Entregado"
        elif self.estado_actual == "Entregado":
            self.estado_actual = "Finalizado"
        else:
            print("El pedido ya ha sido finalizado.")

    def estado_actual(self):
        """Retorna el estado actual del pedido."""
        return self.estado_actual

    def reiniciar_estado(self):
        """Reinicia el estado del pedido a 'Procesando'."""
        self.estado_actual = "Procesando"

    def mostrar_estado(self):
        """Muestra el estado actual."""
        print(f"Estado actual del pedido: {self.estado_actual}")

if __name__ == "__main__":
    # Ejemplo de uso
    pedido = EstadoPedido()
    pedido.mostrar_estado()  # Debería mostrar "Procesando"

    # Simulando el cambio de estados
    for _ in range(5):
        pedido.siguiente_estado()
        pedido.mostrar_estado()
