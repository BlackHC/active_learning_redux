store = {}
store['timestamp']=1621035611
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=15']
store['commit']='5f7c992432b59cee0eb3a035912cbb6cccf9ff9a'
store['github_url']='5f7c992432b59cee0eb3a035912cbb6cccf9ff9a'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=15
store['worker_id']=15
store['num_workers']=30
store['config']={'seed': 1254, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'evaluation_set_size': 100, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.EvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset: FastMNIST (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastFashionMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 40646, 10110, 32775, 33736, 27254, 306, 37354, 19689, 57811, 14640, 39579, 5573, 5715, 47420, 27135, 26129, 16927, 39050, 42295, 45567, 2728, 1774, 33486, 43252, 43803, 50036, 46861, 53831, 54003, 52801, 15969, 57520, 36797, 34198, 27145, 3029, 37047, 31965, 26501, 53689, 31444, 29950, 44803, 396, 56990, 24052, 12108, 54426, 42320, 801, 48031, 2206, 2404, 58741, 29079, 49986, 46464, 17659, 30072, 55187, 34588, 38725, 50466, 40018, 37115, 20801, 23496, 4321, 42102, 26479, 43321, 44048, 45974, 15675, 10508, 49549, 28991, 13074, 9574, 50997, 48032, 40334, 21423, 46870, 18137, 4701, 18693, 17506, 6968, 3792, 10664, 5616, 32972, 30013, 19757, 49169, 47417, 38430, 41512]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.025707483291626})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 2.8455803394317627})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.998870372772217})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.4012913703918457})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.5932, 'crossentropy': 2.2899322265625}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.226649284362793})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.2378954887390137})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 1.2636194229125977})
store['active_learning_steps'][0]['eval_training']['best_epoch']=1
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 33249], ['ood', 4377], ['ood', 56654], ['ood', 16877], ['ood', 3039], ['ood', 43571], ['ood', 45751], ['ood', 40025], ['ood', 34895], ['ood', 52149]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [1.0041841864585876, 0.9746214747428894, 0.9723710417747498, 0.9693301320075989, 0.9687888622283936, 0.9679656624794006, 0.9592986702919006, 0.9531694650650024, 0.951869547367096, 0.9513246417045593]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5751953125, 'crossentropy': 2.3285436630249023})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.636394500732422})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.187711238861084})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.492753267288208})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.5742, 'crossentropy': 2.2612017578125}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 1.435854196548462})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.3940834999084473})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 1.3709903955459595})
store['active_learning_steps'][1]['eval_training']['best_epoch']=3
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 29754], ['id', 200], ['id', 6118], ['id', 40570], ['id', 49863], ['id', 9943], ['id', 54712], ['id', 41131], ['id', 17286], ['id', 41526]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.741314172744751, 0.7391065359115601, 0.7243727445602417, 0.7056050300598145, 0.7051356434822083, 0.7038922905921936, 0.7008253335952759, 0.6992859244346619, 0.690917432308197, 0.6903714537620544]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 1.652829885482788})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.137014389038086})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.813425064086914})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.302452325820923})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.5823, 'crossentropy': 1.7365912109375}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.564453125, 'crossentropy': 1.348676085472107})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.212715744972229})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 1.2220351696014404})
store['active_learning_steps'][2]['eval_training']['best_epoch']=2
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 34620], ['id', 36843], ['ood', 58182], ['id', 10920], ['id', 17751], ['id', 28218], ['id', 28733], ['id', 24661], ['id', 30499], ['id', 13753]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6004159450531006, 0.5593010187149048, 0.5415966510772705, 0.5332223773002625, 0.5284584760665894, 0.5262467861175537, 0.5240909457206726, 0.5229120254516602, 0.5179909467697144, 0.5157965421676636]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 1.5526635646820068})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.0231211185455322})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.3202285766601562})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.5758113861083984})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.5866, 'crossentropy': 1.533612890625}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.55859375, 'crossentropy': 1.3297271728515625})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 1.2807974815368652})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.26697838306427})
store['active_learning_steps'][3]['eval_training']['best_epoch']=3
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 44630], ['id', 47416], ['id', 12089], ['id', 12620], ['id', 54644], ['id', 13530], ['id', 45570], ['id', 37281], ['id', 27220], ['id', 50211]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5158776044845581, 0.4647989273071289, 0.4609156847000122, 0.4422750473022461, 0.43901729583740234, 0.43877196311950684, 0.4366075396537781, 0.4299110174179077, 0.4250861406326294, 0.42344528436660767]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.6125766038894653})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 2.078341007232666})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.163774013519287})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.1553750038146973})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.5915, 'crossentropy': 1.6432755859375}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 1.4074063301086426})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 1.3566280603408813})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.2926923036575317})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 3976], ['id', 42695], ['id', 50521], ['id', 13691], ['ood', 31795], ['id', 39819], ['id', 16640], ['id', 38276], ['id', 45953], ['id', 16659]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.41465258598327637, 0.39857208728790283, 0.39798277616500854, 0.3916918635368347, 0.38705742359161377, 0.38641178607940674, 0.3831501007080078, 0.3830697536468506, 0.3825991153717041, 0.3823566436767578]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.4228668212890625})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.7499372959136963})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.1829476356506348})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 2.623910665512085})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.5933, 'crossentropy': 1.4403099609375}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.5712890625, 'crossentropy': 1.3521392345428467})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.5693359375, 'crossentropy': 1.3039072751998901})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.56640625, 'crossentropy': 1.315629482269287})
store['active_learning_steps'][5]['eval_training']['best_epoch']=2
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 27090], ['id', 43510], ['id', 43265], ['id', 4752], ['id', 39141], ['id', 57504], ['id', 4303], ['id', 37687], ['id', 55729], ['ood', 39203]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.45448023080825806, 0.4459899663925171, 0.43058377504348755, 0.42644619941711426, 0.42344826459884644, 0.4213572144508362, 0.41387587785720825, 0.41177189350128174, 0.40788912773132324, 0.40385711193084717]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5126953125, 'crossentropy': 1.5008877515792847})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 1.6645077466964722})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 2.3203015327453613})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 2.160801410675049})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.5197, 'crossentropy': 1.52632080078125}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.513671875, 'crossentropy': 1.4000499248504639})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.529296875, 'crossentropy': 1.3413488864898682})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.509765625, 'crossentropy': 1.3625143766403198})
store['active_learning_steps'][6]['eval_training']['best_epoch']=2
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 45967], ['id', 15966], ['id', 27592], ['id', 40994], ['id', 14502], ['id', 18579], ['id', 27260], ['id', 54023], ['id', 14067], ['id', 23510]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.36644452810287476, 0.3633681535720825, 0.3618593215942383, 0.3506627082824707, 0.3500065803527832, 0.3493081331253052, 0.3483927845954895, 0.34754955768585205, 0.3438018560409546, 0.3431689739227295]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.505859375, 'crossentropy': 1.4132416248321533})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 1.6228580474853516})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 2.0156426429748535})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.051180362701416})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.5029, 'crossentropy': 1.43933388671875}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.470703125, 'crossentropy': 1.4063427448272705})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.458984375, 'crossentropy': 1.3673359155654907})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.46484375, 'crossentropy': 1.3490413427352905})
store['active_learning_steps'][7]['eval_training']['best_epoch']=3
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 27800], ['id', 3913], ['id', 56439], ['id', 52509], ['id', 36944], ['id', 12410], ['id', 45037], ['id', 59806], ['id', 8681], ['id', 25605]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3886066675186157, 0.38112056255340576, 0.36740171909332275, 0.3668515682220459, 0.3577890396118164, 0.35524487495422363, 0.3546508550643921, 0.3544442653656006, 0.3525019884109497, 0.3503042459487915]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.5205078125, 'crossentropy': 1.5747343301773071})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.5673828125, 'crossentropy': 1.6063756942749023})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.7923979759216309})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.6994138956069946})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.4976, 'crossentropy': 1.6101734375}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.4716796875, 'crossentropy': 1.497049331665039})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.482421875, 'crossentropy': 1.4689581394195557})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.482421875, 'crossentropy': 1.4444340467453003})
store['active_learning_steps'][8]['eval_training']['best_epoch']=3
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 34634], ['id', 47874], ['id', 42311], ['id', 41057], ['id', 24108], ['ood', 2268], ['id', 29354], ['id', 32672], ['ood', 57184], ['id', 35305]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3006089925765991, 0.2991284132003784, 0.29903221130371094, 0.29799604415893555, 0.2964404821395874, 0.2955749034881592, 0.2897512912750244, 0.288960337638855, 0.28704214096069336, 0.28632956743240356]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.48046875, 'crossentropy': 1.5209099054336548})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.4993035793304443})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.564453125, 'crossentropy': 2.1327357292175293})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 2.0642504692077637})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.0292928218841553})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.6009, 'crossentropy': 1.53176279296875}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.552734375, 'crossentropy': 1.4474847316741943})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 1.3252333402633667})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.5673828125, 'crossentropy': 1.2905349731445312})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 1.2644779682159424})
store['active_learning_steps'][9]['eval_training']['best_epoch']=4
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 7327], ['id', 38618], ['id', 6844], ['id', 36568], ['ood', 7406], ['id', 14115], ['ood', 45666], ['ood', 26560], ['id', 2731], ['id', 7626]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.451757550239563, 0.44828319549560547, 0.44413596391677856, 0.4202885627746582, 0.41666126251220703, 0.413859486579895, 0.406585693359375, 0.4052780866622925, 0.4039449691772461, 0.39942848682403564]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.5029296875, 'crossentropy': 1.4851372241973877})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.366912603378296})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.501502275466919})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.552616834640503})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.888198733329773})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.5862, 'crossentropy': 1.433035546875}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.552734375, 'crossentropy': 1.3061293363571167})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.5693359375, 'crossentropy': 1.2324151992797852})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.1971783638000488})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 1.1821441650390625})
store['active_learning_steps'][10]['eval_training']['best_epoch']=4
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 57268], ['id', 32406], ['id', 56332], ['id', 4034], ['id', 55765], ['id', 46237], ['id', 59324], ['id', 57000], ['id', 47772], ['id', 20740]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.4036616086959839, 0.39976370334625244, 0.3984837532043457, 0.3962138891220093, 0.39242398738861084, 0.38026905059814453, 0.37420737743377686, 0.3721212148666382, 0.3709450960159302, 0.370664119720459]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.5166015625, 'crossentropy': 1.576259732246399})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.3450405597686768})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.385941982269287})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.539874792098999})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.5585269927978516})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.6297, 'crossentropy': 1.330330078125}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 1.32002854347229})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.2366255521774292})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.2118185758590698})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.1825158596038818})
store['active_learning_steps'][11]['eval_training']['best_epoch']=4
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 37149], ['id', 35213], ['id', 31705], ['id', 32550], ['ood', 41430], ['id', 50101], ['id', 36854], ['id', 7238], ['id', 52040], ['ood', 14805]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.45179104804992676, 0.4407808780670166, 0.43831783533096313, 0.43399322032928467, 0.42458677291870117, 0.4235270023345947, 0.4233013391494751, 0.4197162985801697, 0.418939471244812, 0.41590988636016846]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.5615234375, 'crossentropy': 1.4501628875732422})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.2899136543273926})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.5149047374725342})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.528831958770752})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.7077622413635254})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.6234, 'crossentropy': 1.2934595703125}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 1.3271236419677734})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.2284533977508545})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.1557176113128662})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.1588544845581055})
store['active_learning_steps'][12]['eval_training']['best_epoch']=3
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 26636], ['id', 31216], ['id', 22616], ['id', 3416], ['id', 9984], ['id', 46439], ['id', 29437], ['id', 32250], ['id', 20027], ['id', 29728]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.33124542236328125, 0.3209911584854126, 0.3199056386947632, 0.31754934787750244, 0.3159182071685791, 0.31532174348831177, 0.3127155303955078, 0.30956196784973145, 0.309298038482666, 0.30840182304382324]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.521484375, 'crossentropy': 1.4625244140625})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.2567148208618164})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.3546708822250366})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.3284790515899658})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.4837640523910522})
store['active_learning_steps'][13]['training']['best_epoch']=2
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6348, 'crossentropy': 1.24041865234375}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 1.3228377103805542})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.2451550960540771})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.1980029344558716})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.1878929138183594})
store['active_learning_steps'][13]['eval_training']['best_epoch']=4
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 22547], ['id', 58220], ['ood', 4263], ['id', 31662], ['id', 14065], ['id', 57751], ['ood', 40532], ['ood', 51201], ['id', 37709], ['ood', 52281]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.3866727352142334, 0.3454486131668091, 0.3426781892776489, 0.34223031997680664, 0.33877527713775635, 0.3372959494590759, 0.33611178398132324, 0.33266115188598633, 0.3314502239227295, 0.330530047416687]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.4833984375, 'crossentropy': 1.5859688520431519})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.3455829620361328})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.3744068145751953})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.3764609098434448})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.411017894744873})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.6084, 'crossentropy': 1.3219470703125}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.5556640625, 'crossentropy': 1.4385180473327637})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.57421875, 'crossentropy': 1.3172590732574463})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 1.2589038610458374})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 1.2654144763946533})
store['active_learning_steps'][14]['eval_training']['best_epoch']=3
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 43105], ['ood', 27473], ['id', 26787], ['id', 42278], ['ood', 27315], ['ood', 27514], ['ood', 53912], ['ood', 53280], ['ood', 9880], ['ood', 13902]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.3559131622314453, 0.3362421989440918, 0.3341214656829834, 0.33380162715911865, 0.3293578624725342, 0.3259158134460449, 0.32531964778900146, 0.3230663537979126, 0.3195115327835083, 0.31915926933288574]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.435546875, 'crossentropy': 1.6412887573242188})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 1.3602824211120605})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.386359691619873})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.380338191986084})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.5094621181488037})
store['active_learning_steps'][15]['training']['best_epoch']=2
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.5832, 'crossentropy': 1.35218388671875}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.5224609375, 'crossentropy': 1.4049628973007202})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.537109375, 'crossentropy': 1.3825645446777344})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.533203125, 'crossentropy': 1.3284943103790283})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.5478515625, 'crossentropy': 1.298986792564392})
store['active_learning_steps'][15]['eval_training']['best_epoch']=4
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 59731], ['id', 7456], ['id', 16530], ['id', 7593], ['id', 41355], ['id', 33773], ['ood', 40140], ['id', 3983], ['ood', 28035], ['ood', 12725]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.3528730869293213, 0.3374958038330078, 0.32441282272338867, 0.32438337802886963, 0.3215756416320801, 0.31713223457336426, 0.3162740468978882, 0.3119642734527588, 0.31169724464416504, 0.3098546266555786]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.4609375, 'crossentropy': 1.5692776441574097})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.5517578125, 'crossentropy': 1.3237202167510986})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 1.3406143188476562})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.2121721506118774})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.3621888160705566})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.5357873439788818})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.480672836303711})
store['active_learning_steps'][16]['training']['best_epoch']=4
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.6414, 'crossentropy': 1.287035546875}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.3224633932113647})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.191280484199524})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.113340139389038})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.1070479154586792})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.0823140144348145})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.1042075157165527})
store['active_learning_steps'][16]['eval_training']['best_epoch']=5
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 24282], ['id', 29287], ['id', 36424], ['id', 58328], ['id', 43193], ['id', 48595], ['id', 9122], ['id', 14667], ['id', 1484], ['id', 43215]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.47169172763824463, 0.4593733549118042, 0.4566326141357422, 0.452620267868042, 0.4332318902015686, 0.42796027660369873, 0.4278334379196167, 0.42573899030685425, 0.41602635383605957, 0.41583341360092163]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.462890625, 'crossentropy': 1.548999309539795})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.57421875, 'crossentropy': 1.304198145866394})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.3018975257873535})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.2093981504440308})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.376983404159546})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.3851416110992432})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.4239845275878906})
store['active_learning_steps'][17]['training']['best_epoch']=4
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.6411, 'crossentropy': 1.22317255859375}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.5634765625, 'crossentropy': 1.2787094116210938})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.1111533641815186})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.0719324350357056})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.0561249256134033})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.019675612449646})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.0255396366119385})
store['active_learning_steps'][17]['eval_training']['best_epoch']=5
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 2369], ['id', 37664], ['id', 33672], ['id', 11901], ['id', 20009], ['id', 35340], ['id', 58320], ['id', 29720], ['id', 5199], ['id', 21258]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.414118155837059, 0.37387025356292725, 0.369128942489624, 0.3686547875404358, 0.3679157495498657, 0.3656604290008545, 0.3652695417404175, 0.363528847694397, 0.3625119924545288, 0.36065202951431274]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.5185546875, 'crossentropy': 1.4651260375976562})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.2625781297683716})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.240792989730835})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.235053300857544})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.314286708831787})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.2996469736099243})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.4695358276367188})
store['active_learning_steps'][18]['training']['best_epoch']=4
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6429, 'crossentropy': 1.30673984375}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.576171875, 'crossentropy': 1.3024013042449951})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 1.1614303588867188})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.1189095973968506})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.0496867895126343})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.0613124370574951})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.0458650588989258})
store['active_learning_steps'][18]['eval_training']['best_epoch']=6
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 27212], ['id', 21049], ['id', 24595], ['ood', 59148], ['id', 13068], ['id', 8763], ['id', 16751], ['ood', 45303], ['id', 30476], ['ood', 38874]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.46788841485977173, 0.45658552646636963, 0.4556255340576172, 0.4536069631576538, 0.44926023483276367, 0.4472329020500183, 0.44634222984313965, 0.4411669373512268, 0.43285971879959106, 0.4314689040184021]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.458984375, 'crossentropy': 1.4860177040100098})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 1.2931575775146484})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.1683299541473389})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.119354009628296})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.3221287727355957})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.315272569656372})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.578070044517517})
store['active_learning_steps'][19]['training']['best_epoch']=4
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6879, 'crossentropy': 1.1520900390625}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 1.2189505100250244})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.039320945739746})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.011263370513916})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 0.9609757661819458})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 0.946682333946228})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 0.9728006720542908})
store['active_learning_steps'][19]['eval_training']['best_epoch']=5
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 12078], ['id', 49135], ['id', 16154], ['id', 25184], ['id', 57772], ['id', 47079], ['id', 45262], ['id', 34750], ['id', 2576], ['id', 19842]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.52116858959198, 0.5009801387786865, 0.483667254447937, 0.427392840385437, 0.4253549575805664, 0.4216667413711548, 0.4207803010940552, 0.4156605005264282, 0.4150432348251343, 0.4122580289840698]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.4560546875, 'crossentropy': 1.5959537029266357})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.53125, 'crossentropy': 1.3027336597442627})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.3199951648712158})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.357602834701538})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.2829444408416748})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.467664122581482})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.6865484714508057})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.8757728338241577})
store['active_learning_steps'][20]['training']['best_epoch']=5
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.6655, 'crossentropy': 1.3610322265625}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.5458984375, 'crossentropy': 1.326460361480713})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.065962791442871})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.0682339668273926})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.0294690132141113})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.0347074270248413})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.0040274858474731})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 0.999103307723999})
store['active_learning_steps'][20]['eval_training']['best_epoch']=7
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 17030], ['id', 30218], ['id', 31717], ['id', 16778], ['id', 27629], ['id', 36117], ['id', 36805], ['id', 10897], ['id', 32791], ['id', 57602]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.550258994102478, 0.5076613426208496, 0.48320984840393066, 0.47489088773727417, 0.4719315767288208, 0.4687694311141968, 0.4412287473678589, 0.44063127040863037, 0.4399665594100952, 0.4390339255332947]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.5166015625, 'crossentropy': 1.505939245223999})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 1.22813081741333})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.2560973167419434})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.2586876153945923})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.2868529558181763})
store['active_learning_steps'][21]['training']['best_epoch']=2
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.5875, 'crossentropy': 1.23503779296875}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.533203125, 'crossentropy': 1.3809547424316406})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.5537109375, 'crossentropy': 1.2673563957214355})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.5556640625, 'crossentropy': 1.2509262561798096})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.5498046875, 'crossentropy': 1.2550103664398193})
store['active_learning_steps'][21]['eval_training']['best_epoch']=3
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 38782], ['id', 54813], ['id', 18729], ['id', 32438], ['id', 57944], ['id', 4689], ['id', 53015], ['id', 38696], ['id', 35913], ['id', 42362]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3063820004463196, 0.298433780670166, 0.2974410057067871, 0.28434109687805176, 0.28251802921295166, 0.28217703104019165, 0.27762889862060547, 0.277249813079834, 0.2700597047805786, 0.26484155654907227]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.458984375, 'crossentropy': 1.5265295505523682})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.5546875, 'crossentropy': 1.2889089584350586})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.5712890625, 'crossentropy': 1.2791938781738281})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 1.3711276054382324})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.4565279483795166})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.6462385654449463})
store['active_learning_steps'][22]['training']['best_epoch']=3
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.5759, 'crossentropy': 1.291770703125}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.5283203125, 'crossentropy': 1.3356969356536865})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.5380859375, 'crossentropy': 1.213991403579712})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.5537109375, 'crossentropy': 1.1638023853302002})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.5439453125, 'crossentropy': 1.1670953035354614})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.5546875, 'crossentropy': 1.1341683864593506})
store['active_learning_steps'][22]['eval_training']['best_epoch']=5
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 7577], ['id', 52556], ['id', 54405], ['id', 46848], ['id', 15124], ['id', 13598], ['ood', 6832], ['id', 15357], ['id', 8196], ['id', 50829]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.31700271368026733, 0.315901517868042, 0.3068547248840332, 0.30657243728637695, 0.305716872215271, 0.2964296340942383, 0.2901850938796997, 0.28968721628189087, 0.2887924909591675, 0.28486210107803345]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.4970703125, 'crossentropy': 1.5393109321594238})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.5634765625, 'crossentropy': 1.2733228206634521})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.3807294368743896})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.2471647262573242})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.271312952041626})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.412942886352539})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.5084400177001953})
store['active_learning_steps'][23]['training']['best_epoch']=4
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.62, 'crossentropy': 1.305069140625}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.5283203125, 'crossentropy': 1.3068668842315674})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 1.1679764986038208})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.0956436395645142})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 1.0741605758666992})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.0796093940734863})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.0415191650390625})
store['active_learning_steps'][23]['eval_training']['best_epoch']=6
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 9692], ['id', 27863], ['id', 26160], ['ood', 18313], ['id', 4701], ['id', 35684], ['id', 25963], ['id', 2846], ['id', 52223], ['id', 35384]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.41179025173187256, 0.4072835445404053, 0.37256062030792236, 0.36648011207580566, 0.3591804504394531, 0.35758084058761597, 0.3571040630340576, 0.3566145896911621, 0.3534706234931946, 0.3513401746749878]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.5087890625, 'crossentropy': 1.5678355693817139})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 1.2243021726608276})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.2861515283584595})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.3180935382843018})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.3819966316223145})
store['active_learning_steps'][24]['training']['best_epoch']=2
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.6024, 'crossentropy': 1.2349728515625}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.5244140625, 'crossentropy': 1.3338582515716553})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.5693359375, 'crossentropy': 1.2669672966003418})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.5595703125, 'crossentropy': 1.2265300750732422})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.5546875, 'crossentropy': 1.215336799621582})
store['active_learning_steps'][24]['eval_training']['best_epoch']=4
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 46563], ['id', 3410], ['id', 50385], ['id', 4935], ['id', 70], ['id', 56380], ['id', 32176], ['ood', 51576], ['id', 37251], ['id', 1254]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.33085405826568604, 0.3123788833618164, 0.30311572551727295, 0.3017728328704834, 0.2941160202026367, 0.28050100803375244, 0.2793252468109131, 0.2780032157897949, 0.2775000333786011, 0.2764793634414673]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.466796875, 'crossentropy': 1.5066089630126953})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 1.2485231161117554})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.1617270708084106})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.2069652080535889})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.3198673725128174})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.3479509353637695})
store['active_learning_steps'][25]['training']['best_epoch']=3
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.6127, 'crossentropy': 1.2116265625}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.5087890625, 'crossentropy': 1.3242690563201904})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.5712890625, 'crossentropy': 1.2006888389587402})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 1.133401870727539})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.1157687902450562})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 1.1242841482162476})
store['active_learning_steps'][25]['eval_training']['best_epoch']=4
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 59638], ['id', 48480], ['id', 20477], ['id', 35583], ['id', 19209], ['id', 8879], ['id', 54078], ['id', 21368], ['id', 57087], ['id', 55459]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.30265694856643677, 0.29294800758361816, 0.29263579845428467, 0.2854653596878052, 0.281963586807251, 0.27444469928741455, 0.27320122718811035, 0.27296972274780273, 0.2698056697845459, 0.2686450481414795]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.572265625, 'crossentropy': 1.5198845863342285})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.133673906326294})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.1514559984207153})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.1631219387054443})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.208504557609558})
store['active_learning_steps'][26]['training']['best_epoch']=2
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.6576, 'crossentropy': 1.14996318359375}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 1.3641417026519775})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.2111101150512695})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.2510353326797485})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.190846562385559})
store['active_learning_steps'][26]['eval_training']['best_epoch']=4
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 23771], ['id', 25005], ['id', 3283], ['id', 3301], ['id', 42536], ['id', 4887], ['id', 59953], ['id', 19138], ['id', 28352], ['id', 36293]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.2756994962692261, 0.26539885997772217, 0.26286983489990234, 0.26212775707244873, 0.257232666015625, 0.2570066452026367, 0.25298070907592773, 0.2510274648666382, 0.24983489513397217, 0.24552381038665771]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.56640625, 'crossentropy': 1.4127476215362549})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.116647481918335})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.1465613842010498})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.2053183317184448})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.2898755073547363})
store['active_learning_steps'][27]['training']['best_epoch']=2
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.6513, 'crossentropy': 1.19905625}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.3616127967834473})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.2551710605621338})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.203700304031372})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.1925933361053467})
store['active_learning_steps'][27]['eval_training']['best_epoch']=4
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 26217], ['id', 13286], ['id', 7402], ['id', 52429], ['id', 40744], ['id', 38203], ['id', 48973], ['id', 22673], ['id', 38256], ['id', 49921]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.359011709690094, 0.35045021772384644, 0.3380216956138611, 0.33784765005111694, 0.3292832374572754, 0.32789433002471924, 0.32331418991088867, 0.32077503204345703, 0.31634968519210815, 0.3153519630432129]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.53125, 'crossentropy': 1.4610705375671387})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.2139474153518677})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.0929265022277832})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.1121282577514648})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.115464210510254})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.1925549507141113})
store['active_learning_steps'][28]['training']['best_epoch']=3
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.6604, 'crossentropy': 1.08522666015625}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.3514512777328491})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.196005940437317})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.101172924041748})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.0781711339950562})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.1154026985168457})
store['active_learning_steps'][28]['eval_training']['best_epoch']=4
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 39750], ['id', 23444], ['id', 2910], ['id', 59691], ['id', 12467], ['id', 18584], ['id', 11374], ['id', 26437], ['id', 30448], ['id', 58130]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.38851726055145264, 0.34614038467407227, 0.3319138288497925, 0.3258620500564575, 0.3169581890106201, 0.31289494037628174, 0.3127312660217285, 0.3042478561401367, 0.3040883541107178, 0.30393993854522705]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.5107421875, 'crossentropy': 1.4906480312347412})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.2317540645599365})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.175354242324829})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.1240248680114746})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.1534810066223145})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.2462314367294312})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.1985626220703125})
store['active_learning_steps'][29]['training']['best_epoch']=4
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.6266, 'crossentropy': 1.1729494140625}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 1.2685878276824951})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.1144520044326782})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.1118855476379395})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.1089414358139038})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.090721845626831})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.0566415786743164})
store['active_learning_steps'][29]['eval_training']['best_epoch']=6
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 20652], ['id', 6000], ['id', 48293], ['id', 33674], ['id', 51163], ['id', 19888], ['id', 38806], ['id', 28914], ['id', 32578], ['ood', 25975]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.46947360038757324, 0.4020618200302124, 0.40199387073516846, 0.39668744802474976, 0.3842524290084839, 0.380500853061676, 0.37751519680023193, 0.3747774362564087, 0.37243664264678955, 0.3704500198364258]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.5234375, 'crossentropy': 1.595641851425171})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.2335679531097412})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.2017722129821777})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.1564829349517822})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.1272263526916504})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.28959059715271})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.3052456378936768})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.379206657409668})
store['active_learning_steps'][30]['training']['best_epoch']=5
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.6757, 'crossentropy': 1.171178125}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 1.2802302837371826})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.0922131538391113})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.0333962440490723})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.0133771896362305})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.0065640211105347})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 0.9901177883148193})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 0.9854214191436768})
store['active_learning_steps'][30]['eval_training']['best_epoch']=7
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 43543], ['id', 36323], ['id', 56627], ['id', 32498], ['ood', 41352], ['id', 39272], ['id', 26588], ['id', 56978], ['id', 15716], ['id', 36120]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3857348561286926, 0.3792515993118286, 0.3738383650779724, 0.37116575241088867, 0.3497658967971802, 0.3495914936065674, 0.3495523929595947, 0.34398138523101807, 0.34315067529678345, 0.3373805284500122]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.4619140625, 'crossentropy': 1.5948388576507568})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.2391166687011719})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.1136728525161743})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.226424217224121})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.1122820377349854})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.1135401725769043})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.216111421585083})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.3143057823181152})
store['active_learning_steps'][31]['training']['best_epoch']=5
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.6651, 'crossentropy': 1.1837462890625}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 1.350074291229248})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.1386929750442505})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.0982418060302734})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.0675690174102783})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.0541176795959473})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.0307343006134033})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.0093287229537964})
store['active_learning_steps'][31]['eval_training']['best_epoch']=7
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 18913], ['id', 54352], ['id', 4821], ['id', 13384], ['id', 57507], ['id', 44743], ['id', 26174], ['id', 45010], ['id', 33781], ['id', 43943]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.44855499267578125, 0.43846559524536133, 0.43049824237823486, 0.42768967151641846, 0.4152268171310425, 0.41511452198028564, 0.41203057765960693, 0.4113168716430664, 0.40914857387542725, 0.4078092575073242]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.4775390625, 'crossentropy': 1.5015732049942017})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 1.2390719652175903})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.0882538557052612})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.1908628940582275})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.1736396551132202})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.171994924545288})
store['active_learning_steps'][32]['training']['best_epoch']=3
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.6687, 'crossentropy': 1.141273046875}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.298378348350525})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.211435079574585})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.1050739288330078})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.1170592308044434})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.1101324558258057})
store['active_learning_steps'][32]['eval_training']['best_epoch']=3
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 22224], ['id', 56635], ['id', 55855], ['id', 55157], ['id', 36674], ['id', 34042], ['id', 28159], ['id', 49008], ['id', 13482], ['id', 51328]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.33255159854888916, 0.3261321783065796, 0.31860435009002686, 0.30932366847991943, 0.3080958127975464, 0.30732834339141846, 0.30383574962615967, 0.30064868927001953, 0.29387640953063965, 0.2937476634979248]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.466796875, 'crossentropy': 1.6361089944839478})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 1.2557032108306885})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.1015334129333496})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.0965744256973267})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.1101555824279785})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.0636920928955078})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.2103228569030762})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.1140739917755127})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.1246063709259033})
store['active_learning_steps'][33]['training']['best_epoch']=6
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.6822, 'crossentropy': 1.09695166015625}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.247232437133789})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 0.9979994297027588})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 0.9806964993476868})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 0.9929527044296265})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 0.920386791229248})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 0.940720796585083})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 0.9260526895523071})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 0.9403367042541504})
store['active_learning_steps'][33]['eval_training']['best_epoch']=5
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 33141], ['id', 29147], ['ood', 53612], ['id', 28962], ['id', 4194], ['id', 29672], ['id', 18754], ['id', 5937], ['id', 19084], ['id', 55160]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.4591473340988159, 0.42800813913345337, 0.39624178409576416, 0.38740074634552, 0.3696100115776062, 0.3662036657333374, 0.3647765815258026, 0.3544321060180664, 0.34684526920318604, 0.3433818221092224]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.548828125, 'crossentropy': 1.4621789455413818})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.210827350616455})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.0729514360427856})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.0729236602783203})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.1011046171188354})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.110257863998413})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.1155359745025635})
store['active_learning_steps'][34]['training']['best_epoch']=4
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.6546, 'crossentropy': 1.11935966796875}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.5634765625, 'crossentropy': 1.3445802927017212})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.1159336566925049})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.0372140407562256})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.0493069887161255})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.034332275390625})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.0599178075790405})
store['active_learning_steps'][34]['eval_training']['best_epoch']=5
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 23684], ['id', 48964], ['id', 34744], ['id', 58583], ['id', 22069], ['id', 17079], ['id', 18183], ['id', 40487], ['id', 59981], ['id', 55576]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.34600865840911865, 0.33936119079589844, 0.3344975709915161, 0.3329315185546875, 0.33097243309020996, 0.3241475820541382, 0.31991255283355713, 0.3196333646774292, 0.3111923336982727, 0.31119048595428467]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.46484375, 'crossentropy': 1.4702658653259277})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.1402974128723145})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.0942693948745728})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.068228006362915})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.1401242017745972})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.1730133295059204})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.1386256217956543})
store['active_learning_steps'][35]['training']['best_epoch']=4
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.6782, 'crossentropy': 1.08409443359375}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.3367531299591064})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.127415418624878})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.066152572631836})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.013256549835205})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 0.9973847270011902})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.022937536239624})
store['active_learning_steps'][35]['eval_training']['best_epoch']=5
store['active_learning_steps'][35]['acquisition']={'indices': [['ood', 10259], ['id', 3294], ['id', 39395], ['id', 1630], ['id', 12994], ['id', 53412], ['id', 59012], ['id', 9445], ['id', 4135], ['id', 25738]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.3530690670013428, 0.3505786657333374, 0.3464154005050659, 0.3381538391113281, 0.3363380432128906, 0.3332747220993042, 0.33229219913482666, 0.3312692642211914, 0.3306180238723755, 0.3304572105407715]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.5185546875, 'crossentropy': 1.5113537311553955})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.217858076095581})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.20558762550354})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.097761631011963})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.1624267101287842})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.1344280242919922})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.1354864835739136})
store['active_learning_steps'][36]['training']['best_epoch']=4
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.6874, 'crossentropy': 1.11496962890625}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.3154178857803345})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.1538017988204956})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.0669519901275635})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.032440185546875})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.0363328456878662})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.011812686920166})
store['active_learning_steps'][36]['eval_training']['best_epoch']=6
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 37650], ['id', 25195], ['id', 44814], ['id', 27652], ['id', 40037], ['id', 51152], ['id', 32244], ['id', 14213], ['id', 18633], ['id', 7729]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.34286391735076904, 0.33332085609436035, 0.32328367233276367, 0.32181859016418457, 0.31957149505615234, 0.3165466785430908, 0.3118029832839966, 0.3111281394958496, 0.3095353841781616, 0.3088415861129761]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.5302734375, 'crossentropy': 1.4439293146133423})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.1304668188095093})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.0023057460784912})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 0.9723327159881592})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 0.9936325550079346})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.028993844985962})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.0145952701568604})
store['active_learning_steps'][37]['training']['best_epoch']=4
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.7042, 'crossentropy': 1.03555703125}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.3052983283996582})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.1044844388961792})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 0.9984153509140015})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 0.9677248001098633})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 0.9913654327392578})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 0.9632589221000671})
store['active_learning_steps'][37]['eval_training']['best_epoch']=6
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 31669], ['id', 49410], ['id', 24079], ['id', 11651], ['ood', 4928], ['id', 55098], ['ood', 28030], ['id', 3694], ['id', 40187], ['id', 31612]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3111886978149414, 0.3090088367462158, 0.30430901050567627, 0.30063390731811523, 0.29493582248687744, 0.2913259267807007, 0.2912571430206299, 0.29070615768432617, 0.28966301679611206, 0.28394389152526855]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.482421875, 'crossentropy': 1.5655860900878906})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.2269827127456665})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.0757042169570923})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.0626155138015747})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.095008373260498})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.048642635345459})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.0566723346710205})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.102339267730713})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.029283046722412})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.186692714691162})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.158125877380371})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.0663275718688965})
store['active_learning_steps'][38]['training']['best_epoch']=9
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.7175, 'crossentropy': 1.0841240234375}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.288327932357788})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0751760005950928})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.0111780166625977})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.0103535652160645})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 0.9346253871917725})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 0.9103101491928101})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 0.9162383079528809})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 0.906295895576477})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 0.9190483093261719})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 0.9050588607788086})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 0.9169007539749146})
store['active_learning_steps'][38]['eval_training']['best_epoch']=10
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 5355], ['id', 31204], ['id', 43054], ['id', 19088], ['id', 2211], ['id', 58777], ['id', 290], ['id', 55932], ['id', 26913], ['id', 28689]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.48978352546691895, 0.45103752613067627, 0.43126869201660156, 0.42579764127731323, 0.4251660108566284, 0.4226212501525879, 0.41790395975112915, 0.41649025678634644, 0.41643840074539185, 0.4148392677307129]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.5361328125, 'crossentropy': 1.4361670017242432})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.182870864868164})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.0078707933425903})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 0.9784380197525024})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 0.9883753061294556})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 0.8961162567138672})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 0.9541114568710327})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 0.946590781211853})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 0.9466625452041626})
store['active_learning_steps'][39]['training']['best_epoch']=6
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.7369, 'crossentropy': 0.94775712890625}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.3396353721618652})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.0551763772964478})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.0144695043563843})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 0.9545013308525085})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 0.9234232902526855})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 0.8945900201797485})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 0.8922204971313477})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 0.901803731918335})
store['active_learning_steps'][39]['eval_training']['best_epoch']=7
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 43346], ['id', 22495], ['ood', 43345], ['id', 37052], ['id', 29501], ['id', 58560], ['id', 22946], ['id', 14591], ['id', 8455], ['id', 23285]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.36379265785217285, 0.35435938835144043, 0.3538888692855835, 0.3535236120223999, 0.3503614664077759, 0.34823089838027954, 0.3476231098175049, 0.3458690643310547, 0.34466099739074707, 0.3424175977706909]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.501953125, 'crossentropy': 1.5114948749542236})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.1595481634140015})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.048701524734497})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 0.9134039878845215})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 0.943171501159668})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 0.9277721643447876})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 0.9415864944458008})
store['active_learning_steps'][40]['training']['best_epoch']=4
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.7148, 'crossentropy': 0.967970703125}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.3116283416748047})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.0968849658966064})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.0507742166519165})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 0.9758123159408569})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.0104929208755493})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 0.950747013092041})
store['active_learning_steps'][40]['eval_training']['best_epoch']=6
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 15021], ['id', 27015], ['id', 35924], ['id', 49763], ['id', 6176], ['id', 27238], ['id', 18094], ['id', 21346], ['id', 55912], ['id', 24622]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.2869664430618286, 0.2844673991203308, 0.27886396646499634, 0.276641309261322, 0.27574342489242554, 0.27208268642425537, 0.271528422832489, 0.27143198251724243, 0.26662081480026245, 0.26540082693099976]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.51953125, 'crossentropy': 1.4786555767059326})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.228363275527954})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.022179126739502})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 0.9897129535675049})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.026463508605957})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 0.9777791500091553})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.0141987800598145})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.1573302745819092})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.0320801734924316})
store['active_learning_steps'][41]['training']['best_epoch']=6
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.714, 'crossentropy': 1.013309765625}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.2923359870910645})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.0824880599975586})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.012450098991394})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 0.9785857200622559})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 0.9521165490150452})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 0.9527760148048401})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 0.9389427900314331})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 0.9542690515518188})
store['active_learning_steps'][41]['eval_training']['best_epoch']=7
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 33357], ['id', 25420], ['id', 37710], ['id', 24433], ['id', 29399], ['id', 53488], ['id', 53268], ['id', 32787], ['id', 27955], ['id', 19906]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4102027416229248, 0.4001927375793457, 0.39600449800491333, 0.37941330671310425, 0.37423253059387207, 0.3737219572067261, 0.3652564287185669, 0.3616371154785156, 0.3584376573562622, 0.3573802709579468]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.4755859375, 'crossentropy': 1.5030463933944702})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.1732633113861084})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.0456960201263428})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 0.9667425155639648})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 0.9636185169219971})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 0.9774004817008972})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 0.9639350771903992})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 0.946916937828064})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 0.9848835468292236})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.0577197074890137})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.1583009958267212})
store['active_learning_steps'][42]['training']['best_epoch']=8
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.6978, 'crossentropy': 1.0278685546875}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 1.2968459129333496})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.0695013999938965})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 0.9258406758308411})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 0.9691094160079956})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 0.8795654773712158})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 0.8720738887786865})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 0.8994021415710449})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 0.8523186445236206})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 0.9200766086578369})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 0.8607444763183594})
store['active_learning_steps'][42]['eval_training']['best_epoch']=8
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 44686], ['id', 55069], ['id', 5918], ['id', 55930], ['id', 34994], ['id', 10674], ['id', 55768], ['id', 25867], ['id', 14562], ['id', 41166]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4691309928894043, 0.46251559257507324, 0.4622792601585388, 0.45536577701568604, 0.44780516624450684, 0.44714999198913574, 0.44600969552993774, 0.445348858833313, 0.4298839569091797, 0.4297354221343994]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.4501953125, 'crossentropy': 1.5498919486999512})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.2802324295043945})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0585806369781494})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 0.9917287826538086})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 0.9802005290985107})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 0.9814111590385437})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 0.9408526420593262})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.0080230236053467})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.0422515869140625})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.0322540998458862})
store['active_learning_steps'][43]['training']['best_epoch']=7
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.7124, 'crossentropy': 0.9641294921875}
