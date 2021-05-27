store = {}
store['timestamp']=1622115591
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=20']
store['commit']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['github_url']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=20
store['worker_id']=20
store['num_workers']=80
store['config']={'seed': 1255, 'uniform_ood': True, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 256, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('FastFashionMNIST Train (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3029, 35714, 21536, 48519, 8821, 11261, 35237, 33891, 37129, 46683, 6968, 15917, 30184, 50055, 14637, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 14035, 42320, 16927, 42102, 39050, 27573, 30980, 53362, 18819, 21800, 44138, 39879, 13092, 51760, 48953, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 26129, 37115, 35072, 36688, 54003, 72, 57690, 7382, 7896, 24110, 35372, 37098, 54536, 34513, 37157, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 26853, 42295, 34121, 19215, 12917, 51600, 27383, 20917, 38856, 15822, 6612, 13359, 28181, 7145, 49775, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 54422, 229, 30072, 4701, 18693, 26516, 43141, 5588, 7356, 55148, 2773, 24971, 57801, 17644, 54479, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 43415, 17659, 12075, 26428, 8705, 29556, 8108, 8710, 17032, 17195, 5481, 24223, 17968, 56054, 39333, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 33581, 48521, 36270, 57175, 11554, 11773, 41082, 37625, 41077, 13036, 32625, 54017, 24360, 10232, 37544, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 44100, 33464, 18880, 11228, 495, 54097, 25589, 14888, 29546, 48602, 25620, 43587, 16157, 38318, 32996, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 5897, 15494, 49595, 27019, 43234, 10432, 52389, 51755, 36367, 26520, 7121, 27580, 29048, 30362, 46700, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428, 257, 43981, 10113, 52679, 17506, 48498, 5380, 19457, 55453, 40466, 6051, 50242, 1707, 52890, 57541]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.490886926651001})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.8523449897766113})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.8437702655792236})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.2704498767852783})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.0792922973632812})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.3304834365844727})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.9288649559020996})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.4357423782348633})
store['active_learning_steps'][0]['training']['best_epoch']=5
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6582, 'crossentropy': 2.9104478515625}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.3323793411254883})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.3138835430145264})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.3048598766326904})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.318731665611267})
store['active_learning_steps'][0]['eval_training']['best_epoch']=1
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 49137], ['id', 18971], ['id', 36475], ['id', 21650], ['ood', 9184]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [1.119840006847543, 1.9645907504397444, 2.5757989478726566, 2.9639428475863845, 3.130965832146213]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.7590662240982056})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.1959927082061768})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.0380382537841797})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.2574617862701416})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.4426631927490234})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.3347222805023193})
store['active_learning_steps'][1]['training']['best_epoch']=3
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7057, 'crossentropy': 1.8836109375}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.218042016029358})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.1263442039489746})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.0869988203048706})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.0996596813201904})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.074159026145935})
store['active_learning_steps'][1]['eval_training']['best_epoch']=5
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 35674], ['id', 29034], ['id', 23388], ['id', 44820], ['id', 17671]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.8755207748368434, 1.627009502534611, 2.1765246027738883, 2.5946617427202323, 2.857745545417501]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.5335725545883179})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.8986272811889648})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.052476644515991})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.9708683490753174})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.2896828651428223})
store['active_learning_steps'][2]['training']['best_epoch']=2
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7346, 'crossentropy': 1.59364765625}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.0426653623580933})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 0.9763063788414001})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 0.9693124890327454})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.014182448387146})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 10107], ['id', 14418], ['id', 49302], ['id', 21188], ['id', 38147]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9563575669807851, 1.7443979418273203, 2.4028360202962347, 2.8090217617406656, 3.0617367191805016]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.3043408393859863})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.5348119735717773})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.6844444274902344})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.599312424659729})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.7761887311935425})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.8379533290863037})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.757928490638733})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 2.152019739151001})
store['active_learning_steps'][3]['training']['best_epoch']=5
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7935, 'crossentropy': 1.6138041015625}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 0.879644513130188})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 0.8154410123825073})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 0.7815372943878174})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 0.7908047437667847})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 0.8155306577682495})
store['active_learning_steps'][3]['eval_training']['best_epoch']=2
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 42315], ['id', 14749], ['id', 52140], ['id', 4814], ['ood', 51075]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.9109280814242582, 1.647679236653071, 2.2050919677801577, 2.5743201852820654, 2.764010864044618]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.3066658973693848})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.4632481336593628})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.5752172470092773})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.7239439487457275})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.872584581375122})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.816444993019104})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 2.0309762954711914})
store['active_learning_steps'][4]['training']['best_epoch']=4
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7798, 'crossentropy': 1.68576640625}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 0.9097206592559814})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 0.9275643825531006})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 0.8727059364318848})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 0.8470970988273621})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 0.8480583429336548})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 0.863898515701294})
store['active_learning_steps'][4]['eval_training']['best_epoch']=4
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 37039], ['id', 20643], ['id', 9603], ['id', 39182], ['id', 46794]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.9011873081766946, 1.710388398826478, 2.3747353760307215, 2.7743744632516973, 3.0026281267655115]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.1668670177459717})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.4337561130523682})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.5913732051849365})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.8339087963104248})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.8804442882537842})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.7671416997909546})
store['active_learning_steps'][5]['training']['best_epoch']=3
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.797, 'crossentropy': 1.4344724609375}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 0.9489150047302246})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 0.9105300903320312})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 0.8722121715545654})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.8035716414451599})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 0.8236469626426697})
store['active_learning_steps'][5]['eval_training']['best_epoch']=4
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 25860], ['id', 23901], ['id', 8859], ['id', 57124], ['id', 4421]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.8148132511007553, 1.5090891230643386, 2.0814118338869845, 2.452274151705746, 2.6748447152734407]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.185824990272522})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.2313666343688965})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.2621424198150635})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.2795382738113403})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.308358073234558})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.4458496570587158})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.4685801267623901})
store['active_learning_steps'][6]['training']['best_epoch']=4
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8348, 'crossentropy': 1.14536015625}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.8007872104644775})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.7585783004760742})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.7032549977302551})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.7506664991378784})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.6567890644073486})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.6885039806365967})
store['active_learning_steps'][6]['eval_training']['best_epoch']=5
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 11943], ['id', 7374], ['id', 59623], ['id', 1875], ['id', 7595]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9460562519042637, 1.6753414382226515, 2.234035841255091, 2.621983123496923, 2.845716017770571]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.1252152919769287})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.5046833753585815})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.2411683797836304})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.3126301765441895})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.572300672531128})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.647425651550293})
store['active_learning_steps'][7]['training']['best_epoch']=3
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8273, 'crossentropy': 1.096555859375}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 0.8526747226715088})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.7387771606445312})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.7341268658638})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.702534556388855})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.7234705090522766})
store['active_learning_steps'][7]['eval_training']['best_epoch']=4
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 14233], ['id', 28375], ['id', 12385], ['id', 14222], ['id', 46250]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8280650197247426, 1.5305335678197314, 2.0576778114025336, 2.408105363288419, 2.64482284508888]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.1305503845214844})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.2839940786361694})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.3081622123718262})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.2917306423187256})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.6190800666809082})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.4006152153015137})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.6277966499328613})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.6304700374603271})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.6679823398590088})
store['active_learning_steps'][8]['training']['best_epoch']=6
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8276, 'crossentropy': 1.2767748046875}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.8458471894264221})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.7558714151382446})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.7121692299842834})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.7590551376342773})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.7318928241729736})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.7079939842224121})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.7206774353981018})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.6712141036987305})
store['active_learning_steps'][8]['eval_training']['best_epoch']=8
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 23642], ['id', 41887], ['id', 17988], ['id', 16900], ['id', 4676]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.88299377293273, 1.569691002261263, 2.08737783487096, 2.473289649988123, 2.718566807055952]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8552223443984985})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8170907497406006})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.9719319939613342})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9088168144226074})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.0623000860214233})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.2393527030944824})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.303138256072998})
store['active_learning_steps'][9]['training']['best_epoch']=4
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.87, 'crossentropy': 0.83912470703125}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.7017607092857361})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.5945779085159302})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.5847272872924805})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.563788115978241})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.5525842905044556})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.5539999604225159})
store['active_learning_steps'][9]['eval_training']['best_epoch']=5
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 15210], ['id', 1370], ['id', 32709], ['id', 29620], ['id', 3168]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.8036496212995936, 1.496929578857093, 2.055729166716942, 2.4851679273902594, 2.746149136092641]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.925815999507904})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8856066465377808})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.9450544118881226})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.023701548576355})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.0899553298950195})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.0944000482559204})
store['active_learning_steps'][10]['training']['best_epoch']=3
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8795, 'crossentropy': 0.8146802734375}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.7567155361175537})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.6360843777656555})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.5759750008583069})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.5476863384246826})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.5250608921051025})
store['active_learning_steps'][10]['eval_training']['best_epoch']=3
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 2740], ['id', 17409], ['id', 39877], ['id', 39873], ['id', 51799]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6929632961661953, 1.3063356914061388, 1.8239699358151382, 2.170936980684229, 2.3965632110407835]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7696625590324402})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8437591195106506})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.0370488166809082})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.008216142654419})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8848, 'crossentropy': 0.69059453125}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.793847918510437})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6718528270721436})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6252848505973816})
store['active_learning_steps'][11]['eval_training']['best_epoch']=2
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 31335], ['id', 19190], ['id', 16125], ['id', 55743], ['id', 41847]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5616196461234539, 1.0723413389262526, 1.487999800081905, 1.8230169905360087, 2.068026949710493]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.9153091907501221})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8409059047698975})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.0159069299697876})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.958315372467041})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 1.0943429470062256})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.1679202318191528})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 1.133730411529541})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 1.2597415447235107})
store['active_learning_steps'][12]['training']['best_epoch']=5
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.887, 'crossentropy': 0.87411982421875}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7295435667037964})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.5842543840408325})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.5468867421150208})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.5378772616386414})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5460596084594727})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.5348273515701294})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.5387521386146545})
store['active_learning_steps'][12]['eval_training']['best_epoch']=5
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 17404], ['id', 51338], ['id', 20072], ['id', 52324], ['id', 53407]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8235750850460501, 1.4922013705181691, 2.04148636826162, 2.452544328724919, 2.7217698346262758]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7686275243759155})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7999720573425293})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8231139779090881})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.9014486074447632})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9667673110961914})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9610055685043335})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9179442524909973})
store['active_learning_steps'][13]['training']['best_epoch']=4
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8959, 'crossentropy': 0.72640693359375}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7255474328994751})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.5755345821380615})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.5668745636940002})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5282231569290161})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5084265470504761})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.5524657964706421})
store['active_learning_steps'][13]['eval_training']['best_epoch']=5
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 49992], ['id', 44901], ['id', 16051], ['id', 27406], ['ood', 28645]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.8081108318289862, 1.5288535152329872, 2.097608505098055, 2.4468179743943343, 2.6709354563807937]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8697383403778076})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7841413021087646})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8488646745681763})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8360669612884521})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8442176580429077})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8178915977478027})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8801884651184082})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.9095906019210815})
store['active_learning_steps'][14]['training']['best_epoch']=5
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9012, 'crossentropy': 0.727621337890625}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6523717045783997})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5031291246414185})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.4721720814704895})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.48618632555007935})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.46585333347320557})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.4495735764503479})
store['active_learning_steps'][14]['eval_training']['best_epoch']=3
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 27024], ['id', 21509], ['id', 22597], ['id', 52938], ['id', 9880]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7292745756536503, 1.3600833413008835, 1.8432848902057106, 2.1804857004483775, 2.3941590010963516]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8728495836257935})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7040113210678101})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7551260590553284})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7677042484283447})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7965912222862244})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7883847951889038})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8856208324432373})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.9676061272621155})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 1.1032928228378296})
store['active_learning_steps'][15]['training']['best_epoch']=6
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9107, 'crossentropy': 0.6961716796875}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6597822904586792})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5142691731452942})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.4759589731693268})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.4484063386917114})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.42779362201690674})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.4113726019859314})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.401553750038147})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.42036736011505127})
store['active_learning_steps'][15]['eval_training']['best_epoch']=5
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 19345], ['id', 34623], ['id', 57379], ['id', 53170], ['id', 57281]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.7640773952431639, 1.4569286371658858, 2.004746697809947, 2.3792171149052272, 2.596335819480535]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8826198577880859})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6712022423744202})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.719150185585022})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7129747271537781})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7191708087921143})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7300736904144287})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7751965522766113})
store['active_learning_steps'][16]['training']['best_epoch']=4
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9178, 'crossentropy': 0.5620673828125}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6608752012252808})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5476751923561096})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.47800612449645996})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.4702441990375519})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.4692065715789795})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.4678453207015991})
store['active_learning_steps'][16]['eval_training']['best_epoch']=3
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 53259], ['id', 16059], ['id', 48397], ['id', 47759], ['id', 48933]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6382689811898727, 1.194557280772612, 1.6763898133689938, 2.020997980554597, 2.2401008343965856]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8554436564445496})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6718150973320007})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5848672389984131})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6504342555999756})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6443703174591064})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7081050276756287})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6625248193740845})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7140294313430786})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6556599140167236})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7429531216621399})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7302569150924683})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7245727777481079})
store['active_learning_steps'][17]['training']['best_epoch']=9
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9299, 'crossentropy': 0.54120458984375}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6165438890457153})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5175701975822449})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.4601804316043854})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.4337857663631439})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4097300171852112})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.4151482582092285})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4055367708206177})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.39135730266571045})
store['active_learning_steps'][17]['eval_training']['best_epoch']=5
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 11837], ['id', 58470], ['id', 40084], ['id', 13259], ['id', 20804]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7681293393401849, 1.453402036517116, 2.00456190173648, 2.379327781865495, 2.598679636004455]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8719156384468079})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6661227345466614})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7075173854827881})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7229914665222168})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7330265045166016})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6928001642227173})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7449628114700317})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.777341365814209})
store['active_learning_steps'][18]['training']['best_epoch']=5
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9243, 'crossentropy': 0.596592724609375}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7191944122314453})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5243136286735535})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.48970648646354675})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.43936729431152344})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.4212234616279602})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.4208391606807709})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.413196861743927})
store['active_learning_steps'][18]['eval_training']['best_epoch']=4
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 43544], ['id', 21816], ['id', 43532], ['id', 45784], ['id', 54892]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8172586086415883, 1.5047357126468235, 2.065750852550524, 2.4429956971537807, 2.647345537572402]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8737277984619141})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.594902515411377})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6834574341773987})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6695950031280518})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6792075634002686})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6958032846450806})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7244459986686707})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7044683694839478})
store['active_learning_steps'][19]['training']['best_epoch']=5
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9252, 'crossentropy': 0.5679904296875}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.722658634185791})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.526225209236145})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.4501681625843048})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.43112248182296753})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.4476287364959717})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.4232161343097687})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.4459768533706665})
store['active_learning_steps'][19]['eval_training']['best_epoch']=5
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 42524], ['id', 12337], ['id', 47297], ['id', 13243], ['id', 37726]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7502812480967338, 1.4122109249554162, 1.966455998640337, 2.3395203866196663, 2.5748563048431805]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.9423824548721313})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6236904859542847})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6454076766967773})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5401070713996887})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5336957573890686})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6308149099349976})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6524660587310791})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6436102390289307})
store['active_learning_steps'][20]['training']['best_epoch']=5
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9304, 'crossentropy': 0.503492578125}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6795865297317505})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.4756860136985779})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.45998144149780273})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.40030723810195923})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4082852005958557})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.39090028405189514})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.39111244678497314})
store['active_learning_steps'][20]['eval_training']['best_epoch']=4
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 11482], ['id', 20641], ['id', 47597], ['id', 4512], ['id', 7596]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7250993067013327, 1.3892453646803093, 1.90842540787113, 2.281188127302304, 2.5069707480555543]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8737393617630005})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6368749141693115})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6352144479751587})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6598411798477173})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6779531836509705})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6087639331817627})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6493878364562988})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.752352774143219})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7441675662994385})
store['active_learning_steps'][21]['training']['best_epoch']=6
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9306, 'crossentropy': 0.51372080078125}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6973737478256226})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5348830223083496})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.4700043201446533})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4167580008506775})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.3958890438079834})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.396724134683609})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.3954429030418396})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.3890365958213806})
store['active_learning_steps'][21]['eval_training']['best_epoch']=8
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 6980], ['id', 18420], ['id', 22167], ['id', 28810], ['id', 13179]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6607227686875246, 1.2874595243177405, 1.7665486450211532, 2.122808372597194, 2.3972185364839067]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8120604753494263})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5715045928955078})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5999299883842468})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5596763491630554})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5892903208732605})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.639096736907959})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7106845378875732})
store['active_learning_steps'][22]['training']['best_epoch']=4
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9298, 'crossentropy': 0.486566259765625}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.7304273843765259})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.507347822189331})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.4584505259990692})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.45276451110839844})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.4287426471710205})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.43263179063796997})
store['active_learning_steps'][22]['eval_training']['best_epoch']=6
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 11044], ['id', 26446], ['id', 21601], ['id', 3010], ['id', 54371]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.651690108701565, 1.2330516509344984, 1.7143059032658066, 2.1044682447496763, 2.3596468269301205]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.8919404149055481})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.684402585029602})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6308210492134094})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7118958234786987})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6896207332611084})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7084602117538452})
store['active_learning_steps'][23]['training']['best_epoch']=3
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9282, 'crossentropy': 0.4944875}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6869391798973083})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5055965185165405})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5031681656837463})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.437361478805542})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.42978209257125854})
store['active_learning_steps'][23]['eval_training']['best_epoch']=4
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 59726], ['id', 55314], ['id', 30692], ['id', 4158], ['id', 4226]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.6986609511956623, 1.3007912400794766, 1.7721492261905754, 2.1510371536012745, 2.3993335067356476]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.9168871641159058})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5993213653564453})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6153562068939209})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5631940364837646})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.591075599193573})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5997949838638306})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6394988298416138})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5871353149414062})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7593945264816284})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.640128493309021})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.7215242385864258})
store['active_learning_steps'][24]['training']['best_epoch']=8
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9399, 'crossentropy': 0.502184130859375}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.688532829284668})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.4770999848842621})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4335835874080658})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.41668471693992615})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.35851478576660156})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.37498265504837036})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.3588515818119049})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.3757671117782593})
store['active_learning_steps'][24]['eval_training']['best_epoch']=5
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 11162], ['id', 12937], ['id', 22537], ['id', 34902], ['id', 744]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.8274662837126479, 1.5578703644692191, 2.0490653114660047, 2.373458637585083, 2.548062215776909]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.8814408779144287})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6169290542602539})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5107862949371338})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6152418851852417})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6172981262207031})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5745117664337158})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6145730018615723})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6080445647239685})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5715541839599609})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.6146854162216187})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7318632006645203})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.6289870738983154})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6476978063583374})
store['active_learning_steps'][25]['training']['best_epoch']=10
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9382, 'crossentropy': 0.5126814453125}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6388384103775024})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.48476776480674744})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.42493289709091187})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.39346957206726074})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.35506415367126465})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.3687724769115448})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.3603615462779999})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.3577539324760437})
store['active_learning_steps'][25]['eval_training']['best_epoch']=5
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 22550], ['id', 47870], ['id', 32513], ['id', 21798], ['id', 19844]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.7839473579525091, 1.4668610368298003, 2.0118035931184295, 2.3935001614862284, 2.586745027887047]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.9710890650749207})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5319020748138428})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5379432439804077})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.48345041275024414})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5337764620780945})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6561390161514282})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5991661548614502})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6275222301483154})
store['active_learning_steps'][26]['training']['best_epoch']=5
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9363, 'crossentropy': 0.470442138671875}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7011310458183289})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.4752022325992584})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4750945568084717})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4183419346809387})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.3893578052520752})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.3811609745025635})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.36031574010849})
store['active_learning_steps'][26]['eval_training']['best_epoch']=7
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 46616], ['id', 14266], ['id', 13491], ['id', 36415], ['id', 29560]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7425001738201102, 1.3766024778505992, 1.8766981867649246, 2.206850815112597, 2.3966965268150497]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8772017955780029})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5799806118011475})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.48579055070877075})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.49929046630859375})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5164921283721924})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.46627098321914673})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5356824398040771})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5437460541725159})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5536948442459106})
store['active_learning_steps'][27]['training']['best_epoch']=6
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9484, 'crossentropy': 0.414064501953125}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6627209186553955})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4717867374420166})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4133426547050476})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.40013524889945984})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3537669777870178})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3464435040950775})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.34066933393478394})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3245210647583008})
store['active_learning_steps'][27]['eval_training']['best_epoch']=8
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 59719], ['id', 14655], ['id', 2980], ['id', 49923], ['id', 982]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7306490306420823, 1.3926714441992356, 1.9354634208265162, 2.303950562983509, 2.5250895248189122]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8832362294197083})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5926022529602051})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5514920353889465})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6155955791473389})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.581749439239502})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.607687771320343})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5251895785331726})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5471417307853699})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6080125570297241})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6726301908493042})
store['active_learning_steps'][28]['training']['best_epoch']=7
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9408, 'crossentropy': 0.45322158203125}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7424749135971069})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4629199504852295})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.40163570642471313})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3494897186756134})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3635094165802002})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3457716405391693})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.34951508045196533})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.36204954981803894})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3413483500480652})
store['active_learning_steps'][28]['eval_training']['best_epoch']=9
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 20784], ['id', 8560], ['id', 57718], ['id', 26052], ['id', 52048]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7397274457534835, 1.4029277333439092, 1.9178207001269758, 2.26112611787564, 2.471365372028875]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8255898952484131})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5052356719970703})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.490406334400177})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.48617297410964966})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.47975271940231323})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4846912920475006})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.538360595703125})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4587300419807434})
store['active_learning_steps'][29]['training']['best_epoch']=5
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9477, 'crossentropy': 0.4055103759765625}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6307240724563599})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4333958923816681})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.429664671421051})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.36158329248428345})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3568645715713501})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.35360845923423767})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.32729727029800415})
store['active_learning_steps'][29]['eval_training']['best_epoch']=7
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 16043], ['id', 52978], ['id', 24630], ['id', 55541], ['id', 31844]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.7054002533383839, 1.3246557395669152, 1.8138299973739143, 2.183038344294915, 2.460897372864922]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.837726354598999})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5558661222457886})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4803023636341095})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4930450916290283})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.48744508624076843})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.47010141611099243})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4762265682220459})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4665701985359192})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5465803146362305})
store['active_learning_steps'][30]['training']['best_epoch']=6
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9526, 'crossentropy': 0.3639611572265625}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7998246550559998})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4801790714263916})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.37943512201309204})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.39623454213142395})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.356079638004303})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3444397449493408})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.32934099435806274})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3256872296333313})
store['active_learning_steps'][30]['eval_training']['best_epoch']=7
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 7793], ['id', 5129], ['id', 48133], ['id', 32829], ['id', 7283]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7382390626602977, 1.3789429252384862, 1.9217481235024256, 2.2629316626221634, 2.480079463004447]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.9138901829719543})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5796182155609131})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5013166666030884})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4958363175392151})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.485044002532959})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.48332563042640686})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5011193752288818})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5432312488555908})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5170019865036011})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5054235458374023})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5670732259750366})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5289948582649231})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5202254056930542})
store['active_learning_steps'][31]['training']['best_epoch']=10
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9482, 'crossentropy': 0.441194921875}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6876533031463623})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4892023503780365})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4484354853630066})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.40047886967658997})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3501107096672058})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.34904468059539795})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3484785556793213})
store['active_learning_steps'][31]['eval_training']['best_epoch']=4
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 24360], ['id', 48360], ['id', 35246], ['id', 47548], ['id', 41276]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7121814329856972, 1.3667905701794947, 1.8917787135906607, 2.2467296274518134, 2.4680885028799135]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8815001845359802})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.522998571395874})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4604511857032776})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.47243621945381165})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4667077660560608})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4710021913051605})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.47537800669670105})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4581623375415802})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5515763759613037})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4934007525444031})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4858711361885071})
store['active_learning_steps'][32]['training']['best_epoch']=8
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9582, 'crossentropy': 0.37819345703125}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6990004777908325})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4924207031726837})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4058292508125305})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.38919776678085327})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.36373499035835266})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.34183818101882935})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.32087814807891846})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.31616005301475525})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3019521236419678})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.2978544235229492})
store['active_learning_steps'][32]['eval_training']['best_epoch']=7
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 16592], ['id', 23140], ['id', 45069], ['ood', 43121], ['ood', 7847]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.7391525981957212, 1.4018739803592903, 1.9347674048039183, 2.3066672145758798, 2.561924926327622]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.0051302909851074})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6008298993110657})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5233005285263062})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5044091939926147})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.48061224818229675})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.524941086769104})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4943072199821472})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5165418982505798})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5056868195533752})
store['active_learning_steps'][33]['training']['best_epoch']=6
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9425, 'crossentropy': 0.451976708984375}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7494779825210571})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.48966795206069946})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3889772891998291})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3895242214202881})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3686905801296234})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3458470106124878})
store['active_learning_steps'][33]['eval_training']['best_epoch']=3
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 42973], ['id', 44101], ['id', 2231], ['id', 43213], ['id', 42096]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.7852782641735456, 1.4472202124467581, 1.9749818355917963, 2.3463016805149417, 2.571891280692496]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9399423599243164})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5520501136779785})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4357321262359619})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.43359488248825073})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4420219659805298})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3953580856323242})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4204687476158142})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4470731019973755})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.44721218943595886})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.42819908261299133})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5042064189910889})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4947679042816162})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.48459723591804504})
store['active_learning_steps'][34]['training']['best_epoch']=10
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9551, 'crossentropy': 0.398877783203125}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6805427074432373})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.44772449135780334})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3738815188407898})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3137916624546051})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.31370171904563904})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.32312941551208496})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.2944071292877197})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.30736255645751953})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.30323487520217896})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.28126421570777893})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.2905137836933136})
store['active_learning_steps'][34]['eval_training']['best_epoch']=8
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 31545], ['id', 58022], ['id', 49160], ['id', 16302], ['id', 8651]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.6826984859017573, 1.3251452285008716, 1.8491782611419083, 2.2020953741660003, 2.448500944112487]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.9431784152984619})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5140164494514465})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.41193443536758423})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.411792516708374})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4212470054626465})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4251999855041504})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3932187557220459})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.43003612756729126})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.41787776350975037})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.444802463054657})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4603876769542694})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.495373398065567})
store['active_learning_steps'][35]['training']['best_epoch']=9
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9568, 'crossentropy': 0.3624355712890625}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7444076538085938})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4324256181716919})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.35081350803375244})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3402487337589264})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.31607770919799805})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.32617291808128357})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.27155062556266785})
store['active_learning_steps'][35]['eval_training']['best_epoch']=4
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 55496], ['id', 7026], ['id', 56838], ['id', 40876], ['ood', 24760]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.7777714215613438, 1.4720178364133076, 1.9742701772035813, 2.326516438343047, 2.548830972201494]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 1.0121698379516602})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5190093517303467})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.44922518730163574})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4124506115913391})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.43473199009895325})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.43868276476860046})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4222407341003418})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.40265631675720215})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.43776941299438477})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.45563727617263794})
store['active_learning_steps'][36]['training']['best_epoch']=7
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9521, 'crossentropy': 0.360236181640625}
