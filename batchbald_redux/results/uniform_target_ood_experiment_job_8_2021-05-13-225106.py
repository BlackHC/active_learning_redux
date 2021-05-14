store = {}
store['timestamp']=1620942666
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=8']
store['commit']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['github_url']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=8
store['worker_id']=8
store['num_workers']=20
store['config']={'seed': 1246, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'evaluation_set_size': 100, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
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
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 37321], ['id', 49877], ['id', 41143], ['id', 31334], ['id', 50806], ['id', 58024], ['id', 10443], ['id', 17643], ['id', 49562], ['id', 57407]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9503889083862305, 0.637075662612915, 1.0299944877624512, 0.669225811958313, 0.9770993590354919, 0.6969566941261292, 0.8811866641044617, 0.6495200395584106, 0.9916349649429321, 0.9756933450698853]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.9207805395126343})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 2.2094578742980957})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.3871724605560303})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 2.790640354156494})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7455, 'crossentropy': 1.792403515625}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.0746259689331055})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.0604276657104492})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 0.9965052604675293})
store['active_learning_steps'][1]['eval_training']['best_epoch']=3
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 25271], ['ood', 47083], ['ood', 14981], ['id', 2513], ['id', 25301], ['id', 37037], ['id', 15731], ['id', 18238], ['id', 48892], ['id', 25762]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6680670976638794, 0.412328839302063, 0.6447278261184692, 0.7833961844444275, 0.8398984670639038, 0.7613622546195984, 0.7673707008361816, 0.6906751394271851, 0.4986257553100586, 0.5756090879440308]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.3083090782165527})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.4794666767120361})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.7448444366455078})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.8591853380203247})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7618, 'crossentropy': 1.2805818359375}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 0.956170916557312})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 0.8851299285888672})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 0.861024796962738})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 12548], ['id', 10255], ['id', 44360], ['id', 2775], ['id', 43588], ['id', 23169], ['id', 57532], ['id', 54898], ['id', 894], ['id', 528]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.579854428768158, 0.6799008846282959, 0.5040931701660156, 0.6292098760604858, 0.5127610564231873, 0.6646294593811035, 0.5754112005233765, 0.49705368280410767, 0.4590708613395691, 0.5835574269294739]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.2134790420532227})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.3607617616653442})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.3707764148712158})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.3918406963348389})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7841, 'crossentropy': 1.1324818359375}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 0.9458180665969849})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 0.9105566740036011})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 0.8426686525344849})
store['active_learning_steps'][3]['eval_training']['best_epoch']=3
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 8489], ['id', 17755], ['id', 3044], ['id', 27271], ['id', 57411], ['id', 57916], ['id', 59259], ['id', 3772], ['id', 16826], ['id', 3862]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5305608510971069, 0.43841463327407837, 0.421400249004364, 0.418021559715271, 0.41897910833358765, 0.734970211982727, 0.5051214694976807, 0.5798925757408142, 0.5498694777488708, 0.5396063923835754]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.0512025356292725})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.1769812107086182})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.2944920063018799})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.4191176891326904})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.8297, 'crossentropy': 0.9296935546875}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.7999095916748047})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8001620769500732})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.7829864025115967})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 52782], ['id', 29935], ['id', 17483], ['id', 25391], ['ood', 7072], ['id', 38316], ['id', 37811], ['id', 44163], ['id', 26511], ['id', 21315]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5228708982467651, 0.4398697018623352, 0.42457646131515503, 0.5435324907302856, 0.27443063259124756, 0.46453362703323364, 0.5925872325897217, 0.43995773792266846, 0.7250953912734985, 0.7631377577781677]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9176164865493774})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.9851292371749878})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.1207258701324463})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.1732122898101807})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8381, 'crossentropy': 0.84205087890625}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8804433345794678})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.8222653865814209})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.7682540416717529})
store['active_learning_steps'][5]['eval_training']['best_epoch']=3
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 37758], ['id', 44998], ['id', 48665], ['id', 903], ['id', 45845], ['id', 46874], ['id', 53019], ['id', 45836], ['id', 33009], ['id', 22310]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5222876071929932, 0.48971760272979736, 0.7107824087142944, 0.5800172090530396, 0.5038665533065796, 0.3738689422607422, 0.639578104019165, 0.33909326791763306, 0.45667093992233276, 0.2939084768295288]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8120237588882446})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8690600395202637})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.9126182794570923})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.1613187789916992})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8593, 'crossentropy': 0.765696435546875}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.8546030521392822})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.7591065168380737})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.7646989822387695})
store['active_learning_steps'][6]['eval_training']['best_epoch']=2
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 22083], ['id', 10062], ['id', 35332], ['id', 17958], ['id', 11218], ['id', 32290], ['id', 59784], ['id', 58470], ['id', 19229], ['id', 4514]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4708365201950073, 0.3132111430168152, 0.3690073490142822, 0.5332069396972656, 0.35702985525131226, 0.3685067296028137, 0.36957240104675293, 0.529119610786438, 0.42985910177230835, 0.3722672462463379]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.8934364318847656})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8668423891067505})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.9485018253326416})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.0837494134902954})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9789315462112427})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8642, 'crossentropy': 0.74650126953125}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.8201300501823425})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.672035813331604})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.6276528835296631})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.6047619581222534})
store['active_learning_steps'][7]['eval_training']['best_epoch']=4
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 4445], ['id', 57315], ['id', 56824], ['id', 20073], ['id', 16754], ['id', 35628], ['id', 2426], ['id', 26898], ['id', 2663], ['id', 21150]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.49629175662994385, 0.37654948234558105, 0.3945046067237854, 0.43259844183921814, 0.42888474464416504, 0.49094200134277344, 0.512672483921051, 0.44718295335769653, 0.4327737092971802, 0.4279289245605469]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8689695000648499})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7107424736022949})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.671595573425293})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7682493925094604})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8060201406478882})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8276880383491516})
store['active_learning_steps'][8]['training']['best_epoch']=3
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.9082, 'crossentropy': 0.569143701171875}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.6983259916305542})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5702087879180908})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5062671899795532})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.4992043673992157})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.4616813063621521})
store['active_learning_steps'][8]['eval_training']['best_epoch']=5
store['active_learning_steps'][8]['acquisition']={'indices': [['ood', 7502], ['id', 46872], ['id', 1390], ['id', 43167], ['id', 56643], ['id', 47510], ['id', 43326], ['id', 29711], ['ood', 14226], ['id', 14902]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.2914154529571533, 0.5739629864692688, 0.5088227987289429, 0.41875410079956055, 0.4747747778892517, 0.4706608057022095, 0.4615591764450073, 0.4183017611503601, 0.49131953716278076, 0.5592600107192993]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8986526727676392})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7610609531402588})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7687535285949707})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7091920375823975})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7991055250167847})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.8091074228286743})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8594173192977905})
store['active_learning_steps'][9]['training']['best_epoch']=4
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.9028, 'crossentropy': 0.607389306640625}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.6862391233444214})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.5745947360992432})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5294653177261353})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.5375407934188843})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.4860405921936035})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.4970936179161072})
store['active_learning_steps'][9]['eval_training']['best_epoch']=5
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 56122], ['id', 969], ['id', 19148], ['id', 53873], ['id', 2659], ['id', 44269], ['id', 31665], ['id', 13720], ['id', 44050], ['id', 18003]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3182275593280792, 0.535396546125412, 0.4060819149017334, 0.45524710416793823, 0.4247252941131592, 0.2646939158439636, 0.3422567546367645, 0.49275854229927063, 0.5743677616119385, 0.522247314453125]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7779489755630493})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5986988544464111})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6102890968322754})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5686594247817993})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6830483078956604})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6199880838394165})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6642601490020752})
store['active_learning_steps'][10]['training']['best_epoch']=4
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.9227, 'crossentropy': 0.493274462890625}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.684886634349823})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5534718036651611})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.4756971001625061})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4333885908126831})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.43565690517425537})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.40919429063796997})
store['active_learning_steps'][10]['eval_training']['best_epoch']=6
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 8680], ['id', 41141], ['ood', 50403], ['id', 11904], ['id', 47792], ['id', 14540], ['id', 29911], ['id', 4723], ['id', 24363], ['id', 59502]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5102892518043518, 0.4805789887905121, 0.6171473860740662, 0.4325542449951172, 0.4483940601348877, 0.519239068031311, 0.4729991555213928, 0.39009934663772583, 0.5214701294898987, 0.3122355341911316]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7864419221878052})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5388054847717285})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.489377498626709})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5033013820648193})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5052840113639832})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.542500376701355})
store['active_learning_steps'][11]['training']['best_epoch']=3
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.9296, 'crossentropy': 0.446876318359375}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7131713032722473})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.482166588306427})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.43316173553466797})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4100746512413025})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.39317232370376587})
store['active_learning_steps'][11]['eval_training']['best_epoch']=5
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 54994], ['id', 45784], ['id', 18240], ['id', 50461], ['id', 8228], ['id', 23452], ['id', 26544], ['id', 57334], ['id', 47909], ['id', 20006]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4293220639228821, 0.4519326090812683, 0.499411940574646, 0.5344184637069702, 0.5140660405158997, 0.41515326499938965, 0.23472774028778076, 0.4489021301269531, 0.3234862983226776, 0.5164516568183899]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8259590268135071})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5562646389007568})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.505317747592926})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.49662065505981445})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.493074893951416})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5501710772514343})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5398591160774231})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5398737192153931})
store['active_learning_steps'][12]['training']['best_epoch']=5
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9315, 'crossentropy': 0.456482275390625}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6445859670639038})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.47661906480789185})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.42384594678878784})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.42009252309799194})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.3865610957145691})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.3950663208961487})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.36064016819000244})
store['active_learning_steps'][12]['eval_training']['best_epoch']=7
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 53728], ['id', 7732], ['id', 5303], ['id', 4530], ['id', 15743], ['id', 57882], ['id', 14843], ['id', 9348], ['id', 55311], ['id', 13923]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4407099485397339, 0.42439132928848267, 0.5382540822029114, 0.45543140172958374, 0.35899817943573, 0.5667896866798401, 0.5081213712692261, 0.2810318171977997, 0.5067835450172424, 0.42902690172195435]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7665713429450989})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.46186476945877075})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.48981258273124695})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5171739459037781})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.46793943643569946})
store['active_learning_steps'][13]['training']['best_epoch']=2
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.9281, 'crossentropy': 0.455042626953125}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6816718578338623})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5280922651290894})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4866371154785156})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.46472030878067017})
store['active_learning_steps'][13]['eval_training']['best_epoch']=4
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 44901], ['ood', 16180], ['id', 18998], ['id', 44496], ['id', 59726], ['id', 39378], ['id', 19380], ['id', 27183], ['id', 11781], ['id', 55011]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.44035327434539795, 0.23543846607208252, 0.47745048999786377, 0.4468842148780823, 0.30990391969680786, 0.332990825176239, 0.379371702671051, 0.34897249937057495, 0.2603682279586792, 0.3949296474456787]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8344486951828003})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6082475781440735})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5408104062080383})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5910910367965698})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6222571134567261})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6415003538131714})
store['active_learning_steps'][14]['training']['best_epoch']=3
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9277, 'crossentropy': 0.498945947265625}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7805726528167725})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5513481497764587})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4836454689502716})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4516568183898926})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.43514785170555115})
store['active_learning_steps'][14]['eval_training']['best_epoch']=5
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 40636], ['id', 46728], ['ood', 47700], ['id', 14793], ['id', 57767], ['ood', 52744], ['id', 137], ['id', 21420], ['id', 22964], ['id', 39034]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.5371424555778503, 0.4874250292778015, 0.33607280254364014, 0.5142635107040405, 0.5314486026763916, 0.40902507305145264, 0.5749621987342834, 0.4783284664154053, 0.48640531301498413, 0.512712836265564]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8825708627700806})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5424818992614746})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4805978536605835})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.45605775713920593})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4914264678955078})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.49126455187797546})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.49276256561279297})
store['active_learning_steps'][15]['training']['best_epoch']=4
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9374, 'crossentropy': 0.4082849365234375}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7516048550605774})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5185341835021973})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.43868815898895264})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.411601185798645})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.39414525032043457})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.37325766682624817})
store['active_learning_steps'][15]['eval_training']['best_epoch']=6
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 8617], ['id', 5063], ['id', 19501], ['id', 39305], ['id', 17231], ['id', 37440], ['ood', 57552], ['id', 29712], ['id', 52968], ['id', 54264]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.44660452008247375, 0.43498700857162476, 0.46475380659103394, 0.3940473198890686, 0.3885996341705322, 0.3538166284561157, 0.17108500003814697, 0.4693969488143921, 0.5044918656349182, 0.2837420105934143]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8853012323379517})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5092498064041138})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4355062246322632})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4423753023147583})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.46703386306762695})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.44793766736984253})
store['active_learning_steps'][16]['training']['best_epoch']=3
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9338, 'crossentropy': 0.4375802734375}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8532588481903076})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4858115315437317})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4470479190349579})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.39633479714393616})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.38811179995536804})
store['active_learning_steps'][16]['eval_training']['best_epoch']=5
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 49968], ['id', 54212], ['id', 55876], ['id', 38970], ['id', 24479], ['id', 182], ['id', 29763], ['id', 22631], ['id', 18397], ['id', 42363]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.27382320165634155, 0.3923085927963257, 0.3546041250228882, 0.30847764015197754, 0.47029733657836914, 0.49629586935043335, 0.3685636520385742, 0.3861541748046875, 0.37425291538238525, 0.2961905002593994]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8620142936706543})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5177309513092041})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4265734553337097})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4466094970703125})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.43723440170288086})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4323887526988983})
store['active_learning_steps'][17]['training']['best_epoch']=3
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9386, 'crossentropy': 0.422034912109375}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6696212887763977})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.499597430229187})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4868333339691162})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.44618409872055054})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.42157959938049316})
store['active_learning_steps'][17]['eval_training']['best_epoch']=5
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 13942], ['id', 14305], ['id', 9368], ['id', 11304], ['id', 35206], ['id', 30088], ['id', 8668], ['id', 8552], ['id', 21355], ['id', 27209]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.37836265563964844, 0.3670165538787842, 0.44936615228652954, 0.5305304527282715, 0.2928192615509033, 0.4409855604171753, 0.5281049013137817, 0.4282658100128174, 0.3889830708503723, 0.43809056282043457]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8753160238265991})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5082443952560425})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4847429394721985})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.43428513407707214})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.42048513889312744})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.49166083335876465})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4163777232170105})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4632232189178467})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.44596055150032043})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.43387526273727417})
store['active_learning_steps'][18]['training']['best_epoch']=7
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9452, 'crossentropy': 0.3954029541015625}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7291786670684814})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.477375328540802})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.40743744373321533})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.376981258392334})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.36121663451194763})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.35997623205184937})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.33336567878723145})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.34220921993255615})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3575461506843567})
store['active_learning_steps'][18]['eval_training']['best_epoch']=7
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 37048], ['id', 28136], ['id', 45800], ['id', 44948], ['id', 26391], ['id', 16985], ['id', 17872], ['id', 50802], ['id', 39262], ['id', 42199]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6957836747169495, 0.5419381260871887, 0.42180103063583374, 0.6488596796989441, 0.46557968854904175, 0.2528371512889862, 0.4812358617782593, 0.5853358507156372, 0.2724453806877136, 0.5397651791572571]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 1.0004019737243652})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5036149024963379})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.42232322692871094})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.41504502296447754})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4080120027065277})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4140663146972656})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.44420191645622253})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3925440013408661})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5139015913009644})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4021851718425751})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4569363594055176})
store['active_learning_steps'][19]['training']['best_epoch']=8
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9523, 'crossentropy': 0.3696292724609375}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6755072474479675})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4086262583732605})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.36628642678260803})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.325503945350647})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.33092060685157776})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.30724769830703735})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3103886842727661})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3041846752166748})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2799729108810425})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.29856717586517334})
store['active_learning_steps'][19]['eval_training']['best_epoch']=9
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 10982], ['id', 54030], ['id', 42973], ['id', 40873], ['id', 47879], ['id', 6418], ['id', 30507], ['id', 27175], ['id', 34058], ['id', 34135]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.3896484076976776, 0.5103603601455688, 0.41634345054626465, 0.5910547375679016, 0.5738919377326965, 0.5608580112457275, 0.5543120503425598, 0.33396561443805695, 0.5220668911933899, 0.3434038758277893]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8050215244293213})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5230639576911926})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.44446462392807007})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4155910313129425})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3839150071144104})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4382748007774353})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.42111343145370483})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4651036858558655})
store['active_learning_steps'][20]['training']['best_epoch']=5
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.949, 'crossentropy': 0.362989453125}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7794874906539917})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.44140052795410156})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4084974527359009})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.37733572721481323})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3396527171134949})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3320249021053314})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3308429718017578})
store['active_learning_steps'][20]['eval_training']['best_epoch']=7
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 47597], ['id', 51552], ['id', 34608], ['id', 41276], ['id', 56460], ['id', 21040], ['id', 30077], ['id', 50417], ['id', 34932], ['id', 34847]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4132482409477234, 0.3960638642311096, 0.3523305058479309, 0.32510077953338623, 0.4910096526145935, 0.3891613483428955, 0.5162323713302612, 0.40554195642471313, 0.4276742935180664, 0.6264737844467163]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.918591320514679})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5020884871482849})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.42208385467529297})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.394980251789093})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.40673989057540894})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3753622770309448})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.38761430978775024})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3940672278404236})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.408816933631897})
store['active_learning_steps'][21]['training']['best_epoch']=6
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9535, 'crossentropy': 0.3477353759765625}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7848472595214844})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.47863268852233887})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3767128586769104})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3561420142650604})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3714967966079712})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33881646394729614})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3206862509250641})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.30975839495658875})
store['active_learning_steps'][21]['eval_training']['best_epoch']=8
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 8709], ['id', 42715], ['id', 19852], ['id', 59370], ['id', 46714], ['id', 22532], ['id', 1236], ['id', 53435], ['id', 52086], ['id', 20641]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.5625176429748535, 0.4986005425453186, 0.28019723296165466, 0.37751370668411255, 0.5720869898796082, 0.3426729440689087, 0.5204900503158569, 0.3511064052581787, 0.4032784700393677, 0.5755831599235535]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.9544910192489624})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.515275239944458})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4538690745830536})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.49636802077293396})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.44147926568984985})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.40934088826179504})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4104292392730713})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.40645694732666016})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.46466121077537537})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.47566676139831543})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4296222925186157})
store['active_learning_steps'][22]['training']['best_epoch']=8
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9458, 'crossentropy': 0.413226220703125}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8546817302703857})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5276175737380981})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4173298180103302})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3807079792022705})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3625496029853821})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.31460046768188477})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.308992475271225})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3274686336517334})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.32631945610046387})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3143014907836914})
store['active_learning_steps'][22]['eval_training']['best_epoch']=7
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 53552], ['id', 44040], ['id', 19590], ['id', 52890], ['id', 32391], ['id', 57742], ['ood', 41378], ['id', 43820], ['id', 57323], ['id', 19430]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3966524600982666, 0.4846000075340271, 0.4517894983291626, 0.572619765996933, 0.33148717880249023, 0.5796014070510864, 0.4740539789199829, 0.3755585551261902, 0.3519176244735718, 0.35462456941604614]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.1002928018569946})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4817672371864319})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3893916606903076})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.44313621520996094})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.38698095083236694})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.37151002883911133})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3663865327835083})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4141644537448883})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.41478317975997925})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4144437611103058})
store['active_learning_steps'][23]['training']['best_epoch']=7
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9524, 'crossentropy': 0.3581927001953125}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7692464590072632})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5137991309165955})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4065382480621338})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3773954510688782})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3533340096473694})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.33947086334228516})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3195694088935852})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2935636043548584})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3198554217815399})
store['active_learning_steps'][23]['eval_training']['best_epoch']=8
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 26588], ['id', 54196], ['id', 2447], ['id', 26429], ['id', 37779], ['id', 43560], ['id', 2148], ['id', 41371], ['id', 54943], ['id', 11848]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4558227062225342, 0.5274243354797363, 0.3445216417312622, 0.3421170115470886, 0.1947976052761078, 0.3971097469329834, 0.5228103399276733, 0.6363728642463684, 0.3337918519973755, 0.2863469123840332]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9927641749382019})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5251950025558472})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4151118993759155})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4093908965587616})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3776685297489166})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.39797672629356384})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3659912347793579})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.40230149030685425})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4139484167098999})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4178604483604431})
store['active_learning_steps'][24]['training']['best_epoch']=7
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9531, 'crossentropy': 0.36093701171875}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8694626688957214})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5149912238121033})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.39740249514579773})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.35160312056541443})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.35605379939079285})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3275149464607239})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.30787238478660583})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3138885498046875})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3083515167236328})
store['active_learning_steps'][24]['eval_training']['best_epoch']=7
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 30885], ['id', 37213], ['id', 50403], ['id', 2434], ['id', 23502], ['id', 7793], ['id', 9147], ['id', 52800], ['id', 18739], ['id', 19833]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.40436387062072754, 0.45092082023620605, 0.4927213191986084, 0.37872421741485596, 0.47210317850112915, 0.37810736894607544, 0.44503116607666016, 0.4765127897262573, 0.35608360171318054, 0.23938480019569397]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9548384547233582})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.47916796803474426})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.40460073947906494})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.40421155095100403})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3458545207977295})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32800352573394775})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3219965398311615})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3235257863998413})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3372003436088562})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3691503405570984})
store['active_learning_steps'][25]['training']['best_epoch']=7
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9601, 'crossentropy': 0.3068120849609375}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7816240787506104})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4642203450202942})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4034106135368347})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3456445336341858})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3096655309200287})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.282711923122406})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.30083441734313965})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2709037661552429})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2751043438911438})
store['active_learning_steps'][25]['eval_training']['best_epoch']=8
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 19546], ['id', 4005], ['id', 15137], ['id', 54628], ['ood', 32429], ['id', 5259], ['id', 4058], ['id', 42181], ['id', 19111], ['ood', 48028]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.6366485357284546, 0.47435593605041504, 0.4534316807985306, 0.4351308345794678, 0.2880537509918213, 0.4635249376296997, 0.5584672689437866, 0.5212457180023193, 0.516015887260437, 0.33948880434036255]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9410953521728516})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.48287397623062134})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3796825110912323})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.32514894008636475})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3555498719215393})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3299190104007721})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3206248879432678})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31366240978240967})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.381649374961853})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3501824140548706})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3333757221698761})
store['active_learning_steps'][26]['training']['best_epoch']=8
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9617, 'crossentropy': 0.29742333984375}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7704443335533142})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.48226743936538696})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3591880202293396})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3500387668609619})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.32402122020721436})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3216697871685028})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3034529685974121})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3096923232078552})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.29035699367523193})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.29776954650878906})
store['active_learning_steps'][26]['eval_training']['best_epoch']=9
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 17082], ['id', 57212], ['id', 23077], ['id', 14096], ['id', 43609], ['id', 45622], ['id', 57378], ['id', 32519], ['id', 29142], ['id', 5790]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3318605124950409, 0.3285329341888428, 0.4611731171607971, 0.4088655114173889, 0.5308976769447327, 0.5809510946273804, 0.41163069009780884, 0.6526618599891663, 0.4227311611175537, 0.47113341093063354]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9737293720245361})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5232166051864624})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.37999284267425537})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3677278757095337})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3792862296104431})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.37020668387413025})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4064999222755432})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9574, 'crossentropy': 0.319389599609375}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.806675910949707})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.45513731241226196})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4195947051048279})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.39248228073120117})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3694881200790405})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3554948568344116})
store['active_learning_steps'][27]['eval_training']['best_epoch']=6
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 52524], ['id', 7142], ['id', 44308], ['id', 32930], ['id', 11889], ['id', 15620], ['id', 5136], ['id', 44342], ['id', 31124], ['id', 1518]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.3733103275299072, 0.36201292276382446, 0.4859555959701538, 0.45880645513534546, 0.5552089214324951, 0.243569016456604, 0.34023886919021606, 0.4725908041000366, 0.6187466979026794, 0.5421283841133118]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9311671257019043})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5378902554512024})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4564260244369507})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4116526246070862})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3710852265357971})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.35903775691986084})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3455314040184021})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3459694981575012})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3778899610042572})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4180159568786621})
store['active_learning_steps'][28]['training']['best_epoch']=7
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9591, 'crossentropy': 0.300285693359375}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7378294467926025})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4621584415435791})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.38409653306007385})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3586809039115906})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3218991756439209})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30419719219207764})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32758527994155884})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.30525198578834534})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.26648133993148804})
store['active_learning_steps'][28]['eval_training']['best_epoch']=9
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 35754], ['id', 32906], ['id', 12089], ['id', 55893], ['id', 46197], ['id', 45026], ['id', 45888], ['id', 32208], ['id', 39411], ['id', 19098]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.5067055821418762, 0.5031620264053345, 0.3814193606376648, 0.46991419792175293, 0.5163261294364929, 0.5631304979324341, 0.42743849754333496, 0.4416203498840332, 0.31600064039230347, 0.4365507960319519]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.1221592426300049})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.47828584909439087})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35295382142066956})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.32978349924087524})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32833027839660645})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.34308385848999023})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32959043979644775})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.334949254989624})
store['active_learning_steps'][29]['training']['best_epoch']=5
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9625, 'crossentropy': 0.2998043212890625}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.886742353439331})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.507153332233429})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3931529223918915})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.39619284868240356})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.38489222526550293})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.33754947781562805})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.30749571323394775})
store['active_learning_steps'][29]['eval_training']['best_epoch']=7
store['active_learning_steps'][29]['acquisition']={'indices': [['ood', 9293], ['id', 49890], ['id', 7259], ['id', 134], ['ood', 51375], ['ood', 57221], ['id', 12752], ['id', 4887], ['id', 16875], ['id', 40240]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.217626690864563, 0.490963339805603, 0.3560006022453308, 0.6001821160316467, 0.2908484935760498, 0.5000216364860535, 0.35935497283935547, 0.43649590015411377, 0.2791353464126587, 0.4053828716278076]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.9274889230728149})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5007433295249939})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4047645330429077})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3621998429298401})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33059731125831604})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.33067142963409424})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3169274628162384})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.31720399856567383})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3276667594909668})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33434534072875977})
store['active_learning_steps'][30]['training']['best_epoch']=7
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9612, 'crossentropy': 0.2744443603515625}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.791301965713501})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.506239652633667})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3810717463493347})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3641843795776367})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.35440483689308167})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.27673953771591187})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2957201302051544})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.29968953132629395})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.28757476806640625})
store['active_learning_steps'][30]['eval_training']['best_epoch']=6
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 49464], ['id', 46658], ['id', 37468], ['id', 7543], ['id', 52060], ['id', 36527], ['id', 228], ['id', 3762], ['id', 491], ['id', 14201]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.3650793433189392, 0.28896331787109375, 0.21662482619285583, 0.3401924669742584, 0.3424760103225708, 0.4268774688243866, 0.4399229884147644, 0.5179592370986938, 0.3470894694328308, 0.47364914417266846]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.1810731887817383})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5198482275009155})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.41922658681869507})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3923569917678833})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31295204162597656})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32600805163383484})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3396607041358948})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3321518301963806})
store['active_learning_steps'][31]['training']['best_epoch']=5
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9611, 'crossentropy': 0.3117705810546875}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.9444229602813721})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.48773473501205444})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4162294268608093})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.42526838183403015})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.36318239569664})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.42045843601226807})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3517867922782898})
store['active_learning_steps'][31]['eval_training']['best_epoch']=7
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 23028], ['id', 38178], ['id', 52566], ['id', 59400], ['ood', 48665], ['id', 13149], ['id', 49563], ['id', 36008], ['id', 38158], ['id', 16011]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.36667096614837646, 0.38692641258239746, 0.5956880450248718, 0.26946187019348145, 0.19821405410766602, 0.46273934841156006, 0.3744858503341675, 0.43917202949523926, 0.3431553840637207, 0.42798811197280884]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.0659072399139404})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.5323932766914368})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3651818633079529})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3298598825931549})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3239706754684448})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3086712956428528})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32321885228157043})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.35795021057128906})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3652591407299042})
store['active_learning_steps'][32]['training']['best_epoch']=6
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9636, 'crossentropy': 0.29198173828125}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8911469578742981})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4839599132537842})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4074825048446655})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.37624233961105347})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.349759042263031})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.32584482431411743})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.303438663482666})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.30991607904434204})
store['active_learning_steps'][32]['eval_training']['best_epoch']=7
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 8772], ['id', 39942], ['id', 42924], ['id', 42355], ['id', 52074], ['id', 2000], ['id', 13650], ['id', 56913], ['id', 23086], ['id', 15141]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.33223408460617065, 0.45085734128952026, 0.27041614055633545, 0.4211411476135254, 0.5471429228782654, 0.539961576461792, 0.315590500831604, 0.3806633949279785, 0.4197583794593811, 0.2600945234298706]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.0664646625518799})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5483167767524719})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.37101995944976807})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3451942205429077})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.30179619789123535})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.35098594427108765})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.31663137674331665})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3473074436187744})
store['active_learning_steps'][33]['training']['best_epoch']=5
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9649, 'crossentropy': 0.3015654052734375}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8429367542266846})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4639791250228882})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3767740726470947})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.37662118673324585})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.34162649512290955})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3175086975097656})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.30630218982696533})
store['active_learning_steps'][33]['eval_training']['best_epoch']=7
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 12220], ['id', 18398], ['id', 33401], ['id', 6478], ['id', 6843], ['id', 50431], ['id', 13018], ['id', 46918], ['id', 38242], ['ood', 682]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.3304499387741089, 0.3482123613357544, 0.33112913370132446, 0.21773704886436462, 0.34941548109054565, 0.43636584281921387, 0.413931667804718, 0.39650028944015503, 0.4138563871383667, 0.27218568325042725]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.0872443914413452})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5796821117401123})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.42645156383514404})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32470348477363586})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.33862608671188354})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3159449100494385})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3363895118236542})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.35265403985977173})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3291809558868408})
store['active_learning_steps'][34]['training']['best_epoch']=6
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9654, 'crossentropy': 0.289182666015625}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8163619041442871})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.47475868463516235})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4073447287082672})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.347861111164093})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.31842246651649475})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.33373361825942993})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3256533443927765})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3186732530593872})
store['active_learning_steps'][34]['eval_training']['best_epoch']=5
store['active_learning_steps'][34]['acquisition']={'indices': [['ood', 59927], ['id', 21023], ['ood', 20486], ['id', 8714], ['id', 7767], ['id', 23350], ['id', 39516], ['id', 20869], ['ood', 48265], ['ood', 43066]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.18677914142608643, 0.45923978090286255, 0.16905176639556885, 0.31025296449661255, 0.33236944675445557, 0.3176047205924988, 0.41731178760528564, 0.37452346086502075, 0.2447509765625, 0.28403329849243164]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.3855977058410645})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.6378554105758667})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4413066506385803})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3710506558418274})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3368789255619049})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3226394057273865})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3046994209289551})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.30301475524902344})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3008701205253601})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2957562208175659})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3046247959136963})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3143501579761505})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3214518427848816})
store['active_learning_steps'][35]['training']['best_epoch']=10
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9687, 'crossentropy': 0.2918007568359375}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8792981505393982})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.500078558921814})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3830452561378479})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.37195461988449097})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33145835995674133})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2987073063850403})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.27362537384033203})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2683379650115967})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31046441197395325})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.266437828540802})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2783709168434143})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.28400176763534546})
store['active_learning_steps'][35]['eval_training']['best_epoch']=10
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 12297], ['id', 1455], ['id', 6226], ['id', 9180], ['id', 19015], ['id', 26516], ['id', 47549], ['id', 31530], ['id', 16292], ['id', 5632]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.5798462629318237, 0.5038588047027588, 0.44326627254486084, 0.3423480987548828, 0.5065791010856628, 0.3958202600479126, 0.4299689531326294, 0.26993852853775024, 0.5130258202552795, 0.3518311083316803]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.9733861088752747})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5585160255432129})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.4047127962112427})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.30894410610198975})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2960205674171448})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.27732768654823303})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2941049635410309})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2970729172229767})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2858043313026428})
store['active_learning_steps'][36]['training']['best_epoch']=6
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9666, 'crossentropy': 0.2638225830078125}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8133838176727295})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5323758125305176})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.361890971660614})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3865346908569336})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32604271173477173})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2794325053691864})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2817314565181732})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2733660340309143})
store['active_learning_steps'][36]['eval_training']['best_epoch']=8
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 27601], ['id', 29827], ['id', 15068], ['id', 14062], ['ood', 49485], ['id', 28371], ['id', 52169], ['id', 15252], ['id', 31672], ['id', 42384]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.36115485429763794, 0.4160665273666382, 0.22131729125976562, 0.37176835536956787, 0.19674158096313477, 0.42596226930618286, 0.4200085401535034, 0.3155307173728943, 0.3677629232406616, 0.4589669704437256]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.1467643976211548})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.5654054880142212})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4141244888305664})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3233385682106018})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2792653441429138})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.30735304951667786})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.27862972021102905})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2876625657081604})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2830909788608551})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29042351245880127})
store['active_learning_steps'][37]['training']['best_epoch']=7
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9677, 'crossentropy': 0.28194013671875}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.9072366952896118})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5047670006752014})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3943132758140564})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.325681209564209})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.31653404235839844})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3224799633026123})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2940385043621063})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31811434030532837})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28763484954833984})
store['active_learning_steps'][37]['eval_training']['best_epoch']=9
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 31652], ['id', 370], ['id', 34829], ['id', 25386], ['id', 50236], ['id', 28150], ['id', 13783], ['id', 1423], ['id', 16624], ['id', 37227]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3336430788040161, 0.4328147768974304, 0.528508186340332, 0.527890682220459, 0.4506244659423828, 0.3351963758468628, 0.22029688954353333, 0.5103517770767212, 0.46112966537475586, 0.38107576966285706]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 1.03716242313385})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5580918192863464})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4306745231151581})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33651143312454224})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.30100488662719727})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2934754490852356})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2793397903442383})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.291533887386322})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2830231487751007})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3067512512207031})
store['active_learning_steps'][38]['training']['best_epoch']=7
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9658, 'crossentropy': 0.2882923583984375}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.8016037940979004})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.49162721633911133})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3809095621109009})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3758518695831299})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2930801510810852})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.27415475249290466})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2772495150566101})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3005613684654236})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28754138946533203})
store['active_learning_steps'][38]['eval_training']['best_epoch']=6
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 2184], ['id', 26292], ['id', 38577], ['id', 7731], ['id', 14722], ['id', 30177], ['id', 30952], ['id', 12257], ['id', 30710], ['id', 46895]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5653527975082397, 0.40890049934387207, 0.27115094661712646, 0.4449611008167267, 0.3147865831851959, 0.46341341733932495, 0.4461015462875366, 0.323890745639801, 0.332574725151062, 0.3887313902378082]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.082453727722168})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5994572639465332})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.43850257992744446})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.35862743854522705})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3215605616569519})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3156723380088806})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2885109484195709})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29817742109298706})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2654303014278412})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.268131822347641})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2976253032684326})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30778613686561584})
store['active_learning_steps'][39]['training']['best_epoch']=9
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9717, 'crossentropy': 0.25556435546875}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.9228839874267578})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.46264415979385376})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.37762174010276794})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3210599422454834})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31320667266845703})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2809702455997467})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27511584758758545})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29339930415153503})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2659771740436554})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.26227349042892456})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2776217460632324})
store['active_learning_steps'][39]['eval_training']['best_epoch']=10
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 53063], ['id', 29206], ['id', 340], ['id', 10503], ['id', 44389], ['id', 31336], ['id', 53784], ['id', 57793], ['id', 11785], ['id', 19159]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.42170387506484985, 0.32511526346206665, 0.495955228805542, 0.37273597717285156, 0.4420217275619507, 0.5555350184440613, 0.4645034074783325, 0.37256282567977905, 0.5320644378662109, 0.409939169883728]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.2217180728912354})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5660769939422607})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.42433416843414307})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.30840247869491577})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.29165929555892944})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2941569685935974})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29978641867637634})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2932976484298706})
store['active_learning_steps'][40]['training']['best_epoch']=5
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9672, 'crossentropy': 0.2770522705078125}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.9126331806182861})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5592288970947266})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4433457851409912})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.37486958503723145})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3272589147090912})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.37908899784088135})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3194560706615448})
store['active_learning_steps'][40]['eval_training']['best_epoch']=7
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 32747], ['id', 6309], ['id', 4638], ['id', 54858], ['id', 15278], ['id', 51988], ['id', 15167], ['id', 49264], ['id', 10824], ['id', 32047]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.5544736981391907, 0.43953800201416016, 0.4882619380950928, 0.4640495777130127, 0.34343421459198, 0.5210102796554565, 0.37319332361221313, 0.2825709581375122, 0.3414965271949768, 0.3618808388710022]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.1607489585876465})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5903737545013428})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.38692137598991394})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34948456287384033})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3281537890434265})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2973940372467041})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31185221672058105})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2662726044654846})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2982977628707886})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27751994132995605})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2555471956729889})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2667927145957947})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27558887004852295})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2813660502433777})
store['active_learning_steps'][41]['training']['best_epoch']=11
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9712, 'crossentropy': 0.2454351318359375}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.0004265308380127})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5311175584793091})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4076906740665436})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.301683247089386})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.26604267954826355})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.24729350209236145})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.24249358475208282})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2528190314769745})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.23633158206939697})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.25128257274627686})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.23410432040691376})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.24408861994743347})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.23139473795890808})
store['active_learning_steps'][41]['eval_training']['best_epoch']=13
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 12594], ['id', 14546], ['id', 47914], ['id', 15210], ['id', 27172], ['id', 23733], ['id', 27085], ['id', 24512], ['id', 843], ['id', 11346]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4005640149116516, 0.35631993412971497, 0.4938412308692932, 0.5170884132385254, 0.6475881934165955, 0.3391687273979187, 0.37738290429115295, 0.5429674386978149, 0.6377279460430145, 0.2653794288635254]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.1516005992889404})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5423842072486877})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.406556636095047})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3084579110145569})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29788488149642944})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2961427569389343})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2799117863178253})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2634756565093994})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2763810157775879})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2764388918876648})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28127822279930115})
store['active_learning_steps'][42]['training']['best_epoch']=8
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9711, 'crossentropy': 0.241562451171875}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.8318557739257812})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5257343649864197})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3520283102989197})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3399657607078552})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.296906054019928})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.28360116481781006})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29601937532424927})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2839663028717041})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2782056927680969})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.25630447268486023})
store['active_learning_steps'][42]['eval_training']['best_epoch']=10
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 55396], ['id', 16722], ['id', 50320], ['id', 56014], ['id', 13259], ['id', 48573], ['id', 50369], ['id', 22633], ['id', 44753], ['id', 55078]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.4309577941894531, 0.35267674922943115, 0.40915918350219727, 0.4121100902557373, 0.5199966430664062, 0.29444003105163574, 0.4351279139518738, 0.4200811982154846, 0.44428545236587524, 0.4014723300933838]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.2981512546539307})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6198250651359558})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.41324982047080994})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.35185325145721436})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31839239597320557})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2917570471763611})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29165011644363403})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2881139814853668})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2810959219932556})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2624818980693817})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2731432616710663})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2887655198574066})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28092053532600403})
store['active_learning_steps'][43]['training']['best_epoch']=10
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9727, 'crossentropy': 0.2467265380859375}
