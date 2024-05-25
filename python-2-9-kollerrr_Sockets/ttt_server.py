import socketserver
import threading

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True
    allow_reuse_address = True

class CapHandler(socketserver. StreamRequestHandler):

    def handle(self) -> None:

        self.opponent = None
        client = f'{self.client_address} on {threading.current_thread().getName()}'

        print(f'Connected: {client}')

        try:
            self.initialize()
            self.process_commands()
        except Exception as e:
            print(e)
        finally:
            try:
                self.opponent.send('OTHER_PLAYER_LEFT')
            except:
                pass
            print(f'Closed: {client}')

        def send(self, message):

            self.wfile.write(f'{message}\n'.encode())
        
        def initialize(self):

            Game.join(self)
            self.send(f'WELCOME {self.mark}')

            if self.mark == 'X':
                self.game.current_player = self
                self.send('MESSAGE: Waiting for another player to connect')
            else:
                self.opponent = self.game.current_player
                self.opponent.opponent = self
                self.opponent.send('MESSAGE: Your move')

        def process_commands(self):

            while True:
                command = self.rfile.readline()
                if not command:
                    break
                command = command.decode()
                if command.startswith('QUIT'):
                    return
                elif command.startswith('MOVE'):
                    self.process_move_command(int(command[5:]))  # число, куда выполняется ход

        def process_move_command(self, location):

            try:
                self.game.move(location, self)
                self.send('VALID MOVE')          # корректный ход
                self.opponent.send(f'OPPONENT_MOVED {location}')

                if self.game.has_winner():
                    self.send('VICTORY')
                    self.opponent.send('DEFEAT')

                elif self.game.board_filled_up():
                    self.send('TIE')            # ничья
                    self.opponent.send('TIE')
                
            except Exception as e:
                self.send('MESSAGE' + str(e))

class Game:

    next_game = None
    game_selection_lock = threading.Lock()

    def __init__(self) -> None:

        self.board = [None]*9
        self.current_player = None
        self.lock = threading.Lock()

    def has_winner(self):

        b = self.board
        return((b[0] is not None and b[0] == b[1] and b[0] == b[2])
               or (b[3] is not None and b[3] == b[4] and b[3] == b[5])
               or (b[6] is not None and b[6] == b[6] and b[6] == b[8])
               
               or (b[0] is not None and b[0] == b[3] and b[0] == b[6])
               or (b[1] is not None and b[1] == b[4] and b[1] == b[7])
               or (b[2] is not None and b[2] == b[5] and b[2] == b[8])
               
               or (b[0] is not None and b[0] == b[4] and b[0] == b[8])
               or (b[2] is not None and b[2] == b[4] and b[2] == b[6]))
    
    def board_filled_up(self):

        return all(cell is not None for cell in self.board)
    
    def move(self, location, player):

        with self.lock:

            if player != self.current_player:
                return ValueError('Not your turn')
            elif player.opponent in None:
                raise ValueError("You don't have an opponent yet")
            elif self.board[location] is not None:
                raise ValueError('Cell is already occupied')
            self.board[location] = self.current_player
            self.current_player = self.current_player.opponent

    @classmethod

    def join(cls, player):  # субкласс - cls; объект класса

        with cls.game_selection_lock:
            if cls.next_game is None:
                cls.next_game = Game()
                player.game = cls.next_game
                player.mark = 'X'
            else:
                player.mark = '0'
                player.game = cls.next_game
                cls.next_game = None
                
with ThreadedTCPServer(('', 59898), CapHandler) as  server
    print("Server is running...")
    server.serve_forever()