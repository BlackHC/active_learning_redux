store = {}
store['timestamp']=1620924521
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=18']
store['commit']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['github_url']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=18
store['worker_id']=18
store['num_workers']=20
store['config']={'seed': 1261, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'evaluation_set_size': 100, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.2005574703216553})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.4250848293304443})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.841845989227295})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.6365866661071777})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6956, 'crossentropy': 2.0028982421875}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.1182928085327148})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.0871222019195557})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.075007677078247})
store['active_learning_steps'][0]['eval_training']['best_epoch']=3
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 15955], ['id', 1749], ['id', 6591], ['id', 3653], ['id', 2288], ['id', 58587], ['id', 27840], ['id', 51265], ['id', 48852], ['id', 17165]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.8905608654022217, 0.7984086275100708, 0.8214589357376099, 0.8298596143722534, 1.0260026454925537, 0.7738630771636963, 0.6704984903335571, 0.9101709127426147, 0.8513492345809937, 1.0405913591384888]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.2492260932922363})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.4736547470092773})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.4325332641601562})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.865902900695801})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6592, 'crossentropy': 2.03113046875}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.3885852098464966})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.222272515296936})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.2598657608032227})
store['active_learning_steps'][1]['eval_training']['best_epoch']=2
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 5499], ['id', 54131], ['id', 2002], ['id', 59889], ['id', 40163], ['id', 40376], ['id', 17985], ['id', 41078], ['id', 46553], ['id', 19983]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.529910683631897, 0.5616964101791382, 0.7346932888031006, 0.5373201370239258, 0.560797929763794, 0.867391049861908, 0.5830894708633423, 0.7709507346153259, 0.6475584506988525, 0.4654644727706909]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.3803998231887817})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.405578851699829})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.5557935237884521})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.714212417602539})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7922, 'crossentropy': 1.213729296875}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 0.9131168127059937})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 0.8631629347801208})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 0.8298903703689575})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 5477], ['id', 8787], ['id', 28219], ['id', 44927], ['id', 19904], ['id', 50724], ['id', 18930], ['id', 42070], ['ood', 29399], ['id', 25326]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5179530382156372, 0.4479631185531616, 0.44372549653053284, 0.4753526449203491, 0.7003322243690491, 0.332213819026947, 0.4080088138580322, 0.6045438647270203, 0.3970482349395752, 0.5294864773750305]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.9883248805999756})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.0686885118484497})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.195206880569458})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.2389799356460571})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.8343, 'crossentropy': 0.8942025390625}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.8359846472740173})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.7489025592803955})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.7297178506851196})
store['active_learning_steps'][3]['eval_training']['best_epoch']=3
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 45813], ['id', 24420], ['id', 50418], ['id', 6610], ['id', 16456], ['id', 26446], ['ood', 32096], ['id', 42951], ['id', 16941], ['id', 36761]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.49631601572036743, 0.41554147005081177, 0.5061287879943848, 0.5314612984657288, 0.4997771978378296, 0.3533952236175537, 0.22995281219482422, 0.4699859023094177, 0.4738568663597107, 0.3413397967815399]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9786412119865417})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.1457738876342773})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.2189993858337402})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.2632516622543335})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.8468, 'crossentropy': 0.84112109375}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8016073703765869})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.7148805856704712})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.7052443027496338})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 45452], ['id', 41255], ['id', 13380], ['id', 1030], ['id', 21015], ['id', 3520], ['id', 1702], ['id', 15853], ['id', 14716], ['id', 58536]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.4734281301498413, 0.5020155906677246, 0.49582213163375854, 0.5043667554855347, 0.3369625210762024, 0.3415343761444092, 0.4671342968940735, 0.3901423215866089, 0.3624505400657654, 0.3814147710800171]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8744009137153625})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9068915247917175})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.979982852935791})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.109762191772461})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8541, 'crossentropy': 0.7650708984375}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.7821884155273438})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.7064563632011414})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.6832373142242432})
store['active_learning_steps'][5]['eval_training']['best_epoch']=3
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 27418], ['id', 13259], ['id', 20032], ['id', 39079], ['id', 7437], ['id', 16692], ['id', 41900], ['id', 28407], ['ood', 3671], ['ood', 27643]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.4178532361984253, 0.5170965194702148, 0.39929521083831787, 0.4805261492729187, 0.5416101813316345, 0.5249747633934021, 0.4911922216415405, 0.45886754989624023, 0.43702924251556396, 0.268208384513855]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8061704635620117})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7530174255371094})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7785070538520813})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8242673873901367})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7777189016342163})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8889, 'crossentropy': 0.665603759765625}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7421345710754395})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.6287976503372192})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.5966529846191406})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.5453044176101685})
store['active_learning_steps'][6]['eval_training']['best_epoch']=4
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 14785], ['id', 50883], ['id', 52060], ['id', 15880], ['id', 51679], ['id', 48811], ['id', 57659], ['id', 45381], ['id', 21754], ['id', 6995]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.40994733572006226, 0.52190101146698, 0.4261054992675781, 0.378528892993927, 0.4899553656578064, 0.4559941291809082, 0.46499621868133545, 0.3813070058822632, 0.4248597025871277, 0.3188813030719757]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7997939586639404})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7698335647583008})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7646905779838562})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7132835388183594})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8308956623077393})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.9046500325202942})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.9208647012710571})
store['active_learning_steps'][7]['training']['best_epoch']=4
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.9053, 'crossentropy': 0.6075046875}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7338156700134277})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.5862454175949097})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5317673087120056})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.5329303741455078})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5016463398933411})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.5197256803512573})
store['active_learning_steps'][7]['eval_training']['best_epoch']=5
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 27359], ['id', 16879], ['id', 843], ['id', 24761], ['id', 16190], ['id', 14105], ['id', 14175], ['id', 13669], ['id', 29503], ['id', 10210]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.44719043374061584, 0.34685516357421875, 0.30109190940856934, 0.520344614982605, 0.4506279230117798, 0.6353570222854614, 0.4546147882938385, 0.519669234752655, 0.3901258707046509, 0.7239032983779907]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7560997605323792})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6307264566421509})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6392867565155029})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6600796580314636})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7606757879257202})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.9095, 'crossentropy': 0.563112255859375}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6868598461151123})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5618780851364136})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5124079585075378})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.4959253668785095})
store['active_learning_steps'][8]['eval_training']['best_epoch']=4
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 46316], ['id', 14679], ['id', 24062], ['id', 20111], ['id', 33678], ['id', 20183], ['id', 34822], ['id', 4955], ['id', 19886], ['id', 27641]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.376200795173645, 0.3178246021270752, 0.3931835889816284, 0.4231046438217163, 0.3127875328063965, 0.4301872253417969, 0.6236165761947632, 0.4164350628852844, 0.37336206436157227, 0.5640402436256409]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8242136836051941})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5804768800735474})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6594767570495605})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6848583221435547})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6929608583450317})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.9185, 'crossentropy': 0.507851904296875}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7110048532485962})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5830340385437012})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.525745689868927})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5179876089096069})
store['active_learning_steps'][9]['eval_training']['best_epoch']=4
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 56152], ['id', 49316], ['id', 39700], ['id', 18003], ['id', 8552], ['id', 56233], ['id', 24408], ['ood', 48879], ['id', 31287], ['id', 48260]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3067270517349243, 0.525140106678009, 0.586097776889801, 0.4197689890861511, 0.4873366951942444, 0.5343837141990662, 0.49947720766067505, 0.23801535367965698, 0.2211545705795288, 0.5880317091941833]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8452785015106201})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7019855380058289})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7086206674575806})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7087165117263794})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7218255996704102})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.899, 'crossentropy': 0.588991845703125}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.74288010597229})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6254903078079224})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.5847787857055664})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5379320383071899})
store['active_learning_steps'][10]['eval_training']['best_epoch']=4
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 59781], ['id', 56260], ['id', 33139], ['id', 54932], ['id', 16091], ['id', 26681], ['id', 39596], ['id', 53147], ['id', 43063], ['id', 53015]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3246958255767822, 0.3819964528083801, 0.28211790323257446, 0.4302191734313965, 0.3139030337333679, 0.37475329637527466, 0.32028257846832275, 0.34394967555999756, 0.2515982985496521, 0.2907562255859375]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8121947050094604})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6094410419464111})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6195809245109558})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6720423102378845})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6074314117431641})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6664959192276001})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6871468424797058})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6766214966773987})
store['active_learning_steps'][11]['training']['best_epoch']=5
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.9239, 'crossentropy': 0.542738232421875}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7294876575469971})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.48586153984069824})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.45905762910842896})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.43878814578056335})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.4219837188720703})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.43863222002983093})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.41807544231414795})
store['active_learning_steps'][11]['eval_training']['best_epoch']=7
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 22591], ['id', 12257], ['id', 21786], ['id', 52225], ['id', 29335], ['id', 16073], ['ood', 54842], ['id', 19148], ['id', 31200], ['id', 20861]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.7168558835983276, 0.5762664079666138, 0.7979803085327148, 0.4394215941429138, 0.5488075017929077, 0.5646266341209412, 0.2763841152191162, 0.6947185397148132, 0.18818598985671997, 0.6201428771018982]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7272005081176758})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5420345664024353})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5388690233230591})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5167747735977173})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5641634464263916})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5244211554527283})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6143302917480469})
store['active_learning_steps'][12]['training']['best_epoch']=4
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9307, 'crossentropy': 0.442156591796875}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.649840235710144})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4953865110874176})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.42522794008255005})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.40833884477615356})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4061647653579712})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.3896574378013611})
store['active_learning_steps'][12]['eval_training']['best_epoch']=6
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 27429], ['id', 27241], ['id', 57575], ['id', 18778], ['id', 3146], ['id', 57124], ['id', 32702], ['id', 32760], ['id', 59395], ['id', 47122]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6039060354232788, 0.4277542233467102, 0.5664169788360596, 0.47390496730804443, 0.5072540044784546, 0.4264053702354431, 0.5182529091835022, 0.4837971329689026, 0.431185781955719, 0.4710029363632202]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.820533037185669})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5552510023117065})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5297430753707886})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5406007170677185})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5473724007606506})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5611813068389893})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.9368, 'crossentropy': 0.430648095703125}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7823179960250854})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.541541337966919})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5175921320915222})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.433978796005249})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.41596242785453796})
store['active_learning_steps'][13]['eval_training']['best_epoch']=5
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 42673], ['id', 18487], ['id', 21894], ['id', 39942], ['id', 38626], ['id', 59158], ['id', 39508], ['id', 6930], ['id', 30600], ['id', 28136]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.3792842626571655, 0.33947092294692993, 0.4268709421157837, 0.5412142872810364, 0.4174083471298218, 0.41534289717674255, 0.28078556060791016, 0.5239045023918152, 0.27884525060653687, 0.38595908880233765]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.9444162845611572})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5849576592445374})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5576778650283813})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5444579124450684})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5695295333862305})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5997114181518555})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5840703845024109})
store['active_learning_steps'][14]['training']['best_epoch']=4
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9284, 'crossentropy': 0.46819111328125}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.765942394733429})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5013593435287476})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.4749468266963959})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.428050696849823})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4287596344947815})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.40432512760162354})
store['active_learning_steps'][14]['eval_training']['best_epoch']=6
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 31044], ['id', 19362], ['id', 46068], ['id', 20378], ['id', 51341], ['id', 42940], ['id', 51337], ['id', 12650], ['id', 39320], ['id', 30461]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.427407443523407, 0.40147602558135986, 0.6427532434463501, 0.45550060272216797, 0.38207411766052246, 0.3502671718597412, 0.42458367347717285, 0.5044049024581909, 0.47424280643463135, 0.5263640880584717]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8999079465866089})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5786678194999695})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5105242729187012})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5139074325561523})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4775746464729309})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5200492143630981})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5043066740036011})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.559481143951416})
store['active_learning_steps'][15]['training']['best_epoch']=5
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9407, 'crossentropy': 0.396852880859375}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.80025315284729})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.49237722158432007})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.42391979694366455})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.39530259370803833})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.36753275990486145})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.39647814631462097})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3721412122249603})
store['active_learning_steps'][15]['eval_training']['best_epoch']=5
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 55610], ['id', 5891], ['id', 37574], ['id', 57383], ['ood', 51231], ['id', 32341], ['id', 3720], ['id', 35102], ['id', 52092], ['id', 56106]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.39623355865478516, 0.5324710607528687, 0.5040888786315918, 0.44648098945617676, 0.3593103885650635, 0.4881686568260193, 0.26701468229293823, 0.27111417055130005, 0.5025426149368286, 0.3326643705368042]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8668049573898315})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5231646299362183})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.48549455404281616})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4665710926055908})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.46046510338783264})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5114779472351074})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4696914553642273})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.49997615814208984})
store['active_learning_steps'][16]['training']['best_epoch']=5
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9453, 'crossentropy': 0.3937397216796875}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7108500003814697})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.47791212797164917})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.43044018745422363})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.3896059989929199})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3897968828678131})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3775599002838135})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.35978466272354126})
store['active_learning_steps'][16]['eval_training']['best_epoch']=7
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 27458], ['id', 4458], ['id', 39031], ['id', 52138], ['id', 53029], ['id', 29], ['ood', 29304], ['id', 1674], ['id', 59458], ['id', 21040]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.39732784032821655, 0.3597724139690399, 0.4105399250984192, 0.5505857467651367, 0.451002299785614, 0.4946601390838623, 0.33608198165893555, 0.49396008253097534, 0.3527930974960327, 0.6044981479644775]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.9152239561080933})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5396295785903931})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4748201072216034})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.47445547580718994})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4641580581665039})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5450091361999512})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.485562801361084})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5233072638511658})
store['active_learning_steps'][17]['training']['best_epoch']=5
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9398, 'crossentropy': 0.419596875}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8351012468338013})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5400383472442627})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.420046865940094})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4138963520526886})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4087744951248169})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.39447087049484253})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.40712153911590576})
store['active_learning_steps'][17]['eval_training']['best_epoch']=6
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 5684], ['id', 35740], ['id', 54002], ['id', 9971], ['id', 27153], ['id', 33048], ['id', 53344], ['id', 31664], ['id', 48594], ['id', 59418]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4120694398880005, 0.419921875, 0.4504539370536804, 0.21681097149848938, 0.6175835728645325, 0.5261297225952148, 0.5747756361961365, 0.5015349388122559, 0.5081324875354767, 0.5673315525054932]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.9208081960678101})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5559342503547668})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4562613368034363})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.41968148946762085})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4278312921524048})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4215366244316101})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.46655964851379395})
store['active_learning_steps'][18]['training']['best_epoch']=4
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9443, 'crossentropy': 0.381024072265625}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6851521730422974})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4915492832660675})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.40416476130485535})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4127602279186249})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3917524516582489})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3974442481994629})
store['active_learning_steps'][18]['eval_training']['best_epoch']=5
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 27765], ['id', 54618], ['id', 24940], ['id', 50343], ['id', 45944], ['id', 8532], ['id', 9330], ['id', 32323], ['id', 16799], ['id', 42645]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.41175031661987305, 0.3137216567993164, 0.23313775658607483, 0.4528365135192871, 0.40030884742736816, 0.30769872665405273, 0.2642691433429718, 0.3324010372161865, 0.39408522844314575, 0.37245064973831177]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.8803178071975708})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.49676060676574707})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.44982242584228516})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.40700632333755493})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.38272625207901})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.43137359619140625})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3969670832157135})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4751596450805664})
store['active_learning_steps'][19]['training']['best_epoch']=5
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9511, 'crossentropy': 0.3498099853515625}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7193081974983215})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.46677452325820923})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.39962857961654663})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3726557493209839})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.349203497171402})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3463331460952759})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.36684906482696533})
store['active_learning_steps'][19]['eval_training']['best_epoch']=6
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 20905], ['id', 30452], ['id', 45658], ['id', 37347], ['id', 38920], ['id', 53470], ['id', 20660], ['id', 46610], ['id', 49014], ['id', 49545]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.3176913261413574, 0.4955430030822754, 0.4155198335647583, 0.4511246085166931, 0.583423376083374, 0.4487913250923157, 0.3946567177772522, 0.4724544882774353, 0.3589639663696289, 0.5588393211364746]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9350516200065613})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5247468948364258})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.41245976090431213})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.40728527307510376})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4335404336452484})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.43104633688926697})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.41460296511650085})
store['active_learning_steps'][20]['training']['best_epoch']=4
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.949, 'crossentropy': 0.362316357421875}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7498122453689575})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5030113458633423})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4034663736820221})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4280549883842468})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.39434996247291565})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3650171756744385})
store['active_learning_steps'][20]['eval_training']['best_epoch']=6
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 7788], ['id', 11877], ['id', 44753], ['id', 19423], ['id', 36471], ['id', 37588], ['id', 22529], ['id', 37062], ['id', 26206], ['id', 29388]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.35568541288375854, 0.36895430088043213, 0.4077087640762329, 0.44798195362091064, 0.30846986174583435, 0.3730306029319763, 0.3318467140197754, 0.3240475654602051, 0.40122997760772705, 0.3984006643295288]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9611653089523315})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.489658921957016})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.42507317662239075})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.38980352878570557})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.40201205015182495})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.408428430557251})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.43268123269081116})
store['active_learning_steps'][21]['training']['best_epoch']=4
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9487, 'crossentropy': 0.3466226806640625}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6707175970077515})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4572726786136627})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.37254926562309265})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3600519299507141})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3581858277320862})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3627157211303711})
store['active_learning_steps'][21]['eval_training']['best_epoch']=5
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 8093], ['id', 30660], ['id', 37672], ['id', 26635], ['ood', 15523], ['ood', 28686], ['id', 19988], ['id', 36126], ['id', 58050], ['id', 6130]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.486034095287323, 0.4065679907798767, 0.5012444257736206, 0.3936845064163208, 0.4675877094268799, 0.4151867628097534, 0.4696686267852783, 0.4950227737426758, 0.46589064598083496, 0.4282470941543579]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9386205673217773})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4838724434375763})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4236885607242584})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4025786519050598})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.37417006492614746})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.37791815400123596})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.36953943967819214})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4193938970565796})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4008214473724365})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4209716320037842})
store['active_learning_steps'][22]['training']['best_epoch']=7
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9521, 'crossentropy': 0.345448388671875}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7287377119064331})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.46370595693588257})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3728567063808441})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.36729612946510315})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3296147882938385})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.31870195269584656})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3307022452354431})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.2930893301963806})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.30587977170944214})
store['active_learning_steps'][22]['eval_training']['best_epoch']=8
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 11611], ['ood', 4194], ['id', 943], ['id', 50461], ['id', 35256], ['id', 38165], ['id', 43560], ['id', 58470], ['id', 2554], ['id', 45623]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.3401695489883423, 0.23513329029083252, 0.3142508864402771, 0.5747191905975342, 0.5712562799453735, 0.5882411003112793, 0.6639769077301025, 0.6841772198677063, 0.305895060300827, 0.3727043867111206]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8825158476829529})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4910755753517151})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4470232129096985})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3699849843978882})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3901563286781311})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3610888123512268})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3735010027885437})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.39385682344436646})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.42785534262657166})
store['active_learning_steps'][23]['training']['best_epoch']=6
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9558, 'crossentropy': 0.3216217529296875}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7527236342430115})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5098540186882019})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3693877160549164})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3698035478591919})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.32064932584762573})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3106963038444519})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.2936939597129822})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2853783965110779})
store['active_learning_steps'][23]['eval_training']['best_epoch']=8
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 55782], ['id', 56130], ['id', 7606], ['id', 55612], ['id', 27085], ['id', 12764], ['id', 45069], ['id', 19866], ['id', 30806], ['id', 54082]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.3416614830493927, 0.3238636255264282, 0.43591415882110596, 0.6222775280475616, 0.42922648787498474, 0.4421447515487671, 0.5509902834892273, 0.3875564932823181, 0.5241122245788574, 0.4529111385345459]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9222657680511475})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5602218508720398})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4588056802749634})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3774048984050751})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4051777720451355})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.39226293563842773})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3810528516769409})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9497, 'crossentropy': 0.3457872314453125}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7941481471061707})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5027533173561096})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4189731180667877})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3724666237831116})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3911750912666321})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3518204391002655})
store['active_learning_steps'][24]['eval_training']['best_epoch']=6
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 7833], ['id', 47946], ['id', 21204], ['id', 20072], ['id', 15019], ['id', 46626], ['id', 9290], ['ood', 49748], ['id', 10800], ['id', 48382]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5724753141403198, 0.34116291999816895, 0.4571816325187683, 0.48236405849456787, 0.2713742256164551, 0.4583318829536438, 0.4459889531135559, 0.22858858108520508, 0.38223063945770264, 0.4200142025947571]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.1164271831512451})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5702581405639648})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.48828792572021484})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.40852367877960205})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.39315083622932434})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.40621650218963623})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3888118267059326})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4092528820037842})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.409266859292984})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.37544751167297363})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3633788824081421})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.37834110856056213})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.39302879571914673})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3911733031272888})
store['active_learning_steps'][25]['training']['best_epoch']=11
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9608, 'crossentropy': 0.3267080078125}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8725889921188354})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.49369239807128906})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4111899733543396})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.36029577255249023})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.35141485929489136})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3098188042640686})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.31148403882980347})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3011833429336548})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.2991223931312561})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.28779274225234985})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.31822872161865234})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2863010764122009})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3094058632850647})
store['active_learning_steps'][25]['eval_training']['best_epoch']=12
store['active_learning_steps'][25]['acquisition']={'indices': [['ood', 15971], ['ood', 19044], ['ood', 2407], ['id', 57741], ['id', 43110], ['ood', 35662], ['id', 29162], ['id', 9550], ['id', 32047], ['id', 34902]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.33640551567077637, 0.25275397300720215, 0.40802276134490967, 0.45680516958236694, 0.5911991000175476, 0.42000019550323486, 0.48073649406433105, 0.38958120346069336, 0.5748445987701416, 0.49099504947662354]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.0217525959014893})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5256379842758179})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4179549813270569})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3574768602848053})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3536154627799988})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3817625641822815})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3589245676994324})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3528885245323181})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3726636469364166})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.39393287897109985})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.39091745018959045})
store['active_learning_steps'][26]['training']['best_epoch']=8
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9549, 'crossentropy': 0.3294174072265625}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.8182429075241089})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.43851593136787415})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3699837923049927})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.34291893243789673})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.31076228618621826})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.29939383268356323})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3027161657810211})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.30624544620513916})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3076801300048828})
store['active_learning_steps'][26]['eval_training']['best_epoch']=6
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 14881], ['id', 52644], ['id', 57270], ['ood', 22752], ['id', 9433], ['id', 13253], ['ood', 59506], ['id', 20549], ['id', 18580], ['id', 57767]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.3440297842025757, 0.5114811658859253, 0.33813780546188354, 0.4813544750213623, 0.5895523428916931, 0.5288296937942505, 0.3624882698059082, 0.42204684019088745, 0.48262202739715576, 0.311694860458374]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.139817714691162})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.52870112657547})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.42255768179893494})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3934476971626282})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4222679138183594})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.34102073311805725})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.34914058446884155})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.34351593255996704})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3417130708694458})
store['active_learning_steps'][27]['training']['best_epoch']=6
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.952, 'crossentropy': 0.3358460693359375}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7793519496917725})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5136279463768005})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3898751139640808})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3477283716201782})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3587765097618103})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3369779586791992})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3544524312019348})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3085775673389435})
store['active_learning_steps'][27]['eval_training']['best_epoch']=8
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 52981], ['id', 50424], ['id', 43393], ['id', 43045], ['id', 49859], ['id', 29310], ['id', 15701], ['id', 8780], ['id', 14635], ['id', 48507]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.40954655408859253, 0.3785512447357178, 0.43689265847206116, 0.5236726999282837, 0.42534154653549194, 0.5804571807384491, 0.518322229385376, 0.4381486773490906, 0.5347653031349182, 0.5698899626731873]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.989859938621521})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5109769701957703})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3997234106063843})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.34064096212387085})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3583400845527649})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.328980952501297})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3251376152038574})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.326213002204895})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3317359685897827})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.39520296454429626})
store['active_learning_steps'][28]['training']['best_epoch']=7
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9597, 'crossentropy': 0.2981651123046875}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9050880670547485})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.514904260635376})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4238051772117615})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.355032742023468})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3364604711532593})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.29843857884407043})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3181818723678589})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3092930316925049})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3051597476005554})
store['active_learning_steps'][28]['eval_training']['best_epoch']=6
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 15202], ['id', 24984], ['id', 32926], ['id', 42383], ['id', 41507], ['id', 44889], ['id', 35537], ['id', 47506], ['id', 56518], ['id', 37994]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.4238318204879761, 0.6746981143951416, 0.24878281354904175, 0.38628292083740234, 0.3624882698059082, 0.5278440713882446, 0.44885265827178955, 0.42001861333847046, 0.3875770568847656, 0.5887952744960785]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.0840132236480713})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5401233434677124})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.428096204996109})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.36077725887298584})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3195829391479492})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.29998284578323364})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2955295145511627})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.31991612911224365})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3028893768787384})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31198519468307495})
store['active_learning_steps'][29]['training']['best_epoch']=7
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9588, 'crossentropy': 0.29995517578125}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.8013817071914673})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4546175003051758})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.40930426120758057})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3299851417541504})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.304865300655365})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3084988594055176})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2954367697238922})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2608957886695862})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.28186386823654175})
store['active_learning_steps'][29]['eval_training']['best_epoch']=8
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 28757], ['id', 16019], ['id', 51759], ['id', 134], ['id', 8690], ['id', 49438], ['id', 50639], ['id', 3388], ['id', 47674], ['id', 30214]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.45070749521255493, 0.42602694034576416, 0.4729411005973816, 0.3772658705711365, 0.25868648290634155, 0.38379180431365967, 0.46918588876724243, 0.4335790276527405, 0.38837382197380066, 0.4506893754005432]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.2391300201416016})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5511176586151123})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.42293357849121094})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3449908494949341})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3530532121658325})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.32009899616241455})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.29991328716278076})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3141041100025177})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3274998664855957})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.309105783700943})
store['active_learning_steps'][30]['training']['best_epoch']=7
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9591, 'crossentropy': 0.30695263671875}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8936158418655396})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4191276729106903})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3889533281326294})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.34639692306518555})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3070630729198456})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3205351233482361})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2728850841522217})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2722524404525757})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2540578842163086})
store['active_learning_steps'][30]['eval_training']['best_epoch']=9
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 44127], ['id', 15068], ['id', 51416], ['id', 5086], ['id', 29623], ['id', 24864], ['id', 44109], ['id', 10496], ['id', 9441], ['id', 53979]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.35199278593063354, 0.41550612449645996, 0.29489779472351074, 0.392707496881485, 0.43966564536094666, 0.4049533009529114, 0.34279727935791016, 0.17681844532489777, 0.2602476626634598, 0.5422011017799377]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.070173978805542})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5636463165283203})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3848007917404175})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.325090229511261})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.31793731451034546})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3271881937980652})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34081363677978516})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3130567669868469})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3134014904499054})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.31249433755874634})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3254956007003784})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3400285840034485})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.34697726368904114})
store['active_learning_steps'][31]['training']['best_epoch']=10
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9645, 'crossentropy': 0.283429736328125}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.8366179466247559})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.439545214176178})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4246484637260437})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.32822003960609436})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3132120370864868})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2883259952068329})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.2888670563697815})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.2869740128517151})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.28171640634536743})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2793596386909485})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2500535845756531})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2587619721889496})
store['active_learning_steps'][31]['eval_training']['best_epoch']=11
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 22607], ['id', 4276], ['id', 52095], ['id', 30], ['id', 14878], ['id', 41537], ['id', 52135], ['id', 5110], ['id', 38642], ['id', 14242]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.4937094449996948, 0.34854817390441895, 0.47150564193725586, 0.35125118494033813, 0.6066188216209412, 0.4445022940635681, 0.39174550771713257, 0.3939023017883301, 0.3647787868976593, 0.3713875114917755]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.9579468369483948})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5182176828384399})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3502618074417114})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3369465470314026})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3076362907886505})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3350636065006256})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3309496343135834})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2996203303337097})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3112185597419739})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3272508978843689})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30802446603775024})
store['active_learning_steps'][32]['training']['best_epoch']=8
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9638, 'crossentropy': 0.3001715576171875}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8914324641227722})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.46546345949172974})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4275325536727905})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3464573919773102})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.2873656749725342})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2931321859359741})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3074130713939667})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.25881069898605347})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.268593966960907})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.26276570558547974})
store['active_learning_steps'][32]['eval_training']['best_epoch']=8
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 15366], ['id', 749], ['id', 29343], ['id', 12637], ['id', 8480], ['id', 36486], ['id', 19034], ['id', 39734], ['id', 59719], ['id', 47609]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4650155007839203, 0.5771248638629913, 0.35337501764297485, 0.3692605495452881, 0.593782365322113, 0.403584748506546, 0.44366639852523804, 0.5149164497852325, 0.5132325291633606, 0.463062584400177]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9789896011352539})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.501140832901001})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3888416290283203})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.325714111328125})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.27401092648506165})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31295478343963623})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.290105402469635})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32337984442710876})
store['active_learning_steps'][33]['training']['best_epoch']=5
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9649, 'crossentropy': 0.2643192138671875}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8094817399978638})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.420585572719574})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4105112552642822})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3398231863975525})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3164188861846924})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.31593289971351624})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.29521238803863525})
store['active_learning_steps'][33]['eval_training']['best_epoch']=7
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 32108], ['id', 26405], ['id', 43648], ['id', 6466], ['id', 55598], ['id', 19888], ['id', 48352], ['ood', 17509], ['id', 24533], ['id', 13878]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.39917927980422974, 0.3862786293029785, 0.37715065479278564, 0.35703957080841064, 0.30679619312286377, 0.42073261737823486, 0.2899325489997864, 0.23093390464782715, 0.4955640435218811, 0.3844078779220581]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.0157723426818848})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5181528925895691})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4055156409740448})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.35146528482437134})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3059435486793518})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3037073016166687})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3368603587150574})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31107938289642334})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.306793212890625})
store['active_learning_steps'][34]['training']['best_epoch']=6
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9644, 'crossentropy': 0.2785933837890625}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.8229178786277771})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5286751389503479})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4020220637321472})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.35305291414260864})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.34569603204727173})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3087899684906006})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2829858064651489})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3109402060508728})
store['active_learning_steps'][34]['eval_training']['best_epoch']=7
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 52968], ['id', 24740], ['id', 23946], ['id', 12273], ['id', 52892], ['id', 15803], ['id', 47291], ['id', 46869], ['id', 26338], ['id', 41549]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.4816098213195801, 0.4449796676635742, 0.3377171754837036, 0.4715961217880249, 0.4137887954711914, 0.33786261081695557, 0.42221248149871826, 0.26294541358947754, 0.2556955814361572, 0.3977263569831848]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.0786281824111938})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5252755880355835})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4368915557861328})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.332624614238739})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32017719745635986})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3190014958381653})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30839431285858154})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3078113794326782})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3106156885623932})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.27474698424339294})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2914432883262634})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3247525691986084})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3284150958061218})
store['active_learning_steps'][35]['training']['best_epoch']=10
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.967, 'crossentropy': 0.2611757080078125}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.9262096881866455})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5006025433540344})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.38166695833206177})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3367028832435608})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.32035934925079346})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2951733469963074})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.26444923877716064})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.27237898111343384})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.27197372913360596})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2795579731464386})
store['active_learning_steps'][35]['eval_training']['best_epoch']=7
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 58468], ['id', 54994], ['id', 52456], ['id', 4694], ['id', 2148], ['id', 39016], ['id', 47056], ['id', 46274], ['ood', 34963], ['id', 16846]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.3197065591812134, 0.5825789570808411, 0.4470368027687073, 0.41301989555358887, 0.4942689538002014, 0.4493405222892761, 0.4093260169029236, 0.440102219581604, 0.3740473985671997, 0.28656771779060364]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.078477382659912})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5941243171691895})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.40879935026168823})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.356149822473526})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.30990660190582275})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.31418371200561523})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.35201236605644226})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3403763771057129})
store['active_learning_steps'][36]['training']['best_epoch']=5
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.961, 'crossentropy': 0.3082604248046875}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7984194755554199})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5214531421661377})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.40451258420944214})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3804965019226074})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3648190498352051})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3384827971458435})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3479216992855072})
store['active_learning_steps'][36]['eval_training']['best_epoch']=6
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 21880], ['id', 40466], ['id', 31428], ['id', 12692], ['id', 7972], ['id', 22561], ['id', 3941], ['id', 12744], ['id', 54520], ['id', 14664]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.47439026832580566, 0.5264193415641785, 0.44978606700897217, 0.4643893241882324, 0.47383660078048706, 0.4195801615715027, 0.4375743269920349, 0.5592771172523499, 0.43713176250457764, 0.37110352516174316]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.0549087524414062})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.538560152053833})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4247196912765503})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33441340923309326})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3129591643810272})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3132449984550476})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3006586730480194})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3224759101867676})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30552220344543457})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.30532005429267883})
store['active_learning_steps'][37]['training']['best_epoch']=7
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9656, 'crossentropy': 0.2825800048828125}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.8474230766296387})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4991922676563263})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3643859624862671})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34252434968948364})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3408152461051941})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31661152839660645})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3209172189235687})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2886883616447449})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29695773124694824})
store['active_learning_steps'][37]['eval_training']['best_epoch']=8
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 36744], ['id', 39286], ['id', 57732], ['id', 12236], ['id', 42828], ['id', 46412], ['id', 42088], ['id', 6291], ['id', 33338], ['id', 22404]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.49388575553894043, 0.44448745250701904, 0.43477946519851685, 0.41005492210388184, 0.5143159627914429, 0.38462376594543457, 0.5548148155212402, 0.5145031809806824, 0.4332597851753235, 0.42579323053359985]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 1.003666877746582})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.49471911787986755})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4356513023376465})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.32790607213974})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.289775013923645})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2982153594493866})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28202348947525024})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2929394245147705})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3161376118659973})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30437421798706055})
store['active_learning_steps'][38]['training']['best_epoch']=7
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9666, 'crossentropy': 0.291986474609375}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.9634238481521606})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5301458835601807})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.43442678451538086})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3626314401626587})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3380252718925476})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3391960859298706})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3442689776420593})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2901481091976166})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2848219871520996})
store['active_learning_steps'][38]['eval_training']['best_epoch']=9
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 8112], ['id', 670], ['id', 29669], ['id', 1909], ['id', 15832], ['id', 40315], ['id', 34824], ['id', 29530], ['id', 22320], ['id', 33150]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.2916821241378784, 0.4545670747756958, 0.4727681875228882, 0.3376590609550476, 0.5820418000221252, 0.41116660833358765, 0.23325204849243164, 0.4931759238243103, 0.36372625827789307, 0.44100630283355713]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.1195039749145508})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5708489418029785})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4111936688423157})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35943686962127686})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.319786012172699})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2890340983867645})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28472763299942017})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30850741267204285})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2916564345359802})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28131017088890076})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2800181210041046})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.30240046977996826})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.33580589294433594})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31759580969810486})
store['active_learning_steps'][39]['training']['best_epoch']=11
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9689, 'crossentropy': 0.248424609375}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8505837917327881})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5099692940711975})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3416680097579956})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3357711434364319})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2778553366661072})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2914557158946991})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.25913089513778687})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.23140333592891693})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.23348942399024963})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.23939242959022522})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.23151564598083496})
store['active_learning_steps'][39]['eval_training']['best_epoch']=8
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 7620], ['id', 414], ['id', 19590], ['id', 54738], ['id', 3227], ['id', 6983], ['id', 2406], ['ood', 48747], ['id', 11864], ['id', 31591]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.38036829233169556, 0.49027156829833984, 0.3694912791252136, 0.43534839153289795, 0.285836398601532, 0.28946954011917114, 0.35879969596862793, 0.16833341121673584, 0.18854528665542603, 0.4293810725212097]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.1626673936843872})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.547781229019165})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3816150426864624})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3703254461288452})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3148508369922638})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2681810259819031})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.26722097396850586})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.299973726272583})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.24498595297336578})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2975625693798065})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27744731307029724})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.262116402387619})
store['active_learning_steps'][40]['training']['best_epoch']=9
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9697, 'crossentropy': 0.246257080078125}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 1.0004141330718994})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4929105341434479})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4095025360584259})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33058929443359375})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31787025928497314})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3005855679512024})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2849549651145935})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.30802541971206665})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.26379692554473877})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2580036520957947})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2663690447807312})
store['active_learning_steps'][40]['eval_training']['best_epoch']=10
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 50757], ['id', 8853], ['id', 43478], ['id', 8771], ['id', 10149], ['id', 47949], ['id', 51164], ['id', 13376], ['id', 55804], ['id', 52938]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4794546961784363, 0.48962509632110596, 0.3009289503097534, 0.439935564994812, 0.42436081171035767, 0.4335021376609802, 0.32242801785469055, 0.5491666197776794, 0.44463253021240234, 0.33559364080429077]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 1.25527024269104})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5864416360855103})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.39962828159332275})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31612271070480347})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.28021788597106934})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2827393114566803})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2620353102684021})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2886735200881958})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2729344069957733})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3007490634918213})
store['active_learning_steps'][41]['training']['best_epoch']=7
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9726, 'crossentropy': 0.2238841552734375}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.9698768854141235})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5252199769020081})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.427615225315094})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3192524313926697})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3230303227901459})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33228617906570435})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27320724725723267})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27349159121513367})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27919071912765503})
store['active_learning_steps'][41]['eval_training']['best_epoch']=7
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 36234], ['id', 15771], ['id', 7250], ['ood', 40100], ['id', 43212], ['id', 7741], ['id', 46021], ['id', 44157], ['id', 35654], ['id', 41772]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3543030023574829, 0.436168909072876, 0.30506837368011475, 0.16242074966430664, 0.4357321262359619, 0.3115346431732178, 0.38687849044799805, 0.36411070823669434, 0.32480698823928833, 0.5636926889419556]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 1.0501681566238403})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5419588685035706})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.39258959889411926})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3244740962982178})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.315791517496109})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2986758351325989})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2850843071937561})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2757546901702881})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2691355347633362})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2836769223213196})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2656428813934326})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2704167664051056})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2953431010246277})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2693280577659607})
store['active_learning_steps'][42]['training']['best_epoch']=11
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9722, 'crossentropy': 0.2331105224609375}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.882390022277832})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.518623948097229})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.37482208013534546})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.33939915895462036})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.307009220123291})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3166729807853699})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.29723918437957764})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2879328727722168})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2562142014503479})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2543207108974457})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.23193109035491943})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.23674239218235016})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.24178017675876617})
store['active_learning_steps'][42]['eval_training']['best_epoch']=11
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 16022], ['id', 14769], ['id', 40575], ['id', 55244], ['id', 18682], ['id', 27576], ['id', 52086], ['id', 32573], ['id', 34771], ['id', 46815]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5739113688468933, 0.6211178600788116, 0.42087703943252563, 0.4556754231452942, 0.37923377752304077, 0.4882286787033081, 0.4332621693611145, 0.5474714040756226, 0.3855028450489044, 0.5515499711036682]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.0977082252502441})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5760658979415894})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.390532910823822})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.35230931639671326})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3097033202648163})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2884541153907776})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.27382683753967285})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.27625197172164917})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2766823470592499})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.30596649646759033})
store['active_learning_steps'][43]['training']['best_epoch']=7
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9721, 'crossentropy': 0.248842041015625}
