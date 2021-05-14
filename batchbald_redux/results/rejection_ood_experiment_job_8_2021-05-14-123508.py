store = {}
store['timestamp']=1620992108
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=8']
store['commit']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['github_url']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=8
store['worker_id']=8
store['num_workers']=20
store['config']={'seed': 1246, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'evaluation_set_size': 100, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.2311999797821045})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.5560708045959473})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.9476380348205566})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.904122829437256})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.666, 'crossentropy': 2.0965587890625}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.2180712223052979})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.2589911222457886})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.182807445526123})
store['active_learning_steps'][0]['eval_training']['best_epoch']=3
store['active_learning_steps'][0]['acquisition']={'indices': [23385, 18324, 38256, 42529, 36244, 18319, 43004, 59762, 54136, 22583], 'labels': [5, 0, 2, 9, 5, 0, 8, 0, 8, 0], 'scores': [0.8478955626487732, 0.7152653932571411, 1.078869879245758, 0.890139639377594, 0.6567435264587402, 0.9122172594070435, 0.9169836640357971, 0.7955865859985352, 0.7825059294700623, 0.9583637118339539]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.239664077758789})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.5596702098846436})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.54530930519104})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.7758278846740723})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6533, 'crossentropy': 2.1214759765625}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.2918610572814941})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.2552626132965088})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.2432045936584473})
store['active_learning_steps'][1]['eval_training']['best_epoch']=3
store['active_learning_steps'][1]['acquisition']={'indices': [35517, 7886, 4167, 5696, 15543, 21375, 57396, 45319, 5536, 39683], 'labels': [6, 9, 5, 8, 4, 8, 3, 2, 8, 0], 'scores': [0.6569660902023315, 0.5761302709579468, 0.6956197619438171, 0.6704435348510742, 0.5242828726768494, 0.5888969302177429, 0.7217930555343628, 0.6882826685905457, 0.5022568702697754, 0.6895986795425415]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.5780695676803589})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.9037861824035645})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 2.087010383605957})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.724964141845703})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7394, 'crossentropy': 1.44771328125}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.1609011888504028})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.0037022829055786})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 0.9852532148361206})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [45415, 35152, 50134, 53540, 36076, 10153, 45657, 49213, 48103, 37721], 'labels': [9, 4, 4, 6, 3, 4, 7, 9, 4, 8], 'scores': [0.5080238580703735, 0.41643840074539185, 0.5048153400421143, 0.47166210412979126, 0.5231738686561584, 0.6083201766014099, 0.36510172486305237, 0.528830349445343, 0.5678384304046631, 0.3013477325439453]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.2546685934066772})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.636305332183838})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.575158953666687})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.8383169174194336})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7854, 'crossentropy': 1.1614359375}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.0136128664016724})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 0.8725882768630981})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 0.8866617679595947})
store['active_learning_steps'][3]['eval_training']['best_epoch']=2
store['active_learning_steps'][3]['acquisition']={'indices': [10994, 23500, 44988, 5474, 38119, 19590, 4729, 29852, 55064, 19545], 'labels': [3, 6, 1, 8, 8, 5, 0, 5, 9, 2], 'scores': [0.3395395874977112, 0.46240997314453125, 0.4515073299407959, 0.5902546644210815, 0.5623056888580322, 0.5272290706634521, 0.5052843689918518, 0.5294041633605957, 0.5968539118766785, 0.5728819966316223]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.240668773651123})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.458655834197998})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.435903549194336})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.5883426666259766})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7924, 'crossentropy': 1.126171875}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.8521032929420471})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 0.8346661329269409})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 0.8109056949615479})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [53475, 55153, 5408, 53873, 3707, 59525, 31930, 9736, 15795, 33015], 'labels': [3, 8, 3, 4, 3, 5, 1, 2, -1, 6], 'scores': [0.3711543679237366, 0.5384348034858704, 0.5123001337051392, 0.4900142550468445, 0.6491724252700806, 0.5059946179389954, 0.6177236437797546, 0.6013301014900208, 0.4419597387313843, 0.5836409330368042]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.0747854709625244})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.1232407093048096})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.2951183319091797})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.2980293035507202})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8218, 'crossentropy': 0.923340234375}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 0.8898539543151855})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.8067502975463867})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.8163701295852661})
store['active_learning_steps'][5]['eval_training']['best_epoch']=2
store['active_learning_steps'][5]['acquisition']={'indices': [1033, 43420, 31624, 10465, 20104, 10261, 17339, 44961, 44365, 20917], 'labels': [2, 6, 9, 5, 6, 0, 2, 8, 6, 2], 'scores': [0.40683841705322266, 0.4340301752090454, 0.5089153051376343, 0.3299652338027954, 0.3981395959854126, 0.43851393461227417, 0.44107842445373535, 0.5234053134918213, 0.4674469828605652, 0.4806280732154846]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 0.9999208450317383})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.0763859748840332})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.1525987386703491})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.454293966293335})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.81, 'crossentropy': 0.938815234375}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 0.8636527061462402})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 0.8411134481430054})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.828899621963501})
store['active_learning_steps'][6]['eval_training']['best_epoch']=3
store['active_learning_steps'][6]['acquisition']={'indices': [35417, 10193, 38895, 51736, 14100, 1392, 16079, 41488, 57376, 38613], 'labels': [7, 9, 6, 5, 5, 7, 7, 6, 7, 8], 'scores': [0.4927898645401001, 0.2631978988647461, 0.3637610673904419, 0.5234092473983765, 0.5362542271614075, 0.45686793327331543, 0.40143609046936035, 0.5226170420646667, 0.5097948312759399, 0.31603753566741943]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.9787576794624329})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.9673037528991699})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.1029211282730103})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.1759493350982666})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.2646645307540894})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8582, 'crossentropy': 0.8483787109375}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7979731559753418})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.6705451011657715})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.6304506063461304})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.6157275438308716})
store['active_learning_steps'][7]['eval_training']['best_epoch']=4
store['active_learning_steps'][7]['acquisition']={'indices': [51419, 14063, 8810, 33598, 20905, 55661, 31024, 24347, 45715, 14107], 'labels': [2, 2, 2, 5, 8, 5, 2, 2, 7, 3], 'scores': [0.6522026658058167, 0.6670295000076294, 0.6594025492668152, 0.46985477209091187, 0.4661833643913269, 0.39387190341949463, 0.5937736928462982, 0.5304205417633057, 0.570372462272644, 0.4612756371498108]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8380770087242126})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7381590008735657})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8338965773582458})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8079310655593872})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7810240983963013})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8842, 'crossentropy': 0.694161181640625}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7029516696929932})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.5712722539901733})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.5584638118743896})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.5350698232650757})
store['active_learning_steps'][8]['eval_training']['best_epoch']=4
store['active_learning_steps'][8]['acquisition']={'indices': [7072, 59903, 30620, 644, 36951, 16164, 1043, 42943, 28561, 36229], 'labels': [-1, -1, 9, 7, 7, -1, 7, 9, -1, 2], 'scores': [0.34951984882354736, 0.41641056537628174, 0.38612115383148193, 0.46514832973480225, 0.5300630927085876, 0.3596388101577759, 0.47392237186431885, 0.467132568359375, 0.40575265884399414, 0.4792308211326599]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8595312833786011})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.808677077293396})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7244469523429871})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7399250268936157})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7501678466796875})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8419058918952942})
store['active_learning_steps'][9]['training']['best_epoch']=3
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8887, 'crossentropy': 0.675453515625}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.7467348575592041})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5378020405769348})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5062371492385864})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.5055955648422241})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.4793044924736023})
store['active_learning_steps'][9]['eval_training']['best_epoch']=5
store['active_learning_steps'][9]['acquisition']={'indices': [34680, 50633, 40466, 23434, 31819, 42144, 6169, 51154, 17478, 30262], 'labels': [2, 5, 8, 5, 5, 9, 5, 3, 4, 5], 'scores': [0.41845232248306274, 0.5140854120254517, 0.5291548371315002, 0.476603627204895, 0.4547475576400757, 0.47700071334838867, 0.42808449268341064, 0.6189232468605042, 0.5203498601913452, 0.4762815237045288]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.797435998916626})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6956349611282349})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6973863244056702})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7339634895324707})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7336958050727844})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8916, 'crossentropy': 0.616477392578125}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7335867881774902})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.5796973705291748})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.558975100517273})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.5342268943786621})
store['active_learning_steps'][10]['eval_training']['best_epoch']=4
store['active_learning_steps'][10]['acquisition']={'indices': [20896, 43123, 53371, 32766, 11338, 26574, 46998, 10635, 569, 38275], 'labels': [6, -1, -1, 8, 5, 5, -1, 3, -1, 2], 'scores': [0.3115307688713074, 0.41919851303100586, 0.38969331979751587, 0.6002339124679565, 0.5945077538490295, 0.5088956356048584, 0.2378392219543457, 0.3328302502632141, 0.38050734996795654, 0.5675696134567261]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7661535739898682})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6475964784622192})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6599715948104858})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7001224756240845})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7272188663482666})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8992, 'crossentropy': 0.60809130859375}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7116039991378784})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5470821857452393})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5415483713150024})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5177568197250366})
store['active_learning_steps'][11]['eval_training']['best_epoch']=4
store['active_learning_steps'][11]['acquisition']={'indices': [52953, 28861, 50415, 44881, 37249, 57486, 10210, 54924, 55208, 25004], 'labels': [2, -1, 6, 2, 5, -1, 3, -1, -1, 2], 'scores': [0.4260975122451782, 0.3267737627029419, 0.3506060838699341, 0.480205237865448, 0.46099144220352173, 0.45176267623901367, 0.5351523756980896, 0.344865083694458, 0.3735523223876953, 0.6209267973899841]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8176752328872681})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6693748235702515})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6823698878288269})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6605929136276245})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6587032079696655})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6976001262664795})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7683943510055542})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7385573387145996})
store['active_learning_steps'][12]['training']['best_epoch']=5
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9114, 'crossentropy': 0.6370845703125}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6524628400802612})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5489733219146729})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.482011616230011})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4762057662010193})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.45722970366477966})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.455430269241333})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.43723446130752563})
store['active_learning_steps'][12]['eval_training']['best_epoch']=7
store['active_learning_steps'][12]['acquisition']={'indices': [46647, 34946, 18049, 27738, 50990, 39835, 22481, 38567, 14751, 31252], 'labels': [8, 8, 3, 4, 0, 7, 7, 4, 8, 5], 'scores': [0.3789815604686737, 0.4874168634414673, 0.47788912057876587, 0.6178383231163025, 0.6428200900554657, 0.4647531509399414, 0.6459470391273499, 0.5526660084724426, 0.598554790019989, 0.6592874228954315]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.9204053282737732})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6259597539901733})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6269237995147705})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6251506805419922})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5794022679328918})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6406000852584839})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6231279373168945})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5991576910018921})
store['active_learning_steps'][13]['training']['best_epoch']=5
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.9263, 'crossentropy': 0.554886376953125}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7067383527755737})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5348680019378662})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4342593550682068})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4268941283226013})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.42940598726272583})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4297190308570862})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.41178107261657715})
store['active_learning_steps'][13]['eval_training']['best_epoch']=7
store['active_learning_steps'][13]['acquisition']={'indices': [56999, 624, 16960, 12838, 49515, 4623, 7438, 39451, 54846, 34012], 'labels': [-1, -1, -1, -1, 2, -1, 7, 1, -1, 6], 'scores': [0.3142080307006836, 0.4483734369277954, 0.44145309925079346, 0.43171870708465576, 0.6285525560379028, 0.598206639289856, 0.7346534132957458, 0.587074875831604, 0.6537063717842102, 0.5202814638614655]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.9147824645042419})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6010289788246155})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6000902056694031})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5846318602561951})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6325017213821411})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5783132910728455})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6038614511489868})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6033221483230591})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6539520621299744})
store['active_learning_steps'][14]['training']['best_epoch']=6
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9254, 'crossentropy': 0.528241455078125}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8225065469741821})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5125058889389038})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4204760193824768})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.40886086225509644})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.36452776193618774})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.38405781984329224})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.36426085233688354})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.38161730766296387})
store['active_learning_steps'][14]['eval_training']['best_epoch']=7
store['active_learning_steps'][14]['acquisition']={'indices': [14188, 17181, 29884, 48149, 54739, 32212, 55318, 59208, 33818, 17358], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.5849797129631042, 0.603369414806366, 0.5363103151321411, 0.46965914964675903, 0.43666356801986694, 0.4020904302597046, 0.3987184166908264, 0.5009763240814209, 0.5378654599189758, 0.5277969241142273]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.772327184677124})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5273236036300659})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.537540078163147})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5720844864845276})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5549540519714355})
store['active_learning_steps'][15]['training']['best_epoch']=2
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9222, 'crossentropy': 0.511978076171875}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6843297481536865})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5372519493103027})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4741690158843994})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4927871525287628})
store['active_learning_steps'][15]['eval_training']['best_epoch']=3
store['active_learning_steps'][15]['acquisition']={'indices': [35077, 27265, 26654, 20329, 22454, 46874, 39865, 58212, 137, 13099], 'labels': [-1, -1, -1, -1, 7, 7, 8, -1, 8, 3], 'scores': [0.21838605403900146, 0.39874160289764404, 0.2331845760345459, 0.2721998691558838, 0.26823464035987854, 0.42417478561401367, 0.3772416114807129, 0.27732908725738525, 0.42819178104400635, 0.6209961175918579]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8877698183059692})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6508553624153137})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.553198516368866})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6178395748138428})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6389672160148621})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6144556999206543})
store['active_learning_steps'][16]['training']['best_epoch']=3
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9178, 'crossentropy': 0.525014453125}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.752761721611023})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5322278738021851})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.49935948848724365})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4515521228313446})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4293474555015564})
store['active_learning_steps'][16]['eval_training']['best_epoch']=5
store['active_learning_steps'][16]['acquisition']={'indices': [19834, 3387, 22169, 38641, 15562, 9290, 6846, 38227, 13231, 59683], 'labels': [3, -1, 2, 8, 9, 9, -1, -1, -1, -1], 'scores': [0.4707183837890625, 0.4178556203842163, 0.48584604263305664, 0.442876935005188, 0.6064736247062683, 0.5285708904266357, 0.3938220739364624, 0.397746205329895, 0.3538295030593872, 0.3413727879524231]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.856906533241272})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6435880661010742})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5325926542282104})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5574880838394165})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6357964277267456})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5544849038124084})
store['active_learning_steps'][17]['training']['best_epoch']=3
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9269, 'crossentropy': 0.474937841796875}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7108993530273438})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.49131450057029724})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4493137300014496})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.447723388671875})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.43451905250549316})
store['active_learning_steps'][17]['eval_training']['best_epoch']=5
store['active_learning_steps'][17]['acquisition']={'indices': [42682, 58282, 8704, 33856, 6604, 19524, 56856, 10170, 10031, 5916], 'labels': [8, -1, 1, 1, 8, 2, -1, -1, -1, -1], 'scores': [0.5571969747543335, 0.4748896360397339, 0.4198337197303772, 0.4228188991546631, 0.6017380356788635, 0.456828773021698, 0.31899863481521606, 0.4126697778701782, 0.5120565891265869, 0.4274179935455322]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.8621783256530762})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5539741516113281})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5258023738861084})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5822923183441162})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6281626224517822})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6217710971832275})
store['active_learning_steps'][18]['training']['best_epoch']=3
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9189, 'crossentropy': 0.502309912109375}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6733933091163635})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5502023696899414})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4387168288230896})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4377402663230896})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4230443239212036})
store['active_learning_steps'][18]['eval_training']['best_epoch']=5
store['active_learning_steps'][18]['acquisition']={'indices': [59335, 28507, 51240, 41933, 32724, 9050, 36408, 52399, 53736, 21356], 'labels': [4, -1, 9, 5, 5, -1, 1, 5, 9, 9], 'scores': [0.46643757820129395, 0.4248422384262085, 0.4508693218231201, 0.5915650725364685, 0.6123039126396179, 0.2674524784088135, 0.4641125798225403, 0.4494673013687134, 0.4212867021560669, 0.4541981816291809]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8820850849151611})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.535831868648529})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4836220443248749})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5125414133071899})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5685739517211914})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5250253677368164})
store['active_learning_steps'][19]['training']['best_epoch']=3
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9346, 'crossentropy': 0.476089990234375}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.714386522769928})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5025349259376526})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.41779959201812744})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.41844743490219116})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.39436689019203186})
store['active_learning_steps'][19]['eval_training']['best_epoch']=5
store['active_learning_steps'][19]['acquisition']={'indices': [54387, 3290, 12416, 44172, 14376, 38986, 40290, 35960, 5086, 49995], 'labels': [8, 4, 3, 8, 5, 3, -1, -1, 3, 5], 'scores': [0.44850993156433105, 0.5172280073165894, 0.4849816560745239, 0.7298754453659058, 0.5789439082145691, 0.3405771851539612, 0.2978103756904602, 0.3352097272872925, 0.5616039037704468, 0.49366408586502075]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8353530168533325})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5006598234176636})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5402809381484985})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.507501482963562})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5141043663024902})
store['active_learning_steps'][20]['training']['best_epoch']=2
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9297, 'crossentropy': 0.469555615234375}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7242678999900818})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5347822904586792})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.497456431388855})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5099478363990784})
store['active_learning_steps'][20]['eval_training']['best_epoch']=3
store['active_learning_steps'][20]['acquisition']={'indices': [5643, 11378, 15853, 52747, 207, 33301, 47781, 43043, 22283, 509], 'labels': [1, 4, 2, 3, 3, -1, 3, 3, 9, 3], 'scores': [0.3315478563308716, 0.3870595693588257, 0.33110150694847107, 0.5101311206817627, 0.5233410596847534, 0.25946182012557983, 0.4214164614677429, 0.5599733591079712, 0.31019747257232666, 0.5499565005302429]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8897361755371094})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5751453638076782})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5274084806442261})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5902892351150513})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5325058698654175})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5348137617111206})
store['active_learning_steps'][21]['training']['best_epoch']=3
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.927, 'crossentropy': 0.485339794921875}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7421835064888})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5405334234237671})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5041874051094055})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.44807595014572144})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4478260576725006})
store['active_learning_steps'][21]['eval_training']['best_epoch']=5
store['active_learning_steps'][21]['acquisition']={'indices': [1239, 48960, 29966, 15877, 50389, 27278, 49509, 33364, 24688, 27248], 'labels': [-1, -1, 6, -1, -1, -1, 8, 2, 1, 3], 'scores': [0.4110015630722046, 0.4350895881652832, 0.4814342260360718, 0.31274306774139404, 0.6024749279022217, 0.29812610149383545, 0.5504626035690308, 0.4971553683280945, 0.3732335567474365, 0.29460132122039795]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8168706893920898})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5004757642745972})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.48974403738975525})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.46045970916748047})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4986502528190613})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4691893458366394})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5545699596405029})
store['active_learning_steps'][22]['training']['best_epoch']=4
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9417, 'crossentropy': 0.409044970703125}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6991614103317261})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5015196800231934})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.45580172538757324})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.40678858757019043})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.35870009660720825})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.39060384035110474})
store['active_learning_steps'][22]['eval_training']['best_epoch']=5
store['active_learning_steps'][22]['acquisition']={'indices': [42865, 42316, 17503, 54455, 19990, 11950, 37424, 6286, 49242, 16777], 'labels': [0, 1, 0, -1, 0, 8, -1, -1, 7, 0], 'scores': [0.35939544439315796, 0.24695265293121338, 0.5203188061714172, 0.34642767906188965, 0.5324971675872803, 0.42465299367904663, 0.28604137897491455, 0.322640061378479, 0.4608309864997864, 0.3697328567504883]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.9098252058029175})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.506867527961731})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4704962968826294})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4628009796142578})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5458774566650391})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.46971893310546875})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5350590944290161})
store['active_learning_steps'][23]['training']['best_epoch']=4
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9407, 'crossentropy': 0.42531103515625}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6779797077178955})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.46746009588241577})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.3856126666069031})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.36648765206336975})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.3876417279243469})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.3641425371170044})
store['active_learning_steps'][23]['eval_training']['best_epoch']=6
store['active_learning_steps'][23]['acquisition']={'indices': [21896, 17714, 3118, 6152, 31460, 53953, 47240, 55241, 58535, 158], 'labels': [8, 7, 5, 8, 7, 8, 4, 8, 5, 7], 'scores': [0.4956105351448059, 0.37503618001937866, 0.5081458687782288, 0.492631196975708, 0.39910757541656494, 0.5176142454147339, 0.42293494939804077, 0.5598198771476746, 0.4641916751861572, 0.4238050580024719]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8629347681999207})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.521597146987915})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5148822069168091})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5060676336288452})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.46955087780952454})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5071070790290833})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.47760939598083496})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5110885500907898})
store['active_learning_steps'][24]['training']['best_epoch']=5
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9413, 'crossentropy': 0.422081640625}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7544300556182861})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4692244529724121})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4126175045967102})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3757699728012085})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.34966766834259033})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.36376434564590454})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.33977192640304565})
store['active_learning_steps'][24]['eval_training']['best_epoch']=7
store['active_learning_steps'][24]['acquisition']={'indices': [224, 56773, 7325, 5278, 18702, 34706, 29305, 28984, 47142, 26020], 'labels': [1, 9, 0, 4, -1, -1, -1, 9, 2, 5], 'scores': [0.6585339307785034, 0.4425962567329407, 0.675674706697464, 0.6401990652084351, 0.38066715002059937, 0.42527544498443604, 0.2642709016799927, 0.45993322134017944, 0.4579263925552368, 0.5271914303302765]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.9689798355102539})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.528863787651062})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.46774983406066895})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4285683333873749})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4649832248687744})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.45905980467796326})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4529169797897339})
store['active_learning_steps'][25]['training']['best_epoch']=4
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9408, 'crossentropy': 0.44337744140625}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7185681462287903})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5209122896194458})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3911648690700531})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.38650012016296387})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3521670699119568})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.36048635840415955})
store['active_learning_steps'][25]['eval_training']['best_epoch']=5
store['active_learning_steps'][25]['acquisition']={'indices': [47659, 31684, 18584, 26358, 37087, 2194, 6902, 27668, 16876, 12602], 'labels': [-1, -1, -1, 3, 4, 8, -1, -1, -1, -1], 'scores': [0.4203328490257263, 0.3796079158782959, 0.4472137689590454, 0.645393967628479, 0.42842692136764526, 0.4175359606742859, 0.36570417881011963, 0.46387434005737305, 0.4085771441459656, 0.26649588346481323]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8720865249633789})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4815639853477478})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4085434079170227})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.42531824111938477})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.407012939453125})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.42473864555358887})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4263051748275757})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4635973572731018})
store['active_learning_steps'][26]['training']['best_epoch']=5
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9438, 'crossentropy': 0.3915849365234375}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7352396249771118})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.44438275694847107})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.43012917041778564})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3903062045574188})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.340107798576355})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3363651633262634})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3468567728996277})
store['active_learning_steps'][26]['eval_training']['best_epoch']=6
store['active_learning_steps'][26]['acquisition']={'indices': [42472, 54969, 2546, 32065, 11885, 49982, 11708, 4205, 22815, 17261], 'labels': [2, 6, 4, 2, 8, -1, 3, 4, -1, -1], 'scores': [0.7019568085670471, 0.4453122615814209, 0.46615487337112427, 0.41687774658203125, 0.4289346933364868, 0.4329257011413574, 0.5918890833854675, 0.39013612270355225, 0.4452001452445984, 0.3709062337875366]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8994039297103882})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5519958734512329})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4494483470916748})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4284611940383911})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.48656755685806274})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.43950265645980835})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4726257920265198})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9358, 'crossentropy': 0.4406212890625}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7659409642219543})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5002516508102417})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.45110654830932617})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.3997412323951721})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.39083290100097656})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3481437563896179})
store['active_learning_steps'][27]['eval_training']['best_epoch']=6
store['active_learning_steps'][27]['acquisition']={'indices': [48112, 25546, 4594, 38698, 14760, 16919, 1662, 56114, 29153, 9494], 'labels': [1, 8, -1, 5, 2, 9, 2, -1, 3, -1], 'scores': [0.3610524535179138, 0.31418055295944214, 0.4403154253959656, 0.5902848243713379, 0.5515807271003723, 0.3338755965232849, 0.41145849227905273, 0.3220491409301758, 0.42911845445632935, 0.4390019178390503]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.9612127542495728})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5412355661392212})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4729471802711487})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4762173593044281})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.45195287466049194})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5272064805030823})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5073626041412354})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4473634660243988})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5700353384017944})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5177086591720581})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4825601577758789})
store['active_learning_steps'][28]['training']['best_epoch']=8
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.947, 'crossentropy': 0.43792626953125}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7953501343727112})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.47025755047798157})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.39068400859832764})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3778361678123474})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.35997074842453003})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3441266417503357})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3198262155056})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.34800031781196594})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3297727108001709})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3228870630264282})
store['active_learning_steps'][28]['eval_training']['best_epoch']=7
store['active_learning_steps'][28]['acquisition']={'indices': [57585, 55450, 47297, 27406, 17756, 42646, 17102, 33862, 43946, 54880], 'labels': [-1, 5, 8, 7, 8, -1, -1, 9, 5, 5], 'scores': [0.29165446758270264, 0.5855075716972351, 0.45551085472106934, 0.5679095983505249, 0.695324182510376, 0.5086716413497925, 0.3610255718231201, 0.3723141849040985, 0.5839620530605316, 0.534425288438797]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.900536298751831})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.48343557119369507})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.44505226612091064})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4368498921394348})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.44327014684677124})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4316920340061188})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.45122015476226807})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.5018948912620544})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.44852739572525024})
store['active_learning_steps'][29]['training']['best_epoch']=6
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9495, 'crossentropy': 0.376545166015625}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7591450214385986})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4879917502403259})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3838183879852295})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.35914647579193115})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3499009609222412})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.31925299763679504})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3180053234100342})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.33586814999580383})
store['active_learning_steps'][29]['eval_training']['best_epoch']=7
store['active_learning_steps'][29]['acquisition']={'indices': [32047, 24121, 22991, 57321, 36935, 14037, 38825, 48732, 38530, 13395], 'labels': [9, -1, -1, -1, -1, -1, -1, -1, 2, -1], 'scores': [0.6760753393173218, 0.30083489418029785, 0.5609143972396851, 0.45217955112457275, 0.24046188592910767, 0.3563491106033325, 0.2825969457626343, 0.45721936225891113, 0.15735889971256256, 0.22104313969612122]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.0159542560577393})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5272008776664734})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4920084774494171})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.45404472947120667})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.45112115144729614})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5082861185073853})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4757227897644043})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4628424048423767})
store['active_learning_steps'][30]['training']['best_epoch']=5
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.949, 'crossentropy': 0.3910086181640625}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.701346755027771})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4833924174308777})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.40658697485923767})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.37065812945365906})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.32645997405052185})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3410908579826355})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.33451569080352783})
store['active_learning_steps'][30]['eval_training']['best_epoch']=5
store['active_learning_steps'][30]['acquisition']={'indices': [36409, 33812, 9472, 5535, 14210, 54542, 3071, 59303, 49497, 49714], 'labels': [3, 6, 2, -1, -1, 7, 4, -1, 0, 9], 'scores': [0.41611677408218384, 0.6466721296310425, 0.6952895522117615, 0.46585261821746826, 0.5466656684875488, 0.6130408048629761, 0.3321725130081177, 0.404327929019928, 0.48239660263061523, 0.39549803733825684]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.9887111186981201})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5229194760322571})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.44371962547302246})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.45040422677993774})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.41630682349205017})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.42240047454833984})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.47039109468460083})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.45749032497406006})
store['active_learning_steps'][31]['training']['best_epoch']=5
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9484, 'crossentropy': 0.38170419921875}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7872574925422668})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.47178566455841064})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4039074182510376})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3723808825016022})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3670840859413147})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3247585892677307})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.33190271258354187})
store['active_learning_steps'][31]['eval_training']['best_epoch']=6
store['active_learning_steps'][31]['acquisition']={'indices': [22525, 13026, 57732, 56662, 17469, 29351, 11208, 35474, 58879, 33995], 'labels': [4, 3, 9, 0, -1, -1, 9, 7, -1, -1], 'scores': [0.4589117169380188, 0.47049063444137573, 0.3574352264404297, 0.4460965394973755, 0.344143271446228, 0.3558516502380371, 0.491563081741333, 0.38977596163749695, 0.29010868072509766, 0.2619894742965698]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.8767638206481934})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5219425559043884})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3830143213272095})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4002780318260193})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.35996532440185547})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4143180251121521})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.41922527551651})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.43186232447624207})
store['active_learning_steps'][32]['training']['best_epoch']=5
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9587, 'crossentropy': 0.3346410400390625}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8488686084747314})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.48611313104629517})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3938820958137512})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.39049434661865234})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.33945393562316895})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.34497013688087463})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.31451845169067383})
store['active_learning_steps'][32]['eval_training']['best_epoch']=7
store['active_learning_steps'][32]['acquisition']={'indices': [23680, 48630, 24318, 1074, 25297, 45451, 34304, 53699, 59734, 14496], 'labels': [-1, -1, -1, -1, -1, -1, 8, -1, 2, -1], 'scores': [0.41612446308135986, 0.47697198390960693, 0.41335010528564453, 0.28128373622894287, 0.49800658226013184, 0.5973348617553711, 0.6320682168006897, 0.4743008613586426, 0.5486948490142822, 0.3084832429885864]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.0237741470336914})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5715494751930237})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4586140811443329})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3726142942905426})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3822473883628845})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4147268533706665})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3766949772834778})
store['active_learning_steps'][33]['training']['best_epoch']=4
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9527, 'crossentropy': 0.3556079345703125}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7937694787979126})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.49532297253608704})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3975495398044586})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.34462133049964905})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3648897409439087})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3368093967437744})
store['active_learning_steps'][33]['eval_training']['best_epoch']=6
store['active_learning_steps'][33]['acquisition']={'indices': [44853, 5794, 1196, 3765, 25092, 52208, 19957, 48404, 11482, 5129], 'labels': [7, -1, 4, 2, 0, -1, 4, -1, 8, 2], 'scores': [0.23545974493026733, 0.27392125129699707, 0.3281680941581726, 0.39502251148223877, 0.4208211898803711, 0.327340304851532, 0.3261124789714813, 0.3446536660194397, 0.5536192059516907, 0.5224378108978271]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.0574716329574585})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5541695356369019})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.445068359375})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.45356523990631104})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4060165286064148})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3819010257720947})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3974553942680359})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.41550135612487793})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4048844277858734})
store['active_learning_steps'][34]['training']['best_epoch']=6
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9552, 'crossentropy': 0.35449375}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8034690022468567})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.45858168601989746})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.40630432963371277})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.36783477663993835})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3327348828315735})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.34160155057907104})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.31014662981033325})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.29686084389686584})
store['active_learning_steps'][34]['eval_training']['best_epoch']=8
store['active_learning_steps'][34]['acquisition']={'indices': [3045, 49391, 46022, 8742, 19756, 6505, 40009, 52192, 10669, 45905], 'labels': [-1, -1, -1, -1, 8, -1, -1, -1, -1, -1], 'scores': [0.49275529384613037, 0.40927428007125854, 0.4083072543144226, 0.40319639444351196, 0.4905344247817993, 0.4972846508026123, 0.445659875869751, 0.6088531017303467, 0.46926331520080566, 0.44447243213653564]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.9386967420578003})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4941750168800354})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.40533867478370667})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.36466965079307556})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.388525128364563})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.36265790462493896})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.34344053268432617})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.36251673102378845})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.31779587268829346})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3946121335029602})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3959875702857971})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3862113654613495})
store['active_learning_steps'][35]['training']['best_epoch']=9
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9581, 'crossentropy': 0.325545703125}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8142791986465454})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4565468430519104})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.33825555443763733})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.34103015065193176})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2878434658050537})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2802579402923584})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2862321436405182})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.27627304196357727})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.26617613434791565})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2587055563926697})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2628542184829712})
store['active_learning_steps'][35]['eval_training']['best_epoch']=10
store['active_learning_steps'][35]['acquisition']={'indices': [46820, 38954, 2345, 31650, 15781, 39457, 22348, 7595, 26756, 31738], 'labels': [-1, -1, -1, 5, 5, -1, -1, -1, 7, 8], 'scores': [0.4115767478942871, 0.31448811292648315, 0.4535849094390869, 0.560910165309906, 0.3829197287559509, 0.4228566884994507, 0.42057693004608154, 0.46905219554901123, 0.452606201171875, 0.674115777015686]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9187307357788086})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5026849508285522})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3767133951187134})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3894329071044922})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.35720422863960266})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.38384363055229187})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.361640989780426})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3818818926811218})
store['active_learning_steps'][36]['training']['best_epoch']=5
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9599, 'crossentropy': 0.310121923828125}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8153681755065918})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4569712281227112})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.39179569482803345})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.36347949504852295})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.33335983753204346})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3283354640007019})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.29626330733299255})
store['active_learning_steps'][36]['eval_training']['best_epoch']=7
store['active_learning_steps'][36]['acquisition']={'indices': [59314, 53508, 22546, 1930, 31959, 58420, 55667, 16676, 59303, 38276], 'labels': [9, 8, -1, 0, -1, -1, 5, 3, 8, -1], 'scores': [0.5274850726127625, 0.4143393635749817, 0.3730310797691345, 0.4389035701751709, 0.428896427154541, 0.3403209447860718, 0.519302248954773, 0.42980849742889404, 0.5657205581665039, 0.3550987243652344]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.993682861328125})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5306487083435059})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4486513137817383})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4385784864425659})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.40202414989471436})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4346954822540283})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3860146105289459})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4005465507507324})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.42361027002334595})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.41561728715896606})
store['active_learning_steps'][37]['training']['best_epoch']=7
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9505, 'crossentropy': 0.3961623291015625}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8995935916900635})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5088734030723572})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.38946154713630676})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.33865225315093994})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.33129191398620605})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3250194787979126})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.30832570791244507})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.30150121450424194})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.311276376247406})
store['active_learning_steps'][37]['eval_training']['best_epoch']=8
store['active_learning_steps'][37]['acquisition']={'indices': [50960, 23171, 38954, 38912, 20949, 37018, 53046, 25771, 7911, 10781], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.5224776864051819, 0.3092794418334961, 0.32776254415512085, 0.5756422877311707, 0.4002246856689453, 0.48663562536239624, 0.46904247999191284, 0.3573196530342102, 0.38901758193969727, 0.5568882822990417]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.1083769798278809})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5088071227073669})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.41256922483444214})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.38523679971694946})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.371455579996109})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.39270007610321045})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4054166078567505})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.42961758375167847})
store['active_learning_steps'][38]['training']['best_epoch']=5
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9538, 'crossentropy': 0.35114306640625}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8220429420471191})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.48027002811431885})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4198380708694458})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.32422882318496704})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3543313145637512})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3376629948616028})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.334181010723114})
store['active_learning_steps'][38]['eval_training']['best_epoch']=4
store['active_learning_steps'][38]['acquisition']={'indices': [20171, 45812, 2342, 24038, 14152, 58655, 57018, 55696, 2104, 59726], 'labels': [5, -1, 2, 1, 7, -1, 9, -1, -1, 5], 'scores': [0.5152596235275269, 0.2807430028915405, 0.4127042591571808, 0.31806275248527527, 0.6120594143867493, 0.2637643814086914, 0.31061041355133057, 0.323661208152771, 0.24745070934295654, 0.5851621031761169]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 1.06107497215271})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5071594715118408})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.43797820806503296})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.333893358707428})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35636723041534424})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.36200782656669617})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.36636313796043396})
store['active_learning_steps'][39]['training']['best_epoch']=4
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9562, 'crossentropy': 0.3411472900390625}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8033704161643982})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4987885057926178})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.47290921211242676})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4105348587036133})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4219169616699219})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3702256679534912})
store['active_learning_steps'][39]['eval_training']['best_epoch']=6
store['active_learning_steps'][39]['acquisition']={'indices': [14647, 28382, 14749, 10421, 40526, 1674, 31184, 6036, 47423, 51993], 'labels': [-1, 6, 0, 5, -1, 9, 9, -1, -1, -1], 'scores': [0.36593055725097656, 0.2759125828742981, 0.4933208227157593, 0.4332481622695923, 0.33528149127960205, 0.44512468576431274, 0.364632248878479, 0.33008456230163574, 0.44104576110839844, 0.4378138780593872]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.157548427581787})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5473340153694153})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.42123496532440186})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.393197238445282})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.42141321301460266})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.38261091709136963})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3802396059036255})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.36681655049324036})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.46601301431655884})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.39250025153160095})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4199472665786743})
store['active_learning_steps'][40]['training']['best_epoch']=8
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9594, 'crossentropy': 0.3488164306640625}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7717270851135254})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4853392243385315})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3558790683746338})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3915858566761017})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3153402805328369})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2919505536556244})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.30739498138427734})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2885415554046631})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.30621084570884705})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2754843831062317})
store['active_learning_steps'][40]['eval_training']['best_epoch']=10
store['active_learning_steps'][40]['acquisition']={'indices': [58772, 6673, 27204, 31591, 33231, 19837, 15842, 35032, 10164, 42740], 'labels': [-1, -1, 6, 8, -1, -1, -1, -1, -1, -1], 'scores': [0.5912126302719116, 0.5720865726470947, 0.6239245533943176, 0.581004798412323, 0.5136014223098755, 0.6762535572052002, 0.4235745668411255, 0.36872315406799316, 0.5916846990585327, 0.5870286226272583]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9863786101341248})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5296277403831482})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.38183242082595825})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.34439945220947266})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3548205494880676})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3748028874397278})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3596544861793518})
store['active_learning_steps'][41]['training']['best_epoch']=4
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9585, 'crossentropy': 0.32437060546875}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8341860771179199})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5222715735435486})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4063258171081543})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.33673596382141113})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3575161099433899})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3444448709487915})
store['active_learning_steps'][41]['eval_training']['best_epoch']=4
store['active_learning_steps'][41]['acquisition']={'indices': [26573, 2765, 47479, 7008, 54061, 34199, 15738, 29621, 46423, 12704], 'labels': [-1, 0, 0, -1, -1, -1, -1, -1, 9, -1], 'scores': [0.36781179904937744, 0.5506148338317871, 0.5101373195648193, 0.3742421865463257, 0.1575002670288086, 0.5427123308181763, 0.42126137018203735, 0.3384101986885071, 0.3494817614555359, 0.3264702558517456]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9811902642250061})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4956989288330078})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4171491861343384})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35238420963287354})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.34993717074394226})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.36015141010284424})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.34920936822891235})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.36263591051101685})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3843386769294739})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4149438738822937})
store['active_learning_steps'][42]['training']['best_epoch']=7
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9602, 'crossentropy': 0.32631572265625}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8995027542114258})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5235332250595093})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4034650921821594})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3259481191635132})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3140254020690918})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3413168787956238})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2982324957847595})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2865048050880432})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31340938806533813})
store['active_learning_steps'][42]['eval_training']['best_epoch']=8
store['active_learning_steps'][42]['acquisition']={'indices': [49804, 47597, 24982, 12318, 49253, 2285, 36653, 27108, 7852, 49164], 'labels': [8, 8, -1, 1, -1, -1, 6, -1, -1, 2], 'scores': [0.41357147693634033, 0.47695690393447876, 0.35213398933410645, 0.3784550726413727, 0.578895092010498, 0.43930840492248535, 0.5557312965393066, 0.30797863006591797, 0.28014159202575684, 0.37290158867836]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.083094596862793})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5265394449234009})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.43200451135635376})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4026070833206177})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.38760465383529663})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35671234130859375})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.34559521079063416})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.36674386262893677})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.39681899547576904})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.38954728841781616})
store['active_learning_steps'][43]['training']['best_epoch']=7
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9604, 'crossentropy': 0.32659931640625}
store['active_learning_steps'][43]['eval_training']={}
store['active_learning_steps'][43]['eval_training']['epochs']=[]
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9856517314910889})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5449905395507812})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4118635654449463})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.351245641708374})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3514736592769623})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3114381730556488})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3073161244392395})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.28051021695137024})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2835191488265991})
store['active_learning_steps'][43]['eval_training']['best_epoch']=8
store['active_learning_steps'][43]['acquisition']={'indices': [12800, 14912, 58917, 2481, 40765, 26314, 58053, 14868, 58469, 51210], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.2848049998283386, 0.44349896907806396, 0.5046964883804321, 0.5770572423934937, 0.4598489999771118, 0.5384703874588013, 0.43794000148773193, 0.3970189690589905, 0.6589513421058655, 0.49554896354675293]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.9876655340194702})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4957624673843384})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.42490071058273315})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3784482479095459})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.36508941650390625})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34256711602211})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3629451096057892})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3872947692871094})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.36920297145843506})
store['active_learning_steps'][44]['training']['best_epoch']=6
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.9597, 'crossentropy': 0.3394424072265625}
store['active_learning_steps'][44]['eval_training']={}
store['active_learning_steps'][44]['eval_training']['epochs']=[]
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7996960878372192})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.49997663497924805})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4167911410331726})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.35686129331588745})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3258373737335205})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3158659040927887})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.31206998229026794})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2888827919960022})
store['active_learning_steps'][44]['eval_training']['best_epoch']=8
store['active_learning_steps'][44]['acquisition']={'indices': [1196, 44409, 56459, 14077, 41934, 42133, 47858, 19501, 23843, 28346], 'labels': [-1, -1, -1, 9, -1, -1, -1, 3, -1, -1], 'scores': [0.33283156156539917, 0.284961462020874, 0.3737863302230835, 0.39653685688972473, 0.4343055486679077, 0.4267522096633911, 0.3708956241607666, 0.3739875555038452, 0.3913527727127075, 0.3099566698074341]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.0908997058868408})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6000688672065735})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4735637903213501})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3727913796901703})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3596826195716858})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3895053267478943})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3562665581703186})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.43637919425964355})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4295772910118103})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.40449702739715576})
store['active_learning_steps'][45]['training']['best_epoch']=7
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.9582, 'crossentropy': 0.3298953125}
store['active_learning_steps'][45]['eval_training']={}
store['active_learning_steps'][45]['eval_training']['epochs']=[]
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8222310543060303})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5000885725021362})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4066576361656189})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.34369218349456787})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3081422448158264})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.29652461409568787})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.32045021653175354})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2641160488128662})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.27695244550704956})
store['active_learning_steps'][45]['eval_training']['best_epoch']=8
store['active_learning_steps'][45]['acquisition']={'indices': [55758, 11594, 34328, 19044, 7250, 39778, 26460, 14580, 3811, 37023], 'labels': [3, -1, 8, 4, 3, 8, 5, 9, 1, 1], 'scores': [0.5140804648399353, 0.3954505920410156, 0.48022836446762085, 0.7415710687637329, 0.5278015732765198, 0.4327462315559387, 0.4886341392993927, 0.39208900928497314, 0.4529794454574585, 0.533271312713623]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.0676419734954834})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6048285961151123})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.39045241475105286})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3712207078933716})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3797644376754761})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3509194850921631})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3672173321247101})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.342415988445282})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3780440092086792})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3643704652786255})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3649049401283264})
store['active_learning_steps'][46]['training']['best_epoch']=8
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.9611, 'crossentropy': 0.3269263671875}
store['active_learning_steps'][46]['eval_training']={}
store['active_learning_steps'][46]['eval_training']['epochs']=[]
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8540890216827393})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5116499066352844})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3734244704246521})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3396044969558716})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.30603140592575073})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3203606903553009})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.30645838379859924})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27931785583496094})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.276090532541275})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2751154899597168})
store['active_learning_steps'][46]['eval_training']['best_epoch']=10
store['active_learning_steps'][46]['acquisition']={'indices': [35722, 23348, 35384, 45580, 59406, 2126, 28690, 17584, 18419, 56457], 'labels': [-1, -1, -1, 6, -1, 6, -1, -1, -1, -1], 'scores': [0.43851613998413086, 0.5162842273712158, 0.4919241666793823, 0.6154846847057343, 0.5124684572219849, 0.7326001524925232, 0.4716205596923828, 0.3290656805038452, 0.4024285078048706, 0.33995068073272705]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.0447094440460205})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5201054811477661})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4360344111919403})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3628298342227936})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3728289306163788})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3675273060798645})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.36854636669158936})
store['active_learning_steps'][47]['training']['best_epoch']=4
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.9506, 'crossentropy': 0.3585103515625}
store['active_learning_steps'][47]['eval_training']={}
store['active_learning_steps'][47]['eval_training']['epochs']=[]
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8768389821052551})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5093072056770325})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.48427096009254456})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.41799086332321167})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.37414392828941345})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.35546791553497314})
store['active_learning_steps'][47]['eval_training']['best_epoch']=6
store['active_learning_steps'][47]['acquisition']={'indices': [12840, 29361, 43405, 13772, 52208, 37194, 3486, 6580, 41018, 10479], 'labels': [9, 5, 9, -1, -1, 6, -1, -1, 6, -1], 'scores': [0.5810889005661011, 0.4422629475593567, 0.49570220708847046, 0.27363765239715576, 0.2951974868774414, 0.35309213399887085, 0.4950745105743408, 0.20723497867584229, 0.33200281858444214, 0.38397324085235596]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.0724047422409058})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5274211764335632})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.41672107577323914})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3339570164680481})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3430004417896271})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34044694900512695})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.36394837498664856})
store['active_learning_steps'][48]['training']['best_epoch']=4
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.9614, 'crossentropy': 0.308091357421875}
store['active_learning_steps'][48]['eval_training']={}
store['active_learning_steps'][48]['eval_training']['epochs']=[]
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8576515316963196})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.47281724214553833})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3811107873916626})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.39936065673828125})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3749765455722809})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3246394991874695})
store['active_learning_steps'][48]['eval_training']['best_epoch']=6
store['active_learning_steps'][48]['acquisition']={'indices': [53862, 16638, 20855, 53844, 38469, 43906, 9227, 55582, 8891, 42285], 'labels': [-1, -1, 6, 5, -1, 4, -1, -1, -1, -1], 'scores': [0.4007645845413208, 0.4922139644622803, 0.46893030405044556, 0.5064632892608643, 0.387617826461792, 0.4526216983795166, 0.5587049722671509, 0.29680490493774414, 0.41120028495788574, 0.4211534261703491]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.1419836282730103})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5874436497688293})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3935009837150574})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33564189076423645})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.372717946767807})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3679717779159546})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3471153974533081})
store['active_learning_steps'][49]['training']['best_epoch']=4
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.961, 'crossentropy': 0.3229716064453125}
store['active_learning_steps'][49]['eval_training']={}
store['active_learning_steps'][49]['eval_training']['epochs']=[]
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.9184346199035645})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5818862915039062})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.44924792647361755})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.37978166341781616})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.32505592703819275})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3951601982116699})
store['active_learning_steps'][49]['eval_training']['best_epoch']=5
store['active_learning_steps'][49]['acquisition']={'indices': [44350, 22095, 44598, 45800, 52294, 18331, 42078, 46412, 37078, 46126], 'labels': [3, 1, 0, 9, 0, -1, 4, 0, 8, 3], 'scores': [0.38002341985702515, 0.17839550971984863, 0.5611766576766968, 0.34800928831100464, 0.5696974992752075, 0.23190534114837646, 0.5265638828277588, 0.4654335379600525, 0.2933293581008911, 0.39514827728271484]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.0526058673858643})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.49604347348213196})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3930433392524719})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3584848642349243})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3331080973148346})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3558354377746582})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32025039196014404})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.35896027088165283})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3383790850639343})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.35660696029663086})
store['active_learning_steps'][50]['training']['best_epoch']=7
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.9652, 'crossentropy': 0.2889780517578125}
store['active_learning_steps'][50]['eval_training']={}
store['active_learning_steps'][50]['eval_training']['epochs']=[]
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7942023277282715})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.45126014947891235})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.37148353457450867})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3380899429321289})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.31944236159324646})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.306815505027771})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3006148338317871})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.29732799530029297})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2929508686065674})
store['active_learning_steps'][50]['eval_training']['best_epoch']=9
store['active_learning_steps'][50]['acquisition']={'indices': [52697, 16176, 10454, 30585, 8608, 3879, 31291, 30927, 16466, 10974], 'labels': [3, -1, -1, -1, -1, -1, -1, 4, -1, -1], 'scores': [0.6339708566665649, 0.35547900199890137, 0.28998464345932007, 0.4308367967605591, 0.25059282779693604, 0.3547983169555664, 0.442532479763031, 0.5000037550926208, 0.5670782327651978, 0.31636321544647217]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.1141998767852783})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5671344995498657})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.37749922275543213})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34846031665802})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32829082012176514})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32562029361724854})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34119606018066406})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.35538411140441895})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3227548897266388})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33619242906570435})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3601541221141815})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.38340872526168823})
store['active_learning_steps'][51]['training']['best_epoch']=9
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.9649, 'crossentropy': 0.292237890625}
store['active_learning_steps'][51]['eval_training']={}
store['active_learning_steps'][51]['eval_training']['epochs']=[]
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8659753203392029})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4714928865432739})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.39837998151779175})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.336742103099823})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3107796907424927})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.31350386142730713})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2910596430301666})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.30072101950645447})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3127675950527191})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.28043830394744873})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2690012454986572})
store['active_learning_steps'][51]['eval_training']['best_epoch']=11
store['active_learning_steps'][51]['acquisition']={'indices': [54380, 39656, 43782, 22547, 59275, 7072, 33984, 50052, 17163, 23910], 'labels': [-1, 0, 3, -1, 3, -1, -1, -1, -1, -1], 'scores': [0.46314239501953125, 0.4835110902786255, 0.5894659757614136, 0.4321908950805664, 0.5212072432041168, 0.6128096580505371, 0.45951080322265625, 0.3147505521774292, 0.41721630096435547, 0.48492008447647095]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.0404103994369507})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5014210939407349})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3894021511077881})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3314630389213562})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3442845344543457})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3477502465248108})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32594913244247437})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3307446837425232})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.337947815656662})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3163083493709564})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3514561653137207})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3713284134864807})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4157187342643738})
store['active_learning_steps'][52]['training']['best_epoch']=10
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.9633, 'crossentropy': 0.28790986328125}
store['active_learning_steps'][52]['eval_training']={}
store['active_learning_steps'][52]['eval_training']['epochs']=[]
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9153251647949219})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5621491074562073})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4255310893058777})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3702235519886017})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.33535099029541016})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.33277860283851624})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3006293773651123})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2924753427505493})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2688707709312439})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2725503444671631})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2641030550003052})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2714304029941559})
store['active_learning_steps'][52]['eval_training']['best_epoch']=11
store['active_learning_steps'][52]['acquisition']={'indices': [8401, 24112, 21315, 18864, 53227, 59482, 14693, 23999, 47847, 41583], 'labels': [-1, 8, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.3746145963668823, 0.3700341582298279, 0.3281872272491455, 0.6081960201263428, 0.49756330251693726, 0.4659915566444397, 0.35656923055648804, 0.4997525215148926, 0.6475037932395935, 0.34485018253326416]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.0016191005706787})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5074720978736877})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.36957287788391113})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.332550972700119})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.31188005208969116})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3551265299320221})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3522987961769104})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.310224711894989})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3181864023208618})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31680285930633545})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30223867297172546})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32892054319381714})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32541579008102417})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3155749440193176})
store['active_learning_steps'][53]['training']['best_epoch']=11
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.9666, 'crossentropy': 0.280665576171875}
store['active_learning_steps'][53]['eval_training']={}
store['active_learning_steps'][53]['eval_training']['epochs']=[]
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8621938824653625})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4746161103248596})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3767600357532501})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3335886001586914})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.29352083802223206})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2820358872413635})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2689792513847351})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27419763803482056})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.27111417055130005})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2648821771144867})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2528974413871765})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.23991326987743378})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.23766736686229706})
store['active_learning_steps'][53]['eval_training']['best_epoch']=13
store['active_learning_steps'][53]['acquisition']={'indices': [5527, 20889, 56719, 2372, 7971, 1960, 1256, 44754, 55055, 41964], 'labels': [-1, 8, 2, -1, -1, -1, 9, -1, -1, -1], 'scores': [0.36475837230682373, 0.31441816687583923, 0.4843499958515167, 0.5133345127105713, 0.5731319785118103, 0.3928421139717102, 0.5276428461074829, 0.389839231967926, 0.5005042552947998, 0.47342944145202637]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.1417206525802612})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5949305295944214})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4194231629371643})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.32241129875183105})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3286069631576538})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3058739900588989})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3279086947441101})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.33387088775634766})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3242643475532532})
store['active_learning_steps'][54]['training']['best_epoch']=6
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.9584, 'crossentropy': 0.29623486328125}
store['active_learning_steps'][54]['eval_training']={}
store['active_learning_steps'][54]['eval_training']['epochs']=[]
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8187130093574524})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.45442163944244385})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.37240439653396606})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3642553985118866})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.29838281869888306})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3437940776348114})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2943266034126282})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.28732818365097046})
store['active_learning_steps'][54]['eval_training']['best_epoch']=8
store['active_learning_steps'][54]['acquisition']={'indices': [51161, 39531, 5640, 29303, 25138, 12655, 53872, 134, 10458, 52889], 'labels': [-1, -1, -1, 8, -1, 9, 8, 1, -1, -1], 'scores': [0.5152698755264282, 0.3718700408935547, 0.33504390716552734, 0.38223254680633545, 0.27475297451019287, 0.4229515790939331, 0.5808078646659851, 0.3610977530479431, 0.23523712158203125, 0.4085482358932495]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.0710124969482422})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5003615617752075})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.40826091170310974})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35862213373184204})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3348068594932556})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33085012435913086})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3069652318954468})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3265659809112549})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30965059995651245})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3560813367366791})
store['active_learning_steps'][55]['training']['best_epoch']=7
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.9662, 'crossentropy': 0.2849833984375}
store['active_learning_steps'][55]['eval_training']={}
store['active_learning_steps'][55]['eval_training']['epochs']=[]
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9310692548751831})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.48487555980682373})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.39005333185195923})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3177924156188965})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.315871000289917})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.26156577467918396})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2899281978607178})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.25529661774635315})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2708525061607361})
store['active_learning_steps'][55]['eval_training']['best_epoch']=8
store['active_learning_steps'][55]['acquisition']={'indices': [46402, 50320, 12349, 19159, 24212, 31642, 2710, 35691, 26516, 56421], 'labels': [-1, 5, -1, 8, 0, -1, -1, -1, -1, -1], 'scores': [0.28712427616119385, 0.5219848155975342, 0.2930300235748291, 0.31462550163269043, 0.3767107129096985, 0.446527361869812, 0.41150593757629395, 0.4435681104660034, 0.39963746070861816, 0.41241514682769775]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.1181191205978394})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5364400148391724})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3759220838546753})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3479527235031128})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3777220547199249})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.29926902055740356})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2935734987258911})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.32030385732650757})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3306514024734497})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3328961133956909})
store['active_learning_steps'][56]['training']['best_epoch']=7
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.9659, 'crossentropy': 0.276395361328125}
store['active_learning_steps'][56]['eval_training']={}
store['active_learning_steps'][56]['eval_training']['epochs']=[]
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9053478240966797})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4944692850112915})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3986043334007263})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3410520851612091})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3210153877735138})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3008047938346863})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3034712076187134})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28352633118629456})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2882097661495209})
store['active_learning_steps'][56]['eval_training']['best_epoch']=8
store['active_learning_steps'][56]['acquisition']={'indices': [29018, 23816, 18419, 19871, 16964, 26822, 16821, 56530, 6856, 9227], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.5302462577819824, 0.534135103225708, 0.6275839805603027, 0.5112076997756958, 0.486278235912323, 0.3801947832107544, 0.4864755868911743, 0.4988783597946167, 0.44276130199432373, 0.7154903411865234]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.0325696468353271})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5251426100730896})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.43829256296157837})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3306904435157776})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31044498085975647})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3100748658180237})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2952142357826233})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3051948547363281})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31814566254615784})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3041020333766937})
store['active_learning_steps'][57]['training']['best_epoch']=7
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.9652, 'crossentropy': 0.281674755859375}
store['active_learning_steps'][57]['eval_training']={}
store['active_learning_steps'][57]['eval_training']['epochs']=[]
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8990692496299744})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5242672562599182})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.38652321696281433})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.32912808656692505})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3318454325199127})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29014450311660767})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2725416421890259})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.252747118473053})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.27817073464393616})
store['active_learning_steps'][57]['eval_training']['best_epoch']=8
store['active_learning_steps'][57]['acquisition']={'indices': [55148, 52864, 10112, 59837, 30596, 30136, 47607, 12272, 14068, 34500], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, 8], 'scores': [0.4585191011428833, 0.2810710668563843, 0.44547879695892334, 0.38043153285980225, 0.5428546667098999, 0.3025059700012207, 0.36909347772598267, 0.2718263864517212, 0.3267490863800049, 0.5068554282188416]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.1468863487243652})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5594995021820068})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.44780775904655457})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3893098533153534})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3264192044734955})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3208027482032776})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.310760498046875})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.31869029998779297})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2996927499771118})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3054261803627014})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3388136029243469})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.32558703422546387})
store['active_learning_steps'][58]['training']['best_epoch']=9
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.9675, 'crossentropy': 0.279741162109375}
store['active_learning_steps'][58]['eval_training']={}
store['active_learning_steps'][58]['eval_training']['epochs']=[]
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.900140643119812})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.50956130027771})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3496817946434021})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3156886696815491})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3354305624961853})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.31526172161102295})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.26764971017837524})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.27799057960510254})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.28368669748306274})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.25118714570999146})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2636204957962036})
store['active_learning_steps'][58]['eval_training']['best_epoch']=10
store['active_learning_steps'][58]['acquisition']={'indices': [23958, 37184, 50736, 23737, 14742, 5594, 18275, 1582, 6727, 4873], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, 8], 'scores': [0.6067614555358887, 0.6549100875854492, 0.5227015614509583, 0.44385838508605957, 0.5139971971511841, 0.49600696563720703, 0.2918424904346466, 0.4741305708885193, 0.3008241057395935, 0.460567831993103]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.12571120262146})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5133292078971863})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4125669300556183})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3233380913734436})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3206678032875061})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30173826217651367})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.32432442903518677})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30608487129211426})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3451966643333435})
store['active_learning_steps'][59]['training']['best_epoch']=6
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.9671, 'crossentropy': 0.280237744140625}
store['active_learning_steps'][59]['eval_training']={}
store['active_learning_steps'][59]['eval_training']['epochs']=[]
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8358120918273926})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.48055410385131836})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3979928493499756})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3483593463897705})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.34694230556488037})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2998092770576477})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29567259550094604})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3447473645210266})
store['active_learning_steps'][59]['eval_training']['best_epoch']=7
store['active_learning_steps'][59]['acquisition']={'indices': [27728, 27498, 56658, 956, 9945, 55898, 41299, 32638, 19654, 3825], 'labels': [-1, 7, -1, -1, -1, -1, 3, -1, -1, -1], 'scores': [0.44599449634552, 0.5192115902900696, 0.40481770038604736, 0.5739173889160156, 0.42685234546661377, 0.37126123905181885, 0.5094019174575806, 0.4494485855102539, 0.42473435401916504, 0.4098832607269287]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.0845065116882324})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.48651760816574097})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.37939050793647766})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3477233350276947})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3234032988548279})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31203562021255493})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.320701539516449})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3159205913543701})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3168599009513855})
store['active_learning_steps'][60]['training']['best_epoch']=6
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.9603, 'crossentropy': 0.29969384765625}
store['active_learning_steps'][60]['eval_training']={}
store['active_learning_steps'][60]['eval_training']['epochs']=[]
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8745149374008179})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5185155868530273})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4003649950027466})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3232240676879883})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34489792585372925})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.32130444049835205})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.283771812915802})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.27425098419189453})
store['active_learning_steps'][60]['eval_training']['best_epoch']=8
store['active_learning_steps'][60]['acquisition']={'indices': [15754, 18607, 58560, 31637, 4536, 51715, 51295, 43745, 49985, 38679], 'labels': [-1, -1, 0, 5, -1, -1, -1, 8, 3, -1], 'scores': [0.3585749864578247, 0.3741946220397949, 0.5565023422241211, 0.47849828004837036, 0.30966782569885254, 0.3607393503189087, 0.4748802185058594, 0.32336950302124023, 0.36607569456100464, 0.3842248320579529]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.2472472190856934})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.6442022919654846})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4530148506164551})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3811560869216919})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3475136458873749})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3247094452381134})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3027035593986511})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.31470611691474915})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3485487699508667})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.349174439907074})
store['active_learning_steps'][61]['training']['best_epoch']=7
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.965, 'crossentropy': 0.3063575439453125}
store['active_learning_steps'][61]['eval_training']={}
store['active_learning_steps'][61]['eval_training']['epochs']=[]
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7152265310287476})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4339772164821625})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.35236287117004395})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.35137367248535156})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3080577850341797})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.31568223237991333})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.286041259765625})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.30828535556793213})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30308955907821655})
store['active_learning_steps'][61]['eval_training']['best_epoch']=7
store['active_learning_steps'][61]['acquisition']={'indices': [42220, 49406, 43038, 4634, 5684, 46148, 14040, 55612, 21636, 35246], 'labels': [3, 3, 4, 8, 6, -1, -1, -1, 2, 8], 'scores': [0.5178755521774292, 0.5280846357345581, 0.5792542695999146, 0.5257397294044495, 0.6329873204231262, 0.4622013568878174, 0.43390464782714844, 0.4324303865432739, 0.4401056170463562, 0.40326106548309326]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.9455915689468384})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5286867618560791})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3698531687259674})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3167950212955475})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3011631965637207})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31021562218666077})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3009698987007141})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3307972848415375})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.323489785194397})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31774625182151794})
store['active_learning_steps'][62]['training']['best_epoch']=7
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.9658, 'crossentropy': 0.281362109375}
store['active_learning_steps'][62]['eval_training']={}
store['active_learning_steps'][62]['eval_training']['epochs']=[]
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7658946514129639})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.48977968096733093})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3614528775215149})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2897964417934418})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.303125262260437})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2661857604980469})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.25635120272636414})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2588649094104767})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2507849931716919})
store['active_learning_steps'][62]['eval_training']['best_epoch']=9
store['active_learning_steps'][62]['acquisition']={'indices': [52197, 24016, 29282, 5898, 59515, 54988, 45319, 34833, 12012, 42403], 'labels': [6, -1, -1, 9, -1, -1, -1, -1, 3, 7], 'scores': [0.44523292779922485, 0.39497464895248413, 0.35495996475219727, 0.35533231496810913, 0.31208276748657227, 0.34381628036499023, 0.3962758779525757, 0.5168598890304565, 0.40184158086776733, 0.37497228384017944]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.0893492698669434})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5773494243621826})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4681330621242523})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3331594467163086})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32430192828178406})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3040997385978699})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3269551396369934})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3250589370727539})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31158167123794556})
store['active_learning_steps'][63]['training']['best_epoch']=6
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.9679, 'crossentropy': 0.2778949951171875}
store['active_learning_steps'][63]['eval_training']={}
store['active_learning_steps'][63]['eval_training']['epochs']=[]
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.854033350944519})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5361323356628418})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.44358810782432556})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3253706395626068})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3533046245574951})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3071630895137787})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.29524558782577515})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.29627326130867004})
store['active_learning_steps'][63]['eval_training']['best_epoch']=7
store['active_learning_steps'][63]['acquisition']={'indices': [43126, 57334, 52462, 24424, 12230, 36072, 31387, 28714, 57507, 49543], 'labels': [3, 7, 9, 1, -1, 2, 7, -1, 0, 8], 'scores': [0.45319169759750366, 0.42302781343460083, 0.5726226568222046, 0.38583534955978394, 0.2636938691139221, 0.399162232875824, 0.4371820092201233, 0.38565707206726074, 0.43436115980148315, 0.5133867263793945]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.2414541244506836})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6102811098098755})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4354150593280792})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.37343841791152954})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3040095269680023})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3120492100715637})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31923237442970276})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3269230127334595})
store['active_learning_steps'][64]['training']['best_epoch']=5
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.9648, 'crossentropy': 0.2933095703125}
store['active_learning_steps'][64]['eval_training']={}
store['active_learning_steps'][64]['eval_training']['epochs']=[]
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.004880666732788})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5545637607574463})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.41836535930633545})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4045582413673401})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3809414505958557})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3206043839454651})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32937002182006836})
store['active_learning_steps'][64]['eval_training']['best_epoch']=6
store['active_learning_steps'][64]['acquisition']={'indices': [3213, 19537, 5013, 39400, 49599, 5520, 5260, 34660, 22610, 54756], 'labels': [-1, -1, 2, -1, 9, -1, -1, 3, -1, 2], 'scores': [0.3837350606918335, 0.3354119062423706, 0.5447825789451599, 0.33669668436050415, 0.3211183547973633, 0.3549530506134033, 0.23144090175628662, 0.21852460503578186, 0.3841139078140259, 0.39107704162597656]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.21779203414917})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.591763436794281})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.43656742572784424})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3392064571380615})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3408202528953552})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3125668466091156})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2878723740577698})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2812579274177551})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2881414294242859})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2859724462032318})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3014577329158783})
store['active_learning_steps'][65]['training']['best_epoch']=8
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.9671, 'crossentropy': 0.2829745361328125}
store['active_learning_steps'][65]['eval_training']={}
store['active_learning_steps'][65]['eval_training']['epochs']=[]
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8437840938568115})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.5089733600616455})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3652016520500183})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3567700684070587})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31157445907592773})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3377748727798462})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3098265528678894})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26483845710754395})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2650879919528961})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.26963090896606445})
store['active_learning_steps'][65]['eval_training']['best_epoch']=8
store['active_learning_steps'][65]['acquisition']={'indices': [41989, 57448, 1075, 18307, 14305, 59731, 4647, 15696, 2574, 17814], 'labels': [-1, -1, 7, -1, -1, 5, -1, -1, -1, 6], 'scores': [0.3104638457298279, 0.2798362970352173, 0.6434370875358582, 0.5563135743141174, 0.5782597064971924, 0.5396429300308228, 0.4276738166809082, 0.42568719387054443, 0.6109491586685181, 0.5181083083152771]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.1531879901885986})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5988874435424805})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.41048651933670044})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33139151334762573})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2926684021949768})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3370986580848694})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3172072768211365})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29887014627456665})
store['active_learning_steps'][66]['training']['best_epoch']=5
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.9704, 'crossentropy': 0.273678076171875}
store['active_learning_steps'][66]['eval_training']={}
store['active_learning_steps'][66]['eval_training']['epochs']=[]
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8663382530212402})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5429947376251221})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.41188526153564453})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.36660540103912354})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31865638494491577})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3106030225753784})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.29853734374046326})
store['active_learning_steps'][66]['eval_training']['best_epoch']=7
store['active_learning_steps'][66]['acquisition']={'indices': [7706, 45658, 7310, 19338, 14255, 24040, 52358, 31242, 14972, 57718], 'labels': [-1, 3, -1, -1, -1, 7, 2, -1, 4, 7], 'scores': [0.24693667888641357, 0.42445850372314453, 0.32532167434692383, 0.2970346212387085, 0.3506704568862915, 0.3397987484931946, 0.5286175012588501, 0.24104607105255127, 0.28618496656417847, 0.46944499015808105]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.3272924423217773})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.6372295618057251})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4646035432815552})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32782816886901855})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.34029829502105713})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3274705410003662})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30688440799713135})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3255622386932373})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3218512535095215})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.32308971881866455})
store['active_learning_steps'][67]['training']['best_epoch']=7
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9693, 'crossentropy': 0.28198759765625}
store['active_learning_steps'][67]['eval_training']={}
store['active_learning_steps'][67]['eval_training']['epochs']=[]
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.9845854043960571})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5064786672592163})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.369947612285614})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.35966214537620544})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33731916546821594})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2943289577960968})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3177322745323181})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2882689833641052})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2673468589782715})
store['active_learning_steps'][67]['eval_training']['best_epoch']=9
store['active_learning_steps'][67]['acquisition']={'indices': [21029, 56914, 16690, 4735, 45501, 58882, 14054, 5244, 35401, 48243], 'labels': [-1, 0, -1, -1, -1, -1, -1, -1, 3, -1], 'scores': [0.4415382146835327, 0.5211243629455566, 0.5351412296295166, 0.33272814750671387, 0.44252753257751465, 0.3383258581161499, 0.4045614004135132, 0.4912693500518799, 0.6058699488639832, 0.3632909655570984]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.286505937576294})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.5679307579994202})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.40816211700439453})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.344102144241333})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30889320373535156})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27478671073913574})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.27728766202926636})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2956157922744751})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.27997875213623047})
store['active_learning_steps'][68]['training']['best_epoch']=6
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.9689, 'crossentropy': 0.2665549560546875}
store['active_learning_steps'][68]['eval_training']={}
store['active_learning_steps'][68]['eval_training']['epochs']=[]
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.893831729888916})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4968646764755249})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.40906548500061035})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.36478888988494873})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32587766647338867})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2767079472541809})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27189910411834717})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.30307596921920776})
store['active_learning_steps'][68]['eval_training']['best_epoch']=7
store['active_learning_steps'][68]['acquisition']={'indices': [12914, 20206, 49194, 40828, 59762, 30615, 59825, 31145, 17814, 52344], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.32084763050079346, 0.3796147108078003, 0.3355981111526489, 0.34247255325317383, 0.2961723804473877, 0.40553057193756104, 0.3535405397415161, 0.30997705459594727, 0.41242527961730957, 0.4041556119918823]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.130457878112793})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.651331901550293})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.39335137605667114})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3617645502090454})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3183993101119995})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.34375235438346863})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3125097453594208})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3139641582965851})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.30178385972976685})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.29700934886932373})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2991813123226166})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2905873656272888})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.30320441722869873})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3189317584037781})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.30287790298461914})
store['active_learning_steps'][69]['training']['best_epoch']=12
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9711, 'crossentropy': 0.271228076171875}
store['active_learning_steps'][69]['eval_training']={}
store['active_learning_steps'][69]['eval_training']['epochs']=[]
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8628356456756592})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5223805904388428})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3829396069049835})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3358655571937561})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2889975905418396})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.29842236638069153})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2790948152542114})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.25590047240257263})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2587851583957672})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2407788783311844})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.23907801508903503})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.22243821620941162})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.24441109597682953})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.23365125060081482})
store['active_learning_steps'][69]['eval_training']['best_epoch']=12
store['active_learning_steps'][69]['acquisition']={'indices': [439, 26850, 26697, 8170, 36141, 22592, 1598, 52706, 48875, 41721], 'labels': [-1, 2, -1, -1, 1, -1, -1, -1, -1, -1], 'scores': [0.4028141498565674, 0.6438656747341156, 0.5811105966567993, 0.33558881282806396, 0.5204264521598816, 0.49478596448898315, 0.6307914853096008, 0.3110945224761963, 0.4176018238067627, 0.46679019927978516]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.0973987579345703})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.561638593673706})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3589346706867218})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3093959093093872})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2913641929626465})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.26988518238067627})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.25995156168937683})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29613474011421204})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.24533972144126892})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.28482604026794434})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2900553345680237})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2672625780105591})
store['active_learning_steps'][70]['training']['best_epoch']=9
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.9705, 'crossentropy': 0.2424510009765625}
store['active_learning_steps'][70]['eval_training']={}
store['active_learning_steps'][70]['eval_training']['epochs']=[]
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9493192434310913})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.49543988704681396})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.37006232142448425})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.38870999217033386})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3045952618122101})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29401105642318726})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27190491557121277})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2579975128173828})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2547481060028076})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28895360231399536})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2590480148792267})
store['active_learning_steps'][70]['eval_training']['best_epoch']=9
store['active_learning_steps'][70]['acquisition']={'indices': [35122, 2060, 49934, 22555, 8778, 56363, 56013, 14948, 50585, 44633], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.41391319036483765, 0.4179458022117615, 0.47621285915374756, 0.4352462887763977, 0.45751047134399414, 0.3250923156738281, 0.5553025007247925, 0.49020540714263916, 0.47421956062316895, 0.4556635618209839]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.143283486366272})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5533934831619263})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4243581295013428})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3373280167579651})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29255127906799316})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3033519387245178})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27444934844970703})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.29426178336143494})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.29221728444099426})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29779309034347534})
store['active_learning_steps'][71]['training']['best_epoch']=7
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.974, 'crossentropy': 0.2544494140625}
store['active_learning_steps'][71]['eval_training']={}
store['active_learning_steps'][71]['eval_training']['epochs']=[]
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.9627896547317505})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5217756032943726})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4346863031387329})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.34658724069595337})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3312033712863922})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.33025962114334106})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2600780129432678})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3103010952472687})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2763909697532654})
store['active_learning_steps'][71]['eval_training']['best_epoch']=7
store['active_learning_steps'][71]['acquisition']={'indices': [3184, 40383, 55404, 31866, 38743, 28815, 59137, 38209, 9151, 43481], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.31528759002685547, 0.3667856454849243, 0.3864792585372925, 0.4492459297180176, 0.39727115631103516, 0.3842397928237915, 0.3675888776779175, 0.35852766036987305, 0.39166736602783203, 0.4826333522796631]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.2061039209365845})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5404979586601257})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.415353000164032})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33973395824432373})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.344784677028656})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2749008536338806})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30657467246055603})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2674388885498047})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.29815733432769775})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2876155972480774})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3268470764160156})
store['active_learning_steps'][72]['training']['best_epoch']=8
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.9685, 'crossentropy': 0.2736794189453125}
store['active_learning_steps'][72]['eval_training']={}
store['active_learning_steps'][72]['eval_training']['epochs']=[]
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9245200157165527})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5136451721191406})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3500273823738098})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2963462471961975})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29560524225234985})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3033899664878845})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28745895624160767})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31477704644203186})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2743220925331116})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2445339858531952})
store['active_learning_steps'][72]['eval_training']['best_epoch']=10
store['active_learning_steps'][72]['acquisition']={'indices': [16379, 56543, 6255, 17950, 47124, 57965, 54080, 15180, 31286, 36031], 'labels': [7, -1, -1, -1, -1, -1, -1, 4, -1, -1], 'scores': [0.4933226704597473, 0.48756372928619385, 0.4514286518096924, 0.4748889207839966, 0.5281916856765747, 0.5311905145645142, 0.46979212760925293, 0.4116714596748352, 0.4846537113189697, 0.3239288330078125]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.1251455545425415})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.5070447325706482})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.38733214139938354})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3198825716972351})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29777276515960693})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.25412294268608093})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28863030672073364})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.30504903197288513})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2932587265968323})
store['active_learning_steps'][73]['training']['best_epoch']=6
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.967, 'crossentropy': 0.2617601806640625}
store['active_learning_steps'][73]['eval_training']={}
store['active_learning_steps'][73]['eval_training']['epochs']=[]
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.98818039894104})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.6044548749923706})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4328168034553528})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.40891391038894653})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.37683388590812683})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30808115005493164})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29635438323020935})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2957618236541748})
store['active_learning_steps'][73]['eval_training']['best_epoch']=8
store['active_learning_steps'][73]['acquisition']={'indices': [20949, 19566, 18648, 7196, 53219, 52889, 56749, 47707, 36570, 24753], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.5662561655044556, 0.4544762372970581, 0.374129056930542, 0.515985369682312, 0.4250710606575012, 0.7026604413986206, 0.5087479948997498, 0.5448651313781738, 0.3769824504852295, 0.5879460573196411]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.2444998025894165})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.6153291463851929})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4294740557670593})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3506811857223511})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3370169401168823})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29866719245910645})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2971917390823364})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30667591094970703})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3088516592979431})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2945236265659332})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.29407447576522827})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.29553866386413574})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.29972612857818604})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2973872423171997})
store['active_learning_steps'][74]['training']['best_epoch']=11
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9724, 'crossentropy': 0.2734095703125}
store['active_learning_steps'][74]['eval_training']={}
store['active_learning_steps'][74]['eval_training']['epochs']=[]
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9000908732414246})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5319497585296631})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3865213990211487})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.33969759941101074})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.307734876871109})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28902554512023926})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2744957208633423})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.24538272619247437})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.23951952159404755})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.24656814336776733})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.24989554286003113})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.24735915660858154})
store['active_learning_steps'][74]['eval_training']['best_epoch']=9
store['active_learning_steps'][74]['acquisition']={'indices': [43702, 32769, 5750, 39728, 24662, 34437, 1325, 46110, 57976, 31652], 'labels': [-1, -1, 6, -1, 7, -1, -1, 8, 2, 9], 'scores': [0.28399455547332764, 0.24391257762908936, 0.2750636041164398, 0.3053741455078125, 0.48241543769836426, 0.29130327701568604, 0.28378164768218994, 0.45552384853363037, 0.47274816036224365, 0.41143763065338135]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.1402084827423096})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5894819498062134})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3694080114364624})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3420029282569885})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3103407025337219})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29030758142471313})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29478806257247925})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.30003786087036133})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28047001361846924})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.29098260402679443})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2798326015472412})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.299193799495697})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3098020553588867})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.29226014018058777})
store['active_learning_steps'][75]['training']['best_epoch']=11
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9702, 'crossentropy': 0.272996875}
store['active_learning_steps'][75]['eval_training']={}
store['active_learning_steps'][75]['eval_training']['epochs']=[]
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8588305711746216})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.5175098180770874})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3615967929363251})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27748891711235046})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.25160691142082214})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2657620310783386})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.25751376152038574})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.24103541672229767})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2213035225868225})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2224140763282776})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.21272429823875427})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2119271159172058})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.20050685107707977})
store['active_learning_steps'][75]['eval_training']['best_epoch']=13
store['active_learning_steps'][75]['acquisition']={'indices': [49481, 46742, 21981, 12880, 10576, 20792, 49339, 6050, 45918, 49540], 'labels': [-1, -1, -1, -1, -1, 9, -1, 7, -1, 7], 'scores': [0.30616211891174316, 0.2997208833694458, 0.2782963514328003, 0.3916969299316406, 0.3719162940979004, 0.5297634601593018, 0.35872554779052734, 0.67766934633255, 0.40669405460357666, 0.38852548599243164]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.1862196922302246})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.6132379174232483})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.41728490591049194})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.35629135370254517})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3357601761817932})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3154464364051819})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3226383924484253})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.26960834860801697})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2893979549407959})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.30057185888290405})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.28350645303726196})
store['active_learning_steps'][76]['training']['best_epoch']=8
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9687, 'crossentropy': 0.26724248046875}
store['active_learning_steps'][76]['eval_training']={}
store['active_learning_steps'][76]['eval_training']['epochs']=[]
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.8868274092674255})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5099928975105286})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.38271600008010864})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.321738064289093})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31644025444984436})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.29121530055999756})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2845541834831238})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2707825303077698})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.255439817905426})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.25449642539024353})
store['active_learning_steps'][76]['eval_training']['best_epoch']=10
store['active_learning_steps'][76]['acquisition']={'indices': [19085, 14670, 36267, 45115, 27812, 17810, 25498, 15407, 21174, 47407], 'labels': [-1, -1, -1, -1, 6, 3, 4, -1, 2, -1], 'scores': [0.30331695079803467, 0.29630255699157715, 0.3628467321395874, 0.2280714511871338, 0.39127618074417114, 0.49545538425445557, 0.4025942087173462, 0.4212247133255005, 0.551825225353241, 0.3616567850112915]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.1580023765563965})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5414615869522095})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.39440596103668213})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3608996272087097})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3067239224910736})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.30365318059921265})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.28074437379837036})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.28503870964050293})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3079623878002167})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.28762781620025635})
store['active_learning_steps'][77]['training']['best_epoch']=7
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9674, 'crossentropy': 0.2721392822265625}
store['active_learning_steps'][77]['eval_training']={}
store['active_learning_steps'][77]['eval_training']['epochs']=[]
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 1.0512772798538208})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5004539489746094})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.40991342067718506})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32810765504837036})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3271706998348236})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28171291947364807})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2731451094150543})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.27374187111854553})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2951279282569885})
store['active_learning_steps'][77]['eval_training']['best_epoch']=7
store['active_learning_steps'][77]['acquisition']={'indices': [15743, 42336, 50761, 27898, 3798, 50346, 5042, 28637, 50459, 30763], 'labels': [3, -1, -1, 2, 7, 8, 8, -1, 8, -1], 'scores': [0.38311195373535156, 0.4470735192298889, 0.2316819429397583, 0.4947705566883087, 0.5544439554214478, 0.3654900789260864, 0.45831501483917236, 0.27749526500701904, 0.5074620246887207, 0.4618886709213257]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.1700360774993896})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.602449893951416})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3916284441947937})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3271610736846924})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.29768818616867065})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29763010144233704})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2961118817329407})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.30254584550857544})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.25576943159103394})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.32067373394966125})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2739852964878082})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2948903441429138})
store['active_learning_steps'][78]['training']['best_epoch']=9
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9705, 'crossentropy': 0.2609343017578125}
store['active_learning_steps'][78]['eval_training']={}
store['active_learning_steps'][78]['eval_training']['epochs']=[]
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.8564660549163818})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4857984185218811})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.36208486557006836})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.28748491406440735})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2786070704460144})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2459547072649002})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26061713695526123})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26950883865356445})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.23928213119506836})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2445524036884308})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.24101844429969788})
store['active_learning_steps'][78]['eval_training']['best_epoch']=9
store['active_learning_steps'][78]['acquisition']={'indices': [48586, 30932, 21910, 30924, 14335, 41469, 23338, 24843, 31799, 49633], 'labels': [5, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.44392120838165283, 0.46558141708374023, 0.4742266535758972, 0.5517602562904358, 0.5825159549713135, 0.3132404088973999, 0.37119197845458984, 0.5351853370666504, 0.41480332612991333, 0.4586361050605774]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.3228788375854492})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5743257999420166})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.361880898475647})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.35126185417175293})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2948607802391052})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30200374126434326})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.28106921911239624})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27262216806411743})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2594132423400879})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.26085537672042847})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.25600630044937134})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.27557241916656494})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.26570039987564087})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2851746380329132})
store['active_learning_steps'][79]['training']['best_epoch']=11
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9761, 'crossentropy': 0.2293950439453125}
store['active_learning_steps'][79]['eval_training']={}
store['active_learning_steps'][79]['eval_training']['epochs']=[]
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8800419569015503})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.48359066247940063})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.40331026911735535})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.31880196928977966})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.28181424736976624})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.261647492647171})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.23367716372013092})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24871599674224854})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2361634075641632})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.22889506816864014})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.24059921503067017})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.23101806640625})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2329479306936264})
store['active_learning_steps'][79]['eval_training']['best_epoch']=10
store['active_learning_steps'][79]['acquisition']={'indices': [48804, 34532, 13776, 20419, 34032, 3030, 59437, 7812, 11708, 30704], 'labels': [-1, 2, -1, -1, -1, 9, -1, -1, -1, -1], 'scores': [0.5424067974090576, 0.4986218214035034, 0.5367427468299866, 0.3980441093444824, 0.30489611625671387, 0.4912094473838806, 0.28748857975006104, 0.3228384852409363, 0.39055049419403076, 0.46212708950042725]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.1530935764312744})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.6016062498092651})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3999263048171997})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3135315179824829})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26435771584510803})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.273131787776947})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.23445335030555725})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27483683824539185})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.25915250182151794})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.24387240409851074})
store['active_learning_steps'][80]['training']['best_epoch']=7
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.9702, 'crossentropy': 0.251819482421875}
store['active_learning_steps'][80]['eval_training']={}
store['active_learning_steps'][80]['eval_training']['epochs']=[]
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.8797521591186523})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.49868857860565186})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3945172131061554})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.33534887433052063})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.29020577669143677})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.261576771736145})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2950604259967804})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2970253825187683})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.28667140007019043})
store['active_learning_steps'][80]['eval_training']['best_epoch']=6
store['active_learning_steps'][80]['acquisition']={'indices': [13840, 10251, 26801, 37655, 25721, 9151, 21816, 59439, 40752, 26104], 'labels': [-1, -1, 7, 2, -1, -1, -1, -1, 3, -1], 'scores': [0.5827504396438599, 0.42070114612579346, 0.3280513286590576, 0.46148696541786194, 0.3794524669647217, 0.41915082931518555, 0.46898114681243896, 0.3154428005218506, 0.4578096866607666, 0.42069554328918457]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.1412632465362549})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5943042039871216})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.38139608502388})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3121876120567322})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3310156464576721})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3036169409751892})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.297247052192688})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3093082010746002})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.298198401927948})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3031778931617737})
store['active_learning_steps'][81]['training']['best_epoch']=7
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9696, 'crossentropy': 0.256437548828125}
store['active_learning_steps'][81]['eval_training']={}
store['active_learning_steps'][81]['eval_training']['epochs']=[]
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8731676936149597})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.5153183937072754})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3859599828720093})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3130159378051758})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3017800748348236})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2854193449020386})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.26230716705322266})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2870291471481323})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27146291732788086})
store['active_learning_steps'][81]['eval_training']['best_epoch']=7
store['active_learning_steps'][81]['acquisition']={'indices': [41866, 14295, 3282, 23973, 29530, 32276, 19998, 7450, 52386, 969], 'labels': [-1, -1, -1, -1, 4, 3, -1, 8, -1, -1], 'scores': [0.35631710290908813, 0.2932583689689636, 0.5537248253822327, 0.5777727365493774, 0.4697713851928711, 0.4978286623954773, 0.6190716028213501, 0.3210669159889221, 0.5902459621429443, 0.5030460357666016]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.2085264921188354})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6308306455612183})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.43656426668167114})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3460419476032257})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3459760844707489})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3110833764076233})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.28563666343688965})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.315032422542572})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.3085073232650757})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.27127406001091003})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.29352396726608276})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.30293262004852295})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2759358882904053})
store['active_learning_steps'][82]['training']['best_epoch']=10
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9705, 'crossentropy': 0.2634345458984375}
store['active_learning_steps'][82]['eval_training']={}
store['active_learning_steps'][82]['eval_training']['epochs']=[]
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9864158630371094})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.520523190498352})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.41994792222976685})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33799755573272705})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30215537548065186})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2917459011077881})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2678961157798767})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2431495487689972})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.25285133719444275})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.25289908051490784})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2463163286447525})
store['active_learning_steps'][82]['eval_training']['best_epoch']=8
store['active_learning_steps'][82]['acquisition']={'indices': [30008, 55015, 20897, 35336, 27555, 27991, 54482, 43226, 45944, 45551], 'labels': [-1, 8, 4, -1, -1, -1, -1, -1, 9, -1], 'scores': [0.33505821228027344, 0.6183515191078186, 0.4842463731765747, 0.44428861141204834, 0.2728586196899414, 0.38491618633270264, 0.412178099155426, 0.4579974412918091, 0.6058640480041504, 0.29856646060943604]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.1958123445510864})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.664336085319519})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3877975344657898})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3554273247718811})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.286414235830307})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.24682030081748962})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.26659703254699707})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.26829513907432556})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.25534090399742126})
store['active_learning_steps'][83]['training']['best_epoch']=6
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9701, 'crossentropy': 0.253900927734375}
store['active_learning_steps'][83]['eval_training']={}
store['active_learning_steps'][83]['eval_training']['epochs']=[]
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.049721598625183})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5969371199607849})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4608757495880127})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.37156569957733154})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3354203402996063})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33720487356185913})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33105751872062683})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.30852994322776794})
store['active_learning_steps'][83]['eval_training']['best_epoch']=8
store['active_learning_steps'][83]['acquisition']={'indices': [30686, 38846, 28815, 9561, 50585, 52033, 3713, 29256, 59683, 5896], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, 8], 'scores': [0.40888655185699463, 0.23517853021621704, 0.4040108919143677, 0.533000111579895, 0.4616720676422119, 0.46669530868530273, 0.4468897581100464, 0.4199258089065552, 0.39996981620788574, 0.4311332106590271]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.2099075317382812})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.6648925542831421})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.44791319966316223})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.37546855211257935})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.33520495891571045})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.26826632022857666})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2920195162296295})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.29479482769966125})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.29060691595077515})
store['active_learning_steps'][84]['training']['best_epoch']=6
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9726, 'crossentropy': 0.26299931640625}
store['active_learning_steps'][84]['eval_training']={}
store['active_learning_steps'][84]['eval_training']['epochs']=[]
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9380950927734375})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.5410782098770142})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.4536157250404358})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3734573721885681})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.33574485778808594})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28373265266418457})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2959630787372589})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.30373722314834595})
store['active_learning_steps'][84]['eval_training']['best_epoch']=6
store['active_learning_steps'][84]['acquisition']={'indices': [1795, 56174, 4961, 53353, 34665, 52834, 54846, 48404, 25011, 57154], 'labels': [-1, -1, -1, -1, 9, 2, -1, -1, -1, -1], 'scores': [0.3728269338607788, 0.4834461212158203, 0.4965234398841858, 0.2565189003944397, 0.4856712818145752, 0.5015842914581299, 0.44746434688568115, 0.4513556957244873, 0.32573968172073364, 0.2912102937698364]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.0874617099761963})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5900397300720215})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.41020888090133667})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.316089928150177})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2904358506202698})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.24697287380695343})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2803023159503937})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28135913610458374})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2677982747554779})
store['active_learning_steps'][85]['training']['best_epoch']=6
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9715, 'crossentropy': 0.2430880859375}
store['active_learning_steps'][85]['eval_training']={}
store['active_learning_steps'][85]['eval_training']['epochs']=[]
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.9860023260116577})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5670413374900818})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.463645339012146})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.39198553562164307})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30569082498550415})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3331400752067566})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.354695200920105})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3260374069213867})
store['active_learning_steps'][85]['eval_training']['best_epoch']=5
store['active_learning_steps'][85]['acquisition']={'indices': [35843, 52790, 23486, 27296, 16011, 8789, 41948, 33485, 36744, 55608], 'labels': [-1, -1, 4, 5, -1, -1, -1, -1, 1, -1], 'scores': [0.28159868717193604, 0.3551274538040161, 0.36964577436447144, 0.4397711157798767, 0.25096046924591064, 0.28350841999053955, 0.2452634572982788, 0.2868342399597168, 0.3315476179122925, 0.36365222930908203]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 1.0614150762557983})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.5438637733459473})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.401642382144928})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.35041606426239014})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31530898809432983})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27779820561408997})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2569632828235626})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2786914110183716})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.31508010625839233})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2707824409008026})
store['active_learning_steps'][86]['training']['best_epoch']=7
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.9719, 'crossentropy': 0.24221630859375}
store['active_learning_steps'][86]['eval_training']={}
store['active_learning_steps'][86]['eval_training']['epochs']=[]
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.9958117008209229})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5415045022964478})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.39582353830337524})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.33883464336395264})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.347793847322464})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2957471013069153})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2566381096839905})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2643983066082001})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.26383936405181885})
store['active_learning_steps'][86]['eval_training']['best_epoch']=7
store['active_learning_steps'][86]['acquisition']={'indices': [49262, 6686, 33086, 34186, 43005, 48704, 1024, 45274, 48543, 59844], 'labels': [-1, -1, -1, 6, -1, -1, 5, 6, -1, -1], 'scores': [0.3652125597000122, 0.36620795726776123, 0.39961719512939453, 0.2889147400856018, 0.4933938980102539, 0.3482377529144287, 0.4540787935256958, 0.37856101989746094, 0.4017442464828491, 0.3674185276031494]}
store['active_learning_steps'].append({})
store['active_learning_steps'][87]['training']={}
store['active_learning_steps'][87]['training']['epochs']=[]
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.047475814819336})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.5239005088806152})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3329591751098633})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3052940368652344})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2813952565193176})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30339425802230835})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27011314034461975})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2703651189804077})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2735457420349121})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2687584459781647})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.24894121289253235})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29064100980758667})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.26984381675720215})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.3005254864692688})
store['active_learning_steps'][87]['training']['best_epoch']=11
store['active_learning_steps'][87]['evaluation_metrics']={'accuracy': 0.974, 'crossentropy': 0.23249970703125}
store['active_learning_steps'][87]['eval_training']={}
store['active_learning_steps'][87]['eval_training']['epochs']=[]
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 1.0371811389923096})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.5132543444633484})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3919057846069336})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3010489046573639})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.28171291947364807})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2529311776161194})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.23675143718719482})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2436906397342682})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.22852012515068054})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.23828117549419403})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2230874001979828})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2338172197341919})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2109852135181427})
store['active_learning_steps'][87]['eval_training']['best_epoch']=13
store['active_learning_steps'][87]['acquisition']={'indices': [36062, 17572, 40887, 20059, 36967, 28784, 15329, 22707, 28105, 52661], 'labels': [-1, -1, -1, 4, -1, -1, -1, -1, -1, 3], 'scores': [0.2520703077316284, 0.30885446071624756, 0.2715608477592468, 0.3242720663547516, 0.45203959941864014, 0.32230186462402344, 0.4501636028289795, 0.39946961402893066, 0.47362279891967773, 0.34616613388061523]}
store['active_learning_steps'].append({})
store['active_learning_steps'][88]['training']={}
store['active_learning_steps'][88]['training']['epochs']=[]
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.2561179399490356})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5953375101089478})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3958836793899536})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34803861379623413})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3256494402885437})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30831217765808105})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27255913615226746})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.322722852230072})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29989948868751526})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3023287057876587})
store['active_learning_steps'][88]['training']['best_epoch']=7
store['active_learning_steps'][88]['evaluation_metrics']={'accuracy': 0.9684, 'crossentropy': 0.25951259765625}
store['active_learning_steps'][88]['eval_training']={}
store['active_learning_steps'][88]['eval_training']['epochs']=[]
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9714866876602173})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.573204517364502})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4013271629810333})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3474574089050293})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30929553508758545})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30305710434913635})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27541181445121765})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27361416816711426})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2787594795227051})
store['active_learning_steps'][88]['eval_training']['best_epoch']=8
store['active_learning_steps'][88]['acquisition']={'indices': [13113, 30567, 14062, 5650, 34294, 15812, 7256, 50355, 29580, 11408], 'labels': [-1, -1, 8, -1, -1, -1, -1, 6, -1, 4], 'scores': [0.45739293098449707, 0.31527483463287354, 0.46004676818847656, 0.3408224582672119, 0.17079269886016846, 0.33930158615112305, 0.32825517654418945, 0.5087270140647888, 0.30532562732696533, 0.21376585960388184]}
store['active_learning_steps'].append({})
store['active_learning_steps'][89]['training']={}
store['active_learning_steps'][89]['training']['epochs']=[]
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.1819846630096436})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5586806535720825})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.4165377616882324})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3796473741531372})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2807553708553314})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29607081413269043})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.32079169154167175})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29512351751327515})
store['active_learning_steps'][89]['training']['best_epoch']=5
store['active_learning_steps'][89]['evaluation_metrics']={'accuracy': 0.9715, 'crossentropy': 0.2737773681640625}
store['active_learning_steps'][89]['eval_training']={}
store['active_learning_steps'][89]['eval_training']['epochs']=[]
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8614209890365601})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.501524806022644})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.41435888409614563})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.37448805570602417})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3352871537208557})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3401727080345154})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.32811713218688965})
store['active_learning_steps'][89]['eval_training']['best_epoch']=7
store['active_learning_steps'][89]['acquisition']={'indices': [48350, 55913, 22687, 46523, 43524, 68, 50005, 39122, 48649, 27763], 'labels': [-1, -1, -1, -1, -1, 0, -1, -1, -1, -1], 'scores': [0.3466554880142212, 0.3166273832321167, 0.3823047876358032, 0.36210107803344727, 0.4386504888534546, 0.336040735244751, 0.28123044967651367, 0.32031047344207764, 0.30122125148773193, 0.30861222743988037]}
store['active_learning_steps'].append({})
store['active_learning_steps'][90]['training']={}
store['active_learning_steps'][90]['training']['epochs']=[]
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.2235324382781982})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.6010242700576782})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.43265414237976074})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.37319856882095337})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.312588095664978})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2732907831668854})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28818151354789734})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.275387167930603})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2627752423286438})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.30683207511901855})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2827989161014557})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2711004614830017})
store['active_learning_steps'][90]['training']['best_epoch']=9
store['active_learning_steps'][90]['evaluation_metrics']={'accuracy': 0.9669, 'crossentropy': 0.2793830078125}
store['active_learning_steps'][90]['eval_training']={}
store['active_learning_steps'][90]['eval_training']['epochs']=[]
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9194693565368652})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5455361604690552})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.4331374168395996})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3372977375984192})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3060852885246277})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.3052067756652832})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2890639305114746})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.24934238195419312})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2811540961265564})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.26061689853668213})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.29298579692840576})
store['active_learning_steps'][90]['eval_training']['best_epoch']=8
store['active_learning_steps'][90]['acquisition']={'indices': [23577, 11379, 5462, 48966, 34708, 7030, 5910, 3374, 25113, 12798], 'labels': [-1, -1, 0, 5, -1, -1, -1, 9, -1, -1], 'scores': [0.28955745697021484, 0.35218071937561035, 0.5103482007980347, 0.517355740070343, 0.296154260635376, 0.3160485029220581, 0.33423125743865967, 0.5080904960632324, 0.42370736598968506, 0.48698508739471436]}
store['active_learning_steps'].append({})
store['active_learning_steps'][91]['training']={}
store['active_learning_steps'][91]['training']['epochs']=[]
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.259080171585083})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5815950632095337})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3908756375312805})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3248441815376282})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31044143438339233})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.27894988656044006})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.25969377160072327})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2667158544063568})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27349039912223816})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2917793393135071})
store['active_learning_steps'][91]['training']['best_epoch']=7
store['active_learning_steps'][91]['evaluation_metrics']={'accuracy': 0.973, 'crossentropy': 0.245065283203125}
store['active_learning_steps'][91]['eval_training']={}
store['active_learning_steps'][91]['eval_training']['epochs']=[]
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.0267021656036377})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.584540843963623})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.4438874423503876})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3546009659767151})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3340409994125366})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3102951645851135})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.29961058497428894})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2765629291534424})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.3056674599647522})
store['active_learning_steps'][91]['eval_training']['best_epoch']=8
store['active_learning_steps'][91]['acquisition']={'indices': [39516, 53458, 21674, 28143, 21381, 38478, 56104, 46938, 46186, 57798], 'labels': [5, -1, -1, -1, -1, -1, -1, 7, -1, -1], 'scores': [0.5446131229400635, 0.45481687784194946, 0.45120787620544434, 0.6051257848739624, 0.4347422122955322, 0.3555487394332886, 0.559807538986206, 0.4114108085632324, 0.4237464666366577, 0.25413620471954346]}
store['active_learning_steps'].append({})
store['active_learning_steps'][92]['training']={}
store['active_learning_steps'][92]['training']['epochs']=[]
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.2977051734924316})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6619787216186523})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.49491626024246216})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.35967788100242615})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3234480321407318})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.300856351852417})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2604031264781952})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.28841790556907654})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2991035580635071})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30929315090179443})
store['active_learning_steps'][92]['training']['best_epoch']=7
store['active_learning_steps'][92]['evaluation_metrics']={'accuracy': 0.965, 'crossentropy': 0.2793823974609375}
store['active_learning_steps'][92]['eval_training']={}
store['active_learning_steps'][92]['eval_training']['epochs']=[]
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8929190635681152})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.5486648678779602})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.417214572429657})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.36450570821762085})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3281067907810211})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3039601147174835})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30894601345062256})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.3227306604385376})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.29709136486053467})
store['active_learning_steps'][92]['eval_training']['best_epoch']=9
store['active_learning_steps'][92]['acquisition']={'indices': [8848, 42953, 21756, 37432, 22704, 13259, 27552, 59934, 27824, 53567], 'labels': [6, 4, -1, -1, 5, 1, -1, 0, -1, -1], 'scores': [0.36528754234313965, 0.48563337326049805, 0.36537033319473267, 0.5167849063873291, 0.4741612672805786, 0.6659420728683472, 0.19528299570083618, 0.43929821252822876, 0.2783913016319275, 0.31374168395996094]}
store['active_learning_steps'].append({})
store['active_learning_steps'][93]['training']={}
store['active_learning_steps'][93]['training']['epochs']=[]
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.0993493795394897})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5729146003723145})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.42929211258888245})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3349781632423401})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2732202112674713})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27722781896591187})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2705360949039459})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2441982626914978})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.24616141617298126})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.2564569115638733})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2439657747745514})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.25286394357681274})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.2451808601617813})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2565271854400635})
store['active_learning_steps'][93]['training']['best_epoch']=11
store['active_learning_steps'][93]['evaluation_metrics']={'accuracy': 0.9738, 'crossentropy': 0.244071826171875}
store['active_learning_steps'][93]['eval_training']={}
store['active_learning_steps'][93]['eval_training']['epochs']=[]
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8955782651901245})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.534285306930542})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.38186824321746826})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.31710925698280334})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.28167903423309326})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2773963212966919})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2505887746810913})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.26163795590400696})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.978515625, 'crossentropy': 0.2437114417552948})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.23412339389324188})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.23075677454471588})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.21494770050048828})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.25239771604537964})
store['active_learning_steps'][93]['eval_training']['best_epoch']=12
store['active_learning_steps'][93]['acquisition']={'indices': [2194, 27991, 19752, 27200, 56292, 9118, 35372, 24456, 145, 59188], 'labels': [-1, -1, 5, -1, 9, 9, -1, -1, -1, -1], 'scores': [0.5208873748779297, 0.5989710092544556, 0.30432575941085815, 0.2632315754890442, 0.6521046161651611, 0.29742681980133057, 0.5254152417182922, 0.38351964950561523, 0.5392640829086304, 0.5778907537460327]}
store['active_learning_steps'].append({})
store['active_learning_steps'][94]['training']={}
store['active_learning_steps'][94]['training']['epochs']=[]
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.10709547996521})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5576894283294678})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3731535077095032})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3208228051662445})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28519192337989807})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.25927481055259705})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.255994975566864})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.25265616178512573})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.23505976796150208})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2417791336774826})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.23884990811347961})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27421194314956665})
store['active_learning_steps'][94]['training']['best_epoch']=9
store['active_learning_steps'][94]['evaluation_metrics']={'accuracy': 0.9757, 'crossentropy': 0.226458154296875}
store['active_learning_steps'][94]['eval_training']={}
store['active_learning_steps'][94]['eval_training']['epochs']=[]
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9762336015701294})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5878065824508667})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.37302014231681824})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30259108543395996})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2825336754322052})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.30222177505493164})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.258029043674469})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.25451916456222534})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2360057681798935})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.23856452107429504})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.21887192130088806})
store['active_learning_steps'][94]['eval_training']['best_epoch']=11
store['active_learning_steps'][94]['acquisition']={'indices': [43265, 15184, 42687, 36036, 31220, 49197, 31311, 42196, 21624, 7931], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.3515831232070923, 0.356441855430603, 0.4997903108596802, 0.4352925419807434, 0.3647192716598511, 0.44336235523223877, 0.44246411323547363, 0.4299203157424927, 0.47080183029174805, 0.4640236496925354]}
store['active_learning_steps'].append({})
store['active_learning_steps'][95]['training']={}
store['active_learning_steps'][95]['training']['epochs']=[]
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.0889923572540283})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5866839289665222})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.37362679839134216})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29871317744255066})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3368191421031952})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2675858736038208})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2527967393398285})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.25184351205825806})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2827056050300598})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2521245777606964})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2407776117324829})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2992255687713623})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2938496172428131})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.28125661611557007})
store['active_learning_steps'][95]['training']['best_epoch']=11
store['active_learning_steps'][95]['evaluation_metrics']={'accuracy': 0.9721, 'crossentropy': 0.237976318359375}
store['active_learning_steps'][95]['eval_training']={}
store['active_learning_steps'][95]['eval_training']['epochs']=[]
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.8452041149139404})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.48106101155281067})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3657808303833008})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.31307923793792725})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28628063201904297})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27012723684310913})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.23707351088523865})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.22944104671478271})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.22930973768234253})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.232408344745636})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2165599912405014})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24936403334140778})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.209936261177063})
store['active_learning_steps'][95]['eval_training']['best_epoch']=13
store['active_learning_steps'][95]['acquisition']={'indices': [9279, 33086, 19502, 17438, 8812, 38912, 43543, 33644, 2266, 29759], 'labels': [-1, -1, 2, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.5723344087600708, 0.3929339647293091, 0.6085907816886902, 0.34750092029571533, 0.29945337772369385, 0.5126081705093384, 0.4320566654205322, 0.44074922800064087, 0.38843512535095215, 0.3423619270324707]}
store['active_learning_steps'].append({})
store['active_learning_steps'][96]['training']={}
store['active_learning_steps'][96]['training']['epochs']=[]
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.1691733598709106})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5909801721572876})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.46941593289375305})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3301461338996887})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2899513840675354})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2800742983818054})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.26355093717575073})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2678573727607727})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2387932538986206})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2652362585067749})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.28237462043762207})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3084123134613037})
store['active_learning_steps'][96]['training']['best_epoch']=9
store['active_learning_steps'][96]['evaluation_metrics']={'accuracy': 0.9725, 'crossentropy': 0.2421573486328125}
store['active_learning_steps'][96]['eval_training']={}
store['active_learning_steps'][96]['eval_training']['epochs']=[]
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.0305200815200806})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5288572311401367})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.37560999393463135})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32243743538856506})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33839261531829834})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2796470522880554})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2875916659832001})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2749031186103821})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.27155232429504395})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.25437819957733154})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.23976989090442657})
store['active_learning_steps'][96]['eval_training']['best_epoch']=11
store['active_learning_steps'][96]['acquisition']={'indices': [514, 5180, 33372, 21218, 53941, 5679, 29839, 21579, 7384, 7395], 'labels': [-1, -1, -1, -1, -1, 3, -1, -1, -1, -1], 'scores': [0.4476855993270874, 0.37165582180023193, 0.5292603969573975, 0.4802093505859375, 0.34374475479125977, 0.4662191867828369, 0.4393373727798462, 0.4122202396392822, 0.2894829511642456, 0.3881872892379761]}
store['active_learning_steps'].append({})
store['active_learning_steps'][97]['training']={}
store['active_learning_steps'][97]['training']['epochs']=[]
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.283012866973877})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.6096553802490234})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.48888975381851196})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.35980096459388733})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3280125856399536})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2894149422645569})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.28053218126296997})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28744351863861084})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.26364296674728394})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2876768708229065})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2513858675956726})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.29650476574897766})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2792442739009857})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3060603737831116})
store['active_learning_steps'][97]['training']['best_epoch']=11
store['active_learning_steps'][97]['evaluation_metrics']={'accuracy': 0.9705, 'crossentropy': 0.269085400390625}
store['active_learning_steps'][97]['eval_training']={}
store['active_learning_steps'][97]['eval_training']['epochs']=[]
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 1.015582799911499})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.5307931303977966})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4354931712150574})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3266254961490631})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2966882586479187})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.272751122713089})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.24989275634288788})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2644384205341339})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.22826707363128662})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2628822922706604})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.24428790807724})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.22937804460525513})
store['active_learning_steps'][97]['eval_training']['best_epoch']=9
store['active_learning_steps'][97]['acquisition']={'indices': [12263, 18125, 20578, 51939, 50517, 59080, 5220, 42212, 53753, 59681], 'labels': [-1, -1, 8, -1, -1, -1, -1, -1, 4, 0], 'scores': [0.5247926115989685, 0.4219832420349121, 0.49465739727020264, 0.6620999574661255, 0.5665592551231384, 0.25326454639434814, 0.3909735679626465, 0.47980940341949463, 0.6851059198379517, 0.7762438356876373]}
store['active_learning_steps'].append({})
store['active_learning_steps'][98]['training']={}
store['active_learning_steps'][98]['training']['epochs']=[]
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.1833322048187256})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.6085608005523682})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.4115491211414337})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3238027095794678})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.35950177907943726})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.29133141040802})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26514917612075806})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27046340703964233})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28354203701019287})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.24749809503555298})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2901676893234253})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2707197964191437})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.257310688495636})
store['active_learning_steps'][98]['training']['best_epoch']=10
store['active_learning_steps'][98]['evaluation_metrics']={'accuracy': 0.9722, 'crossentropy': 0.25576044921875}
store['active_learning_steps'][98]['eval_training']={}
store['active_learning_steps'][98]['eval_training']['epochs']=[]
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9339601397514343})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.5209939479827881})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3767617344856262})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3256663680076599})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29320380091667175})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2745482623577118})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2520847022533417})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.271579384803772})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.25589510798454285})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.243058979511261})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.24701035022735596})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.26550519466400146})
store['active_learning_steps'][98]['eval_training']['best_epoch']=10
store['active_learning_steps'][98]['acquisition']={'indices': [12343, 38252, 19378, 58982, 48330, 36985, 33572, 38822, 20746, 55778], 'labels': [-1, 5, -1, -1, 9, -1, 6, 4, 1, -1], 'scores': [0.5508977174758911, 0.6123247742652893, 0.5113992691040039, 0.3265054225921631, 0.47148025035858154, 0.6776623725891113, 0.36008405685424805, 0.3989364504814148, 0.36778825521469116, 0.5354892015457153]}
store['active_learning_steps'].append({})
store['active_learning_steps'][99]['training']={}
store['active_learning_steps'][99]['training']['epochs']=[]
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.1303606033325195})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.5468865633010864})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.35662391781806946})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28295087814331055})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2809370756149292})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.25386863946914673})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2587815523147583})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.260311096906662})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.26004558801651})
store['active_learning_steps'][99]['training']['best_epoch']=6
store['active_learning_steps'][99]['evaluation_metrics']={'accuracy': 0.9741, 'crossentropy': 0.235492578125}
store['active_learning_steps'][99]['eval_training']={}
store['active_learning_steps'][99]['eval_training']['epochs']=[]
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9221974611282349})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4983299970626831})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.369283527135849})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32993602752685547})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2884528636932373})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.33627864718437195})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28884679079055786})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.24118655920028687})
store['active_learning_steps'][99]['eval_training']['best_epoch']=8
store['active_learning_steps'][99]['acquisition']={'indices': [45758, 13995, 28822, 35010, 39311, 25411, 19537, 31873, 57256, 44597], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.429932177066803, 0.5939949154853821, 0.4190260171890259, 0.4346635341644287, 0.32683730125427246, 0.4964176416397095, 0.4609224796295166, 0.44155585765838623, 0.5597596168518066, 0.4964487552642822]}
store['active_learning_steps'].append({})
store['active_learning_steps'][100]['training']={}
store['active_learning_steps'][100]['training']['epochs']=[]
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.0932807922363281})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.5932317972183228})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3843850791454315})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3296549916267395})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.29135411977767944})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.978515625, 'crossentropy': 0.24090687930583954})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.24204093217849731})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.24300408363342285})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2486693263053894})
store['active_learning_steps'][100]['training']['best_epoch']=6
store['active_learning_steps'][100]['evaluation_metrics']={'accuracy': 0.9772, 'crossentropy': 0.2322454345703125}
store['active_learning_steps'][100]['eval_training']={}
store['active_learning_steps'][100]['eval_training']['epochs']=[]
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8626708984375})
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.49770212173461914})
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3838636875152588})
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.32377302646636963})
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3123664855957031})
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.30153393745422363})
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.281283438205719})
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.29000043869018555})
store['active_learning_steps'][100]['eval_training']['best_epoch']=7
store['active_learning_steps'][100]['acquisition']={'indices': [36353, 46218, 17552, 8940, 13105, 42258, 47019, 13816, 43588, 5483], 'labels': [-1, -1, -1, 6, -1, -1, -1, -1, 8, -1], 'scores': [0.2842615842819214, 0.4178491234779358, 0.39139091968536377, 0.3165365159511566, 0.3364689350128174, 0.376517117023468, 0.4084389805793762, 0.30787694454193115, 0.42665529251098633, 0.27562808990478516]}
store['active_learning_steps'].append({})
store['active_learning_steps'][101]['training']={}
store['active_learning_steps'][101]['training']['epochs']=[]
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.215802550315857})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6273514032363892})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.4049120247364044})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.3214818239212036})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2705114483833313})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2659180462360382})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.24935382604599})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.265497624874115})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.24989822506904602})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.23354198038578033})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.25372469425201416})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2583637237548828})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.25200074911117554})
store['active_learning_steps'][101]['training']['best_epoch']=10
store['active_learning_steps'][101]['evaluation_metrics']={'accuracy': 0.9753, 'crossentropy': 0.2324740966796875}
