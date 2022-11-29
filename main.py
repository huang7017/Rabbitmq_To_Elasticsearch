from app.Rabbitmq import Rabbitmq
from app.Config import Config

if __name__ == '__main__':
    print('run....', flush=True)
    cfg = Config()
    host = cfg.get('rabbitmq', 'Host')
    port = cfg.get('rabbitmq', 'Port')
    user = cfg.get('rabbitmq', 'RabbitmqName')
    password = cfg.get('rabbitmq', 'RabbitmqPassword')
    queue = cfg.get('rabbitmq', 'Queue')
    rabbitmq = Rabbitmq(str(host),str(port),user,password,queue)
    # rabbitmq.send('etw','msgTest')
    rabbitmq.receive(queue)
    rabbitmq.close()