store = {}
store['timestamp']=1620992162
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=14']
store['commit']='50fc0561f6557d261400d89a96a1c6ef6418247b'
store['github_url']='50fc0561f6557d261400d89a96a1c6ef6418247b'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=14
store['worker_id']=14
store['num_workers']=20
store['config']={'seed': 1255, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'evaluation_set_size': 100, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.490886926651001})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.8523449897766113})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.8437702655792236})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.2704498767852783})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6499, 'crossentropy': 2.3039515625}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.2335840463638306})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.2742881774902344})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.2104709148406982})
store['active_learning_steps'][0]['eval_training']['best_epoch']=3
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 45794], ['id', 1505], ['ood', 9894], ['id', 17731], ['id', 56019], ['ood', 51516], ['id', 13854], ['id', 20022], ['id', 6735], ['id', 21650]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5602689981460571, 0.8254597783088684, 0.668445348739624, 0.6422134041786194, 0.9238181114196777, 0.5932110548019409, 0.6983214020729065, 0.8036327958106995, 0.8770997524261475, 0.9132614135742188]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.8046294450759888})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.1534807682037354})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.430666923522949})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.6123745441436768})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6956, 'crossentropy': 1.5892765625}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.2335364818572998})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.1680991649627686})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.1424684524536133})
store['active_learning_steps'][1]['eval_training']['best_epoch']=3
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 34998], ['id', 17444], ['id', 47845], ['id', 29011], ['ood', 4410], ['id', 26086], ['id', 23997], ['id', 33043], ['id', 28969], ['id', 28779]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.42092716693878174, 0.5806132555007935, 0.556486964225769, 0.4713609218597412, 0.3893260955810547, 0.4658101201057434, 0.5175103545188904, 0.6989227533340454, 0.5581052303314209, 0.4223971366882324]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.4476362466812134})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.6848291158676147})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.701345682144165})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.9139244556427002})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7733, 'crossentropy': 1.20238232421875}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.0145611763000488})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 0.9823832511901855})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 0.9211035966873169})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 1648], ['id', 28407], ['id', 41595], ['id', 1951], ['id', 58801], ['id', 35437], ['id', 39958], ['id', 4268], ['id', 37170], ['id', 59735]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5318531394004822, 0.45123040676116943, 0.6298798322677612, 0.38045257329940796, 0.5257804989814758, 0.5963457226753235, 0.44097191095352173, 0.42978155612945557, 0.33733630180358887, 0.280131995677948]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.1065219640731812})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.129175066947937})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.317165732383728})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.4059685468673706})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.8163, 'crossentropy': 1.00257861328125}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.8786741495132446})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.8250740766525269})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 0.834649384021759})
store['active_learning_steps'][3]['eval_training']['best_epoch']=2
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 12957], ['id', 50233], ['id', 14305], ['id', 38593], ['id', 12257], ['id', 16379], ['id', 23806], ['id', 13348], ['id', 2213], ['id', 45888]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.5194436311721802, 0.4729875922203064, 0.39429354667663574, 0.5001233816146851, 0.5190765261650085, 0.5333859324455261, 0.7170612812042236, 0.6906624436378479, 0.5051978826522827, 0.44025909900665283]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9622502326965332})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.0849484205245972})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.3853542804718018})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.397321343421936})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.8282, 'crossentropy': 0.8875857421875}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.8818600177764893})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.7983114123344421})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.8124688267707825})
store['active_learning_steps'][4]['eval_training']['best_epoch']=2
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 20325], ['id', 30435], ['id', 30149], ['id', 48475], ['id', 22583], ['id', 25960], ['id', 23391], ['id', 34628], ['id', 43609], ['id', 37327]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.3258516788482666, 0.29924511909484863, 0.37276434898376465, 0.46576714515686035, 0.38628530502319336, 0.41070789098739624, 0.449551522731781, 0.4267432689666748, 0.3047966957092285, 0.28798484802246094]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.0375627279281616})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.9955202341079712})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.0315237045288086})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.1177315711975098})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.3206557035446167})
store['active_learning_steps'][5]['training']['best_epoch']=2
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8463, 'crossentropy': 0.92485185546875}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.7799996733665466})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.718338131904602})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.6847750544548035})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.6608076691627502})
store['active_learning_steps'][5]['eval_training']['best_epoch']=4
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 6432], ['id', 43381], ['ood', 28297], ['id', 38521], ['id', 38178], ['id', 51856], ['id', 35062], ['id', 42177], ['id', 13647], ['id', 22157]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.48943793773651123, 0.6915872097015381, 0.31910157203674316, 0.5181980729103088, 0.6410396099090576, 0.5607038736343384, 0.48701995611190796, 0.6445738673210144, 0.5981624126434326, 0.5894865989685059]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9131293892860413})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8909052610397339})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.032874584197998})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.0139250755310059})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.0664002895355225})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8534, 'crossentropy': 0.8375001953125}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.7769172191619873})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.7257969379425049})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.6866630911827087})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.6521298885345459})
store['active_learning_steps'][6]['eval_training']['best_epoch']=4
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 56122], ['id', 48535], ['id', 28750], ['id', 30498], ['id', 32466], ['id', 12105], ['id', 28455], ['id', 45580], ['id', 31583], ['id', 21940]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4374682307243347, 0.5755025148391724, 0.6491991877555847, 0.5798931121826172, 0.4970865249633789, 0.4676440358161926, 0.5127367973327637, 0.28852957487106323, 0.40070319175720215, 0.47016477584838867]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8062875270843506})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7448451519012451})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8604055643081665})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8432003259658813})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9660638570785522})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8903, 'crossentropy': 0.612593408203125}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.765860915184021})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6382089853286743})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.5920978784561157})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.5866435766220093})
store['active_learning_steps'][7]['eval_training']['best_epoch']=4
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 32271], ['id', 56839], ['id', 29501], ['id', 46413], ['id', 40507], ['id', 32157], ['id', 11240], ['id', 50576], ['id', 50307], ['id', 7140]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3214907646179199, 0.4320431351661682, 0.4041886329650879, 0.4304690361022949, 0.32795149087905884, 0.3908688426017761, 0.5367067456245422, 0.49624133110046387, 0.537314772605896, 0.5198683738708496]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8429391384124756})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7949967384338379})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7745088338851929})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7277092933654785})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8928764462471008})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8600890636444092})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8816021680831909})
store['active_learning_steps'][8]['training']['best_epoch']=4
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8906, 'crossentropy': 0.656922998046875}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7010427713394165})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6073529720306396})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.5477036237716675})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5263040661811829})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5152633190155029})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5013426542282104})
store['active_learning_steps'][8]['eval_training']['best_epoch']=6
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 24199], ['id', 28366], ['id', 27622], ['id', 3885], ['id', 8866], ['id', 2942], ['id', 34385], ['ood', 14729], ['id', 12820], ['id', 58187]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.4449179768562317, 0.3791608512401581, 0.6975675821304321, 0.5550282597541809, 0.4464161992073059, 0.3688346743583679, 0.4113107919692993, 0.37141263484954834, 0.5419875979423523, 0.398059606552124]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7811708450317383})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6980048418045044})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7355986833572388})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.733858585357666})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8577784299850464})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8995, 'crossentropy': 0.587094775390625}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7304845452308655})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6060893535614014})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5654748678207397})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5578638315200806})
store['active_learning_steps'][9]['eval_training']['best_epoch']=4
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 18778], ['id', 7768], ['id', 14655], ['id', 28371], ['id', 31672], ['id', 41911], ['id', 47283], ['id', 13167], ['id', 42264], ['ood', 30120]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.33995527029037476, 0.4881185293197632, 0.5412184000015259, 0.4155550003051758, 0.3706434965133667, 0.23677527904510498, 0.47659575939178467, 0.35285842418670654, 0.4329872727394104, 0.18608379364013672]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7536320686340332})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6345289945602417})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6165881156921387})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.600934624671936})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6496843695640564})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.696233868598938})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6459214091300964})
store['active_learning_steps'][10]['training']['best_epoch']=4
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.9215, 'crossentropy': 0.4941734375}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7281680107116699})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5371726155281067})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5094955563545227})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.48328322172164917})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.4804684519767761})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.45167672634124756})
store['active_learning_steps'][10]['eval_training']['best_epoch']=6
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 54880], ['id', 44404], ['id', 52473], ['id', 41998], ['id', 31744], ['id', 3300], ['id', 14266], ['id', 8812], ['id', 56213], ['id', 56514]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5628524422645569, 0.36976343393325806, 0.5415976047515869, 0.383392333984375, 0.5221688449382782, 0.22073489427566528, 0.46089428663253784, 0.4887944459915161, 0.6662190854549408, 0.40770697593688965]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8867380619049072})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6214519739151001})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6240637302398682})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6304115056991577})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6189704537391663})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6911160945892334})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6934710741043091})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6904882192611694})
store['active_learning_steps'][11]['training']['best_epoch']=5
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.9202, 'crossentropy': 0.507680810546875}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7100105285644531})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5513858795166016})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.48173701763153076})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.48377180099487305})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.47810372710227966})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.4447285532951355})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.4767298698425293})
store['active_learning_steps'][11]['eval_training']['best_epoch']=6
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 51652], ['id', 17756], ['id', 32511], ['id', 23386], ['id', 29338], ['id', 10716], ['id', 16756], ['id', 12630], ['id', 9650], ['id', 12934]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.4528040885925293, 0.6063251495361328, 0.5432402491569519, 0.4942120909690857, 0.41151919960975647, 0.5173096656799316, 0.6590902209281921, 0.48755311965942383, 0.46663933992385864, 0.6506448984146118]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8040977120399475})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6022905111312866})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.574046790599823})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5944781303405762})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6495968103408813})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6512305736541748})
store['active_learning_steps'][12]['training']['best_epoch']=3
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9237, 'crossentropy': 0.484702880859375}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.754577100276947})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5724360942840576})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.48547178506851196})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.4782387912273407})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4811112582683563})
store['active_learning_steps'][12]['eval_training']['best_epoch']=4
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 14341], ['id', 55612], ['id', 27101], ['id', 3367], ['id', 49734], ['id', 45536], ['id', 35954], ['id', 20172], ['id', 17937], ['id', 50797]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3669126629829407, 0.3849831819534302, 0.45659512281417847, 0.46227407455444336, 0.412265419960022, 0.3330257534980774, 0.35370874404907227, 0.47429823875427246, 0.4068048596382141, 0.47418999671936035]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8733752369880676})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6193791627883911})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.582453727722168})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6135430932044983})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6742365956306458})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7041259407997131})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.9242, 'crossentropy': 0.469592431640625}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6851640343666077})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.507971465587616})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5004929304122925})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.47754570841789246})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.44938725233078003})
store['active_learning_steps'][13]['eval_training']['best_epoch']=5
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 28014], ['id', 30730], ['id', 33219], ['id', 13867], ['id', 36828], ['id', 47615], ['id', 1009], ['id', 23629], ['id', 32190], ['id', 3370]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.29393506050109863, 0.3559398055076599, 0.26902467012405396, 0.24827980995178223, 0.336995005607605, 0.3653934597969055, 0.36251068115234375, 0.3601626753807068, 0.3770827651023865, 0.29721564054489136]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8410831689834595})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5753974914550781})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5750834941864014})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5717040300369263})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6276122331619263})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5894830226898193})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6766270995140076})
store['active_learning_steps'][14]['training']['best_epoch']=4
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.931, 'crossentropy': 0.459264404296875}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7604537010192871})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5134057998657227})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.49894094467163086})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4435711205005646})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4570801556110382})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.43288159370422363})
store['active_learning_steps'][14]['eval_training']['best_epoch']=6
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 6044], ['id', 37887], ['id', 36126], ['id', 5677], ['id', 7653], ['id', 27183], ['id', 31240], ['id', 29640], ['id', 54973], ['id', 27540]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3345155715942383, 0.4006563127040863, 0.43094444274902344, 0.4855981469154358, 0.6506714224815369, 0.5070059895515442, 0.46876561641693115, 0.4390653371810913, 0.5494901537895203, 0.5148971080780029]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8838269710540771})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5294385552406311})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.500670313835144})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5254123210906982})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.510348379611969})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5040262341499329})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.936, 'crossentropy': 0.4213296875}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8459952473640442})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5588754415512085})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5264915227890015})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.46014320850372314})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4411061108112335})
store['active_learning_steps'][15]['eval_training']['best_epoch']=5
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 48638], ['id', 39749], ['id', 14629], ['ood', 26822], ['id', 26527], ['ood', 23027], ['id', 53062], ['id', 9158], ['id', 46148], ['id', 26834]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.4276692271232605, 0.4866533875465393, 0.4632796347141266, 0.23625099658966064, 0.46022868156433105, 0.30616772174835205, 0.32813507318496704, 0.45231980085372925, 0.29819512367248535, 0.4889675974845886]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.886425256729126})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5952425003051758})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5283796191215515})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5316705703735352})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5503993630409241})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5263697504997253})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5559942722320557})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5049508213996887})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5460800528526306})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5236847400665283})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5428492426872253})
store['active_learning_steps'][16]['training']['best_epoch']=8
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9469, 'crossentropy': 0.403132275390625}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6470686197280884})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.48064061999320984})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4269395172595978})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3857797384262085})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3646683692932129})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.36906591057777405})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.34802940487861633})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.34076136350631714})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.34798166155815125})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3537140488624573})
store['active_learning_steps'][16]['eval_training']['best_epoch']=8
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 47597], ['id', 32784], ['id', 24424], ['id', 20322], ['id', 9633], ['id', 53568], ['id', 13942], ['id', 134], ['ood', 28468], ['id', 17055]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5688222646713257, 0.40841159224510193, 0.5140516757965088, 0.7456916570663452, 0.7015631794929504, 0.5600252747535706, 0.5482277870178223, 0.7459096312522888, 0.3495185375213623, 0.3858523368835449]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.9046287536621094})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5503570437431335})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4993051290512085})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5202909708023071})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4800403416156769})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4853785037994385})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5337156057357788})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5799455642700195})
store['active_learning_steps'][17]['training']['best_epoch']=5
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9372, 'crossentropy': 0.42976083984375}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7645493745803833})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5223977565765381})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.42606601119041443})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.40243786573410034})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3854348063468933})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.37170982360839844})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.37875664234161377})
store['active_learning_steps'][17]['eval_training']['best_epoch']=6
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 28078], ['id', 40498], ['id', 46770], ['id', 740], ['id', 12935], ['id', 13049], ['id', 54937], ['id', 9583], ['id', 3676], ['id', 47320]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4933304786682129, 0.3737058937549591, 0.30653828382492065, 0.36350351572036743, 0.5271536111831665, 0.4659847021102905, 0.47143852710723877, 0.33995166420936584, 0.41856318712234497, 0.35213427245616913]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8812788724899292})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.521567702293396})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.40443432331085205})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4343265891075134})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4224357306957245})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.43681231141090393})
store['active_learning_steps'][18]['training']['best_epoch']=3
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9451, 'crossentropy': 0.381877001953125}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7564218640327454})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.49013233184814453})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4767501950263977})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.37151825428009033})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.39152657985687256})
store['active_learning_steps'][18]['eval_training']['best_epoch']=4
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 53704], ['id', 6905], ['id', 274], ['id', 52462], ['id', 506], ['id', 17131], ['id', 25968], ['id', 33744], ['id', 33614], ['id', 28231]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.2668795585632324, 0.2225446105003357, 0.4027971029281616, 0.3990177512168884, 0.4008646011352539, 0.4859476089477539, 0.4144691228866577, 0.42822927236557007, 0.3478388488292694, 0.2794509530067444]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9556968212127686})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6084170341491699})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.49435415863990784})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.47552692890167236})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4940132796764374})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4603561460971832})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4776350259780884})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4767933487892151})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.525673508644104})
store['active_learning_steps'][19]['training']['best_epoch']=6
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9494, 'crossentropy': 0.3773519775390625}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.734050452709198})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.47375762462615967})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3941749036312103})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3749215006828308})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3531683683395386})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3624148368835449})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3469587564468384})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.34233903884887695})
store['active_learning_steps'][19]['eval_training']['best_epoch']=8
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 34740], ['id', 16964], ['id', 1674], ['id', 5750], ['id', 33397], ['id', 58620], ['id', 46673], ['id', 56702], ['id', 644], ['id', 47595]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.42836177349090576, 0.4676346182823181, 0.4299842119216919, 0.3608993887901306, 0.38191525638103485, 0.48624521493911743, 0.422096312046051, 0.5665168762207031, 0.5194410681724548, 0.3757927715778351]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8499168157577515})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5168044567108154})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.48078033328056335})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4721919298171997})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4329454302787781})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4055846333503723})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.47529757022857666})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4490513801574707})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.440596342086792})
store['active_learning_steps'][20]['training']['best_epoch']=6
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9542, 'crossentropy': 0.358171484375}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8355026841163635})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4900049567222595})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.41764116287231445})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.403104692697525})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.37559813261032104})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.37836119532585144})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3281777501106262})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3263373374938965})
store['active_learning_steps'][20]['eval_training']['best_epoch']=8
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 49895], ['id', 5936], ['id', 3013], ['id', 23294], ['id', 29320], ['id', 40720], ['id', 45774], ['id', 24062], ['id', 861], ['ood', 32433]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.5869495272636414, 0.40177178382873535, 0.2702450156211853, 0.3758379817008972, 0.3849526643753052, 0.3308788537979126, 0.3223298490047455, 0.24908733367919922, 0.3897865414619446, 0.23694384098052979]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.9107997417449951})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5838885307312012})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.41535404324531555})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4348876476287842})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4122293293476105})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3900928497314453})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4189152121543884})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.42908743023872375})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3940693140029907})
store['active_learning_steps'][21]['training']['best_epoch']=6
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9544, 'crossentropy': 0.3406886474609375}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7839065790176392})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.48846548795700073})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3720143437385559})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3328496217727661})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3306330442428589})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.31276851892471313})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3324417173862457})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.34372571110725403})
store['active_learning_steps'][21]['eval_training']['best_epoch']=6
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 36653], ['id', 29713], ['id', 24513], ['id', 35538], ['id', 31274], ['id', 27737], ['ood', 37787], ['id', 37118], ['id', 46269], ['id', 45918]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.437150239944458, 0.457217276096344, 0.29113638401031494, 0.3207623064517975, 0.38971376419067383, 0.4744153618812561, 0.2592254877090454, 0.5335254669189453, 0.5164324045181274, 0.3991243243217468]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.9266328811645508})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4913441836833954})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.42752212285995483})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.38846200704574585})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4046710133552551})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.37761664390563965})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.373910129070282})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.38174667954444885})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.36741188168525696})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.40442466735839844})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.39085692167282104})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4253704249858856})
store['active_learning_steps'][22]['training']['best_epoch']=9
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9586, 'crossentropy': 0.3293140380859375}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7484798431396484})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.48095375299453735})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3895334005355835})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.32427212595939636})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3395766019821167})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3327735662460327})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.31263208389282227})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.31630200147628784})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2896881103515625})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.29922837018966675})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2839275002479553})
store['active_learning_steps'][22]['eval_training']['best_epoch']=11
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 40511], ['id', 56198], ['id', 11889], ['id', 16122], ['id', 4459], ['id', 34], ['id', 30475], ['id', 11154], ['id', 48006], ['id', 52086]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.38346511125564575, 0.22750765085220337, 0.6166208982467651, 0.5846444368362427, 0.5548586845397949, 0.44875115156173706, 0.26501691341400146, 0.4499390125274658, 0.4843616783618927, 0.5660908222198486]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.9047284126281738})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5003029704093933})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.40480250120162964})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3593682646751404})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.36917659640312195})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.340433269739151})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.32260823249816895})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.41354596614837646})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.38362884521484375})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3693732023239136})
store['active_learning_steps'][23]['training']['best_epoch']=7
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9587, 'crossentropy': 0.30917998046875}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7465155124664307})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.45279648900032043})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3400038480758667})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3314157724380493})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3030681014060974})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3010672330856323})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.2962266504764557})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.269627183675766})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.29744672775268555})
store['active_learning_steps'][23]['eval_training']['best_epoch']=8
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 33162], ['id', 47387], ['id', 48380], ['id', 21426], ['id', 16444], ['ood', 25757], ['id', 25986], ['id', 4955], ['id', 36072], ['id', 34520]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.42381611466407776, 0.42504894733428955, 0.32135796546936035, 0.4502269923686981, 0.34134143590927124, 0.3388417959213257, 0.5715349912643433, 0.5504024624824524, 0.40936166048049927, 0.6824268698692322]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.9835467338562012})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4713001251220703})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3902602195739746})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32897287607192993})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34439948201179504})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3422424793243408})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.31792736053466797})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33325856924057007})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33263692259788513})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3619863986968994})
store['active_learning_steps'][24]['training']['best_epoch']=7
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9583, 'crossentropy': 0.3236453125}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8305960893630981})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.47834354639053345})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.37326890230178833})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3427239656448364})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3364710807800293})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3175363838672638})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.29057151079177856})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.27711421251296997})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2982564866542816})
store['active_learning_steps'][24]['eval_training']['best_epoch']=8
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 37602], ['id', 45944], ['id', 55438], ['id', 26498], ['id', 31558], ['id', 50342], ['id', 38626], ['id', 8458], ['id', 56612], ['id', 40976]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5141486823558807, 0.5686026215553284, 0.4915275573730469, 0.42142224311828613, 0.3070979416370392, 0.4025275707244873, 0.35499006509780884, 0.4993748664855957, 0.4598733186721802, 0.5273378789424896]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 1.0187184810638428})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5446804761886597})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4049278199672699})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.396797239780426})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.371496319770813})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3412083387374878})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3539254069328308})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33295685052871704})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.38766008615493774})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.34483063220977783})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.37514370679855347})
store['active_learning_steps'][25]['training']['best_epoch']=8
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9606, 'crossentropy': 0.301823974609375}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8323403596878052})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4808118939399719})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3827034533023834})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3735603094100952})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3235885500907898})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2820621728897095})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2908942997455597})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.27744510769844055})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3024998605251312})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.29821890592575073})
store['active_learning_steps'][25]['eval_training']['best_epoch']=8
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 18473], ['id', 44123], ['id', 1518], ['id', 40221], ['id', 51239], ['id', 6606], ['id', 13099], ['id', 48899], ['ood', 125], ['id', 32276]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.36629581451416016, 0.4503418803215027, 0.5233905911445618, 0.556236058473587, 0.3233635425567627, 0.37611842155456543, 0.3813638687133789, 0.5387789607048035, 0.44882941246032715, 0.6140625476837158]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 1.009657621383667})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5095657706260681})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3974407911300659})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3773787021636963})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.34682339429855347})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31417566537857056})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3274794816970825})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31976938247680664})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34958207607269287})
store['active_learning_steps'][26]['training']['best_epoch']=6
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9607, 'crossentropy': 0.3147363525390625}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8323076963424683})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5048099756240845})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3669029474258423})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3649335205554962})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32297617197036743})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3287738561630249})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3310590982437134})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.29802078008651733})
store['active_learning_steps'][26]['eval_training']['best_epoch']=8
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 22510], ['id', 31415], ['id', 49690], ['id', 5227], ['id', 43212], ['id', 12181], ['id', 14878], ['id', 39573], ['id', 34090], ['id', 5932]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.45082199573516846, 0.4776954650878906, 0.41660696268081665, 0.46219515800476074, 0.4545134902000427, 0.443176805973053, 0.6038022637367249, 0.5255347192287445, 0.41027241945266724, 0.35304033756256104]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.1631669998168945})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5417671203613281})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.42706620693206787})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3777470588684082})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.40536263585090637})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3565789759159088})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3388126492500305})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3466460406780243})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3361286520957947})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3458847999572754})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32517218589782715})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.35226476192474365})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3596744239330292})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3368704319000244})
store['active_learning_steps'][27]['training']['best_epoch']=11
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9624, 'crossentropy': 0.2922743896484375}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.9211539030075073})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4685326814651489})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3673948049545288})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3671894073486328})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.28885751962661743})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3131136894226074})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2759803831577301})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.29369133710861206})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.27477070689201355})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.24761962890625})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.26814478635787964})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.25628870725631714})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.26374873518943787})
store['active_learning_steps'][27]['eval_training']['best_epoch']=10
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 18398], ['id', 49487], ['id', 9220], ['id', 24462], ['id', 20529], ['id', 32018], ['id', 27729], ['id', 20939], ['id', 3510], ['id', 14726]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.6511383056640625, 0.4153061509132385, 0.48241084814071655, 0.4409549832344055, 0.42589646577835083, 0.4798898696899414, 0.6562197208404541, 0.5208976864814758, 0.524415910243988, 0.31154900789260864]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.0345818996429443})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.535412073135376})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.46341466903686523})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4056088924407959})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.36805909872055054})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.39014530181884766})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3872990012168884})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3876582980155945})
store['active_learning_steps'][28]['training']['best_epoch']=5
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9568, 'crossentropy': 0.33845859375}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7928372621536255})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5173845291137695})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.444182813167572})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.41729068756103516})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3665597438812256})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.38454461097717285})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.33513742685317993})
store['active_learning_steps'][28]['eval_training']['best_epoch']=7
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 17389], ['id', 34708], ['id', 21306], ['id', 11296], ['id', 32513], ['id', 13129], ['id', 8093], ['id', 34771], ['ood', 29124], ['id', 36333]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.40172213315963745, 0.3665715456008911, 0.40943849086761475, 0.3573024868965149, 0.37470299005508423, 0.33986711502075195, 0.39978134632110596, 0.358137845993042, 0.20413684844970703, 0.3258068561553955]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.0073314905166626})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5261907577514648})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.36217302083969116})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.36487773060798645})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.36495280265808105})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.34154388308525085})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34008097648620605})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3360068202018738})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.39028269052505493})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.34960120916366577})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3431847095489502})
store['active_learning_steps'][29]['training']['best_epoch']=8
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9591, 'crossentropy': 0.2995245849609375}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8903254270553589})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.474153995513916})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.39640676975250244})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3406856060028076})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3237272799015045})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.29953983426094055})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.28606823086738586})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2737768888473511})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.29694581031799316})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2673492431640625})
store['active_learning_steps'][29]['eval_training']['best_epoch']=10
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 27406], ['id', 6832], ['id', 55429], ['id', 55856], ['id', 37440], ['id', 12465], ['id', 17674], ['id', 17503], ['id', 19824], ['id', 7886]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.45210564136505127, 0.534501850605011, 0.37142837047576904, 0.5218829214572906, 0.46603941917419434, 0.3928568959236145, 0.5807273387908936, 0.2992737293243408, 0.565004289150238, 0.3532547950744629]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.0678761005401611})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5799375772476196})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4658125340938568})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.37649649381637573})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3620743751525879})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3459056317806244})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3345194160938263})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33112698793411255})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33580029010772705})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31744253635406494})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3162258267402649})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34154170751571655})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.35694044828414917})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.33492332696914673})
store['active_learning_steps'][30]['training']['best_epoch']=11
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9667, 'crossentropy': 0.282053271484375}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8838569521903992})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5377278327941895})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.39764776825904846})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.35645681619644165})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.29352283477783203})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2899319529533386})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.292833536863327})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2822011709213257})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2673860788345337})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2545836567878723})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.25876832008361816})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26866525411605835})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.24815091490745544})
store['active_learning_steps'][30]['eval_training']['best_epoch']=13
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 24587], ['id', 47278], ['id', 15975], ['id', 55906], ['id', 38780], ['id', 9985], ['id', 26538], ['id', 50387], ['id', 20402], ['id', 32047]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.3602446913719177, 0.6003167927265167, 0.6702517867088318, 0.5752059817314148, 0.37341785430908203, 0.5118923187255859, 0.47008204460144043, 0.3793579936027527, 0.4619535207748413, 0.715038537979126]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.9495360851287842})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.47314876317977905})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3934771418571472})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32286739349365234})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.36216410994529724})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.314558207988739})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30429744720458984})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3190288245677948})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3256661891937256})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32198622822761536})
store['active_learning_steps'][31]['training']['best_epoch']=7
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9682, 'crossentropy': 0.2592556396484375}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8993083238601685})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.49542373418807983})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4231233596801758})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3693038821220398})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34402740001678467})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.30064845085144043})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.30937957763671875})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31629836559295654})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.30338507890701294})
store['active_learning_steps'][31]['eval_training']['best_epoch']=6
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 20903], ['id', 20219], ['id', 42533], ['id', 38656], ['id', 43950], ['id', 43560], ['id', 44172], ['id', 34678], ['id', 19702], ['id', 36704]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3312475085258484, 0.43116897344589233, 0.5081121325492859, 0.553922176361084, 0.518287181854248, 0.52744460105896, 0.46969449520111084, 0.48151564598083496, 0.47732818126678467, 0.47147136926651]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.0325160026550293})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5924243927001953})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.45798006653785706})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.35851937532424927})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3624717891216278})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34903690218925476})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3054487109184265})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33953607082366943})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33288252353668213})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.35000550746917725})
store['active_learning_steps'][32]['training']['best_epoch']=7
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9671, 'crossentropy': 0.2763140625}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.930195689201355})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.5311150550842285})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.43409085273742676})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3486473560333252})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33316630125045776})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3299216628074646})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3098549544811249})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30991411209106445})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28860947489738464})
store['active_learning_steps'][32]['eval_training']['best_epoch']=9
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 43034], ['id', 52109], ['id', 24210], ['id', 30016], ['id', 33304], ['id', 58926], ['id', 17494], ['id', 20169], ['id', 26358], ['id', 5295]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.46106088161468506, 0.2965507507324219, 0.5223261713981628, 0.47627192735671997, 0.3692736029624939, 0.3376014828681946, 0.3461899161338806, 0.5661872029304504, 0.49145179986953735, 0.35758066177368164]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.1026086807250977})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5256531238555908})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4182855784893036})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.38383549451828003})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.32896578311920166})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.35715001821517944})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3465029001235962})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.33854085206985474})
store['active_learning_steps'][33]['training']['best_epoch']=5
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9646, 'crossentropy': 0.3041117919921875}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9136163592338562})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.548613965511322})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4366025924682617})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.38508474826812744})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3746737241744995})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35968005657196045})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3423630893230438})
store['active_learning_steps'][33]['eval_training']['best_epoch']=7
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 37160], ['id', 4322], ['id', 38510], ['id', 41999], ['id', 55715], ['id', 5188], ['ood', 21078], ['id', 16528], ['id', 17684], ['id', 41453]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5080358386039734, 0.4003846049308777, 0.3684743642807007, 0.4492305517196655, 0.3142154812812805, 0.49172407388687134, 0.31026577949523926, 0.4184119701385498, 0.5482597947120667, 0.5178177356719971]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.1658153533935547})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5717499256134033})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4368954598903656})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3396989703178406})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32217931747436523})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33969807624816895})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30319148302078247})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32763561606407166})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.294678270816803})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2883829176425934})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29894089698791504})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31745457649230957})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32913750410079956})
store['active_learning_steps'][34]['training']['best_epoch']=10
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9681, 'crossentropy': 0.2544608154296875}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9347940683364868})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4856274127960205})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3819499611854553})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33799123764038086})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.33816900849342346})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3024151921272278})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2651306986808777})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28489530086517334})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28617745637893677})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2568210959434509})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.27027562260627747})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.26336172223091125})
store['active_learning_steps'][34]['eval_training']['best_epoch']=10
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 50916], ['id', 57516], ['id', 29476], ['ood', 56847], ['id', 49060], ['id', 21023], ['id', 40022], ['id', 32747], ['id', 33306], ['id', 27822]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.432184100151062, 0.4840525984764099, 0.3205574154853821, 0.28762388229370117, 0.40386706590652466, 0.33720242977142334, 0.2821285128593445, 0.5981866121292114, 0.2792600989341736, 0.40650880336761475]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.095022439956665})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.595070481300354})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.403215229511261})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.36646175384521484})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.36615848541259766})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30093687772750854})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30307456851005554})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3102484941482544})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31408339738845825})
store['active_learning_steps'][35]['training']['best_epoch']=6
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9684, 'crossentropy': 0.2603939697265625}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8637261390686035})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5486645698547363})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.42822790145874023})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.36271923780441284})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3324752449989319})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3270947337150574})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.33241006731987})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3058971166610718})
store['active_learning_steps'][35]['eval_training']['best_epoch']=8
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 42438], ['id', 37794], ['id', 13149], ['id', 8765], ['id', 38524], ['id', 32640], ['id', 57701], ['id', 17697], ['id', 41816], ['id', 40704]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3692837357521057, 0.4606468081474304, 0.4111514687538147, 0.3300550580024719, 0.5713793039321899, 0.33367738127708435, 0.4818742275238037, 0.4306250214576721, 0.4070008397102356, 0.4022219181060791]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.1046829223632812})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.576534628868103})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.42513930797576904})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.35192254185676575})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.36173197627067566})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.35424429178237915})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3344832956790924})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3430604338645935})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3051038384437561})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.31249257922172546})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31449705362319946})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3268217444419861})
store['active_learning_steps'][36]['training']['best_epoch']=9
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9661, 'crossentropy': 0.2812038330078125}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.9759869575500488})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5278592109680176})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4189593195915222})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31039196252822876})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.276065856218338})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29875433444976807})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.270518958568573})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.25296950340270996})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26385581493377686})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.25086790323257446})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27053534984588623})
store['active_learning_steps'][36]['eval_training']['best_epoch']=10
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 10064], ['id', 39031], ['id', 36075], ['id', 53116], ['id', 48397], ['id', 37643], ['id', 2845], ['id', 58874], ['id', 45602], ['id', 17888]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7124511301517487, 0.44687914848327637, 0.2730918526649475, 0.3504939675331116, 0.42390257120132446, 0.5897068977355957, 0.4251227080821991, 0.4417300224304199, 0.38220101594924927, 0.5288474559783936]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.092712163925171})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.552369236946106})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.41515880823135376})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.37984317541122437})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.35131776332855225})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29224735498428345})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3270794749259949})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3305250406265259})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32017946243286133})
store['active_learning_steps'][37]['training']['best_epoch']=6
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9676, 'crossentropy': 0.2617496826171875}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8691802024841309})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5140215158462524})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3766756057739258})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3595777153968811})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.34018102288246155})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3439742922782898})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3296126127243042})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.324795126914978})
store['active_learning_steps'][37]['eval_training']['best_epoch']=8
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 57972], ['id', 12623], ['id', 50410], ['id', 35864], ['ood', 46153], ['id', 46369], ['id', 41375], ['id', 26460], ['id', 42042], ['id', 29180]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.36125051975250244, 0.2975286543369293, 0.27683568000793457, 0.44678616523742676, 0.27497923374176025, 0.49842262268066406, 0.39044952392578125, 0.4327385425567627, 0.5082747936248779, 0.5139651298522949]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.1859203577041626})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.6099934577941895})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.47546684741973877})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34893327951431274})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29779911041259766})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3102036714553833})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2996337413787842})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2870500087738037})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32496488094329834})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29952847957611084})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28705114126205444})
store['active_learning_steps'][38]['training']['best_epoch']=8
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9686, 'crossentropy': 0.2565931884765625}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.0701847076416016})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6140136122703552})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4125540852546692})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.37924692034721375})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33955609798431396})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3120197057723999})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28808873891830444})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.298983633518219})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2921040654182434})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27007776498794556})
store['active_learning_steps'][38]['eval_training']['best_epoch']=10
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 34685], ['id', 55727], ['id', 52252], ['id', 58648], ['id', 12345], ['id', 59309], ['id', 50431], ['id', 13983], ['id', 3810], ['id', 31114]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5249180793762207, 0.3886638879776001, 0.4297793507575989, 0.3910590410232544, 0.502871036529541, 0.3911897540092468, 0.4768383502960205, 0.24184006452560425, 0.4300217032432556, 0.48450183868408203]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.1354248523712158})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6342178583145142})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4192259907722473})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3758099675178528})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.36664360761642456})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3336610794067383})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33007508516311646})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2930150032043457})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.360171377658844})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2815815210342407})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3329649269580841})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3472488224506378})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.34190887212753296})
store['active_learning_steps'][39]['training']['best_epoch']=10
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9708, 'crossentropy': 0.2573395751953125}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.9022299647331238})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5507388114929199})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4277300238609314})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.35862061381340027})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3104588985443115})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28876084089279175})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3218114376068115})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2937854528427124})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2908042371273041})
store['active_learning_steps'][39]['eval_training']['best_epoch']=6
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 11616], ['id', 52800], ['id', 32880], ['id', 15832], ['id', 56978], ['id', 59744], ['id', 51600], ['id', 16488], ['id', 626], ['id', 22364]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4139534533023834, 0.4144176244735718, 0.587658166885376, 0.4852616786956787, 0.36381590366363525, 0.3745715022087097, 0.37590324878692627, 0.5166328549385071, 0.5260189771652222, 0.3579939007759094]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.0638494491577148})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5861233472824097})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3851824700832367})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3323715031147003})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31887149810791016})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33052489161491394})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2878243327140808})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27813196182250977})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2577299475669861})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2979835867881775})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.27196961641311646})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2952480912208557})
store['active_learning_steps'][40]['training']['best_epoch']=9
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9711, 'crossentropy': 0.2320690185546875}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.9146044254302979})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.550453245639801})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.37510958313941956})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.35334381461143494})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32576116919517517})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3006259799003601})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2847251296043396})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.29173004627227783})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2802961468696594})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3092794418334961})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.26366299390792847})
store['active_learning_steps'][40]['eval_training']['best_epoch']=11
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 5129], ['id', 42701], ['id', 52971], ['id', 33364], ['id', 52727], ['id', 13004], ['id', 54032], ['id', 57342], ['id', 48933], ['id', 17005]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4321258068084717, 0.31667232513427734, 0.4410737156867981, 0.36914560198783875, 0.37605032324790955, 0.30481207370758057, 0.4386996030807495, 0.4967939853668213, 0.4525097608566284, 0.4281144142150879]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.2367656230926514})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.6016132831573486})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4291200637817383})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.34818994998931885})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31056490540504456})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3208087384700775})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28196626901626587})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2754620909690857})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2506083548069})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29274147748947144})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2849196791648865})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.26706886291503906})
store['active_learning_steps'][41]['training']['best_epoch']=9
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9732, 'crossentropy': 0.230907421875}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8612500429153442})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.48476025462150574})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3700362741947174})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.33514654636383057})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29838019609451294})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2950926721096039})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2726358473300934})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.24753424525260925})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2635120749473572})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2815152406692505})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.23476484417915344})
store['active_learning_steps'][41]['eval_training']['best_epoch']=11
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 13538], ['id', 17203], ['id', 35464], ['id', 27678], ['id', 19412], ['id', 3204], ['id', 20635], ['id', 16011], ['id', 10544], ['id', 38142]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.4876555800437927, 0.36184820532798767, 0.419738233089447, 0.4233975410461426, 0.47400063276290894, 0.411477267742157, 0.47533413767814636, 0.31052088737487793, 0.38119661808013916, 0.4343135952949524]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.295060396194458})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6304581165313721})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4106970429420471})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.35399872064590454})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3216091990470886})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.309987336397171})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29975637793540955})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2857076823711395})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.258808434009552})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30165624618530273})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2926703691482544})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2931467294692993})
store['active_learning_steps'][42]['training']['best_epoch']=9
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9712, 'crossentropy': 0.236324755859375}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8916206359863281})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4855576753616333})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.38123178482055664})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3147050738334656})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.281986266374588})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2779882550239563})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2366359531879425})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2509971261024475})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.271259069442749})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.24526867270469666})
store['active_learning_steps'][42]['eval_training']['best_epoch']=7
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 19464], ['id', 55294], ['id', 42746], ['id', 10218], ['id', 36866], ['id', 49890], ['id', 54268], ['id', 44753], ['id', 30844], ['id', 58832]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.39331305027008057, 0.3467780351638794, 0.3191627860069275, 0.3238774538040161, 0.3318626284599304, 0.4864121675491333, 0.3826340436935425, 0.4316887855529785, 0.5303166508674622, 0.5036351084709167]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.1996679306030273})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.6007767915725708})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4776793122291565})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.37097927927970886})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32793015241622925})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.33484673500061035})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.29733097553253174})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.30603450536727905})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30017614364624023})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27407971024513245})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3034626841545105})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3242966830730438})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.308427095413208})
store['active_learning_steps'][43]['training']['best_epoch']=10
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9735, 'crossentropy': 0.24147216796875}
