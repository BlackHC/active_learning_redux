store = {}
store['timestamp']=1621471678
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=7']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=7
store['worker_id']=7
store['num_workers']=80
store['config']={'seed': 1241, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 256, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples)) + ('FastMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 40646, 10110, 32775, 33736, 27254, 306, 37354, 19689, 57811, 34482, 15494, 19215, 18819, 11554, 8108, 29048, 30362, 48953, 5588, 8719, 48602, 33140, 46397, 56710, 14640, 39579, 5573, 5715, 47420, 27135, 26129, 16927, 39050, 42295, 51555, 51600, 43234, 33891, 20917, 38856, 17032, 13036, 11228, 46700, 50498, 40741, 9834, 24971, 17759, 45567, 2728, 1774, 33486, 43252, 43803, 50036, 46861, 53831, 54003, 53362, 229, 767, 36270, 10432, 23451, 6612, 8710, 41077, 48498, 46683, 45260, 37098, 55148, 49775, 52801, 15969, 57520, 36797, 34198, 27145, 3029, 37047, 31965, 26501, 48519, 5803, 43415, 35794, 33581, 5897, 27573, 30980, 29614, 35237, 51755, 57690, 26516, 5380, 25589, 53689, 31444, 29950, 44803, 396, 56990, 24052, 12108, 54426, 42320, 35072, 21536, 49304, 49595, 44428, 72, 57175, 52679, 41082, 30184, 54017, 10232, 17968, 31935, 43587, 801, 48031, 2206, 2404, 58741, 29079, 49986, 46464, 17659, 30072, 39879, 29556, 52389, 13092, 37129, 11773, 15822, 37625, 7382, 7121, 17195, 32625, 43141, 28181, 50055, 55187, 34588, 38725, 50466, 40018, 37115, 20801, 23496, 4321, 42102, 12075, 54012, 28833, 18880, 26520, 27580, 14637, 40466, 54800, 24110, 13859, 51027, 45005, 57541, 34361, 26479, 43321, 44048, 45974, 15675, 10508, 49549, 28991, 13074, 9574, 44454, 36688, 8821, 12610, 54422, 34121, 27019, 21800, 44138, 36367, 44100, 33464, 51760, 15917, 495, 50997, 48032, 40334, 21423, 46870, 18137, 4701, 18693, 17506, 6968, 13359, 35372, 7356, 2289, 55733, 5481, 37157, 56054, 2400, 56137, 1005, 56096, 53538, 55783, 37709, 3792, 10664, 5616, 32972, 30013, 19757, 49169, 47417, 38430, 41512, 14035, 35714, 16068, 20076, 26853, 26428, 48521, 11261, 12917, 257, 43981, 8705, 27383, 10113, 7896]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 2.6498241424560547})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 3.324516773223877})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 3.849571704864502})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.7473936080932617})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.9901857376098633})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 4.185880661010742})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.7801642417907715})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 4.332874774932861})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 4.322925090789795})
store['active_learning_steps'][0]['training']['best_epoch']=6
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.5978, 'crossentropy': 4.230361328125}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.376159429550171})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.439924955368042})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.5019145011901855})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.4090913534164429})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.5059164762496948})
store['active_learning_steps'][0]['eval_training']['best_epoch']=2
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 57640], ['id', 37259], ['id', 46674], ['id', 36390], ['id', 53599]], 'labels': [-1, -1, -1, 0, 8], 'scores': [1.2442205640893187, 2.1616653988060457, 2.6994303271882547, 2.9530031383775865, 3.0709795142917278]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.22682523727417})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.659888505935669})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.826728105545044})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.958458423614502})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.4810240268707275})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.760800361633301})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.821699619293213})
store['active_learning_steps'][1]['training']['best_epoch']=4
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6448, 'crossentropy': 3.1041873046875}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.2296068668365479})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.2732077836990356})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.2662805318832397})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.2409729957580566})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.2615399360656738})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.2656137943267822})
store['active_learning_steps'][1]['eval_training']['best_epoch']=4
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 7468], ['id', 54511], ['id', 15701], ['id', 12985], ['id', 52127]], 'labels': [-1, -1, -1, -1, 6], 'scores': [1.2137888950120077, 2.154431049040192, 2.757855477855726, 3.0417096125438094, 3.1695508747868164]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.3524858951568604})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.1970162391662598})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.305626392364502})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.4289302825927734})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.801443338394165})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.947009563446045})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.6391332149505615})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 4.179230690002441})
store['active_learning_steps'][2]['training']['best_epoch']=5
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6036, 'crossentropy': 4.02155859375}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.5231473445892334})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.4596583843231201})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.5456669330596924})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.5914477109909058})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.5508915185928345})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.543119192123413})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.508389949798584})
store['active_learning_steps'][2]['eval_training']['best_epoch']=7
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 45039], ['id', 27181], ['id', 53585], ['id', 14084], ['id', 4450]], 'labels': [-1, -1, -1, -1, 2], 'scores': [1.1755403380784044, 2.111523995278264, 2.760848197412521, 3.0296860726003345, 3.135314111747265]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 2.2505064010620117})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.803279399871826})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.757190704345703})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.7754878997802734})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.5943050384521484})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.9775524139404297})
store['active_learning_steps'][3]['training']['best_epoch']=3
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.62, 'crossentropy': 3.52457890625}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.36601984500885})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.4070851802825928})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.495784044265747})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.4234848022460938})
store['active_learning_steps'][3]['eval_training']['best_epoch']=1
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 21138], ['id', 22121], ['id', 35567], ['id', 25409], ['id', 6311]], 'labels': [-1, -1, -1, -1, 0], 'scores': [1.017658910177895, 1.723366460199637, 2.2690600052770487, 2.544793401002485, 2.6692936894791632]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.0998661518096924})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.558764934539795})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.2364585399627686})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.2625021934509277})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.6203, 'crossentropy': 2.16971171875}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.2415733337402344})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.2256121635437012})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.2427338361740112})
store['active_learning_steps'][4]['eval_training']['best_epoch']=2
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 28461], ['id', 36583], ['id', 33106], ['id', 22783], ['id', 17664]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1398842814169177, 1.9047134266844488, 2.443231558576297, 2.774847211033701, 2.9358552783739693]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.132643222808838})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.5632591247558594})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.7641661167144775})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.755495548248291})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.145524263381958})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 3.123307228088379})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.5230093002319336})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.4880330562591553})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.431112766265869})
store['active_learning_steps'][5]['training']['best_epoch']=6
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.631, 'crossentropy': 3.435221875}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.3454563617706299})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.225150227546692})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.267423152923584})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.2995376586914062})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.3088533878326416})
store['active_learning_steps'][5]['eval_training']['best_epoch']=2
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 10210], ['id', 12682], ['id', 41434], ['id', 56866], ['id', 36470]], 'labels': [-1, -1, -1, -1, 0], 'scores': [1.208280003108305, 2.2069683185455977, 2.7950873611548372, 3.0426961405473625, 3.1351831385330406]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 2.1107983589172363})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.8597753047943115})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.1382546424865723})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.3342576026916504})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 3.265068292617798})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.6637587547302246})
store['active_learning_steps'][6]['training']['best_epoch']=3
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.5959, 'crossentropy': 3.4427125}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.3643959760665894})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.3371059894561768})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.3179221153259277})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.3913931846618652})
store['active_learning_steps'][6]['eval_training']['best_epoch']=1
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 50581], ['id', 25891], ['id', 467], ['id', 37025], ['id', 1869]], 'labels': [-1, -1, -1, 6, 7], 'scores': [1.0625652371606544, 1.8505471896923593, 2.361414008783628, 2.6119305543285627, 2.751045494988114]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 2.1009931564331055})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 2.600431442260742})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.95681095123291})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.0059773921966553})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.7086949348449707})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.6084539890289307})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.369905710220337})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.578964948654175})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 3.9738988876342773})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.8229994773864746})
store['active_learning_steps'][7]['training']['best_epoch']=7
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.6042, 'crossentropy': 3.7026859375}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.3625998497009277})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.375603437423706})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.4762035608291626})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.4604250192642212})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.4293930530548096})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.4461398124694824})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.5165979862213135})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.4268913269042969})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.4088382720947266})
store['active_learning_steps'][7]['eval_training']['best_epoch']=8
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 30878], ['id', 16628], ['id', 28594], ['id', 2835], ['id', 46076]], 'labels': [-1, -1, -1, 7, -1], 'scores': [1.368341642151759, 2.4331091591766087, 3.005414928902635, 3.255296566792955, 3.3783833517596964]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 2.23903489112854})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.6214816570281982})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 3.391005754470825})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.1448745727539062})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.518319606781006})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.626530885696411})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.8268423080444336})
store['active_learning_steps'][8]['training']['best_epoch']=4
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.606, 'crossentropy': 3.48424140625}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.4158637523651123})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.3827998638153076})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.4373730421066284})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.4227931499481201})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.4892340898513794})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.506644606590271})
store['active_learning_steps'][8]['eval_training']['best_epoch']=4
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 17876], ['id', 35217], ['id', 34304], ['id', 48684], ['id', 31445]], 'labels': [-1, -1, -1, -1, 2], 'scores': [1.2695926102750217, 2.151396159839559, 2.6884556191217843, 2.935662636711797, 3.0226003979039895]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 2.441507577896118})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.961549758911133})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.7014575004577637})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.978468179702759})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.9585165977478027})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.6042, 'crossentropy': 3.0358482421875}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.488551139831543})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.4172279834747314})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.6184513568878174})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.4763495922088623})
store['active_learning_steps'][9]['eval_training']['best_epoch']=2
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 56168], ['id', 12342], ['id', 4812], ['id', 44735], ['id', 32146]], 'labels': [-1, -1, 5, 1, -1], 'scores': [0.9499684557908123, 1.7161494902142245, 2.196680701502819, 2.5025773515786787, 2.6702503657786147]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.8848626613616943})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.511333703994751})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.6755623817443848})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.3386070728302})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 3.4206624031066895})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.3884782791137695})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.8213629722595215})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 3.4653775691986084})
store['active_learning_steps'][10]['training']['best_epoch']=5
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.6249, 'crossentropy': 3.605548828125}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.505638837814331})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.4215381145477295})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.5948011875152588})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.4566152095794678})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.4769704341888428})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.5040760040283203})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.4419885873794556})
store['active_learning_steps'][10]['eval_training']['best_epoch']=4
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 26863], ['id', 14819], ['id', 51948], ['id', 58267], ['id', 4823]], 'labels': [-1, -1, -1, 2, 2], 'scores': [1.1416177878100173, 2.0333515185384696, 2.5570701267379787, 2.8442552839097965, 2.980839497254034]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.1349520683288574})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.7570314407348633})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.137500524520874})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.6088967323303223})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.366356134414673})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 3.7702105045318604})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.6257805824279785})
store['active_learning_steps'][11]['training']['best_epoch']=4
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.6124, 'crossentropy': 3.435182421875}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.3268905878067017})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.388377070426941})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.4281867742538452})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.5038611888885498})
store['active_learning_steps'][11]['eval_training']['best_epoch']=1
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 5810], ['id', 9200], ['id', 50403], ['id', 19842], ['id', 29792]], 'labels': [-1, -1, 0, 8, 6], 'scores': [1.0507422385983376, 1.9269682548499016, 2.484311095594415, 2.7251456852966056, 2.8333241517613708]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 1.9045040607452393})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 2.7130308151245117})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 3.0356287956237793})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.475116729736328})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.7818474769592285})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.1107637882232666})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.819161891937256})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 3.833415985107422})
store['active_learning_steps'][12]['training']['best_epoch']=5
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.5978, 'crossentropy': 4.030116796875}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.4113759994506836})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.4719877243041992})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.4865684509277344})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.539069652557373})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.5044159889221191})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.4751023054122925})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.5164639949798584})
store['active_learning_steps'][12]['eval_training']['best_epoch']=6
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 11465], ['id', 35560], ['id', 30618], ['id', 20484], ['id', 43746]], 'labels': [-1, -1, -1, 1, 8], 'scores': [1.2303738058836022, 2.0328856093340613, 2.592343017531407, 2.9185914703402602, 3.02903253168001]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.6462398767471313})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.3422493934631348})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.434476137161255})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.6212968826293945})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.728449821472168})
store['active_learning_steps'][13]['training']['best_epoch']=2
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6488, 'crossentropy': 2.350994140625}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.2199699878692627})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.239618182182312})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.2673258781433105})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.2833776473999023})
store['active_learning_steps'][13]['eval_training']['best_epoch']=4
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 51589], ['id', 2090], ['id', 38365], ['id', 6827], ['id', 12584]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.207970516191617, 2.0639839805690166, 2.6600241882317963, 2.947030184472757, 3.06059527743231]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.6974552869796753})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.277296543121338})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.430267810821533})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.8059873580932617})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.929933547973633})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 3.029388427734375})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.2005817890167236})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 3.064152717590332})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.405350923538208})
store['active_learning_steps'][14]['training']['best_epoch']=6
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.6484, 'crossentropy': 3.1715291015625}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.18768310546875})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.2509260177612305})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.3619935512542725})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.2843518257141113})
store['active_learning_steps'][14]['eval_training']['best_epoch']=1
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 46551], ['id', 7985], ['id', 52270], ['id', 22066], ['id', 49640]], 'labels': [-1, -1, -1, 8, 2], 'scores': [1.2823849606543147, 2.1810874285962267, 2.7704277991999806, 3.021497479361675, 3.107456826871405]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.486836314201355})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.296135187149048})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.4748830795288086})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.815688133239746})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.8560428619384766})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 3.1633048057556152})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.0416109561920166})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 3.248474597930908})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.185580253601074})
store['active_learning_steps'][15]['training']['best_epoch']=6
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.6435, 'crossentropy': 3.20328125}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.397998571395874})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.307392954826355})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.3038631677627563})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.3372485637664795})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.4246735572814941})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.3706855773925781})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.422498345375061})
store['active_learning_steps'][15]['eval_training']['best_epoch']=4
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 45735], ['id', 24460], ['id', 19280], ['id', 26315], ['id', 30650]], 'labels': [-1, -1, -1, -1, 2], 'scores': [1.2630141254834273, 2.1364263498341822, 2.6901156356401206, 2.9639685961177022, 3.0897193228166975]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.7786946296691895})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.489621162414551})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.5766706466674805})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.3103952407836914})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.2546911239624023})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.6288, 'crossentropy': 2.44932421875}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.2016817331314087})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.2520490884780884})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.2148551940917969})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.2274441719055176})
store['active_learning_steps'][16]['eval_training']['best_epoch']=3
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 45053], ['id', 39407], ['id', 42583], ['id', 40889], ['id', 42210]], 'labels': [-1, -1, -1, -1, 6], 'scores': [1.304687729891401, 2.173914332705893, 2.728780419750149, 2.995517095895792, 3.074766860097368]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.8130953311920166})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.4513633251190186})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.4138197898864746})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 3.131622552871704})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.0977163314819336})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 3.2300381660461426})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 3.225642204284668})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 3.3184609413146973})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 3.793144702911377})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 3.2976274490356445})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 4.227073669433594})
store['active_learning_steps'][17]['training']['best_epoch']=8
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.6466, 'crossentropy': 3.5649421875}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.258737325668335})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.3150269985198975})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.3161864280700684})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.2771987915039062})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.2950074672698975})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.4524667263031006})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.3711020946502686})
store['active_learning_steps'][17]['eval_training']['best_epoch']=4
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 55172], ['id', 12679], ['id', 47008], ['id', 16167], ['id', 33771]], 'labels': [-1, -1, 2, 1, 5], 'scores': [1.213565659877794, 2.1297252573519474, 2.740231930311566, 3.080561965729286, 3.2092456568451206]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.5515141487121582})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.1260313987731934})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.479220151901245})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.5586116313934326})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 3.049100399017334})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.9239251613616943})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 3.3485770225524902})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 3.0611391067504883})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 3.206730365753174})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 3.298123836517334})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 3.412071466445923})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 3.2837750911712646})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 3.3783249855041504})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.7979683876037598})
store['active_learning_steps'][18]['training']['best_epoch']=11
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6545, 'crossentropy': 3.714115625}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.1858594417572021})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.2136049270629883})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.3232711553573608})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.2946107387542725})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.237625002861023})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.2481626272201538})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.2954866886138916})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.2246580123901367})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.161968469619751})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.2030082941055298})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.1828070878982544})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.2764873504638672})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.1958394050598145})
store['active_learning_steps'][18]['eval_training']['best_epoch']=12
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 58484], ['id', 47953], ['id', 46585], ['id', 49149], ['id', 46289]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2611898658579412, 2.2650019285425733, 2.897091105673443, 3.2223733192070556, 3.365811440616664]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.709824800491333})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.9413857460021973})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.480733871459961})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.43487286567688})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.703375816345215})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.876368522644043})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 3.1335573196411133})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.8165369033813477})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 3.2507290840148926})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 3.530684471130371})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 3.244798183441162})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.8947296142578125})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.882307291030884})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 3.2145071029663086})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 3.3130311965942383})
store['active_learning_steps'][19]['training']['best_epoch']=12
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6496, 'crossentropy': 3.34986484375}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.2962193489074707})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.2610845565795898})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.26393461227417})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.2750667333602905})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.2378665208816528})
store['active_learning_steps'][19]['eval_training']['best_epoch']=2
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 13496], ['id', 6343], ['id', 59424], ['id', 52580], ['id', 17421]], 'labels': [-1, -1, -1, 6, 4], 'scores': [1.2186607859006435, 2.1936206738738884, 2.858307349034906, 3.1167129171230847, 3.2275701763095865]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.54927396774292})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.017174482345581})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.247370958328247})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.269011974334717})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.352398157119751})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.819699287414551})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.8459105491638184})
store['active_learning_steps'][20]['training']['best_epoch']=4
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.6665, 'crossentropy': 2.4748400390625}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.1935067176818848})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.2265751361846924})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.1576210260391235})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.221339225769043})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.1930428743362427})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.1792348623275757})
store['active_learning_steps'][20]['eval_training']['best_epoch']=5
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 42570], ['id', 4542], ['id', 13717], ['id', 28869], ['id', 7210]], 'labels': [-1, -1, 3, 5, -1], 'scores': [1.0546631486464229, 1.905213146455433, 2.44025900388551, 2.7426370408814496, 2.8666100336910985]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.3322964906692505})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.795994758605957})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.978372573852539})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.27034330368042})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.295687675476074})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.396688938140869})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.577739715576172})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.3461573123931885})
store['active_learning_steps'][21]['training']['best_epoch']=5
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.678, 'crossentropy': 2.5104646484375}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.1651487350463867})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.1920607089996338})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.0903886556625366})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.0766782760620117})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.1176340579986572})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.159726619720459})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.0921183824539185})
store['active_learning_steps'][21]['eval_training']['best_epoch']=7
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 20097], ['id', 33030], ['id', 58494], ['id', 16028], ['id', 59168]], 'labels': [-1, -1, -1, -1, 0], 'scores': [1.2618119779777293, 2.172663301395388, 2.7413594996280413, 3.0168044394918523, 3.146506015888269]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.5096244812011719})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.9340344667434692})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.9704720973968506})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.52690052986145})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.749734878540039})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 3.0613327026367188})
store['active_learning_steps'][22]['training']['best_epoch']=3
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.6547, 'crossentropy': 2.31263671875}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.2535507678985596})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.1918277740478516})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.1387206315994263})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.2152273654937744})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.2126927375793457})
store['active_learning_steps'][22]['eval_training']['best_epoch']=3
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 36187], ['id', 24101], ['id', 27131], ['id', 54014], ['id', 45331]], 'labels': [-1, -1, -1, -1, 0], 'scores': [1.1891637117275904, 2.105067101900966, 2.664823572958415, 2.9408082612992104, 3.078595609656535]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.47462797164917})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.8615466356277466})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.9762165546417236})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.309494972229004})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.4085330963134766})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.2928032875061035})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.552203893661499})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.618593692779541})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.865264892578125})
store['active_learning_steps'][23]['training']['best_epoch']=6
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.6758, 'crossentropy': 2.5107703125}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.1309151649475098})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.1186360120773315})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.065272331237793})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.1013777256011963})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.0495307445526123})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.0751500129699707})
store['active_learning_steps'][23]['eval_training']['best_epoch']=3
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 12091], ['id', 20087], ['id', 47164], ['id', 3106], ['id', 41280]], 'labels': [-1, -1, 9, -1, 4], 'scores': [1.1181483790112916, 1.9692508527385129, 2.4763120373740524, 2.713590905323473, 2.7815355992994286]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.3246721029281616})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.5399746894836426})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.7226850986480713})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.073439121246338})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.9803731441497803})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.511838674545288})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.4168920516967773})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.6813, 'crossentropy': 2.1189671875}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.1499342918395996})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.0302002429962158})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.1272779703140259})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.0296566486358643})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.0484429597854614})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.046358346939087})
store['active_learning_steps'][24]['eval_training']['best_epoch']=6
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 32567], ['id', 23545], ['id', 19655], ['id', 30683], ['id', 46676]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.029521855534486, 1.8990497100845323, 2.5034825351319507, 2.7949633460658374, 2.965914213327534]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.4663803577423096})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.630831003189087})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.8646512031555176})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.0041921138763428})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.1496753692626953})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.250988483428955})
store['active_learning_steps'][25]['training']['best_epoch']=3
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.6914, 'crossentropy': 1.983925390625}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.0660488605499268})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.0133707523345947})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.0232548713684082})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.02669358253479})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 0.9685266017913818})
store['active_learning_steps'][25]['eval_training']['best_epoch']=5
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 22169], ['id', 26003], ['id', 10347], ['id', 35770], ['id', 18290]], 'labels': [-1, -1, -1, 9, 0], 'scores': [1.0945708958040445, 2.0368089749224234, 2.5661302566114195, 2.8323165705999687, 2.9837033993043587]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.2963104248046875})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.857677698135376})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.9558038711547852})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.2151284217834473})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.357123374938965})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.71012020111084})
store['active_learning_steps'][26]['training']['best_epoch']=3
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.6588, 'crossentropy': 2.1825798828125}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.2036256790161133})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.119076132774353})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.0797373056411743})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.1858365535736084})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.0927956104278564})
store['active_learning_steps'][26]['eval_training']['best_epoch']=2
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 19655], ['id', 2847], ['id', 46632], ['id', 44848], ['id', 26516]], 'labels': [-1, -1, 4, -1, -1], 'scores': [1.03745042686109, 1.8055408208079275, 2.336028214720767, 2.6629684447768316, 2.816411315782325]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.3963860273361206})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.6440924406051636})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.8663628101348877})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.2197651863098145})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.118685722351074})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.3466272354125977})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.57499098777771})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.6717, 'crossentropy': 2.442355078125}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.236872911453247})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.1419141292572021})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.0832815170288086})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.207790732383728})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.2356618642807007})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.07349693775177})
store['active_learning_steps'][27]['eval_training']['best_epoch']=6
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 13577], ['id', 55648], ['id', 54545], ['id', 28747], ['id', 24844]], 'labels': [-1, -1, -1, -1, 3], 'scores': [1.0880839942462615, 1.957804683687744, 2.524037107891184, 2.8085937879735656, 2.9394993038239434]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.3334542512893677})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.672899842262268})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.0508475303649902})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.128291606903076})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.6078596115112305})
store['active_learning_steps'][28]['training']['best_epoch']=2
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.6617, 'crossentropy': 1.8585689453125}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.187819004058838})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.1029322147369385})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.0880825519561768})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.0364642143249512})
store['active_learning_steps'][28]['eval_training']['best_epoch']=4
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 59835], ['id', 16111], ['id', 9080], ['id', 34871], ['id', 46164]], 'labels': [-1, -1, 8, -1, 2], 'scores': [1.130273851940291, 1.9201888690930935, 2.454863175812993, 2.7369841721071655, 2.8487028982257296]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.37052321434021})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.4895009994506836})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.8166162967681885})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.9947409629821777})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.230685234069824})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.444729804992676})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.2268502712249756})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.467529296875})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.5868582725524902})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.448868751525879})
store['active_learning_steps'][29]['training']['best_epoch']=7
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.6902, 'crossentropy': 2.507621484375}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.1049976348876953})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.1376935243606567})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.0488762855529785})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.1142208576202393})
store['active_learning_steps'][29]['eval_training']['best_epoch']=1
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 52785], ['id', 49500], ['id', 23262], ['id', 40610], ['id', 52619]], 'labels': [-1, -1, -1, 9, 6], 'scores': [1.1893439520653888, 2.122543181373257, 2.707080849705995, 2.906234482948814, 2.953827278666676]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.313286542892456})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.4913442134857178})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.8441681861877441})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.1330599784851074})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.182861566543579})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.5296292304992676})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.4998888969421387})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.6390960216522217})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.728635311126709})
store['active_learning_steps'][30]['training']['best_epoch']=6
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.6903, 'crossentropy': 2.553212890625}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.1366081237792969})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.263271450996399})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.0919305086135864})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.1035633087158203})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.1449379920959473})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.133232831954956})
store['active_learning_steps'][30]['eval_training']['best_epoch']=3
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 58162], ['id', 17760], ['id', 54405], ['id', 10327], ['id', 45211]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2974721137189962, 2.198285229671275, 2.780685865958838, 3.0687320796852795, 3.1967302474116948]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.3390038013458252})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.6235127449035645})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.7910473346710205})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.294496536254883})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.3713159561157227})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.325582981109619})
store['active_learning_steps'][31]['training']['best_epoch']=3
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.6823, 'crossentropy': 1.9342287109375}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.1716521978378296})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.0446096658706665})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.0684943199157715})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.0943986177444458})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.0501103401184082})
store['active_learning_steps'][31]['eval_training']['best_epoch']=3
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 4096], ['id', 739], ['id', 47256], ['id', 30345], ['id', 17602]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9659341656484788, 1.733530856996913, 2.1800516439205566, 2.4660394477995693, 2.6261845682454314]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.471411943435669})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.733234167098999})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.902781367301941})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.9817817211151123})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.1714537143707275})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.4636735916137695})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.6303415298461914})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.558241128921509})
store['active_learning_steps'][32]['training']['best_epoch']=5
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.6773, 'crossentropy': 2.36896796875}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.1316827535629272})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.0631202459335327})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.1671359539031982})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.0952794551849365})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.0833337306976318})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.0953816175460815})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.1044278144836426})
store['active_learning_steps'][32]['eval_training']['best_epoch']=7
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 58841], ['id', 57802], ['id', 53733], ['id', 30651], ['id', 26456]], 'labels': [-1, -1, -1, -1, 7], 'scores': [1.1470895920342539, 1.968583159304989, 2.5201491787418977, 2.7920448667113913, 2.881568219418594]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.386130690574646})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.603418231010437})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.92189359664917})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.0846691131591797})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.301436185836792})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.2920947074890137})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.378840923309326})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.470015048980713})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.9110002517700195})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.5119102001190186})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.87825345993042})
store['active_learning_steps'][33]['training']['best_epoch']=8
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.6726, 'crossentropy': 2.757431640625}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.181653380393982})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.1156599521636963})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.1556637287139893})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.2034292221069336})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.1951229572296143})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.2112605571746826})
store['active_learning_steps'][33]['eval_training']['best_epoch']=3
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 35837], ['id', 31962], ['id', 28880], ['id', 56733], ['id', 9093]], 'labels': [-1, -1, 1, -1, -1], 'scores': [1.322705133044156, 2.259828624579919, 2.7909401965283465, 3.076935852856961, 3.202932387621347]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.3358230590820312})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.6573312282562256})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.9071705341339111})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.352618455886841})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.413186550140381})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.2671055793762207})
store['active_learning_steps'][34]['training']['best_epoch']=3
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.6712, 'crossentropy': 2.004946875}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.247619867324829})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.0594508647918701})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.1479817628860474})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.124417781829834})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.1171488761901855})
store['active_learning_steps'][34]['eval_training']['best_epoch']=5
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 21962], ['id', 54857], ['id', 21347], ['id', 33020], ['id', 29560]], 'labels': [-1, -1, -1, -1, 2], 'scores': [1.0407754033483518, 1.8564422515966053, 2.393816933657358, 2.681075825101943, 2.784904089770161]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.354418158531189})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.7303268909454346})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.9617106914520264})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.4017326831817627})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.314324378967285})
store['active_learning_steps'][35]['training']['best_epoch']=2
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.6605, 'crossentropy': 1.7317568359375}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.1562426090240479})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.108079433441162})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.0726953744888306})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.0505750179290771})
store['active_learning_steps'][35]['eval_training']['best_epoch']=4
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 42805], ['id', 29311], ['id', 26901], ['id', 52393], ['id', 10800]], 'labels': [-1, -1, -1, -1, 3], 'scores': [1.0160565669522086, 1.767451077314159, 2.3158279502199353, 2.623646286555905, 2.7787881610266147]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.3410608768463135})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.591728925704956})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.844067096710205})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.0010266304016113})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.224764347076416})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 2.309429168701172})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.4837658405303955})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.4217448234558105})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.5179827213287354})
store['active_learning_steps'][36]['training']['best_epoch']=6
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.6867, 'crossentropy': 2.5098603515625}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.2360682487487793})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.1812045574188232})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.1705763339996338})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.1973896026611328})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.1327320337295532})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.2097516059875488})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.1223745346069336})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.1402686834335327})
store['active_learning_steps'][36]['eval_training']['best_epoch']=8
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 10215], ['id', 47189], ['id', 13157], ['id', 59415], ['id', 31310]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1085091888469925, 1.9722289918443376, 2.5934682217709826, 2.9445110750301904, 3.038880268786775]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.3107733726501465})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.5764151811599731})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.8757283687591553})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.1714062690734863})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.2713615894317627})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.613348960876465})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.2268834114074707})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.5028624534606934})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.5423269271850586})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.596315622329712})
store['active_learning_steps'][37]['training']['best_epoch']=7
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.6835, 'crossentropy': 2.3939486328125}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.2099628448486328})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.09579598903656})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.1244018077850342})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.1050833463668823})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.1301946640014648})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.0964083671569824})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.114793300628662})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.1809673309326172})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.1155881881713867})
store['active_learning_steps'][37]['eval_training']['best_epoch']=7
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 11997], ['id', 46567], ['id', 1538], ['id', 13676], ['id', 36596]], 'labels': [-1, -1, -1, -1, 7], 'scores': [1.1529376071496793, 2.1004691667652855, 2.594709619486827, 2.8267030630769723, 2.9171011784406993]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.3938555717468262})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.660759687423706})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.877834439277649})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.2244420051574707})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.331350803375244})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.7046046257019043})
store['active_learning_steps'][38]['training']['best_epoch']=3
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.68, 'crossentropy': 2.0179138671875}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.1417157649993896})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.1068768501281738})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.106713056564331})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.1237719058990479})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.0736606121063232})
store['active_learning_steps'][38]['eval_training']['best_epoch']=5
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 50177], ['id', 40350], ['id', 40040], ['id', 54074], ['id', 48509]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1227400779167467, 1.9384187305251492, 2.552242835894519, 2.8998531534012413, 3.059977972392957]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.301085114479065})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.5905866622924805})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.791695237159729})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.130405902862549})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.1982409954071045})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.2206549644470215})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.128178119659424})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.5135836601257324})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.6946187019348145})
store['active_learning_steps'][39]['training']['best_epoch']=6
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.6765, 'crossentropy': 2.4470349609375}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.2269337177276611})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.2075259685516357})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.1648496389389038})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.0916762351989746})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.1559964418411255})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.249402642250061})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.12245774269104})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.1242012977600098})
store['active_learning_steps'][39]['eval_training']['best_epoch']=7
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 6973], ['id', 44901], ['id', 29991], ['id', 31297], ['id', 10429]], 'labels': [-1, -1, -1, -1, 3], 'scores': [1.0277012312976948, 1.8806560662252765, 2.4116533811224166, 2.6711508972254903, 2.770779142219281]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.4084837436676025})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.7082128524780273})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.9593358039855957})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.228116512298584})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.2900238037109375})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.391348123550415})
store['active_learning_steps'][40]['training']['best_epoch']=3
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.6686, 'crossentropy': 1.972431640625}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.1265625953674316})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.0991816520690918})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.0399773120880127})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.0474131107330322})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0733835697174072})
store['active_learning_steps'][40]['eval_training']['best_epoch']=3
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 5398], ['id', 40216], ['id', 47479], ['id', 3106], ['id', 36339]], 'labels': [-1, -1, 5, -1, -1], 'scores': [1.0489849776255529, 1.8445108469538152, 2.4135861855161593, 2.786671852042508, 2.9772604407821532]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.4670743942260742})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.5444761514663696})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.008911371231079})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.20033860206604})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.2842416763305664})
store['active_learning_steps'][41]['training']['best_epoch']=2
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.6644, 'crossentropy': 1.7900654296875}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.140187382698059})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.1121935844421387})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.0804789066314697})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.0336945056915283})
store['active_learning_steps'][41]['eval_training']['best_epoch']=4
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 34416], ['id', 31942], ['id', 30325], ['id', 29336], ['id', 27020]], 'labels': [-1, -1, -1, 9, 3], 'scores': [0.9211636227498734, 1.6185315875251831, 2.136498387795273, 2.46109926184855, 2.6070649348001353]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.3146145343780518})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.5474737882614136})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.972529649734497})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.0828847885131836})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.9653385877609253})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 2.202604293823242})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.5367469787597656})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.3379032611846924})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.5858874320983887})
store['active_learning_steps'][42]['training']['best_epoch']=6
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.6866, 'crossentropy': 2.40645703125}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.1153665781021118})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.126415491104126})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.1078217029571533})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.115304708480835})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.1237142086029053})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0271270275115967})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.094273567199707})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.0307064056396484})
store['active_learning_steps'][42]['eval_training']['best_epoch']=6
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 24546], ['id', 55395], ['id', 47726], ['id', 43834], ['id', 34829]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.926166784122588, 1.6928936690200986, 2.272647649048942, 2.559102913480043, 2.6743467369600014]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.3221478462219238})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.5426249504089355})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.8864097595214844})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.2088234424591064})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.3056540489196777})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.489506244659424})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.5999984741210938})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.8028576374053955})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.5803332328796387})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.96626615524292})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.902207374572754})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 3.0477921962738037})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.7900662422180176})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 3.5540621280670166})
store['active_learning_steps'][43]['training']['best_epoch']=11
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.6705, 'crossentropy': 3.0822861328125}
store['active_learning_steps'][43]['eval_training']={}
store['active_learning_steps'][43]['eval_training']['epochs']=[]
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.2029378414154053})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.1586631536483765})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.1885358095169067})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.2363020181655884})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.2697336673736572})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.117197036743164})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.2293190956115723})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.1429858207702637})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.253316879272461})
store['active_learning_steps'][43]['eval_training']['best_epoch']=6
store['active_learning_steps'][43]['acquisition']={'indices': [['id', 25489], ['id', 50689], ['id', 26773], ['id', 56951], ['id', 17643]], 'labels': [-1, -1, -1, 8, -1], 'scores': [1.2889919088756767, 2.2702870379602453, 2.748168953647184, 2.961793116943948, 3.0368146584452163]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.354963779449463})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.4432004690170288})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.91493558883667})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.971129059791565})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.4120664596557617})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.285182476043701})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.720550537109375})
store['active_learning_steps'][44]['training']['best_epoch']=4
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.6937, 'crossentropy': 1.9919697265625}
store['active_learning_steps'][44]['eval_training']={}
store['active_learning_steps'][44]['eval_training']['epochs']=[]
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.146846055984497})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.0519238710403442})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.101225733757019})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.0715709924697876})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.075772762298584})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.0679821968078613})
store['active_learning_steps'][44]['eval_training']['best_epoch']=4
store['active_learning_steps'][44]['acquisition']={'indices': [['id', 11170], ['id', 51214], ['id', 48211], ['id', 4743], ['id', 44162]], 'labels': [-1, -1, -1, -1, 1], 'scores': [0.9244734088962692, 1.6668626370525161, 2.210663257588096, 2.539835396673567, 2.690442645632788]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.2493470907211304})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.6608577966690063})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.8505630493164062})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.8531951904296875})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.311939239501953})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.2502198219299316})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.314112424850464})
store['active_learning_steps'][45]['training']['best_epoch']=4
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.6857, 'crossentropy': 2.048623828125}
store['active_learning_steps'][45]['eval_training']={}
store['active_learning_steps'][45]['eval_training']['epochs']=[]
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.1485984325408936})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.0553375482559204})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.0581554174423218})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.044337272644043})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0996999740600586})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.0591213703155518})
store['active_learning_steps'][45]['eval_training']['best_epoch']=6
store['active_learning_steps'][45]['acquisition']={'indices': [['id', 7939], ['id', 49448], ['id', 54383], ['id', 26781], ['id', 38121]], 'labels': [-1, -1, -1, -1, 4], 'scores': [1.1673546644311656, 2.0696683521128394, 2.590310352643069, 2.8093489601536152, 2.895787324197376]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.2747852802276611})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.4883015155792236})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.576129674911499})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.0285606384277344})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.0155158042907715})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.269749641418457})
store['active_learning_steps'][46]['training']['best_epoch']=3
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.701, 'crossentropy': 1.67824765625}
store['active_learning_steps'][46]['eval_training']={}
store['active_learning_steps'][46]['eval_training']['epochs']=[]
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.0545076131820679})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.027230978012085})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 0.9397925138473511})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 0.9852668046951294})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 0.9804716110229492})
store['active_learning_steps'][46]['eval_training']['best_epoch']=5
store['active_learning_steps'][46]['acquisition']={'indices': [['id', 34829], ['id', 5345], ['id', 48435], ['id', 2125], ['id', 32311]], 'labels': [-1, -1, -1, -1, 5], 'scores': [1.0055064424236768, 1.8681595281938104, 2.4413350897721475, 2.6981623231721983, 2.811468454495939]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.2817845344543457})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.4818816184997559})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.8677350282669067})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.7991611957550049})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.2179179191589355})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 2.2169289588928223})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.7777011394500732})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.705345630645752})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.576880693435669})
store['active_learning_steps'][47]['training']['best_epoch']=6
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.7003, 'crossentropy': 2.2527537109375}
store['active_learning_steps'][47]['eval_training']={}
store['active_learning_steps'][47]['eval_training']['epochs']=[]
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.1243693828582764})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.1211744546890259})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.050689697265625})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.1079789400100708})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.090172290802002})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.0663630962371826})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.0579638481140137})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.0707337856292725})
store['active_learning_steps'][47]['eval_training']['best_epoch']=8
store['active_learning_steps'][47]['acquisition']={'indices': [['id', 10002], ['id', 26701], ['id', 42883], ['id', 49157], ['id', 30843]], 'labels': [-1, -1, -1, 4, 3], 'scores': [0.9972024197739583, 1.8042274960648417, 2.3135043933205406, 2.6120080646098653, 2.776850743843422]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.153131365776062})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.5065910816192627})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.6363232135772705})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.8209445476531982})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.237365245819092})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.298553943634033})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.0633432865142822})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 2.2919769287109375})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.49118709564209})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.799879550933838})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.5326037406921387})
store['active_learning_steps'][48]['training']['best_epoch']=8
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.7031, 'crossentropy': 2.404821484375}
store['active_learning_steps'][48]['eval_training']={}
store['active_learning_steps'][48]['eval_training']['epochs']=[]
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.121216058731079})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.052700400352478})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.083817958831787})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.025390625})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.1319425106048584})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.0585815906524658})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.043148159980774})
store['active_learning_steps'][48]['eval_training']['best_epoch']=4
store['active_learning_steps'][48]['acquisition']={'indices': [['id', 59489], ['id', 35787], ['id', 4046], ['id', 22886], ['id', 31796]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1078086683518582, 1.972321476712993, 2.557506922849409, 2.8539296007957278, 2.9660757491271994]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.177940845489502})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.5402204990386963})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.6269868612289429})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.9043132066726685})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.1196370124816895})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 2.294279098510742})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.6025390625})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.45344614982605})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 2.5921266078948975})
store['active_learning_steps'][49]['training']['best_epoch']=6
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.6957, 'crossentropy': 2.52126171875}
store['active_learning_steps'][49]['eval_training']={}
store['active_learning_steps'][49]['eval_training']['epochs']=[]
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.2378263473510742})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.1547901630401611})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.0797010660171509})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.1312015056610107})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.2272288799285889})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.0779204368591309})
store['active_learning_steps'][49]['eval_training']['best_epoch']=3
store['active_learning_steps'][49]['acquisition']={'indices': [['id', 15734], ['id', 57132], ['id', 46613], ['id', 2566], ['id', 31301]], 'labels': [-1, 0, -1, -1, 4], 'scores': [1.0389575327878415, 1.9066999017018866, 2.543216380120379, 2.84966358967327, 2.995635081220674]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.278839349746704})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.4034740924835205})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.5723607540130615})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.877591609954834})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.8914071321487427})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 2.1641650199890137})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.506927967071533})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.4889345169067383})
store['active_learning_steps'][50]['training']['best_epoch']=5
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.7117, 'crossentropy': 1.9954337890625}
store['active_learning_steps'][50]['eval_training']={}
store['active_learning_steps'][50]['eval_training']['epochs']=[]
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.161025047302246})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0143824815750122})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.0082049369812012})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 0.9961144924163818})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.0202391147613525})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.041921854019165})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.0297242403030396})
store['active_learning_steps'][50]['eval_training']['best_epoch']=6
store['active_learning_steps'][50]['acquisition']={'indices': [['id', 23104], ['id', 26147], ['id', 21084], ['id', 3106], ['id', 52550]], 'labels': [-1, -1, -1, -1, 5], 'scores': [1.0222871589577354, 1.8967356166487064, 2.490169069415909, 2.8026651493140493, 2.89047509040053]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.3326213359832764})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.3675758838653564})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.6041185855865479})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.7701743841171265})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 2.01424241065979})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.8410656452178955})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 2.2672948837280273})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.5019073486328125})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 2.3988170623779297})
store['active_learning_steps'][51]['training']['best_epoch']=6
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.7111, 'crossentropy': 2.0047658203125}
store['active_learning_steps'][51]['eval_training']={}
store['active_learning_steps'][51]['eval_training']['epochs']=[]
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.0498132705688477})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 0.980841875076294})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 0.9650918245315552})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 0.9642543196678162})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 0.9520093202590942})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 0.934167742729187})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 0.942302942276001})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 0.9566166400909424})
store['active_learning_steps'][51]['eval_training']['best_epoch']=5
store['active_learning_steps'][51]['acquisition']={'indices': [['id', 9542], ['id', 7859], ['id', 52083], ['id', 39592], ['id', 3066]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.091955539329161, 1.996313842369687, 2.542782227602361, 2.861837082675481, 3.014447031979925]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.165543794631958})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.421452522277832})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.6361875534057617})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.9412232637405396})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.0539448261260986})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.867494821548462})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 2.2493743896484375})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.216002941131592})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 2.3692593574523926})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 2.2804770469665527})
store['active_learning_steps'][52]['training']['best_epoch']=7
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.6988, 'crossentropy': 2.450576171875}
store['active_learning_steps'][52]['eval_training']={}
store['active_learning_steps'][52]['eval_training']['epochs']=[]
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.1507599353790283})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.0959635972976685})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.1594051122665405})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.083627700805664})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.1768584251403809})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.0785902738571167})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.1624103784561157})
store['active_learning_steps'][52]['eval_training']['best_epoch']=4
store['active_learning_steps'][52]['acquisition']={'indices': [['id', 44658], ['id', 15031], ['id', 38890], ['id', 28375], ['id', 32204]], 'labels': [-1, 8, 2, -1, 2], 'scores': [1.1873682058099693, 2.134232346225254, 2.765865094130767, 3.034122292426738, 3.1772887984893146]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.1665127277374268})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.3184541463851929})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.596832513809204})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.8300964832305908})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.9700864553451538})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.9862035512924194})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.0319721698760986})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 2.064706325531006})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.249399185180664})
store['active_learning_steps'][53]['training']['best_epoch']=6
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.703, 'crossentropy': 2.1865796875}
store['active_learning_steps'][53]['eval_training']={}
store['active_learning_steps'][53]['eval_training']['epochs']=[]
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.1197900772094727})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 0.9836937189102173})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 0.9814881086349487})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.0054107904434204})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.0270533561706543})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.052435278892517})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.0882525444030762})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0218987464904785})
store['active_learning_steps'][53]['eval_training']['best_epoch']=7
store['active_learning_steps'][53]['acquisition']={'indices': [['id', 32368], ['id', 14075], ['id', 3780], ['id', 10251], ['id', 40894]], 'labels': [-1, -1, -1, 5, 1], 'scores': [1.148745409878048, 2.0599840556812996, 2.6077931358483446, 2.909032730125818, 3.048985392947044]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.1713273525238037})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.3013992309570312})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.5484941005706787})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.661928653717041})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.9222140312194824})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.8621039390563965})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 2.0378050804138184})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 2.1072535514831543})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 2.071587085723877})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 2.451183319091797})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 2.344611167907715})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 2.2759971618652344})
store['active_learning_steps'][54]['training']['best_epoch']=9
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.7072, 'crossentropy': 2.2319525390625}
