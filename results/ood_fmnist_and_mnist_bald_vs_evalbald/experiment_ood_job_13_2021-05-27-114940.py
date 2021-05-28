store = {}
store['timestamp']=1622112580
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=13']
store['commit']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['github_url']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=13
store['worker_id']=13
store['num_workers']=80
store['config']={'seed': 1247, 'uniform_ood': True, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 256, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('FastMNIST Train (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 40646, 10110, 32775, 33736, 27254, 306, 37354, 19689, 57811, 34482, 15494, 19215, 18819, 11554, 8108, 29048, 30362, 48953, 5588, 8719, 48602, 33140, 46397, 56710, 14640, 39579, 5573, 5715, 47420, 27135, 26129, 16927, 39050, 42295, 51555, 51600, 43234, 33891, 20917, 38856, 17032, 13036, 11228, 46700, 50498, 40741, 9834, 24971, 17759, 45567, 2728, 1774, 33486, 43252, 43803, 50036, 46861, 53831, 54003, 53362, 229, 767, 36270, 10432, 23451, 6612, 8710, 41077, 48498, 46683, 45260, 37098, 55148, 49775, 52801, 15969, 57520, 36797, 34198, 27145, 3029, 37047, 31965, 26501, 48519, 5803, 43415, 35794, 33581, 5897, 27573, 30980, 29614, 35237, 51755, 57690, 26516, 5380, 25589, 53689, 31444, 29950, 44803, 396, 56990, 24052, 12108, 54426, 42320, 35072, 21536, 49304, 49595, 44428, 72, 57175, 52679, 41082, 30184, 54017, 10232, 17968, 31935, 43587, 801, 48031, 2206, 2404, 58741, 29079, 49986, 46464, 17659, 30072, 39879, 29556, 52389, 13092, 37129, 11773, 15822, 37625, 7382, 7121, 17195, 32625, 43141, 28181, 50055, 55187, 34588, 38725, 50466, 40018, 37115, 20801, 23496, 4321, 42102, 12075, 54012, 28833, 18880, 26520, 27580, 14637, 40466, 54800, 24110, 13859, 51027, 45005, 57541, 34361, 26479, 43321, 44048, 45974, 15675, 10508, 49549, 28991, 13074, 9574, 44454, 36688, 8821, 12610, 54422, 34121, 27019, 21800, 44138, 36367, 44100, 33464, 51760, 15917, 495, 50997, 48032, 40334, 21423, 46870, 18137, 4701, 18693, 17506, 6968, 13359, 35372, 7356, 2289, 55733, 5481, 37157, 56054, 2400, 56137, 1005, 56096, 53538, 55783, 37709, 3792, 10664, 5616, 32972, 30013, 19757, 49169, 47417, 38430, 41512, 14035, 35714, 16068, 20076, 26853, 26428, 48521, 11261, 12917, 257, 43981, 8705, 27383, 10113, 7896]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.2398428916931152})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.6114959716796875})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.7276222705841064})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.416717052459717})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.5967, 'crossentropy': 2.317501953125}
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 7909], ['ood', 45048], ['ood', 11166], ['id', 55778], ['ood', 58471]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [1.2607522664877484, 2.283134657936516, 3.1187576345388965, 3.6575453434170475, 4.019580735650797]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.8011596202850342})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 2.548109531402588})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.7235116958618164})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.0106492042541504})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.07090425491333})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.1573731899261475})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.495793581008911})
store['active_learning_steps'][1]['training']['best_epoch']=4
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.5938, 'crossentropy': 2.8976130859375}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 47659], ['ood', 37258], ['id', 23066], ['id', 25701], ['id', 4791]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0462813458401792, 1.9367518646587518, 2.689493455590352, 3.265839765883154, 3.698567907046451]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.3399078845977783})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.9002208709716797})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.207580089569092})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.9846758842468262})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.3991053104400635})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.5868303775787354})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.4800703525543213})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.49252986907959})
store['active_learning_steps'][2]['training']['best_epoch']=5
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6198, 'crossentropy': 2.588861328125}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 1799], ['id', 13195], ['id', 987], ['id', 53914], ['ood', 36289]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [1.0127079319543935, 1.8998094583849583, 2.633080560306304, 3.23941452542636, 3.7050999092621257]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.5518169403076172})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.9734926223754883})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 2.478121519088745})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 2.609157085418701})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.7425193786621094})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.724996566772461})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.5989456176757812})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.751878499984741})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.6431422233581543})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.6349244117736816})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.228787899017334})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.9129981994628906})
store['active_learning_steps'][3]['training']['best_epoch']=9
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6101, 'crossentropy': 2.801396875}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 30703], ['id', 36568], ['id', 49224], ['id', 33574], ['id', 36456]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [1.0108037599451738, 1.871390890724299, 2.636177499285962, 3.252920939285925, 3.695343931162377]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.4334944486618042})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.8560817241668701})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 2.133051872253418})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 2.343008518218994})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.8272600173950195})
store['active_learning_steps'][4]['training']['best_epoch']=2
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.5953, 'crossentropy': 1.996526953125}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 50210], ['id', 31904], ['id', 42487], ['id', 19651], ['id', 41243]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.8924587286309815, 1.6235144628330298, 2.2853543966681222, 2.811474203043262, 3.244981075843504]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.337611198425293})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.6411985158920288})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.968139886856079})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.243656635284424})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.0465331077575684})
store['active_learning_steps'][5]['training']['best_epoch']=2
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.6358, 'crossentropy': 1.7141576171875}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 46518], ['id', 59771], ['id', 20624], ['id', 58300], ['id', 7298]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8505838878470358, 1.6046920623191951, 2.278408233586016, 2.8229424480255787, 3.2597152219588894]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.331323266029358})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.4530067443847656})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.0099637508392334})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.9954307079315186})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.265888214111328})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.4502015113830566})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.129126787185669})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.4034063816070557})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.4910669326782227})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.4423575401306152})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.591035842895508})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.2418293952941895})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.5134410858154297})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.7214510440826416})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.899564743041992})
store['active_learning_steps'][6]['training']['best_epoch']=12
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.643, 'crossentropy': 2.3632150390625}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 749], ['id', 51163], ['id', 20428], ['id', 3301], ['id', 34994]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1624448529874214, 2.0868637349510166, 2.849551097828485, 3.4626884923408854, 3.904306785388629]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.349376916885376})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.4990993738174438})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.7743468284606934})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.971414566040039})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.1517767906188965})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.272709608078003})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.0749406814575195})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.3813300132751465})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.21347975730896})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.413090705871582})
store['active_learning_steps'][7]['training']['best_epoch']=7
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.6399, 'crossentropy': 2.1901556640625}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 53134], ['id', 45262], ['id', 22069], ['id', 48804], ['id', 15274]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0428502823391987, 2.0170553492383663, 2.821275746380774, 3.425580037482388, 3.8459027981132596]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.3872506618499756})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.5627127885818481})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.9180132150650024})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.056401491165161})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.478841543197632})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.3454904556274414})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.5628981590270996})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.4821736812591553})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.7825160026550293})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.935126781463623})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.945415496826172})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.670623302459717})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.5249509811401367})
store['active_learning_steps'][8]['training']['best_epoch']=10
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.6315, 'crossentropy': 3.2155337890625}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 19566], ['id', 47728], ['id', 29482], ['id', 35913], ['id', 5192]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.040929869797003, 1.9854024922378035, 2.796718410603442, 3.430383953474493, 3.869153701398517]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.2369862794876099})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.477359414100647})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.6893203258514404})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.05263614654541})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.985389232635498})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.010941743850708})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.167118787765503})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.205719470977783})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.3296544551849365})
store['active_learning_steps'][9]['training']['best_epoch']=6
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.6519, 'crossentropy': 2.245355859375}
store['active_learning_steps'][9]['acquisition']={'indices': [['ood', 11476], ['id', 8990], ['id', 43510], ['id', 29012], ['id', 58966]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.8850296391277892, 1.7278079325195748, 2.478625943034044, 3.08124486907753, 3.5405294968230683]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.3130031824111938})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.8124781847000122})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.006298780441284})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.006021499633789})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.0855369567871094})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.2431235313415527})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.513375759124756})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.8175477981567383})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.4061989784240723})
store['active_learning_steps'][10]['training']['best_epoch']=6
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.6397, 'crossentropy': 2.3848087890625}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 49763], ['id', 39279], ['id', 36674], ['id', 32351], ['id', 57132]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8526479761617274, 1.6502784865886797, 2.362558163818048, 2.9786540370854597, 3.451154373720847]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.4304802417755127})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.5350505113601685})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.6869292259216309})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.8558545112609863})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.243586540222168})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.4048643112182617})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.417208671569824})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.2272963523864746})
store['active_learning_steps'][11]['training']['best_epoch']=5
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.631, 'crossentropy': 2.2543150390625}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 37710], ['id', 20390], ['id', 12078], ['id', 18584], ['id', 31587]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.852001737778691, 1.6376852148030148, 2.3392714227929163, 2.955926932581871, 3.451903285925405]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.3109978437423706})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.4221303462982178})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.5417556762695312})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.74113130569458})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.002701759338379})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.8186078071594238})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.171111583709717})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.3721041679382324})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.1012773513793945})
store['active_learning_steps'][12]['training']['best_epoch']=6
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.6538, 'crossentropy': 1.897891796875}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 44606], ['id', 59281], ['id', 35684], ['id', 2767], ['id', 25144]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.9200125219529491, 1.7392022934545959, 2.472684923949231, 3.08257439785592, 3.555705891175732]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.4404451847076416})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.3162341117858887})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.449663758277893})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.5897741317749023})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.6121571063995361})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.8367007970809937})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.1773972511291504})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.9566919803619385})
store['active_learning_steps'][13]['training']['best_epoch']=5
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6622, 'crossentropy': 1.8143318359375}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 17698], ['id', 20348], ['ood', 53528], ['id', 3410], ['ood', 28904]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.9167565649426201, 1.6899245691481708, 2.3869266148583, 2.9731390660485193, 3.4216018302573428]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5458984375, 'crossentropy': 1.4110379219055176})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.3092799186706543})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.5383455753326416})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.6851708889007568})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.8128936290740967})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.9608407020568848})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.9149441719055176})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.1525864601135254})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.21579647064209})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.380824089050293})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.5423312187194824})
store['active_learning_steps'][14]['training']['best_epoch']=8
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.652, 'crossentropy': 2.33308203125}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 54405], ['id', 25060], ['id', 36052], ['id', 21929], ['id', 39272]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0088292860482586, 1.8689740464575184, 2.6398968852673406, 3.2395795185502836, 3.690277646739692]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.3618614673614502})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.2357103824615479})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.541273832321167})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.5223933458328247})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.6356638669967651})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.7105762958526611})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.929152488708496})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.8857088088989258})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.03126859664917})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.9694905281066895})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.9742262363433838})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.8502495288848877})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.176875591278076})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.115927219390869})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.331631660461426})
store['active_learning_steps'][15]['training']['best_epoch']=12
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.6757, 'crossentropy': 2.00638359375}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 26636], ['id', 44144], ['id', 38613], ['id', 7593], ['id', 26279]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [1.0505709065576072, 1.988080560376405, 2.7380290214041505, 3.337735397187757, 3.785283851278132]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 1.400055170059204})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.2972619533538818})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.5225577354431152})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.6264119148254395})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.6969504356384277})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.7850748300552368})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.9107600450515747})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.9520952701568604})
store['active_learning_steps'][16]['training']['best_epoch']=5
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.666, 'crossentropy': 1.79618125}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 46563], ['id', 59651], ['id', 41355], ['id', 27685], ['id', 12428]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9132301560464924, 1.6983524867508262, 2.404949850380401, 2.9765099140523503, 3.4414253495515847]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.3423941135406494})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.3496471643447876})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.347196102142334})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.5458505153656006})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.8553634881973267})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.7345685958862305})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.8177814483642578})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.1787493228912354})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.790763020515442})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.8849445581436157})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.7967119216918945})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.049147605895996})
store['active_learning_steps'][17]['training']['best_epoch']=9
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.7002, 'crossentropy': 1.8252736328125}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 50770], ['id', 36120], ['ood', 16065], ['id', 9968], ['id', 44404]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0211229880753983, 1.8884686907884447, 2.650161660211367, 3.27013933368423, 3.7327379238854643]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.3012988567352295})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.174731969833374})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.1996135711669922})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.3316951990127563})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.5525137186050415})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.6512188911437988})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.5800464153289795})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.8644943237304688})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.8527765274047852})
store['active_learning_steps'][18]['training']['best_epoch']=6
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6922, 'crossentropy': 1.65635}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 55098], ['id', 3694], ['id', 33773], ['id', 55968], ['id', 32738]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7753688969379866, 1.5067683410638102, 2.1776557752281915, 2.7729119980229147, 3.228873676420184]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 1.3470652103424072})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.202584147453308})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.2368767261505127})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.4594731330871582})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.5186947584152222})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.7361319065093994})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.7339988946914673})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.5896828174591064})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.8328661918640137})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.0674619674682617})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.0038633346557617})
store['active_learning_steps'][19]['training']['best_epoch']=8
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6976, 'crossentropy': 1.6867056640625}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 34841], ['id', 29164], ['id', 40187], ['id', 44743], ['id', 21864]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9415037543517295, 1.794115758067468, 2.5614657649304826, 3.144425323620405, 3.584029621157698]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.4931640625, 'crossentropy': 1.525373101234436})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.2790495157241821})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.341766595840454})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.3585714101791382})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.4564173221588135})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.4383025169372559})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.653381586074829})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.808098554611206})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.78273606300354})
store['active_learning_steps'][20]['training']['best_epoch']=6
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.6936, 'crossentropy': 1.6294919921875}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 20643], ['id', 31654], ['id', 39750], ['id', 51688], ['id', 51918]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.9322849292124951, 1.7847457241745106, 2.52126573253031, 3.1270887509499214, 3.5846226978276015]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 1.3871983289718628})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.2250159978866577})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.301973819732666})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.2936649322509766})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.5427672863006592})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.53841233253479})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.680254578590393})
store['active_learning_steps'][21]['training']['best_epoch']=4
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.7007, 'crossentropy': 1.373763671875}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 54352], ['id', 50529], ['id', 50846], ['id', 4436], ['id', 32110]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8166258788602059, 1.550256940177071, 2.2199920746625548, 2.755903954775647, 3.2096973203806805]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.5322265625, 'crossentropy': 1.5070123672485352})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.2061412334442139})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.3101238012313843})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.3612886667251587})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.4042818546295166})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.5101351737976074})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.583183765411377})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.6763536930084229})
store['active_learning_steps'][22]['training']['best_epoch']=5
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.6917, 'crossentropy': 1.52061796875}
store['active_learning_steps'][22]['acquisition']={'indices': [['ood', 6598], ['id', 33141], ['id', 42682], ['id', 29277], ['ood', 31020]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.7885280574497899, 1.5405788460381018, 2.2131236332787703, 2.7881483589467724, 3.2584094047181633]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.3963334560394287})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.1195127964019775})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.1211692094802856})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.2668864727020264})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.2461237907409668})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.38326096534729})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.419935941696167})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.4377782344818115})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.5750653743743896})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.5672121047973633})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.6264121532440186})
store['active_learning_steps'][23]['training']['best_epoch']=8
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.7244, 'crossentropy': 1.50885517578125}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 44841], ['ood', 8593], ['id', 70], ['id', 46619], ['ood', 26882]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [1.0689506182979123, 1.9273659546509827, 2.665682253738341, 3.262221445223269, 3.7054191249436492]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.5517578125, 'crossentropy': 1.3929188251495361})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.1392920017242432})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.1145975589752197})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.2409985065460205})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.317352294921875})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.3258976936340332})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.4675066471099854})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.7090420722961426})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.6040005683898926})
store['active_learning_steps'][24]['training']['best_epoch']=6
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.7103, 'crossentropy': 1.4413451171875}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 4915], ['id', 37441], ['id', 47079], ['id', 35231], ['id', 22547]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.8752241201663606, 1.6339568968144476, 2.3284144572166046, 2.890336978782198, 3.3580641913861102]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 1.423363447189331})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.1316049098968506})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.083109736442566})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.1942155361175537})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.2630517482757568})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.4048585891723633})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.5022633075714111})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.4156025648117065})
store['active_learning_steps'][25]['training']['best_epoch']=5
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.7168, 'crossentropy': 1.36366640625}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 26760], ['id', 47764], ['id', 39951], ['id', 1382], ['id', 41608]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7496660128130839, 1.456307571907423, 2.1150999373121895, 2.678733424587257, 3.134850499821983]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.53125, 'crossentropy': 1.4439760446548462})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.2123985290527344})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.1630656719207764})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.2187525033950806})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.3509092330932617})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.4447851181030273})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.4964423179626465})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.6016733646392822})
store['active_learning_steps'][26]['training']['best_epoch']=5
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.6832, 'crossentropy': 1.42776728515625}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 49891], ['id', 26676], ['id', 3437], ['id', 34739], ['id', 56900]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8032821766388349, 1.475477795975435, 2.092832313957704, 2.6341752621084575, 3.0911618538778622]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.4697265625, 'crossentropy': 1.5157009363174438})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.1912100315093994})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.167872667312622})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.2593683004379272})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.355183482170105})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.6010600328445435})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.5068962574005127})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.5179669857025146})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.6923017501831055})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.7435035705566406})
store['active_learning_steps'][27]['training']['best_epoch']=7
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.6772, 'crossentropy': 1.7021103515625}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 35305], ['id', 8324], ['id', 59860], ['id', 23469], ['id', 46507]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.8609215533283152, 1.6550994006231448, 2.3655606069319424, 2.9608629059598064, 3.4544395933096474]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.435546875, 'crossentropy': 1.6172555685043335})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.2065932750701904})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.1584584712982178})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.1971197128295898})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.2382975816726685})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.3894376754760742})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.4113601446151733})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.439141035079956})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.5074924230575562})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.7309095859527588})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.563614845275879})
store['active_learning_steps'][28]['training']['best_epoch']=8
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.7023, 'crossentropy': 1.5189546875}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 42403], ['id', 24753], ['id', 32394], ['id', 48647], ['id', 54065]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.9052212050296595, 1.6946632609580239, 2.399850103326223, 2.978213723205627, 3.4462996262519834]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.447265625, 'crossentropy': 1.535535454750061})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.1808156967163086})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.1193432807922363})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.1711924076080322})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.1748673915863037})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.324591875076294})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.382951021194458})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.3994615077972412})
store['active_learning_steps'][29]['training']['best_epoch']=5
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.7108, 'crossentropy': 1.23176005859375}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 9924], ['id', 1921], ['id', 36798], ['id', 37829], ['id', 42507]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7894338488215784, 1.4881426179677995, 2.104312634180939, 2.6383673282632243, 3.0823737253770735]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.4697265625, 'crossentropy': 1.5315113067626953})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.2243106365203857})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.1665465831756592})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.144258737564087})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.3725725412368774})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.5836139917373657})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.6245596408843994})
store['active_learning_steps'][30]['training']['best_epoch']=4
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.6915, 'crossentropy': 1.203538671875}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 26217], ['id', 37052], ['id', 1473], ['id', 13598], ['id', 688]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.6390947014306705, 1.1895975008576292, 1.7138083039312804, 2.190718755832142, 2.6279789492878542]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.4619140625, 'crossentropy': 1.5104429721832275})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.2159628868103027})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.1545766592025757})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.139256238937378})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.241584062576294})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.4236102104187012})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.4028162956237793})
store['active_learning_steps'][31]['training']['best_epoch']=4
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.7044, 'crossentropy': 1.19356337890625}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 56781], ['id', 40112], ['id', 36343], ['id', 57751], ['id', 38121]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5791007146505001, 1.1114016514577996, 1.6191538014315077, 2.08999633155758, 2.508884224027055]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.4443359375, 'crossentropy': 1.569275140762329})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.2170127630233765})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.253259301185608})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.2755894660949707})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.1702767610549927})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.3762327432632446})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.472320556640625})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.459691047668457})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.5408689975738525})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.5618479251861572})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.4426655769348145})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.4394396543502808})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.8558409214019775})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.648030400276184})
store['active_learning_steps'][32]['training']['best_epoch']=11
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.7251, 'crossentropy': 1.50928876953125}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 10052], ['id', 1882], ['id', 52556], ['id', 17565], ['id', 51167]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9375686827683569, 1.77749043993302, 2.5079316489408683, 3.1225320861416908, 3.5956565287262316]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.5107421875, 'crossentropy': 1.5123834609985352})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.1181252002716064})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.1418770551681519})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.1918997764587402})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.2301950454711914})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.3069124221801758})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.2505918741226196})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.3507479429244995})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.4163402318954468})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.466160535812378})
store['active_learning_steps'][33]['training']['best_epoch']=7
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.7265, 'crossentropy': 1.3241607421875}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 51071], ['id', 30650], ['ood', 44856], ['id', 58130], ['id', 28390]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8230987738812363, 1.5387597376071445, 2.2005263623592253, 2.7781191657438074, 3.255059351703636]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.4482421875, 'crossentropy': 1.5581634044647217})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.1698756217956543})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.043365478515625})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.1287200450897217})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.1471890211105347})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.2060143947601318})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.313058853149414})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.2534193992614746})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.3944733142852783})
store['active_learning_steps'][34]['training']['best_epoch']=6
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.7249, 'crossentropy': 1.2123826171875}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 54078], ['id', 41547], ['id', 13390], ['id', 28962], ['id', 30540]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7342397175752087, 1.4090601858189085, 2.0173791718928893, 2.5333223519492565, 2.9887707601467035]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.4912109375, 'crossentropy': 1.5031654834747314})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.118410587310791})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.0062671899795532})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.018546223640442})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.1171786785125732})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.0940991640090942})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.1684269905090332})
store['active_learning_steps'][35]['training']['best_epoch']=4
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.7207, 'crossentropy': 1.0727060546875}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 42536], ['ood', 23800], ['id', 47740], ['id', 43291], ['ood', 10417]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.5920278019126475, 1.1514644255761715, 1.6763874944839996, 2.157129076059377, 2.5837196127988884]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.4833984375, 'crossentropy': 1.582902431488037})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.178295612335205})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0750807523727417})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.0751001834869385})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.1540664434432983})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.1312530040740967})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.2284924983978271})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.3023202419281006})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.3572932481765747})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.3871567249298096})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.4399869441986084})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.5484973192214966})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.5817828178405762})
store['active_learning_steps'][36]['training']['best_epoch']=10
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.7416, 'crossentropy': 1.37931123046875}
