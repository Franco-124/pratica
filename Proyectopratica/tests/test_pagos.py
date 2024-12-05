import unittest
from unittest.mock import patch, mock_open
import asyncio
from Evento.Pagos import pagar_evento, generar_factura

class TestPagos(unittest.TestCase):

    def setUp(self):
        self.usuario = {
            'nombre': 'John Doe',
            'presupuesto': 2000
        }
        self.evento = {
            'nombre': 'Concierto',
            'total_evento': 1500
        }

    @patch('builtins.open', new_callable=mock_open)
    @patch('Evento.Pagos.datetime')
    def test_pagar_evento_exitoso(self, mock_datetime, mock_file):
        mock_datetime.now.return_value.strftime.return_value = "2023-01-01 12:00:00"
        
        loop = asyncio.get_event_loop()
        loop.run_until_complete(pagar_evento(self.usuario, self.evento))
        
        self.assertEqual(self.usuario['presupuesto'], 500)
        mock_file.assert_called_once_with('Concierto_John Doe.txt', 'w')
        mock_file().write.assert_called_once()
        factura_content = (
            "------Factura evento----\n"
            "----------------------------\n"
            "Responsable: John Doe\n"
            "Nombre evento: Concierto\n"
            "Fecha: 2023-01-01 12:00:00\n"
            "Monto: 1500\n"
            "Presupuesto restante: 500\n"
        )
        mock_file().write.assert_called_once_with(factura_content)

    @patch('builtins.print')
    def test_pagar_evento_presupuesto_insuficiente(self, mock_print):
        self.usuario['presupuesto'] = 1000
        
        loop = asyncio.get_event_loop()
        loop.run_until_complete(pagar_evento(self.usuario, self.evento))
        
        self.assertEqual(self.usuario['presupuesto'], 1000)
        mock_print.assert_any_call("No hay presupuesto suficiente para pagar el evento Concierto")

if __name__ == '__main__':
    unittest.main()