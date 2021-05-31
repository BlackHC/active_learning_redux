store = {}
store['timestamp']=1622112611
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=11']
store['commit']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['github_url']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
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
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 2.5390117168426514})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.0283045768737793})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.287804126739502})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.6477279663085938})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 3.9458885192871094})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.6916303634643555})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.917158603668213})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 4.068984031677246})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.9307594299316406})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 4.089231491088867})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 4.326560020446777})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 4.039659023284912})
store['active_learning_steps'][0]['training']['best_epoch']=9
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6088, 'crossentropy': 4.098341796875}
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 11692], ['ood', 32065], ['ood', 35184], ['ood', 47634], ['id', 18255]], 'labels': [-1, -1, -1, -1, 8], 'scores': [1.58182983351273, 2.837964747771215, 3.6817925935488844, 4.1683227072535844, 4.419933486158909]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 2.937180995941162})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.9978442192077637})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.9345860481262207})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.714029312133789})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.8714683055877686})
store['active_learning_steps'][1]['training']['best_epoch']=2
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.5825, 'crossentropy': 3.4126453125}
store['active_learning_steps'][1]['acquisition']={'indices': [['ood', 28588], ['ood', 24223], ['ood', 4765], ['ood', 59747], ['ood', 31020]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5320229378548555, 2.668267018554889, 3.5332523669596885, 4.082347082283038, 4.351073416912931]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 2.3807973861694336})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.9546189308166504})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.383645534515381})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.2807042598724365})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.902728319168091})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.7264599800109863})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 3.5072078704833984})
store['active_learning_steps'][2]['training']['best_epoch']=4
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6001, 'crossentropy': 3.5924125}
store['active_learning_steps'][2]['acquisition']={'indices': [['ood', 23474], ['ood', 30454], ['ood', 49889], ['ood', 22531], ['ood', 57488]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4025955327575963, 2.569342793118361, 3.4990108064012464, 4.06530238646135, 4.350535778252275]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.4171855449676514})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.1625800132751465})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.8493146896362305})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.957681655883789})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.230752944946289})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.353015422821045})
store['active_learning_steps'][3]['training']['best_epoch']=3
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6043, 'crossentropy': 3.348694140625}
store['active_learning_steps'][3]['acquisition']={'indices': [['ood', 25086], ['ood', 41516], ['ood', 56936], ['ood', 51986], ['id', 27449]], 'labels': [-1, -1, -1, -1, 8], 'scores': [1.6165023784934494, 2.813851358128936, 3.6718767773677055, 4.1519264138296545, 4.393623853523977]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 2.4572815895080566})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.995053291320801})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.2773046493530273})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.5662097930908203})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.616358757019043})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.6101107597351074})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.729274272918701})
store['active_learning_steps'][4]['training']['best_epoch']=4
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.6043, 'crossentropy': 3.660661328125}
store['active_learning_steps'][4]['acquisition']={'indices': [['ood', 20794], ['ood', 45048], ['ood', 51968], ['ood', 4355], ['ood', 11631]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4607879710515395, 2.63900181270701, 3.5214478963915656, 4.051554413424604, 4.331437345090695]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.0549285411834717})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 2.6437368392944336})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.807684898376465})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.119051456451416})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.8447513580322266})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.3395578861236572})
store['active_learning_steps'][5]['training']['best_epoch']=3
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.6116, 'crossentropy': 3.117677734375}
store['active_learning_steps'][5]['acquisition']={'indices': [['ood', 44672], ['ood', 11642], ['ood', 45048], ['ood', 11709], ['ood', 59459]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4761030454562936, 2.6046909503886075, 3.486696311734149, 4.006830553735461, 4.299615221673429]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 2.5963664054870605})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.207707643508911})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.265246868133545})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.3823060989379883})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 3.919762134552002})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.586, 'crossentropy': 3.48308515625}
store['active_learning_steps'][6]['acquisition']={'indices': [['ood', 1239], ['ood', 13129], ['ood', 54092], ['ood', 50910], ['ood', 4759]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.557540842635785, 2.8043707732879755, 3.6977709928658227, 4.148022749754896, 4.381314561192697]}
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
store['active_learning_steps'][7]['acquisition']={'indices': [['ood', 55476], ['ood', 8357], ['ood', 45048], ['ood', 29638], ['ood', 49448]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4774714554514068, 2.701310930506221, 3.5430229664337425, 4.065914021370902, 4.336274046133578]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.0611839294433594})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.7444326877593994})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.8308968544006348})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.0628654956817627})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.3391151428222656})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.9582629203796387})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.3005242347717285})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 3.1725237369537354})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 3.3226242065429688})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.203705310821533})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.411487579345703})
store['active_learning_steps'][8]['training']['best_epoch']=8
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.6318, 'crossentropy': 3.1898158203125}
store['active_learning_steps'][8]['acquisition']={'indices': [['ood', 42595], ['ood', 25180], ['ood', 8611], ['ood', 18416], ['ood', 32355]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5366166319139376, 2.6910934160120252, 3.5799794588489666, 4.097082501609089, 4.364285300240484]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.386310577392578})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.717834711074829})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 3.131277084350586})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.7355237007141113})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.6261816024780273})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.928565502166748})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 4.088595867156982})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.4872641563415527})
store['active_learning_steps'][9]['training']['best_epoch']=5
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.5874, 'crossentropy': 3.797116015625}
store['active_learning_steps'][9]['acquisition']={'indices': [['ood', 48545], ['ood', 56866], ['ood', 34481], ['ood', 20903], ['ood', 19895]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5492856666822978, 2.8540454640031054, 3.7149124329055985, 4.1722624132754635, 4.390432576286731]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.50931453704834})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.2213757038116455})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.627528429031372})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.6951749324798584})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.958474636077881})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.7890632152557373})
store['active_learning_steps'][10]['training']['best_epoch']=3
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.5984, 'crossentropy': 3.504053515625}
store['active_learning_steps'][10]['acquisition']={'indices': [['ood', 10589], ['ood', 37830], ['ood', 59426], ['id', 17482], ['ood', 36166]], 'labels': [-1, -1, -1, 5, -1], 'scores': [1.3632081617446863, 2.53387275541593, 3.3808116890058084, 3.908282151220681, 4.22781155073493]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 2.512575626373291})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.2207179069519043})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.231220245361328})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.161221504211426})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.2285995483398438})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.724447250366211})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 4.139650821685791})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 4.13338565826416})
store['active_learning_steps'][11]['training']['best_epoch']=5
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.6088, 'crossentropy': 3.64063515625}
store['active_learning_steps'][11]['acquisition']={'indices': [['ood', 42697], ['ood', 54403], ['ood', 44836], ['ood', 33659], ['ood', 22607]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5796493259662725, 2.7985646439053316, 3.654600487409205, 4.131373637142621, 4.389280194520888]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 2.2883942127227783})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.9444503784179688})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.1494898796081543})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.5821521282196045})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.3763158321380615})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.5427441596984863})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.6946310997009277})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 4.144687652587891})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 4.264612197875977})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 4.163941383361816})
store['active_learning_steps'][12]['training']['best_epoch']=7
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.6182, 'crossentropy': 3.928048046875}
store['active_learning_steps'][12]['acquisition']={'indices': [['ood', 12972], ['ood', 48323], ['ood', 32126], ['ood', 8571], ['ood', 48420]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6249982276958643, 2.863921905861993, 3.6702557879222617, 4.190533371655283, 4.422331602030802]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.1767208576202393})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.9437079429626465})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.0899956226348877})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.134429454803467})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.438563823699951})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.1167922019958496})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.396733045578003})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.450653314590454})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.5848889350891113})
store['active_learning_steps'][13]['training']['best_epoch']=6
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6122, 'crossentropy': 3.301398828125}
store['active_learning_steps'][13]['acquisition']={'indices': [['ood', 48706], ['ood', 45057], ['ood', 44737], ['ood', 47260], ['ood', 14823]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5541497790482914, 2.785970618561115, 3.696612861444838, 4.170019776150722, 4.4007273613400395]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.1772093772888184})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.345630168914795})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.1814684867858887})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.2389798164367676})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.854525566101074})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.2157347202301025})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.5181760787963867})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 4.240118980407715})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.8884313106536865})
store['active_learning_steps'][14]['training']['best_epoch']=6
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.6069, 'crossentropy': 3.54150546875}
store['active_learning_steps'][14]['acquisition']={'indices': [['ood', 17850], ['ood', 27752], ['ood', 29908], ['ood', 12758], ['ood', 49824]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6372370372513791, 2.8430230875017704, 3.7215635683315416, 4.194406112133393, 4.414750262997025]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 2.871966600418091})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 3.325226306915283})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.633274555206299})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 3.5494375228881836})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.824535369873047})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 4.024896621704102})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 4.540606498718262})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 3.992009162902832})
store['active_learning_steps'][15]['training']['best_epoch']=5
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.584, 'crossentropy': 4.277838671875}
store['active_learning_steps'][15]['acquisition']={'indices': [['ood', 18092], ['ood', 18324], ['ood', 32329], ['ood', 45056], ['ood', 56900]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5752457107610027, 2.699771711627221, 3.5910070399058363, 4.095980864950539, 4.349270819665789]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.721658706665039})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 3.248474597930908})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.85986590385437})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 4.129761695861816})
store['active_learning_steps'][16]['training']['best_epoch']=1
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.594, 'crossentropy': 2.6847138671875}
store['active_learning_steps'][16]['acquisition']={'indices': [['ood', 14715], ['ood', 21882], ['ood', 26752], ['ood', 42934], ['id', 36091]], 'labels': [-1, -1, -1, -1, 2], 'scores': [1.2668547963531567, 2.3151054322525306, 3.085012293636611, 3.6258530769710227, 3.97784349533098]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.3506202697753906})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.26688289642334})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.7631359100341797})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.860616683959961})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.5661849975585938})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.843445301055908})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.776212692260742})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.949174404144287})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.5417885780334473})
store['active_learning_steps'][17]['training']['best_epoch']=6
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.6141, 'crossentropy': 4.11408203125}
store['active_learning_steps'][17]['acquisition']={'indices': [['ood', 55084], ['ood', 41426], ['ood', 29132], ['ood', 4733], ['ood', 36231]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5100199992596102, 2.76202219816029, 3.651648985818653, 4.145292714825707, 4.398172743318845]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.1415295600891113})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.90350079536438})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.3583104610443115})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.224625587463379})
store['active_learning_steps'][18]['training']['best_epoch']=1
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.609, 'crossentropy': 2.16708359375}
store['active_learning_steps'][18]['acquisition']={'indices': [['ood', 35312], ['ood', 325], ['ood', 1682], ['ood', 13052], ['ood', 10986]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3364580299586728, 2.3378090860746505, 3.1340115862871105, 3.704086943360336, 4.0532375374863046]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.101942539215088})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.826845645904541})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.1136624813079834})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.0022315979003906})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.2555112838745117})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.5357751846313477})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.2893059253692627})
store['active_learning_steps'][19]['training']['best_epoch']=4
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6085, 'crossentropy': 3.31773984375}
store['active_learning_steps'][19]['acquisition']={'indices': [['ood', 44901], ['ood', 34645], ['ood', 57148], ['ood', 35158], ['ood', 5909]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4981359295265693, 2.71683907018425, 3.566197810570899, 4.071241412550185, 4.345431717203536]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.165973663330078})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.7958884239196777})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.0646462440490723})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.088738203048706})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.052712917327881})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.354686737060547})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.2293972969055176})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.2283754348754883})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.352156639099121})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.2322723865509033})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.0886499881744385})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.9367995262145996})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.300868272781372})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.0309178829193115})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.5739288330078125})
store['active_learning_steps'][20]['training']['best_epoch']=12
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.633, 'crossentropy': 3.417319140625}
store['active_learning_steps'][20]['acquisition']={'indices': [['ood', 14801], ['ood', 40455], ['ood', 27719], ['ood', 37740], ['ood', 53949]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6110928904909652, 2.8767660215255404, 3.7103360120193845, 4.171740321224325, 4.416462782881128]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.4214229583740234})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.552766799926758})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 3.0928707122802734})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.0250096321105957})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.5093512535095215})
store['active_learning_steps'][21]['training']['best_epoch']=2
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.6342, 'crossentropy': 2.8816279296875}
store['active_learning_steps'][21]['acquisition']={'indices': [['ood', 54805], ['ood', 2773], ['ood', 57516], ['ood', 11184], ['ood', 36281]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4410492881051367, 2.642415406466643, 3.543674971690681, 4.045711701212785, 4.316348471146975]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.207303524017334})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.4399912357330322})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.890723705291748})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.1847219467163086})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.65177321434021})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.529508590698242})
store['active_learning_steps'][22]['training']['best_epoch']=3
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.6209, 'crossentropy': 3.0608951171875}
store['active_learning_steps'][22]['acquisition']={'indices': [['ood', 45329], ['ood', 17652], ['ood', 14673], ['ood', 32399], ['ood', 16600]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3649995314745185, 2.520465866456208, 3.3483874984991537, 3.9189033886647877, 4.2303051041606885]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.360548496246338})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.611449718475342})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.7580583095550537})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.157113790512085})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.438821792602539})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.7380003929138184})
store['active_learning_steps'][23]['training']['best_epoch']=3
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.6199, 'crossentropy': 3.2296119140625}
store['active_learning_steps'][23]['acquisition']={'indices': [['ood', 42934], ['ood', 4727], ['ood', 35930], ['ood', 22531], ['ood', 44805]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4513082169893918, 2.6193806592390136, 3.4805004037729166, 3.9916501798162196, 4.2852500335043135]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.2344963550567627})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.765286922454834})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.0069680213928223})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.2815685272216797})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.3640382289886475})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.4803285598754883})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.5486583709716797})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.7774100303649902})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.640928268432617})
store['active_learning_steps'][24]['training']['best_epoch']=6
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.6339, 'crossentropy': 3.6469875}
store['active_learning_steps'][24]['acquisition']={'indices': [['ood', 43513], ['ood', 6890], ['ood', 33046], ['ood', 5477], ['ood', 33832]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6479135472755178, 2.9045060082172385, 3.777779306198452, 4.254779859466009, 4.4566460033864]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.4237260818481445})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.7721824645996094})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.409442663192749})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.5920064449310303})
store['active_learning_steps'][25]['training']['best_epoch']=1
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.5989, 'crossentropy': 2.508878125}
store['active_learning_steps'][25]['acquisition']={'indices': [['ood', 6088], ['ood', 24968], ['ood', 24587], ['id', 50403], ['id', 17985]], 'labels': [-1, -1, -1, 0, 5], 'scores': [1.2036944800292098, 2.274108757948243, 3.0701457528966607, 3.5821380593881305, 3.9563647402729103]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.1662395000457764})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.857288122177124})
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
store['active_learning_steps'][26]['acquisition']={'indices': [['ood', 44836], ['ood', 28967], ['ood', 50636], ['ood', 24821], ['ood', 18324]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5965185547462393, 2.808117887424925, 3.7025939870617126, 4.200841588556431, 4.436012865564814]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.137399911880493})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.71547269821167})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.799503803253174})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 3.088212490081787})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.2914299964904785})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.2788360118865967})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 3.5116517543792725})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.6433, 'crossentropy': 3.0560755859375}
store['active_learning_steps'][27]['acquisition']={'indices': [['ood', 59389], ['ood', 27051], ['ood', 40980], ['id', 11823], ['ood', 8238]], 'labels': [-1, -1, -1, 6, -1], 'scores': [1.5215058893854398, 2.7374945430616067, 3.627623107819659, 4.1004138464629225, 4.357019221066132]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.0702064037323})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.577916145324707})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.6918044090270996})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.745711326599121})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 3.251859664916992})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.069202184677124})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.2897915840148926})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.2298574447631836})
store['active_learning_steps'][28]['training']['best_epoch']=5
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.627, 'crossentropy': 3.466902734375}
store['active_learning_steps'][28]['acquisition']={'indices': [['ood', 14715], ['ood', 36427], ['ood', 25051], ['ood', 39059], ['ood', 48437]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.559047259842234, 2.8051330536776726, 3.6615523353262533, 4.158316829571204, 4.402189147750221]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 2.2171645164489746})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.493140697479248})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.295924663543701})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.2058401107788086})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.5183095932006836})
store['active_learning_steps'][29]['training']['best_epoch']=2
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.6193, 'crossentropy': 2.7331333984375}
store['active_learning_steps'][29]['acquisition']={'indices': [['ood', 3657], ['ood', 37665], ['ood', 4827], ['ood', 54288], ['ood', 48029]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3623925817577467, 2.5958819342793458, 3.4241926809478107, 3.9651260841133755, 4.259748736496617]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.083664894104004})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.6337151527404785})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.032662868499756})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.313974380493164})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.586544990539551})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.535421848297119})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.423600196838379})
store['active_learning_steps'][30]['training']['best_epoch']=4
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.6258, 'crossentropy': 3.310098046875}
store['active_learning_steps'][30]['acquisition']={'indices': [['ood', 4833], ['ood', 48463], ['ood', 24740], ['ood', 4741], ['ood', 26417]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.502135758365408, 2.6937635943273484, 3.5811745028800797, 4.110556992240538, 4.375085930274036]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 2.1363682746887207})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.6306557655334473})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.950369358062744})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.9277892112731934})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.400698661804199})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.6081929206848145})
store['active_learning_steps'][31]['training']['best_epoch']=3
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.6123, 'crossentropy': 3.17929296875}
store['active_learning_steps'][31]['acquisition']={'indices': [['ood', 46864], ['ood', 32776], ['ood', 42309], ['ood', 32351], ['ood', 29852]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4806513998231452, 2.6357838960115423, 3.514983041427114, 4.040352858920315, 4.335696319624532]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 2.117523670196533})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 2.711193084716797})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.578765869140625})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.0699219703674316})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.9984869956970215})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.257692813873291})
store['active_learning_steps'][32]['training']['best_epoch']=3
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.6194, 'crossentropy': 2.8129859375}
store['active_learning_steps'][32]['acquisition']={'indices': [['ood', 56416], ['ood', 11598], ['ood', 14819], ['ood', 17728], ['ood', 2773]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3678812274775425, 2.5080432641090074, 3.4061806307418285, 3.983119448874266, 4.301780717532601]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 2.2077126502990723})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.7828094959259033})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.028057336807251})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.4117136001586914})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.4262213706970215})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.3683104515075684})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.863654851913452})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.8785462379455566})
store['active_learning_steps'][33]['training']['best_epoch']=5
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.6344, 'crossentropy': 3.432862890625}
store['active_learning_steps'][33]['acquisition']={'indices': [['ood', 37212], ['ood', 25419], ['ood', 15660], ['ood', 39260], ['ood', 27991]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4960276527167464, 2.7075477123314844, 3.5698021666265287, 4.116022955286539, 4.364662617059322]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.012845993041992})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.7376210689544678})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.8657915592193604})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.856957197189331})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.7657265663146973})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.791510820388794})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.9911065101623535})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.0590977668762207})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.1841588020324707})
store['active_learning_steps'][34]['training']['best_epoch']=6
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.6392, 'crossentropy': 2.8869373046875}
store['active_learning_steps'][34]['acquisition']={'indices': [['ood', 32776], ['ood', 4799], ['ood', 40515], ['ood', 25091], ['id', 23444]], 'labels': [-1, -1, -1, -1, 2], 'scores': [1.4684045490621607, 2.6288568403979684, 3.538542273087579, 4.056509005686171, 4.3373453582184425]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.8548579216003418})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.605696678161621})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.9944519996643066})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.9734528064727783})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.1344351768493652})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.985757827758789})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.871791362762451})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.406858444213867})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.933699131011963})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.7947843074798584})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 3.250561475753784})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.7698488235473633})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.9945554733276367})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.528268575668335})
store['active_learning_steps'][35]['training']['best_epoch']=11
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.6316, 'crossentropy': 3.647646484375}
store['active_learning_steps'][35]['acquisition']={'indices': [['ood', 19927], ['ood', 37084], ['ood', 51151], ['ood', 32039], ['ood', 19945]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6252305225225179, 2.8964606799616877, 3.768141765868391, 4.264216405151878, 4.456250610966894]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 2.540070056915283})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.1575567722320557})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.360386371612549})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 3.1940157413482666})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.6979918479919434})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 3.8869664669036865})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.6624832153320312})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.601529121398926})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 3.9840071201324463})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.963376522064209})
store['active_learning_steps'][36]['training']['best_epoch']=7
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.6097, 'crossentropy': 3.81951640625}
store['active_learning_steps'][36]['acquisition']={'indices': [['ood', 32056], ['ood', 50294], ['ood', 42678], ['ood', 33250], ['ood', 28215]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.441629651183244, 2.6431226256085574, 3.5427792468672052, 4.0771524547815465, 4.354400448816201]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.9400441646575928})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.427051067352295})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.592672824859619})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.124103546142578})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.1316475868225098})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.1301071643829346})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.3710687160491943})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.139000415802002})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.49216365814209})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.2004055976867676})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.4701972007751465})
store['active_learning_steps'][37]['training']['best_epoch']=8
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.6382, 'crossentropy': 3.29038359375}
store['active_learning_steps'][37]['acquisition']={'indices': [['ood', 33010], ['ood', 54805], ['ood', 28081], ['ood', 49058], ['ood', 10632]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4784967649081289, 2.7237289050541067, 3.611916111999345, 4.148249438502696, 4.381379964065955]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 2.2575221061706543})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.4953413009643555})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.6895432472229004})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.423748016357422})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.368673086166382})
store['active_learning_steps'][38]['training']['best_epoch']=2
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.6253, 'crossentropy': 2.7730619140625}
store['active_learning_steps'][38]['acquisition']={'indices': [['ood', 53956], ['ood', 5536], ['ood', 40471], ['ood', 10620], ['ood', 32776]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3908839857271644, 2.5263520479229022, 3.315909346567384, 3.8350949922567237, 4.15801408074975]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.7974510192871094})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.343465805053711})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.030282497406006})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.8161611557006836})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.085228443145752})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.5407967567443848})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.9755306243896484})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.1860506534576416})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.237525701522827})
store['active_learning_steps'][39]['training']['best_epoch']=6
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.6174, 'crossentropy': 3.537986328125}
store['active_learning_steps'][39]['acquisition']={'indices': [['ood', 13682], ['ood', 54068], ['ood', 56567], ['ood', 20960], ['ood', 9531]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4617298158857392, 2.630035796005644, 3.531480166279165, 4.043174216303664, 4.320929642222081]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.0601446628570557})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.5376739501953125})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.900482654571533})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.5816397666931152})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.0325658321380615})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.1580214500427246})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.198859214782715})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.1990952491760254})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.03043794631958})
store['active_learning_steps'][40]['training']['best_epoch']=6
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.627, 'crossentropy': 3.392209375}
store['active_learning_steps'][40]['acquisition']={'indices': [['ood', 2652], ['ood', 38733], ['ood', 3950], ['ood', 35230], ['ood', 35184]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5463338891784972, 2.7740476520263178, 3.5865301745946603, 4.067581070909325, 4.355653923345329]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 2.1334352493286133})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 2.7266035079956055})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.0685484409332275})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.214449405670166})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.4353864192962646})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.301697254180908})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.758528709411621})
store['active_learning_steps'][41]['training']['best_epoch']=4
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.5959, 'crossentropy': 3.42139921875}
store['active_learning_steps'][41]['acquisition']={'indices': [['ood', 23041], ['ood', 47260], ['ood', 19893], ['ood', 4646], ['ood', 4717]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.538740997095886, 2.707967073462993, 3.499144511420109, 4.038741006723631, 4.315784157539114]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.9982366561889648})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 2.7562618255615234})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.807615280151367})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.3326807022094727})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.404897689819336})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.3001747131347656})
store['active_learning_steps'][42]['training']['best_epoch']=3
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.6138, 'crossentropy': 2.97328671875}
store['active_learning_steps'][42]['acquisition']={'indices': [['ood', 53956], ['ood', 55739], ['ood', 59453], ['ood', 34708], ['ood', 3200]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4741748728248354, 2.5477170603861925, 3.3770476239891165, 3.9111745971120335, 4.231328426374093]}
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
store['active_learning_steps'][43]['acquisition']={'indices': [['ood', 1674], ['ood', 43760], ['ood', 9468], ['id', 51163], ['ood', 25293]], 'labels': [-1, -1, -1, 0, -1], 'scores': [1.515483184259058, 2.7444457219215015, 3.594124168930356, 4.116473362691399, 4.3815714452500245]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.135256052017212})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.5392565727233887})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.6264095306396484})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.105377674102783})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.114640951156616})
store['active_learning_steps'][44]['training']['best_epoch']=2
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.616, 'crossentropy': 2.61153515625}
store['active_learning_steps'][44]['acquisition']={'indices': [['ood', 36187], ['ood', 4360], ['ood', 4785], ['ood', 1227], ['ood', 24011]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3219827779130746, 2.4043448704287558, 3.2313267468670075, 3.8065566095929393, 4.1387423858133285]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 2.2897679805755615})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.7693030834198})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 3.248997449874878})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.2708544731140137})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.2512764930725098})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.2929399013519287})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.4294259548187256})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.6953768730163574})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.730595111846924})
store['active_learning_steps'][45]['training']['best_epoch']=6
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.6179, 'crossentropy': 3.73714609375}
store['active_learning_steps'][45]['acquisition']={'indices': [['ood', 53956], ['ood', 43294], ['ood', 59878], ['ood', 26752], ['ood', 41937]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.441736777582821, 2.6385713648806974, 3.512812471630701, 4.064765936192365, 4.331148189852697]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.9424502849578857})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.50258207321167})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.872617244720459})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.152595043182373})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.0242109298706055})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.186007022857666})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.538780450820923})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.388212203979492})
store['active_learning_steps'][46]['training']['best_epoch']=5
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.6223, 'crossentropy': 3.0325703125}
store['active_learning_steps'][46]['acquisition']={'indices': [['ood', 36283], ['ood', 40157], ['ood', 48029], ['ood', 13241], ['ood', 23347]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4861200496483782, 2.7396501041371337, 3.564770187079163, 4.071492817328212, 4.34328719477735]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.410972833633423})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.737398624420166})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 3.0162439346313477})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 3.9452147483825684})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 4.260731220245361})
store['active_learning_steps'][47]['training']['best_epoch']=2
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.5997, 'crossentropy': 2.846359765625}
store['active_learning_steps'][47]['acquisition']={'indices': [['ood', 44377], ['ood', 27302], ['ood', 23162], ['ood', 18092], ['ood', 24740]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4403584910399405, 2.6101995074197326, 3.525781353663657, 4.04032161706491, 4.303393826830841]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.0139169692993164})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 2.7446916103363037})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.943131446838379})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.2073676586151123})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.4550747871398926})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.5340871810913086})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.397339344024658})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.5314745903015137})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.848245143890381})
store['active_learning_steps'][48]['training']['best_epoch']=6
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.6217, 'crossentropy': 3.407746875}
store['active_learning_steps'][48]['acquisition']={'indices': [['ood', 34012], ['ood', 38788], ['ood', 18288], ['ood', 2733], ['ood', 20322]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.529921632937512, 2.762269029674286, 3.6265133589858767, 4.136145227768811, 4.401410503733182]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.002760648727417})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.7080531120300293})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.950411319732666})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.298581123352051})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.4549684524536133})
store['active_learning_steps'][49]['training']['best_epoch']=2
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.6127, 'crossentropy': 2.790596484375}
store['active_learning_steps'][49]['acquisition']={'indices': [['ood', 2284], ['ood', 52544], ['ood', 32459], ['ood', 37863], ['ood', 22679]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3210318716001597, 2.441874640945591, 3.2643975572931643, 3.8100397702930966, 4.154684121025808]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.9066563844680786})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 2.7590644359588623})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.7076425552368164})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.8033480644226074})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.8077614307403564})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 2.991267204284668})
store['active_learning_steps'][50]['training']['best_epoch']=3
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.6169, 'crossentropy': 2.7630435546875}
store['active_learning_steps'][50]['acquisition']={'indices': [['ood', 44520], ['ood', 53956], ['ood', 16309], ['ood', 47912], ['ood', 29311]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.380976538982514, 2.599398207151619, 3.4911885196244645, 4.032656913366871, 4.3172104150763335]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 2.144285202026367})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.5703125, 'crossentropy': 2.7882423400878906})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.2017698287963867})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.499974250793457})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.491267681121826})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.604832172393799})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.216942310333252})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 4.219141960144043})
store['active_learning_steps'][51]['training']['best_epoch']=5
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.6072, 'crossentropy': 3.374919921875}
store['active_learning_steps'][51]['acquisition']={'indices': [['ood', 38788], ['ood', 39414], ['ood', 37995], ['ood', 35832], ['ood', 35452]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5415728765152346, 2.8051411621986153, 3.6431622023105845, 4.1425176860058786, 4.398034577470584]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.3143255710601807})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.9767274856567383})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.107560396194458})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.0951290130615234})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.3872618675231934})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.7350151538848877})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.5801239013671875})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.398711919784546})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.5448083877563477})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.76784086227417})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.532667398452759})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.716423988342285})
store['active_learning_steps'][52]['training']['best_epoch']=9
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.6365, 'crossentropy': 3.72571640625}
store['active_learning_steps'][52]['acquisition']={'indices': [['ood', 20013], ['ood', 27302], ['ood', 19044], ['ood', 24484], ['ood', 20050]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5222549926337967, 2.7245649727187002, 3.654621024186909, 4.173425254848928, 4.408638236531913]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.130002021789551})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.606658458709717})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.9119272232055664})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.155385971069336})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.338995933532715})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.41243839263916})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.3421506881713867})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.206132173538208})
store['active_learning_steps'][53]['training']['best_epoch']=5
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.6231, 'crossentropy': 3.475058984375}
store['active_learning_steps'][53]['acquisition']={'indices': [['ood', 4799], ['ood', 54805], ['ood', 18324], ['ood', 33007], ['ood', 26444]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.557034169338071, 2.7865698145850586, 3.64533686412053, 4.153748179064835, 4.395138087180274]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.0673317909240723})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.3387062549591064})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.80275559425354})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.1008920669555664})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 2.882406711578369})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.964045763015747})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.318554162979126})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.54959774017334})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.4159650802612305})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.2059879302978516})
store['active_learning_steps'][54]['training']['best_epoch']=7
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.6086, 'crossentropy': 3.513325}
