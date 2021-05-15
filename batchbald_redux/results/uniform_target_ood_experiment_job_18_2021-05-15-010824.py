store = {}
store['timestamp']=1621037304
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=18']
store['commit']='5f7c992432b59cee0eb3a035912cbb6cccf9ff9a'
store['github_url']='5f7c992432b59cee0eb3a035912cbb6cccf9ff9a'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=18
store['worker_id']=18
store['num_workers']=30
store['config']={'seed': 1258, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'evaluation_set_size': 100, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.EvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset: FastMNIST (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastFashionMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 40646, 10110, 32775, 33736, 27254, 306, 37354, 19689, 57811, 14640, 39579, 5573, 5715, 47420, 27135, 26129, 16927, 39050, 42295, 45567, 2728, 1774, 33486, 43252, 43803, 50036, 46861, 53831, 54003, 52801, 15969, 57520, 36797, 34198, 27145, 3029, 37047, 31965, 26501, 53689, 31444, 29950, 44803, 396, 56990, 24052, 12108, 54426, 42320, 801, 48031, 2206, 2404, 58741, 29079, 49986, 46464, 17659, 30072, 55187, 34588, 38725, 50466, 40018, 37115, 20801, 23496, 4321, 42102, 26479, 43321, 44048, 45974, 15675, 10508, 49549, 28991, 13074, 9574, 50997, 48032, 40334, 21423, 46870, 18137, 4701, 18693, 17506, 6968, 3792, 10664, 5616, 32972, 30013, 19757, 49169, 47417, 38430, 41512]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.2973294258117676})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.0331573486328125})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 3.4356398582458496})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.5713491439819336})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.5896, 'crossentropy': 2.4716611328125}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 1.3905104398727417})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.3733279705047607})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.362920880317688})
store['active_learning_steps'][0]['eval_training']['best_epoch']=3
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 34216], ['ood', 25903], ['ood', 8650], ['ood', 12972], ['ood', 906], ['ood', 37594], ['ood', 42304], ['ood', 56705], ['ood', 36280], ['ood', 25260]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [1.0233023762702942, 1.0124993324279785, 1.0012484788894653, 0.9978724718093872, 0.9858410358428955, 0.9845951199531555, 0.9776577949523926, 0.9759377241134644, 0.9730293154716492, 0.9715993404388428]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 1.9796032905578613})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 2.7745585441589355})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 3.546489953994751})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 2.9746975898742676})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.5779, 'crossentropy': 2.042293359375}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.2682749032974243})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.2856576442718506})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.2433552742004395})
store['active_learning_steps'][1]['eval_training']['best_epoch']=3
store['active_learning_steps'][1]['acquisition']={'indices': [['ood', 2450], ['ood', 39673], ['ood', 58030], ['ood', 9459], ['ood', 16909], ['ood', 20816], ['ood', 20142], ['ood', 23813], ['ood', 31672], ['ood', 7286]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.7536228895187378, 0.7342381477355957, 0.7112671136856079, 0.7074320912361145, 0.7073610424995422, 0.7053843140602112, 0.7008060216903687, 0.6975084543228149, 0.6831481456756592, 0.6826430559158325]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5654296875, 'crossentropy': 1.7693012952804565})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.572265625, 'crossentropy': 2.2703304290771484})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 2.477900981903076})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 3.069413185119629})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.57, 'crossentropy': 1.758095703125}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 1.2795881032943726})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 1.254054069519043})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 1.2848610877990723})
store['active_learning_steps'][2]['eval_training']['best_epoch']=2
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 50752], ['id', 33308], ['id', 44433], ['id', 46518], ['id', 23869], ['id', 44903], ['id', 39083], ['id', 12717], ['id', 37497], ['id', 56700]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.540431022644043, 0.5356751680374146, 0.5344493389129639, 0.5330456495285034, 0.5324543714523315, 0.5279287099838257, 0.5261398553848267, 0.5192747116088867, 0.5153179168701172, 0.5150853395462036]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.57421875, 'crossentropy': 1.643373727798462})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 2.1909713745117188})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 2.719632148742676})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.2726967334747314})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.557, 'crossentropy': 1.7557208984375}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.572265625, 'crossentropy': 1.3334324359893799})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.5791015625, 'crossentropy': 1.3406113386154175})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.5791015625, 'crossentropy': 1.3271530866622925})
store['active_learning_steps'][3]['eval_training']['best_epoch']=3
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 32771], ['id', 36771], ['id', 2731], ['id', 35031], ['id', 12089], ['id', 11439], ['id', 17293], ['id', 7588], ['id', 24287], ['id', 52020]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5067174434661865, 0.4899793863296509, 0.4824042320251465, 0.47936463356018066, 0.47639238834381104, 0.4665919542312622, 0.4664302468299866, 0.46548008918762207, 0.46435558795928955, 0.46326160430908203]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 1.5241851806640625})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 2.1626038551330566})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.573329448699951})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 3.189828395843506})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.555, 'crossentropy': 1.61408876953125}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.5693359375, 'crossentropy': 1.4040981531143188})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.5751953125, 'crossentropy': 1.4194790124893188})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 1.3505438566207886})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 4770], ['id', 40994], ['id', 20917], ['id', 49480], ['id', 25057], ['id', 59490], ['id', 27717], ['id', 20920], ['id', 52283], ['id', 18334]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3863484859466553, 0.3831433057785034, 0.38031327724456787, 0.378947377204895, 0.3761429786682129, 0.37489235401153564, 0.37412071228027344, 0.3731729984283447, 0.371883749961853, 0.37095606327056885]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.501953125, 'crossentropy': 1.6338486671447754})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 1.6191983222961426})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 2.049706220626831})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.4781713485717773})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.3714401721954346})
store['active_learning_steps'][5]['training']['best_epoch']=2
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.5815, 'crossentropy': 1.7221716796875}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 1.3242219686508179})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.2597635984420776})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.3082976341247559})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.3023905754089355})
store['active_learning_steps'][5]['eval_training']['best_epoch']=2
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 29562], ['id', 12995], ['id', 36128], ['id', 34690], ['id', 49606], ['id', 42528], ['id', 6399], ['id', 12327], ['id', 5613], ['id', 23099]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4109379053115845, 0.4072301387786865, 0.40578436851501465, 0.4037090539932251, 0.3885234594345093, 0.3862226605415344, 0.3855689764022827, 0.38330304622650146, 0.383156418800354, 0.38282036781311035]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.537109375, 'crossentropy': 1.573898434638977})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 1.6791645288467407})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 1.8627656698226929})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 2.102916717529297})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.5195, 'crossentropy': 1.6015859375}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.4970703125, 'crossentropy': 1.5815147161483765})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.5087890625, 'crossentropy': 1.5562019348144531})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.505859375, 'crossentropy': 1.5387895107269287})
store['active_learning_steps'][6]['eval_training']['best_epoch']=3
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 51447], ['id', 42778], ['id', 37053], ['id', 12326], ['id', 21346], ['id', 6176], ['id', 24622], ['id', 25868], ['id', 55912], ['id', 18288]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.26505422592163086, 0.2610069513320923, 0.26098906993865967, 0.25955629348754883, 0.25593578815460205, 0.2548215389251709, 0.2529418468475342, 0.2519904375076294, 0.2508162260055542, 0.2504427433013916]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.552734375, 'crossentropy': 1.503046989440918})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.617469072341919})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.021618127822876})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.097623109817505})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.5207, 'crossentropy': 1.55941767578125}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.478515625, 'crossentropy': 1.4816420078277588})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.5361328125, 'crossentropy': 1.438907265663147})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.53515625, 'crossentropy': 1.428008794784546})
store['active_learning_steps'][7]['eval_training']['best_epoch']=3
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 39766], ['id', 4068], ['id', 41210], ['id', 45716], ['id', 44063], ['id', 37292], ['id', 41415], ['id', 8098], ['id', 18182], ['id', 12890]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.2844400405883789, 0.2654372453689575, 0.2637975215911865, 0.26341044902801514, 0.26124048233032227, 0.25841963291168213, 0.2576601505279541, 0.2568213939666748, 0.2560584545135498, 0.2557608485221863]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.548828125, 'crossentropy': 1.525923728942871})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.4670778512954712})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.617692470550537})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.825610637664795})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.8533298969268799})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.5932, 'crossentropy': 1.4968095703125}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.548828125, 'crossentropy': 1.3702255487442017})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.323622465133667})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 1.2891192436218262})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.307121753692627})
store['active_learning_steps'][8]['eval_training']['best_epoch']=3
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 22547], ['id', 40399], ['id', 31065], ['id', 35305], ['id', 50045], ['id', 2910], ['id', 43277], ['id', 36843], ['id', 4752], ['id', 43265]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.4626486301422119, 0.4477989077568054, 0.4344574213027954, 0.4180797338485718, 0.4159303903579712, 0.4109309911727905, 0.40948301553726196, 0.4086911678314209, 0.4071047306060791, 0.4042310118675232]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.5, 'crossentropy': 1.5195916891098022})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.3712713718414307})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.5678988695144653})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.895512580871582})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.9211207628250122})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.603, 'crossentropy': 1.46232470703125}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.56640625, 'crossentropy': 1.3420579433441162})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.275404691696167})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.273949146270752})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.2475550174713135})
store['active_learning_steps'][9]['eval_training']['best_epoch']=4
store['active_learning_steps'][9]['acquisition']={'indices': [['ood', 29759], ['ood', 58471], ['ood', 32511], ['id', 6887], ['ood', 22547], ['id', 32498], ['ood', 33639], ['ood', 43823], ['id', 47079], ['ood', 29367]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.43555498123168945, 0.3968343734741211, 0.39253538846969604, 0.3908480405807495, 0.3767915964126587, 0.37371826171875, 0.37244200706481934, 0.37132811546325684, 0.36645740270614624, 0.36278998851776123]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.53125, 'crossentropy': 1.4765442609786987})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.460161566734314})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.4579124450683594})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.7508270740509033})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.229363441467285})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.2703840732574463})
store['active_learning_steps'][10]['training']['best_epoch']=3
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.6042, 'crossentropy': 1.6311798828125}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 1.269599437713623})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.248556137084961})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.2353708744049072})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.1999733448028564})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.2208759784698486})
store['active_learning_steps'][10]['eval_training']['best_epoch']=4
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 39141], ['id', 51252], ['ood', 6427], ['id', 40720], ['ood', 8007], ['ood', 55792], ['id', 41239], ['ood', 8700], ['ood', 10207], ['ood', 27987]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.43976306915283203, 0.4317361116409302, 0.40815675258636475, 0.40408772230148315, 0.40015971660614014, 0.39726316928863525, 0.39622509479522705, 0.3956589698791504, 0.3933802843093872, 0.3910977840423584]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.3974609375, 'crossentropy': 1.6718244552612305})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.4075425863265991})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.4061601161956787})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.5213360786437988})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.5818651914596558})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.5400032997131348})
store['active_learning_steps'][11]['training']['best_epoch']=3
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.6177, 'crossentropy': 1.464814453125}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.5439453125, 'crossentropy': 1.3220739364624023})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.2180297374725342})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.2513564825057983})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.153580665588379})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.163854718208313})
store['active_learning_steps'][11]['eval_training']['best_epoch']=4
store['active_learning_steps'][11]['acquisition']={'indices': [['ood', 51415], ['id', 53583], ['id', 13391], ['id', 55078], ['id', 7375], ['id', 51772], ['id', 47416], ['id', 27220], ['id', 13598], ['id', 53275]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.40287137031555176, 0.39126890897750854, 0.3796691298484802, 0.3780386447906494, 0.3776516914367676, 0.36428558826446533, 0.36349570751190186, 0.36166322231292725, 0.3583648204803467, 0.34987908601760864]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.4345703125, 'crossentropy': 1.5677640438079834})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 1.383422613143921})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.326459527015686})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.39053213596344})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.4837923049926758})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.6590487957000732})
store['active_learning_steps'][12]['training']['best_epoch']=3
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.6292, 'crossentropy': 1.4141064453125}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.5654296875, 'crossentropy': 1.3016886711120605})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.225738286972046})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.1637448072433472})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.1652507781982422})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.185103178024292})
store['active_learning_steps'][12]['eval_training']['best_epoch']=3
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 29437], ['id', 28002], ['id', 47886], ['id', 2388], ['id', 35859], ['id', 55381], ['id', 22805], ['id', 37347], ['id', 11174], ['id', 30185]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.3668128252029419, 0.3628838062286377, 0.3375598192214966, 0.3367985486984253, 0.3359271287918091, 0.3210163116455078, 0.32024431228637695, 0.31567633152008057, 0.3145827054977417, 0.31134504079818726]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.404296875, 'crossentropy': 1.6401559114456177})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.548828125, 'crossentropy': 1.4112651348114014})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.3429763317108154})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.3796228170394897})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.4761767387390137})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.5719215869903564})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6083, 'crossentropy': 1.37097099609375}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.5654296875, 'crossentropy': 1.3640297651290894})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.2848396301269531})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.213590145111084})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.249403476715088})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.1991119384765625})
store['active_learning_steps'][13]['eval_training']['best_epoch']=5
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 14410], ['id', 36985], ['id', 36343], ['id', 35508], ['id', 28869], ['id', 58130], ['id', 63], ['id', 28543], ['id', 52002], ['id', 27763]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.44094908237457275, 0.4027438163757324, 0.39514482021331787, 0.3949403762817383, 0.391369104385376, 0.390460729598999, 0.3770594596862793, 0.3753129243850708, 0.3686763048171997, 0.36234962940216064]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.4365234375, 'crossentropy': 1.557908058166504})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.576171875, 'crossentropy': 1.3726170063018799})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.3590515851974487})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.28776216506958})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.4686059951782227})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.5085830688476562})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.7349226474761963})
store['active_learning_steps'][14]['training']['best_epoch']=4
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.6362, 'crossentropy': 1.379237109375}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.5712890625, 'crossentropy': 1.2819747924804688})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.1495726108551025})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.1736502647399902})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.1603708267211914})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.1352096796035767})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.108720064163208})
store['active_learning_steps'][14]['eval_training']['best_epoch']=6
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 20968], ['id', 37650], ['id', 9718], ['id', 21258], ['id', 23444], ['id', 34203], ['id', 17753], ['id', 54103], ['id', 53522], ['id', 48364]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4306471347808838, 0.4248642921447754, 0.41970574855804443, 0.4178310036659241, 0.41749370098114014, 0.4137953519821167, 0.410228967666626, 0.4096180200576782, 0.40813905000686646, 0.4052072763442993]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.482421875, 'crossentropy': 1.5892914533615112})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 1.327341079711914})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.3623886108398438})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.4972761869430542})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.5641967058181763})
store['active_learning_steps'][15]['training']['best_epoch']=2
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.5793, 'crossentropy': 1.3656330078125}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.5107421875, 'crossentropy': 1.40481436252594})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 1.2714513540267944})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 1.2783716917037964})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 1.2811453342437744})
store['active_learning_steps'][15]['eval_training']['best_epoch']=2
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 57392], ['id', 46875], ['id', 21381], ['id', 45740], ['id', 54881], ['id', 17886], ['id', 37090], ['id', 1254], ['id', 30119], ['id', 12689]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.29527080059051514, 0.29106080532073975, 0.290016770362854, 0.2892954349517822, 0.28381919860839844, 0.28182506561279297, 0.2757159471511841, 0.2727004289627075, 0.2722458839416504, 0.27141672372817993]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.513671875, 'crossentropy': 1.6923139095306396})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 1.3474078178405762})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.317360520362854})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.2608168125152588})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.3320975303649902})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.5396870374679565})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.6388919353485107})
store['active_learning_steps'][16]['training']['best_epoch']=4
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.6526, 'crossentropy': 1.328823828125}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.5556640625, 'crossentropy': 1.3214553594589233})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.1629865169525146})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.1043193340301514})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.142850637435913})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.097448706626892})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.0834978818893433})
store['active_learning_steps'][16]['eval_training']['best_epoch']=6
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 10147], ['id', 27800], ['id', 19069], ['id', 34793], ['id', 52950], ['id', 22568], ['id', 21011], ['id', 14060], ['id', 54287], ['id', 19315]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.45401763916015625, 0.4299440383911133, 0.4267648458480835, 0.41927146911621094, 0.41763836145401, 0.41737842559814453, 0.41709625720977783, 0.4134589433670044, 0.4131354093551636, 0.4112390875816345]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.453125, 'crossentropy': 1.6041239500045776})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 1.4397097826004028})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.3295061588287354})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.4961847066879272})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.5700318813323975})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.8497488498687744})
store['active_learning_steps'][17]['training']['best_epoch']=3
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.6037, 'crossentropy': 1.3738474609375}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.498046875, 'crossentropy': 1.4380428791046143})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 1.2291505336761475})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 1.213775396347046})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.136573076248169})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.175272822380066})
store['active_learning_steps'][17]['eval_training']['best_epoch']=4
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 1033], ['id', 32980], ['id', 54813], ['id', 32110], ['ood', 8668], ['id', 850], ['id', 35985], ['id', 49376], ['id', 18814], ['id', 2181]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.40185612440109253, 0.3864032030105591, 0.3732752799987793, 0.3663841485977173, 0.3589547872543335, 0.35351526737213135, 0.34960323572158813, 0.3492114543914795, 0.34532225131988525, 0.34372758865356445]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.443359375, 'crossentropy': 1.6084266901016235})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.5146484375, 'crossentropy': 1.4448912143707275})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.34315824508667})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.4979462623596191})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.7781943082809448})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.0070598125457764})
store['active_learning_steps'][18]['training']['best_epoch']=3
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6051, 'crossentropy': 1.41633359375}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.517578125, 'crossentropy': 1.4083099365234375})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.5791015625, 'crossentropy': 1.269885540008545})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 1.2234673500061035})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.55859375, 'crossentropy': 1.2384183406829834})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.572265625, 'crossentropy': 1.2525956630706787})
store['active_learning_steps'][18]['eval_training']['best_epoch']=3
store['active_learning_steps'][18]['acquisition']={'indices': [['ood', 37074], ['id', 17324], ['ood', 10350], ['id', 53540], ['ood', 23110], ['id', 57979], ['id', 59786], ['id', 50616], ['id', 59620], ['id', 6594]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.41384613513946533, 0.39438116550445557, 0.3935117721557617, 0.3905940055847168, 0.38717085123062134, 0.3862440586090088, 0.3857078552246094, 0.3801673650741577, 0.3789612054824829, 0.3782902956008911]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.4990234375, 'crossentropy': 1.5976128578186035})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.55859375, 'crossentropy': 1.3469083309173584})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.2040724754333496})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.2698503732681274})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.451143741607666})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.4366273880004883})
store['active_learning_steps'][19]['training']['best_epoch']=3
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6147, 'crossentropy': 1.2841302734375}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.521484375, 'crossentropy': 1.3460266590118408})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 1.2070059776306152})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.1366678476333618})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.1448116302490234})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.1226321458816528})
store['active_learning_steps'][19]['eval_training']['best_epoch']=5
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 43432], ['id', 28159], ['id', 3806], ['id', 36674], ['id', 23414], ['id', 34042], ['id', 24079], ['id', 57295], ['id', 23637], ['id', 428]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.31928372383117676, 0.3134578466415405, 0.31298828125, 0.30873823165893555, 0.30864417552948, 0.3059689998626709, 0.30481016635894775, 0.30155515670776367, 0.2915821075439453, 0.2907872200012207]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.470703125, 'crossentropy': 1.5938429832458496})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.546875, 'crossentropy': 1.3929922580718994})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.3001132011413574})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.3897954225540161})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.4154691696166992})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.3025882244110107})
store['active_learning_steps'][20]['training']['best_epoch']=3
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.6226, 'crossentropy': 1.2919208984375}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.4873046875, 'crossentropy': 1.409837007522583})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.5703125, 'crossentropy': 1.2943915128707886})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.200150489807129})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.2051503658294678})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.1990785598754883})
store['active_learning_steps'][20]['eval_training']['best_epoch']=5
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 20624], ['id', 49891], ['ood', 57268], ['id', 28733], ['id', 22836], ['ood', 19102], ['id', 3410], ['ood', 10248], ['ood', 27409], ['id', 31216]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.34521162509918213, 0.3189738988876343, 0.3168560266494751, 0.3151973485946655, 0.3151284456253052, 0.3119734525680542, 0.31048882007598877, 0.3096580505371094, 0.3094353675842285, 0.307802677154541]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.5009765625, 'crossentropy': 1.4714914560317993})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 1.2971525192260742})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.1894434690475464})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.2962087392807007})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.3375217914581299})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.423193335533142})
store['active_learning_steps'][21]['training']['best_epoch']=3
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.638, 'crossentropy': 1.2327453125}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.5234375, 'crossentropy': 1.3487744331359863})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.2061179876327515})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.1684472560882568})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.1144897937774658})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.1195926666259766})
store['active_learning_steps'][21]['eval_training']['best_epoch']=4
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 42133], ['id', 37884], ['id', 20874], ['id', 48671], ['id', 12617], ['id', 20686], ['id', 5535], ['id', 8181], ['id', 42994], ['id', 20166]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.3667284846305847, 0.3560090661048889, 0.35570067167282104, 0.3536221981048584, 0.3515668511390686, 0.35049617290496826, 0.3429105281829834, 0.3428466320037842, 0.3371713161468506, 0.3330514430999756]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.455078125, 'crossentropy': 1.6515998840332031})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 1.3193304538726807})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.3354337215423584})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.2299587726593018})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.1402935981750488})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.1864328384399414})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.333944320678711})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.4217941761016846})
store['active_learning_steps'][22]['training']['best_epoch']=5
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.6637, 'crossentropy': 1.199842578125}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.5576171875, 'crossentropy': 1.2506828308105469})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.107643485069275})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.0324822664260864})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.0169692039489746})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.0260347127914429})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 0.9741920828819275})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 0.9734916090965271})
store['active_learning_steps'][22]['eval_training']['best_epoch']=7
store['active_learning_steps'][22]['acquisition']={'indices': [['ood', 53077], ['id', 7478], ['id', 27719], ['id', 4267], ['id', 31557], ['id', 6977], ['id', 18584], ['id', 6512], ['id', 4571], ['id', 50249]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.40805888175964355, 0.38329142332077026, 0.3790017366409302, 0.36960411071777344, 0.3676157593727112, 0.3585056662559509, 0.3573564291000366, 0.34588897228240967, 0.3427038788795471, 0.34178030490875244]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.5302734375, 'crossentropy': 1.4606010913848877})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.2125906944274902})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.1477999687194824})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.134640097618103})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.209338665008545})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.2690434455871582})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.2540216445922852})
store['active_learning_steps'][23]['training']['best_epoch']=4
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.6545, 'crossentropy': 1.1646361328125}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.576171875, 'crossentropy': 1.2738595008850098})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.1191765069961548})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.1118260622024536})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.0439088344573975})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.0388352870941162})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.0055404901504517})
store['active_learning_steps'][23]['eval_training']['best_epoch']=6
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 20652], ['id', 1776], ['id', 49224], ['id', 52428], ['id', 43193], ['id', 28962], ['id', 57213], ['id', 14874], ['id', 4008], ['id', 35913]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.36053466796875, 0.35814785957336426, 0.3517817258834839, 0.34954720735549927, 0.340152382850647, 0.33230316638946533, 0.33181262016296387, 0.330230712890625, 0.3287088871002197, 0.3271563649177551]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.4853515625, 'crossentropy': 1.4994231462478638})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.2021373510360718})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.1680843830108643})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.179969072341919})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.2323354482650757})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.186143398284912})
store['active_learning_steps'][24]['training']['best_epoch']=3
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.6146, 'crossentropy': 1.2416158203125}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.5302734375, 'crossentropy': 1.3336668014526367})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 1.1782969236373901})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 1.1475777626037598})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.1366240978240967})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.1119464635849})
store['active_learning_steps'][24]['eval_training']['best_epoch']=5
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 70], ['id', 26160], ['id', 55098], ['id', 34750], ['id', 26636], ['id', 38782], ['id', 16154], ['id', 52223], ['id', 50385], ['id', 40800]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3955662250518799, 0.3728335499763489, 0.3670692443847656, 0.361133337020874, 0.36091649532318115, 0.3541828989982605, 0.3532242774963379, 0.35157930850982666, 0.3509029150009155, 0.3476996421813965]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.515625, 'crossentropy': 1.4687256813049316})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.1824493408203125})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.2063227891921997})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.1277928352355957})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.2247976064682007})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.2360813617706299})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.2728986740112305})
store['active_learning_steps'][25]['training']['best_epoch']=4
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.6529, 'crossentropy': 1.1615248046875}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.2452664375305176})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.095503807067871})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.0871495008468628})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.0435441732406616})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.0077816247940063})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.0341547727584839})
store['active_learning_steps'][25]['eval_training']['best_epoch']=5
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 23684], ['id', 56635], ['id', 41119], ['id', 48595], ['ood', 37249], ['id', 49777], ['id', 10251], ['id', 51418], ['id', 3300], ['ood', 8731]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.42739737033843994, 0.39672327041625977, 0.3936384916305542, 0.3785831928253174, 0.37824416160583496, 0.36675703525543213, 0.3649873733520508, 0.3599487543106079, 0.3591621518135071, 0.35616910457611084]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.5078125, 'crossentropy': 1.531680941581726})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.2325823307037354})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.156116247177124})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.1193251609802246})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.1499836444854736})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.1178388595581055})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.181717038154602})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.259753942489624})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.225172758102417})
store['active_learning_steps'][26]['training']['best_epoch']=6
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.6778, 'crossentropy': 1.24469306640625}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.2310843467712402})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.1018180847167969})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.0269522666931152})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.0030405521392822})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 0.989246666431427})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 0.941104531288147})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 0.9455903172492981})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 0.9322985410690308})
store['active_learning_steps'][26]['eval_training']['best_epoch']=8
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 34981], ['id', 19888], ['id', 52334], ['id', 19136], ['id', 45641], ['id', 1799], ['id', 53796], ['id', 29915], ['id', 17481], ['id', 12302]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.46513134241104126, 0.4527098536491394, 0.44716084003448486, 0.4467354416847229, 0.4265049695968628, 0.422078013420105, 0.4216398596763611, 0.415988564491272, 0.41534680128097534, 0.4138834476470947]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.4755859375, 'crossentropy': 1.5688023567199707})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 1.2349680662155151})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.1472636461257935})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.116945743560791})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.123808741569519})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.1484479904174805})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.1856974363327026})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.65, 'crossentropy': 1.17317763671875}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.5234375, 'crossentropy': 1.333516240119934})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.1325440406799316})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.102689504623413})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.0508077144622803})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.0527483224868774})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.0722217559814453})
store['active_learning_steps'][27]['eval_training']['best_epoch']=4
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 2747], ['id', 25654], ['id', 10052], ['id', 27449], ['id', 47090], ['id', 22066], ['id', 54196], ['id', 37658], ['id', 46820], ['id', 29501]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.36810481548309326, 0.3435131311416626, 0.3347511291503906, 0.3166998624801636, 0.3118668794631958, 0.3110088109970093, 0.3099701404571533, 0.30926376581192017, 0.30861979722976685, 0.3077826499938965]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.49609375, 'crossentropy': 1.4914402961730957})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.55859375, 'crossentropy': 1.2948706150054932})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.1493535041809082})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.0512819290161133})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.0923796892166138})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.0996499061584473})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.1109857559204102})
store['active_learning_steps'][28]['training']['best_epoch']=4
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.6845, 'crossentropy': 1.08911123046875}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.2399108409881592})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.1167216300964355})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.0258290767669678})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.0110085010528564})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 0.9870522618293762})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 0.9728132486343384})
store['active_learning_steps'][28]['eval_training']['best_epoch']=6
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 32759], ['id', 3913], ['id', 56380], ['id', 59953], ['id', 31662], ['id', 39483], ['id', 30476], ['id', 33674], ['id', 52042], ['id', 2846]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.3411564826965332, 0.3355088233947754, 0.3296118974685669, 0.3287184238433838, 0.32450413703918457, 0.323269248008728, 0.3183184862136841, 0.31435835361480713, 0.31291890144348145, 0.3100799322128296]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.5, 'crossentropy': 1.5460063219070435})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.2533907890319824})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.1162714958190918})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.07981538772583})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.1287035942077637})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.1144561767578125})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.2536081075668335})
store['active_learning_steps'][29]['training']['best_epoch']=4
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.6803, 'crossentropy': 1.12733828125}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 1.2525439262390137})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.0534014701843262})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.0915651321411133})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 0.965263307094574})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.0050783157348633})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 0.950060248374939})
store['active_learning_steps'][29]['eval_training']['best_epoch']=6
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 19174], ['id', 19682], ['id', 27178], ['id', 15841], ['id', 17030], ['id', 6389], ['id', 37489], ['id', 54078], ['id', 53412], ['id', 18568]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.41209912300109863, 0.3745361566543579, 0.37048250436782837, 0.3636057376861572, 0.36204278469085693, 0.35545647144317627, 0.35422515869140625, 0.35336482524871826, 0.3452620506286621, 0.34217381477355957]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.48046875, 'crossentropy': 1.470024824142456})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.2585296630859375})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.1103837490081787})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.1421985626220703})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.1377005577087402})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.1964818239212036})
store['active_learning_steps'][30]['training']['best_epoch']=3
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.6464, 'crossentropy': 1.15322734375}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.53515625, 'crossentropy': 1.3709467649459839})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.2221676111221313})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.1455061435699463})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.1277495622634888})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.1158654689788818})
store['active_learning_steps'][30]['eval_training']['best_epoch']=5
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 7593], ['id', 43346], ['id', 52641], ['id', 52509], ['id', 3830], ['id', 49650], ['id', 32229], ['id', 25420], ['id', 44573], ['id', 52168]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.3129383325576782, 0.308383584022522, 0.30170130729675293, 0.28512394428253174, 0.2813119888305664, 0.27939069271087646, 0.27406489849090576, 0.2739051580429077, 0.2707051634788513, 0.2703515291213989]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.470703125, 'crossentropy': 1.596314549446106})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.5615234375, 'crossentropy': 1.2595257759094238})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.1910936832427979})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.2180721759796143})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.1612828969955444})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.199441909790039})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.1718426942825317})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.2637042999267578})
store['active_learning_steps'][31]['training']['best_epoch']=5
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.6638, 'crossentropy': 1.19306142578125}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.5751953125, 'crossentropy': 1.3307867050170898})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.1598392724990845})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.0632716417312622})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.0447040796279907})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.0480698347091675})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.0449638366699219})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.0163819789886475})
store['active_learning_steps'][31]['eval_training']['best_epoch']=7
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 33716], ['id', 41912], ['id', 11442], ['id', 20009], ['id', 18670], ['id', 57485], ['id', 44686], ['id', 19362], ['id', 38618], ['id', 47904]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3663041591644287, 0.3615971803665161, 0.360742449760437, 0.3576242923736572, 0.3575461506843567, 0.35251128673553467, 0.35038328170776367, 0.34895336627960205, 0.3477749824523926, 0.3426569700241089]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.5283203125, 'crossentropy': 1.5424141883850098})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.2119073867797852})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.1209384202957153})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.0617296695709229})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.0918147563934326})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.1713601350784302})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.1254162788391113})
store['active_learning_steps'][32]['training']['best_epoch']=4
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.6836, 'crossentropy': 1.05245263671875}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.5595703125, 'crossentropy': 1.3210375308990479})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.1451635360717773})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.0794975757598877})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.022257924079895})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.0400112867355347})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.0197160243988037})
store['active_learning_steps'][32]['eval_training']['best_epoch']=6
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 2613], ['id', 51688], ['id', 38058], ['id', 688], ['id', 55475], ['id', 17191], ['id', 30901], ['id', 33778], ['id', 55037], ['id', 41355]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.3243722915649414, 0.31457948684692383, 0.3082859516143799, 0.3056443929672241, 0.3045154809951782, 0.30427443981170654, 0.29976344108581543, 0.2995874881744385, 0.2986915111541748, 0.2976851463317871]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.5458984375, 'crossentropy': 1.4801487922668457})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.57421875, 'crossentropy': 1.2698804140090942})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.0707571506500244})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.030247688293457})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.0769648551940918})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.055991530418396})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.082592487335205})
store['active_learning_steps'][33]['training']['best_epoch']=4
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.6712, 'crossentropy': 1.04998681640625}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.5498046875, 'crossentropy': 1.3144984245300293})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.203716516494751})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.1164271831512451})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.0662713050842285})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.0443763732910156})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.0253784656524658})
store['active_learning_steps'][33]['eval_training']['best_epoch']=6
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 33781], ['id', 9302], ['id', 23126], ['id', 12019], ['id', 58038], ['ood', 50598], ['id', 3301], ['id', 37695], ['id', 24792], ['id', 20913]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.31167638301849365, 0.2975412607192993, 0.2885481119155884, 0.2884413003921509, 0.2857145071029663, 0.285150408744812, 0.2830806374549866, 0.28234875202178955, 0.28057217597961426, 0.28006547689437866]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.4921875, 'crossentropy': 1.5468595027923584})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.54296875, 'crossentropy': 1.2634639739990234})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.1973896026611328})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0754684209823608})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.1070892810821533})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.0981557369232178})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.1375716924667358})
store['active_learning_steps'][34]['training']['best_epoch']=4
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.6607, 'crossentropy': 1.091466015625}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.5400390625, 'crossentropy': 1.3744173049926758})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 1.2098345756530762})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.1302247047424316})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.070838212966919})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.1217753887176514})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.0639654397964478})
store['active_learning_steps'][34]['eval_training']['best_epoch']=6
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 10181], ['id', 37709], ['id', 48243], ['id', 51236], ['id', 18530], ['id', 18284], ['id', 28843], ['id', 45171], ['id', 12078], ['id', 26805]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.27750325202941895, 0.2740285396575928, 0.27311384677886963, 0.2730870246887207, 0.272691011428833, 0.2726325988769531, 0.27174413204193115, 0.2693824768066406, 0.267863392829895, 0.25964415073394775]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.474609375, 'crossentropy': 1.5545802116394043})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.5654296875, 'crossentropy': 1.2870513200759888})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.179689884185791})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.1450939178466797})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.0950138568878174})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.098777413368225})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.07318115234375})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.081498384475708})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.1456105709075928})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.1656851768493652})
store['active_learning_steps'][35]['training']['best_epoch']=7
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.6873, 'crossentropy': 1.16693330078125}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.564453125, 'crossentropy': 1.3585913181304932})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.1106173992156982})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.0266989469528198})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 0.9873338937759399})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.0006215572357178})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 0.9653915166854858})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 0.9383491277694702})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 0.9347691535949707})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 0.9241079092025757})
store['active_learning_steps'][35]['eval_training']['best_epoch']=9
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 10381], ['id', 32404], ['id', 35583], ['id', 7577], ['id', 13144], ['id', 33592], ['id', 4148], ['id', 47971], ['id', 55765], ['id', 21184]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.44655317068099976, 0.42423194646835327, 0.4210653305053711, 0.41842591762542725, 0.4097830057144165, 0.4000062942504883, 0.39911675453186035, 0.39887404441833496, 0.38289499282836914, 0.3769652843475342]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.53515625, 'crossentropy': 1.486556053161621})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.2119636535644531})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.1324810981750488})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.0541787147521973})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.0610536336898804})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.0854861736297607})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.010482668876648})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.0202893018722534})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.0567585229873657})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.122750997543335})
store['active_learning_steps'][36]['training']['best_epoch']=7
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.7074, 'crossentropy': 1.06725859375}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.2331602573394775})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.076643705368042})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 0.9556697607040405})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 0.9513469934463501})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 0.8790507316589355})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 0.9219107627868652})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 0.8802474737167358})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 0.863317608833313})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 0.8828612565994263})
store['active_learning_steps'][36]['eval_training']['best_epoch']=8
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 26568], ['id', 32338], ['id', 44570], ['id', 47989], ['id', 22212], ['id', 58841], ['id', 43415], ['id', 34192], ['id', 21981], ['id', 2526]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4451630711555481, 0.42261093854904175, 0.40648186206817627, 0.4008800983428955, 0.3931591510772705, 0.38656342029571533, 0.3813440799713135, 0.37926262617111206, 0.3792259693145752, 0.3708861470222473]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.54296875, 'crossentropy': 1.463036298751831})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.1909645795822144})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.1243236064910889})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.0395183563232422})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.073352336883545})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.0216376781463623})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.0610816478729248})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.023725986480713})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.060665249824524})
store['active_learning_steps'][37]['training']['best_epoch']=6
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.6902, 'crossentropy': 1.0543234375}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.2283555269241333})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.0701253414154053})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 0.968609094619751})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 0.9970943927764893})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 0.9510833621025085})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 0.9119662046432495})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 0.897383987903595})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 0.9045590162277222})
store['active_learning_steps'][37]['eval_training']['best_epoch']=7
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 4450], ['id', 59012], ['id', 35588], ['id', 39814], ['id', 33268], ['id', 22414], ['id', 2298], ['id', 24430], ['id', 13565], ['id', 11655]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4156343936920166, 0.4143904447555542, 0.41288435459136963, 0.4069136381149292, 0.3946681022644043, 0.3924379348754883, 0.3908303380012512, 0.3884040117263794, 0.3811596632003784, 0.380839467048645]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.50390625, 'crossentropy': 1.5108065605163574})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.1878310441970825})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.099970817565918})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.00569486618042})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.037567138671875})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.010894775390625})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.033439040184021})
store['active_learning_steps'][38]['training']['best_epoch']=4
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.6616, 'crossentropy': 1.07256572265625}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.5537109375, 'crossentropy': 1.2951958179473877})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.1500117778778076})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.0890395641326904})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.0320892333984375})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.0615029335021973})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.018571376800537})
store['active_learning_steps'][38]['eval_training']['best_epoch']=6
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 14436], ['id', 24406], ['id', 4219], ['id', 22360], ['id', 28501], ['id', 22224], ['id', 37928], ['id', 47659], ['id', 5135], ['id', 16608]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.3149775266647339, 0.3056206703186035, 0.29835206270217896, 0.29270386695861816, 0.291978120803833, 0.28989601135253906, 0.2847334146499634, 0.2831461429595947, 0.2823629379272461, 0.281791090965271]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.5224609375, 'crossentropy': 1.5592107772827148})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.248010516166687})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.1013102531433105})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.0378036499023438})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 0.97620689868927})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.0167100429534912})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.0063273906707764})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 0.9977136850357056})
store['active_learning_steps'][39]['training']['best_epoch']=5
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.6887, 'crossentropy': 1.0164830078125}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.564453125, 'crossentropy': 1.3452653884887695})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.11026930809021})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.0444276332855225})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 0.9972749948501587})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 0.9723328351974487})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 0.9656692743301392})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 0.9501878023147583})
store['active_learning_steps'][39]['eval_training']['best_epoch']=7
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 1031], ['id', 14763], ['id', 39951], ['id', 46619], ['id', 58242], ['id', 19842], ['id', 31055], ['id', 40721], ['id', 16530], ['id', 48954]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.366397500038147, 0.3653716444969177, 0.3622145652770996, 0.358739972114563, 0.33233654499053955, 0.33001959323883057, 0.3254110813140869, 0.3252081871032715, 0.3236587643623352, 0.31840771436691284]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.509765625, 'crossentropy': 1.4932290315628052})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.2411668300628662})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.1967453956604004})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.0362164974212646})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.0201221704483032})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 0.9437004923820496})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.0585477352142334})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 0.9605716466903687})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 0.987655758857727})
store['active_learning_steps'][40]['training']['best_epoch']=6
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.7196, 'crossentropy': 0.9569212890625}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.3288078308105469})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.0929056406021118})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 0.9612306356430054})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 0.9507140517234802})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 0.9491695761680603})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 0.9424369931221008})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 0.9386379718780518})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 0.9052982330322266})
store['active_learning_steps'][40]['eval_training']['best_epoch']=8
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 16457], ['id', 3889], ['id', 7563], ['id', 9461], ['id', 52373], ['id', 52095], ['id', 59105], ['id', 53457], ['id', 2413], ['id', 31683]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.39640772342681885, 0.3818744421005249, 0.37856996059417725, 0.3659864664077759, 0.3652687668800354, 0.35608208179473877, 0.3522195816040039, 0.3513376712799072, 0.3487287759780884, 0.3416825532913208]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.5068359375, 'crossentropy': 1.590684175491333})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.2535653114318848})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.1204845905303955})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 0.9998474717140198})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 0.9858483672142029})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.0042200088500977})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.003629446029663})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.0033550262451172})
store['active_learning_steps'][41]['training']['best_epoch']=5
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.6949, 'crossentropy': 1.00376318359375}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.5537109375, 'crossentropy': 1.3354125022888184})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.174604892730713})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.0990965366363525})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.0322487354278564})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.0277687311172485})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 0.9681958556175232})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 0.9776022434234619})
store['active_learning_steps'][41]['eval_training']['best_epoch']=6
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 27863], ['id', 55778], ['id', 49763], ['id', 46547], ['id', 5572], ['id', 22576], ['id', 8455], ['id', 36293], ['id', 4436], ['id', 25058]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.3427577614784241, 0.3282480239868164, 0.322955846786499, 0.31722819805145264, 0.2893611192703247, 0.28779083490371704, 0.28696978092193604, 0.2867509722709656, 0.2848236560821533, 0.28218913078308105]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.4638671875, 'crossentropy': 1.596040964126587})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.1647682189941406})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.0574862957000732})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.0739308595657349})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.0045323371887207})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.0171198844909668})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0040171146392822})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.0965192317962646})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.068497896194458})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.0124399662017822})
store['active_learning_steps'][42]['training']['best_epoch']=7
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.7079, 'crossentropy': 1.01673603515625}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.2563230991363525})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.0161082744598389})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.0128921270370483})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 0.9266254901885986})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 0.9112436175346375})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 0.8757562041282654})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 0.9105900526046753})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 0.8766949772834778})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 0.8786606788635254})
store['active_learning_steps'][42]['eval_training']['best_epoch']=6
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 39750], ['ood', 7782], ['id', 53579], ['id', 13179], ['ood', 48107], ['id', 5587], ['id', 11058], ['id', 55165], ['id', 56983], ['id', 12968]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.4733348488807678, 0.4219886064529419, 0.40499234199523926, 0.39806652069091797, 0.39475786685943604, 0.3922532796859741, 0.39198893308639526, 0.3865191340446472, 0.38464510440826416, 0.38307249546051025]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.5390625, 'crossentropy': 1.5242576599121094})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.2367305755615234})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.1386792659759521})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.0055310726165771})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.0624210834503174})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 0.9631270170211792})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.0076372623443604})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.0109342336654663})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 0.9258872270584106})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 0.9698294401168823})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.0357409715652466})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.0666210651397705})
store['active_learning_steps'][43]['training']['best_epoch']=9
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.7337, 'crossentropy': 0.9454671875}
