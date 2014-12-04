class SimpleFactory(object):
    @staticmethod # This decorator allows to run method without
                # class instance, .e. SimpleFactory.build_connection
    def build_connection(protocol):
      if protocol == 'http':
        return HTTPConnection()
      elif protocol == 'ftp':
        return FTPConnection()

      else:
        raise RuntimeError('Unknown protocol')

if __name__ == '__main__':
    protocol = raw_input('Which Protocol to use? (http or ftp): ')
    protocol = SimpleFactory.build_connection(protocol)
    protocol.connect()
    print protocol.get_response()

