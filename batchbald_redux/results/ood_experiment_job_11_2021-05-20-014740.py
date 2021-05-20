store = {}
store['timestamp']=1621471660
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=11']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=11
store['worker_id']=11
store['num_workers']=80
store['config']={'seed': 1245, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 16, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples)) + ('FastMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 14640, 45567, 52801, 53689, 801, 55187, 26479, 50997, 3792]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 2.5390119552612305})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.0283045768737793})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.287803888320923})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.6477279663085938})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 3.9458885192871094})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.6916303634643555})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.917158603668213})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 4.068984031677246})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.9307596683502197})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 4.089231491088867})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 4.326560020446777})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 4.039659023284912})
store['active_learning_steps'][0]['training']['best_epoch']=9
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6088, 'crossentropy': 4.098341796875}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 11692], ['id', 32065], ['id', 35184], ['id', 47634], ['id', 18255]], 'labels': [-1, -1, -1, -1, 8], 'scores': [1.5818298340930945, 2.8379647476979994, 3.6817925959921887, 4.168322720300377, 4.419933512841247]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 2.937180995941162})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.9978442192077637})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.9345860481262207})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.714029312133789})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.8714680671691895})
store['active_learning_steps'][1]['training']['best_epoch']=2
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.5825, 'crossentropy': 3.4126453125}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 28588], ['id', 24223], ['id', 4765], ['id', 59747], ['id', 31020]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5320229377751597, 2.668267023864864, 3.5332523798464575, 4.082347100706885, 4.351073449417504]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 2.3807976245880127})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.9546189308166504})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.383645534515381})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.2807042598724365})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.9027280807495117})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.7264602184295654})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 3.5072078704833984})
store['active_learning_steps'][2]['training']['best_epoch']=4
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6001, 'crossentropy': 3.5924125}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 23474], ['id', 30454], ['id', 49889], ['id', 22531], ['id', 57488]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4025955350372876, 2.569342802743308, 3.499010830926279, 4.06530242644207, 4.35053581887348]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.4171855449676514})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.1625802516937256})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.8493146896362305})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.957681894302368})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.230752944946289})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.3530149459838867})
store['active_learning_steps'][3]['training']['best_epoch']=3
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6043, 'crossentropy': 3.348694140625}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 25086], ['id', 41516], ['id', 56936], ['id', 51986], ['id', 27449]], 'labels': [-1, -1, -1, -1, 8], 'scores': [1.6165023803599166, 2.813851364869491, 3.6718767902153333, 4.151926443939095, 4.393623888802605]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 2.4572815895080566})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.995053291320801})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.2773046493530273})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.5662097930908203})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.616358757019043})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.6101107597351074})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.729274034500122})
store['active_learning_steps'][4]['training']['best_epoch']=4
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.6043, 'crossentropy': 3.660661328125}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 20794], ['id', 45048], ['id', 51968], ['id', 4355], ['id', 11631]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4607879137329218, 2.6390017603012543, 3.5214478632196062, 4.051554399130286, 4.331437337182519]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.054928779602051})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 2.6437368392944336})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.807684898376465})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.119051218032837})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.8447513580322266})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.3395578861236572})
store['active_learning_steps'][5]['training']['best_epoch']=3
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.6116, 'crossentropy': 3.117677734375}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 44672], ['id', 11642], ['id', 45048], ['id', 11709], ['id', 59459]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4761030471455847, 2.604690960073066, 3.486696328563127, 4.006830577030687, 4.299615245644]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 2.5963664054870605})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.207707643508911})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.265246868133545})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.3823060989379883})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 3.919761896133423})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.586, 'crossentropy': 3.48308515625}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 1239], ['id', 13129], ['id', 54092], ['id', 50910], ['id', 4759]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5575408443512853, 2.8043707806217455, 3.6977710047399466, 4.1480227691281595, 4.38131458066708]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.3621954917907715})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.069136142730713})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.065460681915283})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.3435025215148926})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.554213762283325})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.6870646476745605})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.6757264137268066})
store['active_learning_steps'][7]['training']['best_epoch']=4
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.6171, 'crossentropy': 3.51881015625}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 55476], ['id', 8357], ['id', 45048], ['id', 29638], ['id', 49448]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4774714551931751, 2.701310929776597, 3.543022969495132, 4.065914028998936, 4.3362740575504635]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.0611839294433594})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.7444326877593994})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.8308966159820557})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.062865734100342})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.3391151428222656})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.9582626819610596})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.3005239963531494})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 3.1725239753723145})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 3.3226242065429688})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.203705310821533})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.411487579345703})
store['active_learning_steps'][8]['training']['best_epoch']=8
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.6318, 'crossentropy': 3.1898154296875}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 42595], ['id', 25180], ['id', 8611], ['id', 18416], ['id', 32355]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5366166320200647, 2.6910934176318086, 3.579979471598886, 4.097082505568427, 4.364285319896041]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.386310338973999})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.717834711074829})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 3.131277561187744})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.7355237007141113})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.6261816024780273})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.928565263748169})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 4.088595867156982})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.4872641563415527})
store['active_learning_steps'][9]['training']['best_epoch']=5
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.5874, 'crossentropy': 3.79711640625}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 48545], ['id', 56866], ['id', 34481], ['id', 20903], ['id', 19895]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5492856673560413, 2.8540454668374506, 3.7149124340156625, 4.172262413983664, 4.390432575495953]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.50931453704834})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.2213757038116455})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.627528667449951})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.6951746940612793})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.958474636077881})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.7890632152557373})
store['active_learning_steps'][10]['training']['best_epoch']=3
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.5984, 'crossentropy': 3.504053515625}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 10589], ['id', 37830], ['id', 59426], ['id', 17482], ['id', 36166]], 'labels': [-1, -1, -1, 5, -1], 'scores': [1.3632081624008636, 2.5338727574653728, 3.38081169735557, 3.908282170100062, 4.227811570555741]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 2.512575626373291})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.220717430114746})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.23121976852417})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.1612210273742676})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.2285995483398438})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.724447250366211})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 4.139651298522949})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 4.13338565826416})
store['active_learning_steps'][11]['training']['best_epoch']=5
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.6088, 'crossentropy': 3.64063515625}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 42697], ['id', 54403], ['id', 44836], ['id', 33659], ['id', 22607]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5796493245704575, 2.798564641777037, 3.654600489579372, 4.131373637953606, 4.389280197038785]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 2.2883944511413574})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.9444503784179688})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.1494898796081543})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.5821523666381836})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.3763158321380615})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.5427439212799072})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.6946310997009277})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 4.144687652587891})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 4.264612197875977})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 4.163941383361816})
store['active_learning_steps'][12]['training']['best_epoch']=7
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.6182, 'crossentropy': 3.928048046875}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 12972], ['id', 48323], ['id', 32126], ['id', 8571], ['id', 48420]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6249982284612545, 2.8639219120884816, 3.67025579074123, 4.1905333748398395, 4.42233160991573]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.1767208576202393})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.9437079429626465})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.089995861053467})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.134429454803467})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.4385643005371094})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.1167922019958496})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.396733045578003})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.450653076171875})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.5848889350891113})
store['active_learning_steps'][13]['training']['best_epoch']=6
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6122, 'crossentropy': 3.30139921875}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 48706], ['id', 45057], ['id', 44737], ['id', 47260], ['id', 14823]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5541497786845822, 2.78597061951169, 3.696612863099551, 4.170019782714455, 4.400727372072488]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.1772091388702393})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.345630168914795})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.1814684867858887})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.2389798164367676})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.854525566101074})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.2157347202301025})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.518176317214966})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 4.240118980407715})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.8884315490722656})
store['active_learning_steps'][14]['training']['best_epoch']=6
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.6069, 'crossentropy': 3.54150546875}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 17850], ['id', 27752], ['id', 29908], ['id', 12758], ['id', 49824]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6372370363411575, 2.8430230881001846, 3.7215635670604277, 4.194406108947261, 4.414750262576893]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 2.871966600418091})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 3.3252267837524414})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.633274555206299})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 3.5494375228881836})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.8245351314544678})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 4.024896621704102})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 4.540606498718262})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 3.992009162902832})
store['active_learning_steps'][15]['training']['best_epoch']=5
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.584, 'crossentropy': 4.277838671875}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 18092], ['id', 18324], ['id', 32329], ['id', 45056], ['id', 56900]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.57524565109407, 2.699771656631756, 3.5910069779700553, 4.095980808878982, 4.349270770554332]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.721658706665039})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 3.248474359512329})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.859866142272949})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 4.129762172698975})
store['active_learning_steps'][16]['training']['best_epoch']=1
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.594, 'crossentropy': 2.6847138671875}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 14715], ['id', 21882], ['id', 26752], ['id', 42934], ['id', 36091]], 'labels': [-1, -1, -1, -1, 2], 'scores': [1.266854797131387, 2.3151054401367768, 3.085012308150745, 3.625853088440733, 3.9778435205034164]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.3506202697753906})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.26688289642334})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.7631359100341797})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.860617160797119})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.5661849975585938})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.8434457778930664})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.776212692260742})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.949174642562866})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.5417885780334473})
store['active_learning_steps'][17]['training']['best_epoch']=6
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.6141, 'crossentropy': 4.11408203125}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 55084], ['id', 41426], ['id', 29132], ['id', 4733], ['id', 36231]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5100199999643509, 2.762022201415654, 3.6516490008702522, 4.145292739324659, 4.398172780771548]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.1415295600891113})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.903501033782959})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.3583102226257324})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.224625587463379})
store['active_learning_steps'][18]['training']['best_epoch']=1
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.609, 'crossentropy': 2.16708359375}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 35312], ['id', 325], ['id', 1682], ['id', 13052], ['id', 10986]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3364580294584782, 2.337809079642695, 3.1340115847622574, 3.7040869511785726, 4.053237550150898]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.101942539215088})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.826845645904541})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.1136624813079834})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.0022315979003906})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.2555112838745117})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.5357751846313477})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.289306163787842})
store['active_learning_steps'][19]['training']['best_epoch']=4
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6085, 'crossentropy': 3.31773984375}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 44901], ['id', 34645], ['id', 57148], ['id', 35158], ['id', 5909]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4981359298351986, 2.7168390727865397, 3.5661978210843044, 4.071241403659005, 4.345431702646553]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.165973663330078})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.7958884239196777})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.0646462440490723})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.088737964630127})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.052712917327881})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.354686737060547})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.2293972969055176})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.2283756732940674})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.352156639099121})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.2322723865509033})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.0886497497558594})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.9367995262145996})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.300868272781372})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.0309176445007324})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.5739288330078125})
store['active_learning_steps'][20]['training']['best_epoch']=12
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.633, 'crossentropy': 3.417319140625}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 14801], ['id', 40455], ['id', 27719], ['id', 37740], ['id', 53949]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6110928918449217, 2.87676603093346, 3.7103359625171697, 4.171740280755735, 4.416462732172569]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.4214229583740234})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.5527665615081787})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 3.0928707122802734})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.0250096321105957})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.5093512535095215})
store['active_learning_steps'][21]['training']['best_epoch']=2
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.6342, 'crossentropy': 2.8816279296875}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 54805], ['id', 2773], ['id', 57516], ['id', 11184], ['id', 36281]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4410492882997517, 2.642415405872439, 3.543674975399818, 4.04571172022311, 4.316348491347208]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.207303524017334})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.4399912357330322})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.890723705291748})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.1847219467163086})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.651772975921631})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.5295090675354004})
store['active_learning_steps'][22]['training']['best_epoch']=3
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.6209, 'crossentropy': 3.0608951171875}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 45329], ['id', 17652], ['id', 14673], ['id', 32399], ['id', 16600]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.364999530976225, 2.520465867163781, 3.3483874969541443, 3.9189033931974313, 4.230305114746777]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.360548734664917})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.611449718475342})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.7580583095550537})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.157113790512085})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.438821792602539})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.7380003929138184})
store['active_learning_steps'][23]['training']['best_epoch']=3
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.6199, 'crossentropy': 3.2296119140625}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 42934], ['id', 4727], ['id', 35930], ['id', 22531], ['id', 44805]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4513082191052817, 2.6193806666436146, 3.4805004208965755, 3.9916502030052756, 4.28525006080715]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.2344963550567627})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.765287399291992})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.0069680213928223})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.2815685272216797})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.3640384674072266})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.4803285598754883})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.5486583709716797})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.7774100303649902})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.640928268432617})
store['active_learning_steps'][24]['training']['best_epoch']=6
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.6339, 'crossentropy': 3.646987109375}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 43513], ['id', 6890], ['id', 33046], ['id', 5477], ['id', 33832]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6479135501445858, 2.9045060175310358, 3.77777931936391, 4.254779883711251, 4.456646031701318]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.4237260818481445})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.7721824645996094})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.409442663192749})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.5920066833496094})
store['active_learning_steps'][25]['training']['best_epoch']=1
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.5989, 'crossentropy': 2.508878125}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 6088], ['id', 24968], ['id', 24587], ['id', 50403], ['id', 17985]], 'labels': [-1, -1, -1, 0, 5], 'scores': [1.2036944819098934, 2.2741087008651544, 3.070145699136277, 3.5821380054227276, 3.9563646817338194]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.1662392616271973})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.857288360595703})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.4781107902526855})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.681337833404541})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.44340181350708})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.543262004852295})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.8446245193481445})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.658067226409912})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.934749126434326})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 4.314525127410889})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 4.134604454040527})
store['active_learning_steps'][26]['training']['best_epoch']=8
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.6181, 'crossentropy': 3.9330515625}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 44836], ['id', 28967], ['id', 50636], ['id', 24821], ['id', 18324]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5965185568929, 2.808117891030817, 3.702593989999949, 4.200841587582406, 4.436012870303518]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.137399911880493})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.71547269821167})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.799503803253174})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 3.088212490081787})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.2914302349090576})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.2788360118865967})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 3.5116515159606934})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.6433, 'crossentropy': 3.0560751953125}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 59389], ['id', 27051], ['id', 40980], ['id', 11823], ['id', 8238]], 'labels': [-1, -1, -1, 6, -1], 'scores': [1.521505888707516, 2.7374945433183524, 3.627623110402089, 4.100413856806302, 4.357019250036469]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.0702061653137207})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.577916145324707})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.6918046474456787})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.745711326599121})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 3.251859664916992})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.069202184677124})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.2897915840148926})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.2298574447631836})
store['active_learning_steps'][28]['training']['best_epoch']=5
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.627, 'crossentropy': 3.46690234375}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 14715], ['id', 36427], ['id', 25051], ['id', 39059], ['id', 48437]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.559047259425168, 2.8051330524208895, 3.661552333083444, 4.15831683242528, 4.4021891535725945]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 2.2171645164489746})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.493140697479248})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.295924663543701})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.2058398723602295})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.5183095932006836})
store['active_learning_steps'][29]['training']['best_epoch']=2
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.6193, 'crossentropy': 2.7331333984375}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 3657], ['id', 37665], ['id', 4827], ['id', 54288], ['id', 48029]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.362392580757994, 2.595881933081809, 3.42419268042765, 3.965126091332486, 4.259748749538741]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.083664655685425})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.6337151527404785})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.032662868499756})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.313974380493164})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.586544990539551})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.5354220867156982})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.423600196838379})
store['active_learning_steps'][30]['training']['best_epoch']=4
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.6258, 'crossentropy': 3.310098046875}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 4833], ['id', 48463], ['id', 24740], ['id', 4741], ['id', 26417]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5021357583490182, 2.6937635940813127, 3.581174507057776, 4.110556994822598, 4.375085932148664]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 2.1363682746887207})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.6306557655334473})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.950369358062744})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.9277889728546143})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.400698661804199})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.6081929206848145})
store['active_learning_steps'][31]['training']['best_epoch']=3
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.6123, 'crossentropy': 3.17929296875}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 46864], ['id', 32776], ['id', 42309], ['id', 32351], ['id', 29852]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4806514000942173, 2.635783903764881, 3.5149830513998674, 4.040352878056963, 4.335696352147793]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 2.117523670196533})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 2.711193084716797})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.578765630722046})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.0699219703674316})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.9984869956970215})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.257693290710449})
store['active_learning_steps'][32]['training']['best_epoch']=3
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.6194, 'crossentropy': 2.8129859375}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 56416], ['id', 11598], ['id', 14819], ['id', 17728], ['id', 2773]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3678812253450852, 2.508043259271904, 3.4061806309492138, 3.983119448094185, 4.3017807092675415]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 2.2077126502990723})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.7828094959259033})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.028057098388672})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.4117138385772705})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.4262213706970215})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.3683104515075684})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.863654613494873})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.8785462379455566})
store['active_learning_steps'][33]['training']['best_epoch']=5
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.6344, 'crossentropy': 3.432862890625}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 37212], ['id', 25419], ['id', 15660], ['id', 39260], ['id', 27991]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4960276533569608, 2.7075477163780146, 3.5698021691131316, 4.116022962280754, 4.364662617476094]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.012845993041992})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.737621307373047})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.8657917976379395})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.856957197189331})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.765726327896118})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.791511058807373})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.9911062717437744})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.0590980052948})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.1841588020324707})
store['active_learning_steps'][34]['training']['best_epoch']=6
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.6392, 'crossentropy': 2.8869373046875}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 32776], ['id', 4799], ['id', 40515], ['id', 25091], ['id', 23444]], 'labels': [-1, -1, -1, -1, 2], 'scores': [1.468404549670196, 2.6288568456624932, 3.5385422188032685, 4.056508967024888, 4.337345323932466]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.8548579216003418})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.605696678161621})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.9944519996643066})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.9734528064727783})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.1344356536865234})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.985757827758789})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.871791362762451})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.406858444213867})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.933699131011963})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.7947840690612793})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 3.2505617141723633})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.7698488235473633})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.9945549964904785})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.528268575668335})
store['active_learning_steps'][35]['training']['best_epoch']=11
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.6316, 'crossentropy': 3.647646484375}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 19927], ['id', 37084], ['id', 51151], ['id', 32039], ['id', 19945]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6252305247587007, 2.896460686834999, 3.768141775402947, 4.264216411742115, 4.45625061360316]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 2.540070056915283})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.1575567722320557})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.360386371612549})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 3.1940157413482666})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.6979916095733643})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 3.8869664669036865})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.6624832153320312})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.601529121398926})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 3.984006881713867})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.963376045227051})
store['active_learning_steps'][36]['training']['best_epoch']=7
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.6097, 'crossentropy': 3.81951640625}
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 32056], ['id', 50294], ['id', 42678], ['id', 33250], ['id', 28215]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.441629654245638, 2.6431226325005976, 3.5427792594223444, 4.077152462267945, 4.354400445243898]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.9400441646575928})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.427051067352295})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.592672824859619})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.124103546142578})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.131647825241089})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.1301074028015137})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.3710684776306152})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.139000415802002})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.49216365814209})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.2004058361053467})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.4701972007751465})
store['active_learning_steps'][37]['training']['best_epoch']=8
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.6382, 'crossentropy': 3.29038359375}
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 33010], ['id', 54805], ['id', 28081], ['id', 49058], ['id', 10632]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.478496766288158, 2.7237289051114626, 3.611916111234965, 4.148249436423465, 4.381379962148248]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 2.257521629333496})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.4953413009643555})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.6895430088043213})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.423748016357422})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.368673086166382})
store['active_learning_steps'][38]['training']['best_epoch']=2
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.6253, 'crossentropy': 2.7730619140625}
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 53956], ['id', 5536], ['id', 40471], ['id', 10620], ['id', 32776]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3908839865992264, 2.5263520554536236, 3.3159093553627246, 3.8350950010332143, 4.158014088138991]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.797451138496399})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.343465805053711})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.030282497406006})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.8161613941192627})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.085228443145752})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.5407967567443848})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.9755306243896484})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.1860506534576416})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.2375259399414062})
store['active_learning_steps'][39]['training']['best_epoch']=6
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.6174, 'crossentropy': 3.537986328125}
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 13682], ['id', 54068], ['id', 56567], ['id', 20960], ['id', 9531]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4617298184780825, 2.630035803308724, 3.5314801801679927, 4.043174237293995, 4.32092966597472]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.0601446628570557})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.5376739501953125})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.900482654571533})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.5816397666931152})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.0325660705566406})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.1580214500427246})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.198859214782715})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.1990952491760254})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.03043794631958})
store['active_learning_steps'][40]['training']['best_epoch']=6
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.627, 'crossentropy': 3.392209375}
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 2652], ['id', 38733], ['id', 3950], ['id', 35230], ['id', 35184]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.546333887838632, 2.774047649618556, 3.586530168661744, 4.06758107848834, 4.355653929389511]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 2.1334352493286133})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 2.7266035079956055})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.0685486793518066})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.214449405670166})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.4353864192962646})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.301697015762329})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.758528709411621})
store['active_learning_steps'][41]['training']['best_epoch']=4
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.5959, 'crossentropy': 3.421399609375}
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 23041], ['id', 47260], ['id', 19893], ['id', 4646], ['id', 4717]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5387409986814258, 2.7079670789629438, 3.499144522188181, 4.038741027602767, 4.315784174491343]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.9982365369796753})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 2.7562618255615234})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.807615280151367})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.3326807022094727})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.404897689819336})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.3001747131347656})
store['active_learning_steps'][42]['training']['best_epoch']=3
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.6138, 'crossentropy': 2.97328671875}
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 53956], ['id', 55739], ['id', 59453], ['id', 34708], ['id', 3200]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.474174874241438, 2.5477170683144754, 3.377047634885451, 3.91117460699466, 4.231328433264576]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 2.0716445446014404})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.573498249053955})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.1169848442077637})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.0670418739318848})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.233823299407959})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.9301345348358154})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.176459550857544})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.4501864910125732})
store['active_learning_steps'][43]['training']['best_epoch']=5
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.6329, 'crossentropy': 3.2517787109375}
store['active_learning_steps'][43]['acquisition']={'indices': [['id', 1674], ['id', 43760], ['id', 9468], ['id', 51163], ['id', 25293]], 'labels': [-1, -1, -1, 0, -1], 'scores': [1.515483183408841, 2.7444457190886937, 3.594124162806927, 4.116473352920586, 4.381571433969815]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.135255813598633})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.5392565727233887})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.6264095306396484})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.1053781509399414})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.1146411895751953})
store['active_learning_steps'][44]['training']['best_epoch']=2
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.616, 'crossentropy': 2.61153515625}
store['active_learning_steps'][44]['acquisition']={'indices': [['id', 36187], ['id', 4360], ['id', 4785], ['id', 1227], ['id', 24011]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3219827780421587, 2.404344880619773, 3.2313267644340176, 3.8065566292965602, 4.138742416871183]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 2.2897677421569824})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.7693030834198})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 3.248997449874878})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.2708544731140137})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.2512764930725098})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.2929396629333496})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.4294257164001465})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.6953768730163574})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.730595588684082})
store['active_learning_steps'][45]['training']['best_epoch']=6
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.6179, 'crossentropy': 3.73714609375}
store['active_learning_steps'][45]['acquisition']={'indices': [['id', 53956], ['id', 43294], ['id', 59878], ['id', 26752], ['id', 41937]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4417367781109132, 2.6385713678084306, 3.5128124757147816, 4.064765950382881, 4.331148214646429]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.9424504041671753})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.50258207321167})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.872617244720459})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.152595043182373})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.0242109298706055})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.186007022857666})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.5387802124023438})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.3882124423980713})
store['active_learning_steps'][46]['training']['best_epoch']=5
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.6223, 'crossentropy': 3.0325705078125}
store['active_learning_steps'][46]['acquisition']={'indices': [['id', 36283], ['id', 40157], ['id', 48029], ['id', 13241], ['id', 23347]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4861200507121182, 2.7396501085075586, 3.5647701907536753, 4.0714928253799965, 4.343287212414088]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.410972833633423})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.737398624420166})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 3.0162439346313477})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 3.9452147483825684})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 4.2607316970825195})
store['active_learning_steps'][47]['training']['best_epoch']=2
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.5997, 'crossentropy': 2.846359765625}
store['active_learning_steps'][47]['acquisition']={'indices': [['id', 44377], ['id', 27302], ['id', 23162], ['id', 18092], ['id', 24740]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4403584911109304, 2.6101995076317297, 3.525781360622359, 4.0403216245267215, 4.30339383688697]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.0139169692993164})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 2.744691848754883})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.943131446838379})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.2073676586151123})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.4550747871398926})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.5340871810913086})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.3973388671875})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.5314745903015137})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.848245143890381})
store['active_learning_steps'][48]['training']['best_epoch']=6
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.6217, 'crossentropy': 3.407746875}
store['active_learning_steps'][48]['acquisition']={'indices': [['id', 34012], ['id', 38788], ['id', 18288], ['id', 2733], ['id', 20322]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5299216309876633, 2.7622690315774405, 3.6265133656324675, 4.136145245043005, 4.401410530400758]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.002760648727417})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.7080531120300293})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.950411319732666})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.2985808849334717})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.4549684524536133})
store['active_learning_steps'][49]['training']['best_epoch']=2
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.6127, 'crossentropy': 2.790596484375}
store['active_learning_steps'][49]['acquisition']={'indices': [['id', 2284], ['id', 52544], ['id', 32459], ['id', 37863], ['id', 22679]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.32103187016678, 2.4418746441481662, 3.2643975638461944, 3.8100397917620246, 4.15468414306843]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.906656265258789})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 2.759064197540283})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.7076425552368164})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.8033480644226074})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.8077614307403564})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 2.991267204284668})
store['active_learning_steps'][50]['training']['best_epoch']=3
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.6169, 'crossentropy': 2.7630435546875}
store['active_learning_steps'][50]['acquisition']={'indices': [['id', 44520], ['id', 53956], ['id', 16309], ['id', 47912], ['id', 29311]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.380976539507122, 2.599398210519432, 3.4911885264532607, 4.032656923856478, 4.317210434269608]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 2.144285202026367})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.5703125, 'crossentropy': 2.7882421016693115})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.2017698287963867})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.499974250793457})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.491267681121826})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.604832172393799})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.216942310333252})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 4.219142436981201})
store['active_learning_steps'][51]['training']['best_epoch']=5
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.6072, 'crossentropy': 3.374919921875}
store['active_learning_steps'][51]['acquisition']={'indices': [['id', 38788], ['id', 39414], ['id', 37995], ['id', 35832], ['id', 35452]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5415728776754574, 2.805141168355109, 3.6431622081976833, 4.142517694962317, 4.398034579524612]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.3143255710601807})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.9767274856567383})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.107560157775879})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.0951290130615234})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.3872618675231934})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.7350151538848877})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.5801239013671875})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.398711919784546})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.5448083877563477})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.76784086227417})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.532667636871338})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.716423988342285})
store['active_learning_steps'][52]['training']['best_epoch']=9
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.6365, 'crossentropy': 3.72571640625}
store['active_learning_steps'][52]['acquisition']={'indices': [['id', 20013], ['id', 27302], ['id', 19044], ['id', 24484], ['id', 20050]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.522254995228727, 2.7245649791665354, 3.6546210216681043, 4.173425260776803, 4.408638211319749]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.130002021789551})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.606658458709717})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.9119272232055664})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.155385971069336})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.338996410369873})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.412438154220581})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.342151165008545})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.206131935119629})
store['active_learning_steps'][53]['training']['best_epoch']=5
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.6231, 'crossentropy': 3.475059375}
store['active_learning_steps'][53]['acquisition']={'indices': [['id', 4799], ['id', 54805], ['id', 18324], ['id', 33007], ['id', 26444]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5570341696843535, 2.786569821906145, 3.6453368872138956, 4.153748221242415, 4.395138123427967]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.0673317909240723})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.3387062549591064})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.802755355834961})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.1008923053741455})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 2.882406711578369})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.964045763015747})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.318554401397705})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.54959774017334})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.4159650802612305})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.2059876918792725})
store['active_learning_steps'][54]['training']['best_epoch']=7
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.6086, 'crossentropy': 3.513325}
