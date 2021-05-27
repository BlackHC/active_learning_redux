store = {}
store['timestamp']=1622127792
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=38']
store['commit']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['github_url']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=38
store['worker_id']=38
store['num_workers']=80
store['config']={'seed': 1274, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 256, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('FastFashionMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3029, 35714, 21536, 48519, 8821, 11261, 35237, 33891, 37129, 46683, 6968, 15917, 30184, 50055, 14637, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 14035, 42320, 16927, 42102, 39050, 27573, 30980, 53362, 18819, 21800, 44138, 39879, 13092, 51760, 48953, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 26129, 37115, 35072, 36688, 54003, 72, 57690, 7382, 7896, 24110, 35372, 37098, 54536, 34513, 37157, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 26853, 42295, 34121, 19215, 12917, 51600, 27383, 20917, 38856, 15822, 6612, 13359, 28181, 7145, 49775, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 54422, 229, 30072, 4701, 18693, 26516, 43141, 5588, 7356, 55148, 2773, 24971, 57801, 17644, 54479, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 43415, 17659, 12075, 26428, 8705, 29556, 8108, 8710, 17032, 17195, 5481, 24223, 17968, 56054, 39333, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 33581, 48521, 36270, 57175, 11554, 11773, 41082, 37625, 41077, 13036, 32625, 54017, 24360, 10232, 37544, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 44100, 33464, 18880, 11228, 495, 54097, 25589, 14888, 29546, 48602, 25620, 43587, 16157, 38318, 32996, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 5897, 15494, 49595, 27019, 43234, 10432, 52389, 51755, 36367, 26520, 7121, 27580, 29048, 30362, 46700, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428, 257, 43981, 10113, 52679, 17506, 48498, 5380, 19457, 55453, 40466, 6051, 50242, 1707, 52890, 57541]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.50911283493042})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.7940354347229004})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.4583425521850586})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.0745673179626465})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.5141797065734863})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.562791347503662})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.6893839836120605})
store['active_learning_steps'][0]['training']['best_epoch']=4
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6597, 'crossentropy': 2.8695677734375}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.1985266208648682})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.1493843793869019})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.1918514966964722})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.1325552463531494})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.156511664390564})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.1678788661956787})
store['active_learning_steps'][0]['eval_training']['best_epoch']=4
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 36475], ['id', 29246], ['id', 10025], ['id', 8509], ['id', 56775]], 'labels': [2, 3, 0, 0, 0], 'scores': [1.3163556880127452, 2.214728035776967, 2.8747070546764544, 3.284634351130026, 3.5161982555948104]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.30465030670166})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.9328551292419434})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.130610942840576})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.3256609439849854})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.411872625350952})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.559330463409424})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.3571653366088867})
store['active_learning_steps'][1]['training']['best_epoch']=4
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6615, 'crossentropy': 2.998073046875}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.2348761558532715})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.2061787843704224})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.2617535591125488})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.2570960521697998})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.2308405637741089})
store['active_learning_steps'][1]['eval_training']['best_epoch']=2
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 4834], ['id', 36826], ['id', 24311], ['id', 17658], ['ood', 13417]], 'labels': [8, 6, 8, 8, -1], 'scores': [1.1167800279735425, 2.0321805453037203, 2.707647567489845, 3.0909701396006977, 3.2532540342267815]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.7508583068847656})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.2816121578216553})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.837331771850586})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 2.1834726333618164})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.8564019203186035})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.4943602085113525})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.9830260276794434})
store['active_learning_steps'][2]['training']['best_epoch']=4
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7404, 'crossentropy': 2.1313833984375}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.008880853652954})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.0506682395935059})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.0340526103973389})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.017455816268921})
store['active_learning_steps'][2]['eval_training']['best_epoch']=1
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 12019], ['id', 11762], ['id', 24479], ['id', 9306], ['ood', 30119]], 'labels': [4, 9, 8, 9, -1], 'scores': [0.8653734745291985, 1.5942755759465181, 2.137221190061724, 2.4815668545526997, 2.66553787902519]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.6924452781677246})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.8190734386444092})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.8435062170028687})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.9955835342407227})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 2.0756494998931885})
store['active_learning_steps'][3]['training']['best_epoch']=2
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7762, 'crossentropy': 1.586523828125}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 0.9710304737091064})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 0.9018458724021912})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 0.9104783535003662})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 0.883325457572937})
store['active_learning_steps'][3]['eval_training']['best_epoch']=4
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 21851], ['id', 7005], ['id', 23105], ['id', 33203], ['id', 35674]], 'labels': [8, 2, 5, 2, 5], 'scores': [0.9076933524453765, 1.7119267105796663, 2.358398909587514, 2.726141016805281, 2.942057058201282]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.594048023223877})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 2.040469169616699})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.8375935554504395})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.7932326793670654})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.7725684642791748})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.9097082614898682})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 2.075155735015869})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 2.172590732574463})
store['active_learning_steps'][4]['training']['best_epoch']=5
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7775, 'crossentropy': 1.5838240234375}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 0.9678583741188049})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 0.8714487552642822})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 0.8400522470474243})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 0.8007820248603821})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 0.789665699005127})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 0.795091986656189})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 0.7989482879638672})
store['active_learning_steps'][4]['eval_training']['best_epoch']=6
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 27556], ['id', 40654], ['id', 287], ['id', 48113], ['id', 13865]], 'labels': [6, 5, 5, 5, 6], 'scores': [1.020278920178809, 1.8619653004452892, 2.4316315297036297, 2.797316598555982, 3.0230074102477396]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.5663347244262695})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.839250922203064})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.9798099994659424})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.724290370941162})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.9634861946105957})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 2.168863534927368})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 2.231856346130371})
store['active_learning_steps'][5]['training']['best_epoch']=4
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7913, 'crossentropy': 1.5272888671875}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.0088392496109009})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 0.8540633916854858})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 0.8138593435287476})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 0.8187133073806763})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 0.8393263816833496})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 0.8239340782165527})
store['active_learning_steps'][5]['eval_training']['best_epoch']=3
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 45047], ['id', 59957], ['id', 55756], ['id', 15245], ['id', 44684]], 'labels': [2, 3, 7, 3, 3], 'scores': [0.944478264275797, 1.7349538775947106, 2.3526290860820867, 2.7625812161683916, 2.9489051414558807]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.1584928035736084})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.3484506607055664})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.301100254058838})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.4184198379516602})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.619986891746521})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.5714753866195679})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.6282881498336792})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 2.0133485794067383})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.673163652420044})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.6510512828826904})
store['active_learning_steps'][6]['training']['best_epoch']=7
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.834, 'crossentropy': 1.39000146484375}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.7563275694847107})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.6718048453330994})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.6523958444595337})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.6234387755393982})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.6348620653152466})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.6474628448486328})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.6101017594337463})
store['active_learning_steps'][6]['eval_training']['best_epoch']=4
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 244], ['id', 49926], ['id', 23195], ['id', 37447], ['ood', 55394]], 'labels': [5, 3, 6, 4, -1], 'scores': [1.0488114543507292, 1.905168925214967, 2.5350983637880526, 2.892454308005746, 3.0382475753131963]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.0930542945861816})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.1182808876037598})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.1800904273986816})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.1568949222564697})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.3012866973876953})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.2555253505706787})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.3432331085205078})
store['active_learning_steps'][7]['training']['best_epoch']=4
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8572, 'crossentropy': 1.0137083984375}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.7709856033325195})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.649590015411377})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.6249913573265076})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.6401934623718262})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.5973595380783081})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.5999724864959717})
store['active_learning_steps'][7]['eval_training']['best_epoch']=3
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 1423], ['id', 47260], ['id', 9687], ['id', 41078], ['ood', 27940]], 'labels': [0, 6, 0, 8, -1], 'scores': [0.9257126508308222, 1.6633395653120058, 2.2148263941382096, 2.584775662028113, 2.7845346928677532]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.0830154418945312})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.1430623531341553})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.3505604267120361})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.467471718788147})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.5170871019363403})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.832, 'crossentropy': 1.07195986328125}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.8040540218353271})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.7791673541069031})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.6943187713623047})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.6905232071876526})
store['active_learning_steps'][8]['eval_training']['best_epoch']=3
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 1724], ['id', 21393], ['id', 24795], ['id', 17756], ['id', 46726]], 'labels': [2, 4, 4, 8, 0], 'scores': [0.812821411693649, 1.4576253893988484, 2.011046769732877, 2.3957922467496617, 2.6511449988584683]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.1010525226593018})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.9976565837860107})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.0715107917785645})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.1883450746536255})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.1748342514038086})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.1517727375030518})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.3518235683441162})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.37882399559021})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.4672119617462158})
store['active_learning_steps'][9]['training']['best_epoch']=6
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8555, 'crossentropy': 1.15305419921875}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.789913535118103})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.6810269355773926})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.6736752986907959})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.604499876499176})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.6111902594566345})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.611186146736145})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.6197257041931152})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.6118944883346558})
store['active_learning_steps'][9]['eval_training']['best_epoch']=5
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 14749], ['id', 42255], ['id', 15655], ['id', 14751], ['id', 36268]], 'labels': [0, 3, 5, 8, 5], 'scores': [0.9333423895682713, 1.6738156256914722, 2.2932385913605247, 2.6812892987247183, 2.8992116987202596]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.0859652757644653})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.1822717189788818})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.3366457223892212})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.4883430004119873})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.3035244941711426})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.243992805480957})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.302114725112915})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.4070093631744385})
store['active_learning_steps'][10]['training']['best_epoch']=5
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8436, 'crossentropy': 1.22014599609375}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.8419405221939087})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.7271161079406738})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.6869725584983826})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.7008910179138184})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.6587437987327576})
store['active_learning_steps'][10]['eval_training']['best_epoch']=2
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 10744], ['id', 42313], ['id', 37769], ['id', 48665], ['id', 45452]], 'labels': [7, 8, 7, 2, 5], 'scores': [0.815295056852211, 1.5115266100771163, 2.080544859971466, 2.445962487227881, 2.642551464977844]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.010301113128662})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.0817811489105225})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.2136332988739014})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.2741776704788208})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.297727346420288})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.3121263980865479})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.254361867904663})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.2994440793991089})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.5014450550079346})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.300502896308899})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.466768741607666})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.6220718622207642})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.4565856456756592})
store['active_learning_steps'][11]['training']['best_epoch']=10
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.856, 'crossentropy': 1.25889375}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.7832352519035339})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.6254703402519226})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.6083071827888489})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.5764017105102539})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.545727014541626})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.5535151362419128})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.5761000514030457})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.5810933709144592})
store['active_learning_steps'][11]['eval_training']['best_epoch']=5
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 44961], ['id', 42793], ['id', 20709], ['id', 28925], ['id', 18096]], 'labels': [8, 4, 8, 1, 6], 'scores': [0.9943374234919562, 1.8469791335953127, 2.4784582321645248, 2.838915524601104, 3.0505996904133967]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.9523128271102905})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8834924101829529})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.0410206317901611})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9228176474571228})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9337992668151855})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.1912087202072144})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 1.1985749006271362})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 1.113671064376831})
store['active_learning_steps'][12]['training']['best_epoch']=5
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8887, 'crossentropy': 0.83801318359375}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7128328084945679})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5484619140625})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5162626504898071})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5093173384666443})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.4915030002593994})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.4756390452384949})
store['active_learning_steps'][12]['eval_training']['best_epoch']=3
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 10194], ['id', 13460], ['id', 37397], ['id', 21421], ['id', 56780]], 'labels': [2, 5, 3, 8, 7], 'scores': [0.9447927728523083, 1.657303540933781, 2.1760766222841794, 2.506984254712183, 2.685863514801304]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.9101223945617676})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7150363922119141})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8177876472473145})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.854438066482544})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8211022615432739})
store['active_learning_steps'][13]['training']['best_epoch']=2
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8827, 'crossentropy': 0.70886875}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.6751006841659546})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.5540881156921387})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.5366530418395996})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.5163399577140808})
store['active_learning_steps'][13]['eval_training']['best_epoch']=2
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 43648], ['id', 5315], ['id', 4421], ['ood', 43952], ['id', 10412]], 'labels': [5, 3, 7, -1, 5], 'scores': [0.7397798581956672, 1.380566009174133, 1.8725627337799864, 2.2054455360769554, 2.4286534017515855]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9508162140846252})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8252935409545898})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9387696981430054})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8565250039100647})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9127334952354431})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9775478839874268})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8922085165977478})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8998948335647583})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.9449264407157898})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 1.1208866834640503})
store['active_learning_steps'][14]['training']['best_epoch']=7
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8966, 'crossentropy': 0.8422630859375}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.7631040215492249})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.5579072833061218})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.5379238128662109})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.4809223413467407})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.48413562774658203})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.4568507671356201})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.47993916273117065})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.44052866101264954})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.4550921320915222})
store['active_learning_steps'][14]['eval_training']['best_epoch']=8
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 34332], ['id', 48975], ['id', 13757], ['id', 17777], ['id', 37168]], 'labels': [9, 2, 9, 3, 7], 'scores': [0.8650135430577792, 1.668373444544478, 2.322223167117074, 2.717755068751061, 2.962711561065432]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7682044506072998})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6506427526473999})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6671215891838074})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6982694268226624})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7217082977294922})
store['active_learning_steps'][15]['training']['best_epoch']=2
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9061, 'crossentropy': 0.659975634765625}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6645809412002563})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5370490550994873})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5144335627555847})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.4934544563293457})
store['active_learning_steps'][15]['eval_training']['best_epoch']=4
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 59380], ['id', 2352], ['id', 21402], ['id', 31415], ['id', 40507]], 'labels': [8, 0, 1, 5, 9], 'scores': [0.7384566108026971, 1.383243313678812, 1.9206068427828002, 2.2635901891810617, 2.4915592278684597]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8534537553787231})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6550483703613281})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6754071712493896})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7022911310195923})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7777520418167114})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7840273976325989})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.8513604402542114})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7036976218223572})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7946834564208984})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.951820433139801})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.8065780401229858})
store['active_learning_steps'][16]['training']['best_epoch']=8
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9095, 'crossentropy': 0.702934765625}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6716854572296143})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5270216464996338})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.4576810598373413})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4437929391860962})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4519243836402893})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4145192801952362})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4098152220249176})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4073478579521179})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.41794872283935547})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.40756896138191223})
store['active_learning_steps'][16]['eval_training']['best_epoch']=9
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 47409], ['id', 49945], ['id', 50802], ['id', 53220], ['id', 14144]], 'labels': [2, 9, 2, 6, 5], 'scores': [0.8680715042672162, 1.681166835208217, 2.2856643851339546, 2.6921148618215023, 2.9317104345019924]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.794796347618103})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6786080598831177})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6487743854522705})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6463693380355835})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6292408108711243})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7363075017929077})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.669727623462677})
store['active_learning_steps'][17]['training']['best_epoch']=4
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9119, 'crossentropy': 0.628733984375}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6651873588562012})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5101816058158875})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4518837630748749})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.4295140504837036})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4095292091369629})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.41280075907707214})
store['active_learning_steps'][17]['eval_training']['best_epoch']=6
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 39875], ['id', 3719], ['id', 2092], ['ood', 35145], ['ood', 15237]], 'labels': [4, 2, 3, -1, -1], 'scores': [0.873781377348366, 1.5625263122596649, 2.129249454885233, 2.494923197412257, 2.7180297073132147]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8279892206192017})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6363780498504639})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6852176785469055})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6460877060890198})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.660578727722168})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7478306889533997})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.7306849956512451})
store['active_learning_steps'][18]['training']['best_epoch']=4
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9167, 'crossentropy': 0.602858251953125}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6691742539405823})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5106471180915833})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.45036065578460693})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.449274480342865})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.43024832010269165})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.43482866883277893})
store['active_learning_steps'][18]['eval_training']['best_epoch']=6
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 32880], ['id', 15899], ['id', 13752], ['id', 17238], ['id', 19909]], 'labels': [0, 9, 9, 4, 5], 'scores': [0.789321129714506, 1.464175683817404, 1.9755434949312143, 2.306344788205344, 2.518778532947401]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.9179000854492188})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6437428593635559})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6203593015670776})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6818943023681641})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.696173906326294})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6810500025749207})
store['active_learning_steps'][19]['training']['best_epoch']=3
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9121, 'crossentropy': 0.586510498046875}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7004590034484863})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.49726855754852295})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4631706476211548})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4517289400100708})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4645835757255554})
store['active_learning_steps'][19]['eval_training']['best_epoch']=5
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 20050], ['id', 59468], ['id', 42438], ['id', 58575], ['id', 51759]], 'labels': [9, 7, 9, 0, 3], 'scores': [0.7416130014883042, 1.414996228869076, 1.9347748962242601, 2.309869869930168, 2.535446552464564]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.9547945261001587})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.637367308139801})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5966387987136841})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5727847814559937})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6751703023910522})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6548764109611511})
store['active_learning_steps'][20]['training']['best_epoch']=3
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9208, 'crossentropy': 0.55614833984375}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7698782086372375})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5625580549240112})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.46139299869537354})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4633267819881439})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.45688730478286743})
store['active_learning_steps'][20]['eval_training']['best_epoch']=4
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 52140], ['id', 14394], ['id', 35474], ['ood', 11271], ['ood', 33781]], 'labels': [4, 3, 7, -1, -1], 'scores': [0.7380910318908565, 1.4159560931861632, 1.9882972998626594, 2.371117014663567, 2.605444972554314]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.9829936027526855})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5683131814002991})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5833402276039124})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5852920413017273})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.629650890827179})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6715744733810425})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6343135833740234})
store['active_learning_steps'][21]['training']['best_epoch']=4
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9287, 'crossentropy': 0.522489208984375}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7483158707618713})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.47823816537857056})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.41423505544662476})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3914630711078644})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.40088951587677})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3833158314228058})
store['active_learning_steps'][21]['eval_training']['best_epoch']=6
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 4005], ['id', 22083], ['id', 22505], ['id', 41267], ['id', 27473]], 'labels': [2, 2, 9, 3, 4], 'scores': [0.7489109092098152, 1.3906993968871237, 1.9338360043728455, 2.3307024814424704, 2.5834411074514767]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.00704026222229})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.660821795463562})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5593711137771606})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5912028551101685})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6166211366653442})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6762816905975342})
store['active_learning_steps'][22]['training']['best_epoch']=3
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9287, 'crossentropy': 0.549180859375}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7275991439819336})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5732872486114502})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5312404036521912})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4776049256324768})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4586770832538605})
store['active_learning_steps'][22]['eval_training']['best_epoch']=4
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 8932], ['id', 414], ['id', 45687], ['id', 19904], ['id', 43404]], 'labels': [0, 4, 3, 7, 0], 'scores': [0.6698475001484867, 1.23949587119637, 1.7309246756184047, 2.0831396944820844, 2.3228401281638256]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.9609442949295044})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6117544174194336})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5359766483306885})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5993121862411499})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5896902084350586})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5938500761985779})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.650115966796875})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6171215176582336})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6609047651290894})
store['active_learning_steps'][23]['training']['best_epoch']=6
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9403, 'crossentropy': 0.50983740234375}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6828796863555908})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4745190143585205})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.42041143774986267})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3949323296546936})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3591264486312866})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.34995245933532715})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.35207295417785645})
store['active_learning_steps'][23]['eval_training']['best_epoch']=4
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 11208], ['id', 44806], ['id', 55645], ['id', 47600], ['ood', 38613]], 'labels': [9, 8, 6, 7, -1], 'scores': [0.7822314506766825, 1.4878280381950457, 2.0454427007539744, 2.4494355021307674, 2.6531563573237156]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8937692642211914})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5823013782501221})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5376584529876709})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6372987627983093})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5816235542297363})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5781587362289429})
store['active_learning_steps'][24]['training']['best_epoch']=3
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9215, 'crossentropy': 0.535207421875}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7315362691879272})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5140960812568665})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.48020756244659424})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4356262981891632})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.4838378429412842})
store['active_learning_steps'][24]['eval_training']['best_epoch']=4
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 47475], ['id', 53170], ['id', 3273], ['ood', 22188], ['id', 17296]], 'labels': [5, 8, 8, -1, 9], 'scores': [0.6484808091958285, 1.224412237445363, 1.7097123652735453, 2.0797310690040742, 2.303772747560739]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8389222621917725})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6510365009307861})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6098715662956238})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5894289016723633})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6382068395614624})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6182703971862793})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6528416872024536})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5903552770614624})
store['active_learning_steps'][25]['training']['best_epoch']=5
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.916, 'crossentropy': 0.60170673828125}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6957529783248901})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.48857399821281433})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.46945691108703613})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.44006502628326416})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.45975711941719055})
store['active_learning_steps'][25]['eval_training']['best_epoch']=2
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 38050], ['id', 26898], ['id', 34496], ['id', 50755], ['id', 45761]], 'labels': [6, 7, 9, 3, 4], 'scores': [0.7721077714575921, 1.4440361929748118, 1.961349137750143, 2.3392712948801035, 2.5530948684946333]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8915057182312012})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5858356952667236})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5584738254547119})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5869433879852295})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5980126857757568})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6880024671554565})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6449785232543945})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.7074037194252014})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6013880968093872})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6771272420883179})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.7521493434906006})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6413735151290894})
store['active_learning_steps'][26]['training']['best_epoch']=9
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.933, 'crossentropy': 0.5649775390625}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6929707527160645})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.48771780729293823})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.41912713646888733})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.39737528562545776})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.39257803559303284})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.36950212717056274})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.3663891553878784})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.3481081426143646})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3565255403518677})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.36249321699142456})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.34407421946525574})
store['active_learning_steps'][26]['eval_training']['best_epoch']=9
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 35654], ['id', 52169], ['id', 26358], ['ood', 19767], ['ood', 16218]], 'labels': [1, 2, 3, -1, -1], 'scores': [0.8944030833167067, 1.6528404415683307, 2.197469454651947, 2.5011913207164262, 2.697779348913352]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.9279685616493225})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6019522547721863})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.574748694896698})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5953149795532227})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5262857675552368})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5233826637268066})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5841354131698608})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.604239284992218})
store['active_learning_steps'][27]['training']['best_epoch']=5
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9352, 'crossentropy': 0.487687158203125}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7306032180786133})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.49436554312705994})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.43188682198524475})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4148021340370178})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.427436888217926})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.37389370799064636})
store['active_learning_steps'][27]['eval_training']['best_epoch']=3
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 8432], ['id', 45586], ['id', 42741], ['ood', 26972], ['ood', 51121]], 'labels': [8, 3, 2, -1, -1], 'scores': [0.7873593649280481, 1.4161573484340835, 1.9537738391987158, 2.337449568172815, 2.582473009640718]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.9291913509368896})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5838714838027954})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6002880334854126})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6137317419052124})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6198405623435974})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6183900833129883})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6275918483734131})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5883412957191467})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.7781791090965271})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6540862917900085})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6885882616043091})
store['active_learning_steps'][28]['training']['best_epoch']=8
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9305, 'crossentropy': 0.6069775390625}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7241673469543457})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.47732478380203247})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4137022793292999})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4058143198490143})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3834630250930786})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.369736909866333})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3552434742450714})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.36625903844833374})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.34902340173721313})
store['active_learning_steps'][28]['eval_training']['best_epoch']=6
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 35089], ['id', 18573], ['id', 47322], ['id', 6608], ['id', 15133]], 'labels': [1, 5, 8, 4, 0], 'scores': [0.8559987839478924, 1.5830761146540802, 2.1691596541162474, 2.5544719619120215, 2.7767143256869504]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.9811903238296509})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5720239877700806})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5375552773475647})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5857871174812317})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5867838263511658})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5407499074935913})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5802778005599976})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5740444660186768})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.6266682147979736})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5788271427154541})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.639188826084137})
store['active_learning_steps'][29]['training']['best_epoch']=8
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9344, 'crossentropy': 0.56163125}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6700815558433533})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.47042596340179443})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4332761764526367})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4191998243331909})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3695383071899414})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.38807761669158936})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.34915030002593994})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3544137477874756})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.34540867805480957})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.33951979875564575})
store['active_learning_steps'][29]['eval_training']['best_epoch']=8
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 59747], ['id', 20573], ['id', 39248], ['ood', 19378], ['id', 16937]], 'labels': [5, 9, 4, -1, 8], 'scores': [0.7835717534115465, 1.5037429513722484, 2.0350035804582225, 2.3959665202462403, 2.6134601048921366]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.932875394821167})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5017951726913452})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.49438101053237915})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.542034387588501})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.44867995381355286})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.526823878288269})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.5374926924705505})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5172245502471924})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5120229721069336})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.6151002645492554})
store['active_learning_steps'][30]['training']['best_epoch']=7
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9371, 'crossentropy': 0.522760546875}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.663898766040802})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4700808823108673})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.43704456090927124})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3782827854156494})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.33915892243385315})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3354530930519104})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3323896527290344})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3260192275047302})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3184041380882263})
store['active_learning_steps'][30]['eval_training']['best_epoch']=8
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 32724], ['id', 41979], ['id', 25156], ['id', 26519], ['ood', 10939]], 'labels': [5, 9, 2, 8, -1], 'scores': [0.8302136925180723, 1.4987048023401481, 2.0288971125261437, 2.3825372764082378, 2.5953273784217368]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9232200384140015})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5712541341781616})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5031132102012634})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4455365538597107})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4588289260864258})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.479684054851532})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4776170253753662})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4714471399784088})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5389302372932434})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.538989245891571})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.47192472219467163})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.47894251346588135})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5237430930137634})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.482662558555603})
store['active_learning_steps'][31]['training']['best_epoch']=11
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9443, 'crossentropy': 0.5004646484375}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6729917526245117})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4101327657699585})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3750995397567749})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3584229350090027})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3639124631881714})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.33128345012664795})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.31111574172973633})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3219118118286133})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3076620101928711})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.31881189346313477})
store['active_learning_steps'][31]['eval_training']['best_epoch']=7
store['active_learning_steps'][31]['acquisition']={'indices': [['ood', 41362], ['id', 14062], ['ood', 32974], ['ood', 33141], ['id', 54603]], 'labels': [-1, 8, -1, -1, 3], 'scores': [0.8001483676779586, 1.5076298076322443, 2.074985242793101, 2.4616116218582302, 2.7019145920028746]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8349249362945557})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5460081100463867})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4656609296798706})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4591811001300812})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4902087450027466})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4812718629837036})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4895382821559906})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4727952480316162})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5213372707366943})
store['active_learning_steps'][32]['training']['best_epoch']=6
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9466, 'crossentropy': 0.45277490234375}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6225600838661194})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.44171538949012756})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.40328556299209595})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3592730462551117})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3409014344215393})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3185141980648041})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3129115104675293})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.2952006459236145})
store['active_learning_steps'][32]['eval_training']['best_epoch']=7
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 57742], ['id', 12840], ['ood', 9049], ['id', 36578], ['ood', 19378]], 'labels': [6, 9, -1, 6, -1], 'scores': [0.8467280795986099, 1.5448591153237317, 2.133564052302239, 2.561633770922491, 2.8251199269108485]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.9376301765441895})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5454181432723999})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4660433232784271})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5091412663459778})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4643791615962982})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5410541296005249})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5308359861373901})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5311468839645386})
store['active_learning_steps'][33]['training']['best_epoch']=5
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9411, 'crossentropy': 0.46531962890625}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8039771914482117})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5054410696029663})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4425013065338135})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.3681551218032837})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3665231466293335})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.37929192185401917})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3680979013442993})
store['active_learning_steps'][33]['eval_training']['best_epoch']=7
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 59339], ['id', 20641], ['id', 38497], ['ood', 11672], ['id', 16592]], 'labels': [1, 9, 0, -1, 5], 'scores': [0.6940853968881147, 1.3068150580984912, 1.8061119658973057, 2.145598852530762, 2.379801571013835]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.0134694576263428})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5950049757957458})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4628424644470215})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4966338276863098})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.46922630071640015})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4566463828086853})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4927223026752472})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4936181902885437})
store['active_learning_steps'][34]['training']['best_epoch']=5
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9464, 'crossentropy': 0.427322021484375}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7122632265090942})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.476846307516098})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.42509281635284424})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4274177551269531})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.379932165145874})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3579657971858978})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3757852613925934})
store['active_learning_steps'][34]['eval_training']['best_epoch']=5
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 37778], ['id', 54004], ['ood', 45307], ['id', 52978], ['id', 11196]], 'labels': [8, 0, -1, 0, 9], 'scores': [0.7958216699666736, 1.5056527668195572, 2.0944460151987707, 2.4850339635239083, 2.688376536002732]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.9373593330383301})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5479625463485718})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.46247899532318115})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4760913848876953})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.45881831645965576})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5109375715255737})
store['active_learning_steps'][35]['training']['best_epoch']=3
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9404, 'crossentropy': 0.426545849609375}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6896083354949951})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.45810380578041077})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4451046586036682})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.40231969952583313})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4189332127571106})
store['active_learning_steps'][35]['eval_training']['best_epoch']=5
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 20035], ['id', 29662], ['id', 14760], ['id', 13127], ['id', 45607]], 'labels': [8, 2, 2, 3, 5], 'scores': [0.6405884901720889, 1.2111048289593063, 1.6725522900772214, 2.0315141000242587, 2.290808214421851]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.0915682315826416})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5373811721801758})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.45520704984664917})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.46038663387298584})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4482373595237732})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4611138701438904})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.47808918356895447})
store['active_learning_steps'][36]['training']['best_epoch']=4
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9465, 'crossentropy': 0.417556884765625}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7690470218658447})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4833625555038452})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4055076539516449})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3783344030380249})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3839963674545288})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.34705495834350586})
store['active_learning_steps'][36]['eval_training']['best_epoch']=6
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 42078], ['id', 12497], ['id', 2636], ['id', 27758], ['id', 46134]], 'labels': [4, 0, 8, 7, 3], 'scores': [0.7476634316484052, 1.4006857830741328, 1.862250073671337, 2.1720543906108594, 2.3747545298917423]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.0275095701217651})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5817784070968628})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5011247992515564})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4360097646713257})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.46117693185806274})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.43146437406539917})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4644858241081238})
store['active_learning_steps'][37]['training']['best_epoch']=4
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9502, 'crossentropy': 0.4093626220703125}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6819205284118652})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4934690296649933})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4352385997772217})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.41912660002708435})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.37651821970939636})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3837110102176666})
store['active_learning_steps'][37]['eval_training']['best_epoch']=6
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 12305], ['id', 21023], ['ood', 47952], ['id', 22497], ['ood', 35168]], 'labels': [9, 2, -1, 7, -1], 'scores': [0.7394817800628211, 1.4028884197133626, 1.8841154940709899, 2.233168376487037, 2.443036135671937]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 1.0076971054077148})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5457461476325989})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4636214077472687})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.44442683458328247})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.42964041233062744})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.435504674911499})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.45446598529815674})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4420565962791443})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.45629096031188965})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.41307753324508667})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.42690280079841614})
store['active_learning_steps'][38]['training']['best_epoch']=8
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.95, 'crossentropy': 0.3899637939453125}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7486559152603149})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.478256493806839})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3792969584465027})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3365275263786316})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3426002860069275})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3243367671966553})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.28818991780281067})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2861056923866272})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2928500175476074})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2907096743583679})
store['active_learning_steps'][38]['eval_training']['best_epoch']=10
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 49282], ['id', 11616], ['id', 26613], ['id', 12379], ['id', 7434]], 'labels': [2, 7, 2, 8, 6], 'scores': [0.7597345578332728, 1.4708560074627939, 2.0099744838507405, 2.3701859046484373, 2.599245925557658]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9619806408882141})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5516505241394043})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5338307023048401})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.46010053157806396})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.45848405361175537})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4630264341831207})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4234107732772827})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4791601002216339})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4631732404232025})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.47141778469085693})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.5348318815231323})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.5173336267471313})
store['active_learning_steps'][39]['training']['best_epoch']=9
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9523, 'crossentropy': 0.43352685546875}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8103792667388916})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4957405924797058})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4003930389881134})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3579481244087219})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.34437498450279236})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.34091562032699585})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3246298134326935})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3393487334251404})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3138549327850342})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.31609874963760376})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.30522090196609497})
store['active_learning_steps'][39]['eval_training']['best_epoch']=9
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 34610], ['id', 44342], ['id', 31926], ['id', 7301], ['id', 51502]], 'labels': [5, 4, 5, 7, 7], 'scores': [0.7862122935414531, 1.4909561561729614, 2.087458393158463, 2.453178568287342, 2.6793052113863824]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 1.0469913482666016})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.52020263671875})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.43481314182281494})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4301374554634094})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4791080355644226})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.41773825883865356})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4751318097114563})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4212269186973572})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4446413815021515})
store['active_learning_steps'][40]['training']['best_epoch']=6
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9482, 'crossentropy': 0.4029258544921875}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7269084453582764})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.47502875328063965})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4221728444099426})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4002661406993866})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.36674362421035767})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3566163182258606})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3160219192504883})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.33904004096984863})
store['active_learning_steps'][40]['eval_training']['best_epoch']=5
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 54377], ['id', 16834], ['id', 54935], ['id', 6254], ['ood', 54326]], 'labels': [3, 5, 8, 1, -1], 'scores': [0.6234926489853252, 1.1773147866677989, 1.6393855353195086, 1.9580446121526176, 2.15696744995409]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.9107441306114197})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4656376838684082})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4449712038040161})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.434332013130188})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4494204521179199})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.41404885053634644})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.422590434551239})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.37895044684410095})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.43334758281707764})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.426175057888031})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4224894046783447})
store['active_learning_steps'][41]['training']['best_epoch']=8
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.96, 'crossentropy': 0.3373094970703125}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6959506869316101})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4927733540534973})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3555198907852173})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.33355778455734253})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.33792954683303833})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3205748498439789})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.289876788854599})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.29677489399909973})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.27950143814086914})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2872248888015747})
store['active_learning_steps'][41]['eval_training']['best_epoch']=10
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 19868], ['id', 34946], ['id', 26150], ['id', 44480], ['id', 40664]], 'labels': [5, 8, 5, 5, 1], 'scores': [0.8376883810340034, 1.5425686459631915, 2.095698427137074, 2.433567433437524, 2.663025783209874]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.0013272762298584})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.510017991065979})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4369654655456543})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.418114572763443})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.44382214546203613})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.47743573784828186})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.4033307135105133})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.4155121445655823})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3960886299610138})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4016724228858948})
store['active_learning_steps'][42]['training']['best_epoch']=7
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9628, 'crossentropy': 0.351448388671875}
