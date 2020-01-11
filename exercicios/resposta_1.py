# 1) Adicione um argumento no parser da rotina 'add_arguments'
#     ...
#     self.parser.add_argument('-novo_argumento', required=False, type=str, default='valor')
#     ...
#
# 2) Escolha qual processo irá usar o argumento; (Para o exemplo, escolhi a API)
#
#
# def get_api_arguments(self):
#     """Return all the arguments necessary for the API.
#
#     :returns list: List of arguments"""
#
#     args = self.parser.parse_args()
#
#     if not args.secret:
#         secret = self.secret
#     else:
#         secret = args.secret
#
#     if args.url == 'localhost':
#         args.url = '127.0.0.1'
#
#     // Ultimo elemento da lista é o novo argumento
#     return [args.url, args.ap, args.sp, args.mp, args.step_t, args.first_t, args.mtd, args.log, args.sa_timeout, secret, args.novo_argumento]
#
# 3) Esta feito!!! O resto o arquivo thread_starter resolve enviando os elementos dessa lista para o processo em questão