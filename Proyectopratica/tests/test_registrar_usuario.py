import unittest
from unittest.mock import patch
from Evento.usuario import registrar_usuario

class TestRegistrarUsuario(unittest.TestCase):

    @patch('builtins.input', side_effect=['John Doe', '1234', '25', 'john@example.com', '1500'])
    @patch('getpass.getpass', return_value='1234')
    def test_registrar_usuario_success(self, mock_getpass, mock_input):
        usuarios = []
        with patch('builtins.print') as mock_print:
            registrar_usuario(usuarios)
            self.assertEqual(len(usuarios), 1)
            self.assertEqual(usuarios[0]['nombre'], 'John Doe')
            self.assertEqual(usuarios[0]['id'], '1234')
            self.assertEqual(usuarios[0]['edad'], 25)
            self.assertEqual(usuarios[0]['email'], 'john@example.com')
            self.assertEqual(usuarios[0]['presupuesto'], 1500)
            mock_print.assert_any_call("Cliente registrado con éxito")
            mock_print.assert_any_call("Proceso finalizado")

    @patch('builtins.input', side_effect=['Jane Doe', '5678', '17', 'jane@example.com', '500'])
    @patch('getpass.getpass', return_value='5678')
    def test_registrar_usuario_underage_and_low_budget(self, mock_getpass, mock_input):
        usuarios = []
        with patch('builtins.print') as mock_print:
            registrar_usuario(usuarios)
            mock_print.assert_any_call("Cliente registrado con éxito")
            mock_print.assert_any_call("Proceso finalizado")
            mock_print.assert_any_call("Usted no tendrá dinero suficiente para registrar un evento")
            mock_print.assert_any_call("Tenga en cuenta que no puede registrar un evento siendo menor de edad")
            self.assertEqual(len(usuarios), 1)
            self.assertEqual(usuarios[0]['nombre'], 'Jane Doe')
            self.assertEqual(usuarios[0]['id'], '5678')
            self.assertEqual(usuarios[0]['edad'], 17)
            self.assertEqual(usuarios[0]['email'], 'jane@example.com')
            self.assertEqual(usuarios[0]['presupuesto'], 500)

if __name__ == '__main__':
    unittest.main()