store = {}
store['timestamp']=1620920896
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=4']
store['commit']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['github_url']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=4
store['worker_id']=4
store['num_workers']=20
store['config']={'seed': 1240, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'evaluation_set_size': 100, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.504276990890503})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.3698782920837402})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.887885570526123})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.925203800201416})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.9974164962768555})
store['active_learning_steps'][0]['training']['best_epoch']=2
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6982, 'crossentropy': 2.15694375}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.176171898841858})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.1046385765075684})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.0906438827514648})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.0906240940093994})
store['active_learning_steps'][0]['eval_training']['best_epoch']=4
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 25738], ['ood', 48902], ['id', 8221], ['id', 52534], ['id', 857], ['id', 50503], ['ood', 46783], ['ood', 53704], ['id', 16875], ['id', 13294]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6071839332580566, 0.41418886184692383, 0.5560811758041382, 0.7185481786727905, 0.8801699876785278, 0.7483623623847961, 0.4954805374145508, 0.5558898448944092, 0.7567662596702576, 0.7060873508453369]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.5856841802597046})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.0739526748657227})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.222006320953369})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 2.167483329772949})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7104, 'crossentropy': 1.462312890625}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.1247552633285522})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.0473062992095947})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.0130014419555664})
store['active_learning_steps'][1]['eval_training']['best_epoch']=3
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 27632], ['id', 12426], ['id', 31263], ['id', 12268], ['id', 34268], ['id', 53696], ['id', 6883], ['id', 47619], ['id', 8780], ['id', 30383]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6137522459030151, 0.6855076551437378, 0.5914808511734009, 0.6378209590911865, 0.6929734945297241, 0.5047314167022705, 0.5524532794952393, 0.8196440935134888, 0.5407229065895081, 0.5921662449836731]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.55708646774292})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.6878857612609863})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.8557181358337402})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 2.158942461013794})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7113, 'crossentropy': 1.51476494140625}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.1658375263214111})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.1009047031402588})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0755038261413574})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 13130], ['id', 44169], ['id', 15815], ['id', 14305], ['id', 31395], ['id', 43648], ['id', 7979], ['id', 49529], ['id', 9743], ['id', 44820]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4588375687599182, 0.4707939624786377, 0.324287474155426, 0.2884894609451294, 0.3925369381904602, 0.3961002826690674, 0.47483861446380615, 0.4864920377731323, 0.5782582759857178, 0.48209619522094727]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.2017977237701416})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.3649647235870361})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.5766513347625732})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.606318473815918})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7458, 'crossentropy': 1.20042685546875}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.0091832876205444})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 0.9145734310150146})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 0.9428383111953735})
store['active_learning_steps'][3]['eval_training']['best_epoch']=2
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 27542], ['id', 45073], ['ood', 44809], ['id', 51221], ['ood', 44532], ['ood', 33589], ['id', 39929], ['id', 1534], ['id', 38645], ['id', 53824]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4405674338340759, 0.5777877569198608, 0.38527947664260864, 0.46396398544311523, 0.44391071796417236, 0.37556350231170654, 0.49696218967437744, 0.5485538244247437, 0.4701566696166992, 0.2801719903945923]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.016688346862793})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.1323127746582031})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.2838928699493408})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.4520379304885864})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.799, 'crossentropy': 0.97594140625}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 0.9207615852355957})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 0.8716791272163391})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.8141101598739624})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 44013], ['id', 22627], ['id', 16285], ['id', 12119], ['id', 15518], ['id', 15134], ['id', 49469], ['id', 8755], ['id', 31162], ['id', 20333]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.482174277305603, 0.3639376163482666, 0.22498106956481934, 0.43959224224090576, 0.2811211347579956, 0.4246639013290405, 0.36431431770324707, 0.3343096971511841, 0.3738943338394165, 0.3581498861312866]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8977558612823486})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.9072694778442383})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.061840534210205})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.0208015441894531})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8434, 'crossentropy': 0.86704677734375}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8830329179763794})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7715367674827576})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7873246669769287})
store['active_learning_steps'][5]['eval_training']['best_epoch']=2
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 36492], ['id', 1356], ['id', 25483], ['id', 53598], ['id', 44109], ['id', 8688], ['id', 679], ['id', 15886], ['id', 56531], ['id', 46047]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.2597278356552124, 0.46592313051223755, 0.3283424973487854, 0.4739845395088196, 0.45809394121170044, 0.41493308544158936, 0.446655809879303, 0.4186750054359436, 0.43219733238220215, 0.32056593894958496]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.9924709796905518})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.845624566078186})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.9774436950683594})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.036635160446167})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.0042128562927246})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.87, 'crossentropy': 0.8127955078125}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7603963613510132})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.6469032764434814})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.615168571472168})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.602658212184906})
store['active_learning_steps'][6]['eval_training']['best_epoch']=4
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 2000], ['id', 2277], ['id', 26346], ['id', 24512], ['id', 6540], ['id', 55007], ['id', 53504], ['id', 25185], ['id', 176], ['id', 7924]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.681189239025116, 0.48978883028030396, 0.4292793869972229, 0.4123764634132385, 0.48426735401153564, 0.3399760127067566, 0.613461971282959, 0.47217971086502075, 0.5843732953071594, 0.5509601831436157]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.9247556924819946})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8756911754608154})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.932916522026062})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9573766589164734})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9350835084915161})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8691, 'crossentropy': 0.76599873046875}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8129432201385498})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.6784594058990479})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.6525803804397583})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.640484094619751})
store['active_learning_steps'][7]['eval_training']['best_epoch']=4
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 44878], ['id', 47246], ['id', 44907], ['id', 26419], ['id', 56228], ['id', 37291], ['id', 7368], ['id', 29725], ['id', 32359], ['id', 49183]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3490990400314331, 0.4110679030418396, 0.3242342472076416, 0.41836750507354736, 0.47803252935409546, 0.5385394096374512, 0.5506620407104492, 0.4550279378890991, 0.355083167552948, 0.3994024991989136]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8979132175445557})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.767915666103363})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8423252105712891})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8164783120155334})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9806638956069946})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8888, 'crossentropy': 0.719813818359375}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7580204606056213})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6000396609306335})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5985116958618164})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.5735008120536804})
store['active_learning_steps'][8]['eval_training']['best_epoch']=4
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 27420], ['id', 26579], ['id', 49503], ['id', 38656], ['id', 45179], ['id', 49364], ['id', 58881], ['id', 38165], ['id', 47107], ['id', 57195]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6951954364776611, 0.6055259108543396, 0.4775514006614685, 0.42842042446136475, 0.43068593740463257, 0.5780777931213379, 0.6225865483283997, 0.5257413387298584, 0.5254824757575989, 0.39935851097106934]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7742189168930054})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6908959150314331})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6157950162887573})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6452528238296509})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7168318033218384})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7272030115127563})
store['active_learning_steps'][9]['training']['best_epoch']=3
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.9116, 'crossentropy': 0.574848388671875}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6625909805297852})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5311805605888367})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.4866042733192444})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.4532460570335388})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.46760162711143494})
store['active_learning_steps'][9]['eval_training']['best_epoch']=4
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 26146], ['id', 3470], ['id', 32970], ['id', 9380], ['id', 1258], ['id', 7266], ['id', 32173], ['id', 10894], ['id', 23690], ['id', 2593]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6435856819152832, 0.469179630279541, 0.4415281414985657, 0.44184035062789917, 0.3420454263687134, 0.2913396656513214, 0.5859004259109497, 0.3091222643852234, 0.3434634208679199, 0.3227033019065857]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.9055934548377991})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7188793420791626})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6954402923583984})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8378568887710571})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7000633478164673})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9399896860122681})
store['active_learning_steps'][10]['training']['best_epoch']=3
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.9025, 'crossentropy': 0.66906669921875}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7430442571640015})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5644617080688477})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5386067628860474})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5226860642433167})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5136730670928955})
store['active_learning_steps'][10]['eval_training']['best_epoch']=5
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 59361], ['id', 13337], ['id', 2098], ['id', 45761], ['id', 9476], ['id', 48072], ['id', 59601], ['id', 22982], ['id', 1392], ['id', 26850]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5979210138320923, 0.5885017216205597, 0.35729852318763733, 0.6258753538131714, 0.5143448710441589, 0.5575324296951294, 0.5766297578811646, 0.436978816986084, 0.4955369830131531, 0.6263841390609741]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8168268799781799})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5980925559997559})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6219533681869507})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5756281614303589})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6527227163314819})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7784726619720459})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.702137291431427})
store['active_learning_steps'][11]['training']['best_epoch']=4
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.9198, 'crossentropy': 0.52136318359375}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.737654447555542})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.539408802986145})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4682733714580536})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.46461087465286255})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.43086421489715576})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4169608950614929})
store['active_learning_steps'][11]['eval_training']['best_epoch']=6
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 14279], ['id', 5320], ['id', 20653], ['id', 4282], ['id', 29472], ['id', 47748], ['id', 29702], ['id', 33349], ['id', 47505], ['id', 4488]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6044471859931946, 0.6641574501991272, 0.6112081408500671, 0.47023141384124756, 0.6267547011375427, 0.5185105204582214, 0.5531514883041382, 0.38461923599243164, 0.49519026279449463, 0.38150548934936523]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8406496047973633})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6116509437561035})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5813664793968201})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6529315710067749})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.651459813117981})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6118893623352051})
store['active_learning_steps'][12]['training']['best_epoch']=3
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.916, 'crossentropy': 0.528925244140625}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7271294593811035})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5328302383422852})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.46837207674980164})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4311111867427826})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.42549288272857666})
store['active_learning_steps'][12]['eval_training']['best_epoch']=5
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 31046], ['id', 38892], ['id', 22870], ['id', 24730], ['id', 39327], ['id', 16951], ['id', 57308], ['id', 36324], ['id', 36978], ['id', 56224]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6989201307296753, 0.3756437301635742, 0.5385942459106445, 0.4954439401626587, 0.41800743341445923, 0.4829292893409729, 0.4152482748031616, 0.4485582113265991, 0.4717260003089905, 0.46754735708236694]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.9148318767547607})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5522874593734741})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5706678628921509})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5586860179901123})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6073123216629028})
store['active_learning_steps'][13]['training']['best_epoch']=2
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.9228, 'crossentropy': 0.502498583984375}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7663313746452332})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5796186327934265})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.510753333568573})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.503616213798523})
store['active_learning_steps'][13]['eval_training']['best_epoch']=4
store['active_learning_steps'][13]['acquisition']={'indices': [['ood', 8982], ['id', 7729], ['id', 57882], ['id', 43098], ['id', 39597], ['id', 43430], ['id', 746], ['id', 30811], ['ood', 16319], ['id', 45502]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.24675369262695312, 0.2942737340927124, 0.5125755071640015, 0.36610734462738037, 0.3539726734161377, 0.34849703311920166, 0.4820992946624756, 0.3707115054130554, 0.25138354301452637, 0.4012213945388794]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7852322459220886})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5363413095474243})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5701770782470703})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5419537425041199})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5830199718475342})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9149, 'crossentropy': 0.509456640625}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7543805241584778})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5811412930488586})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5332131385803223})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4441301226615906})
store['active_learning_steps'][14]['eval_training']['best_epoch']=4
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 47297], ['id', 45732], ['id', 40866], ['id', 50639], ['id', 18840], ['id', 18687], ['id', 5536], ['id', 40639], ['id', 36491], ['id', 26358]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.27403557300567627, 0.4365164637565613, 0.35382789373397827, 0.2908075451850891, 0.3748840093612671, 0.372978150844574, 0.32979243993759155, 0.47200608253479004, 0.3156609535217285, 0.372933030128479]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9838666915893555})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5989000201225281})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6676853895187378})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5432467460632324})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5619443655014038})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5495309233665466})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6057409644126892})
store['active_learning_steps'][15]['training']['best_epoch']=4
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.931, 'crossentropy': 0.48159853515625}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6928511261940002})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5006548166275024})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.43843841552734375})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.42548272013664246})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4126524329185486})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4115998148918152})
store['active_learning_steps'][15]['eval_training']['best_epoch']=6
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 40241], ['id', 18728], ['id', 23429], ['id', 48933], ['id', 29868], ['id', 27345], ['id', 46248], ['id', 50616], ['id', 52814], ['id', 49354]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.47102296352386475, 0.4116210341453552, 0.4942571818828583, 0.5151997208595276, 0.38921451568603516, 0.4667263627052307, 0.4237668514251709, 0.4952086806297302, 0.3282936215400696, 0.5255571603775024]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7990512847900391})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5227357149124146})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4498694837093353})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5078856945037842})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4802916646003723})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5084255933761597})
store['active_learning_steps'][16]['training']['best_epoch']=3
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9375, 'crossentropy': 0.4181810546875}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7267472743988037})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5507797002792358})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.44158226251602173})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4418455958366394})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.401123970746994})
store['active_learning_steps'][16]['eval_training']['best_epoch']=5
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 31264], ['id', 27299], ['id', 1852], ['id', 55918], ['id', 55028], ['id', 7879], ['id', 30968], ['id', 25096], ['id', 47913], ['id', 6213]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.41636669635772705, 0.41582125425338745, 0.3464980125427246, 0.3636600971221924, 0.3206521272659302, 0.44182372093200684, 0.3450400233268738, 0.42449814081192017, 0.410167932510376, 0.5259962677955627]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9438679814338684})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5304878950119019})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4877448081970215})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4224942624568939})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.443656861782074})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4422648549079895})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.44791048765182495})
store['active_learning_steps'][17]['training']['best_epoch']=4
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9508, 'crossentropy': 0.366434375}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7373096942901611})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.44815319776535034})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.3976869285106659})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.34701651334762573})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.34803736209869385})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.34493938088417053})
store['active_learning_steps'][17]['eval_training']['best_epoch']=6
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 20006], ['id', 9633], ['id', 37906], ['id', 44328], ['id', 45121], ['ood', 40318], ['id', 38698], ['id', 15963], ['id', 15812], ['id', 30638]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.4242256283760071, 0.445264995098114, 0.37548506259918213, 0.41311317682266235, 0.3503097891807556, 0.3616909980773926, 0.5990106463432312, 0.43463122844696045, 0.28471893072128296, 0.2852151393890381]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8666456341743469})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.47700002789497375})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4367526173591614})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3800307512283325})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.39808234572410583})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4124014973640442})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.43387842178344727})
store['active_learning_steps'][18]['training']['best_epoch']=4
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9473, 'crossentropy': 0.375605078125}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8022984266281128})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5737521052360535})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.45284023880958557})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4115966558456421})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.39513319730758667})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4033104181289673})
store['active_learning_steps'][18]['eval_training']['best_epoch']=5
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 57159], ['id', 44128], ['id', 10258], ['id', 59280], ['id', 44484], ['id', 15948], ['ood', 24008], ['ood', 50479], ['id', 59741], ['ood', 39872]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.1846258044242859, 0.3902297019958496, 0.26302534341812134, 0.48445361852645874, 0.420362651348114, 0.36387038230895996, 0.27355629205703735, 0.2835952043533325, 0.3436630964279175, 0.3221694231033325]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9095281362533569})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.485263854265213})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.434546560049057})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4895773231983185})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4399160146713257})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.39234495162963867})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.47132545709609985})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.41884809732437134})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.43216702342033386})
store['active_learning_steps'][19]['training']['best_epoch']=6
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9555, 'crossentropy': 0.3479004638671875}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8428078889846802})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.49065062403678894})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4146786630153656})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.39247214794158936})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3471546173095703})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.33969318866729736})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.33442461490631104})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.34008848667144775})
store['active_learning_steps'][19]['eval_training']['best_epoch']=7
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 55314], ['id', 36722], ['id', 581], ['id', 41426], ['id', 38370], ['id', 2636], ['id', 53873], ['id', 53158], ['id', 37522], ['id', 40576]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5222673416137695, 0.48573002219200134, 0.3795086741447449, 0.5125097036361694, 0.38390302658081055, 0.5399592518806458, 0.5836027264595032, 0.47046583890914917, 0.5312082767486572, 0.38806265592575073]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9012556076049805})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5083670020103455})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4482704997062683})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.37664997577667236})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4014514088630676})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.35745203495025635})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3856516480445862})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.36797812581062317})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.37338584661483765})
store['active_learning_steps'][20]['training']['best_epoch']=6
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9597, 'crossentropy': 0.32352548828125}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.770694375038147})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4709666967391968})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3967769742012024})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.33195143938064575})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.32510852813720703})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3152693510055542})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3137306571006775})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.32272660732269287})
store['active_learning_steps'][20]['eval_training']['best_epoch']=7
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 40589], ['id', 36230], ['id', 46070], ['id', 49489], ['id', 50353], ['id', 10091], ['id', 38630], ['id', 10446], ['ood', 46614], ['id', 31628]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.34183067083358765, 0.3320503234863281, 0.4962772727012634, 0.38625168800354004, 0.4043252468109131, 0.34091705083847046, 0.5049816966056824, 0.502688467502594, 0.22174596786499023, 0.4043327569961548]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8923124074935913})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.49697333574295044})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4503011107444763})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3536604046821594})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3825989365577698})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3799596428871155})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3610515594482422})
store['active_learning_steps'][21]['training']['best_epoch']=4
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9547, 'crossentropy': 0.3458873779296875}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8211352825164795})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.543834924697876})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.44506147503852844})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.39631029963493347})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3857477903366089})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3885602056980133})
store['active_learning_steps'][21]['eval_training']['best_epoch']=5
store['active_learning_steps'][21]['acquisition']={'indices': [['ood', 21608], ['id', 5062], ['id', 43745], ['id', 2980], ['id', 52210], ['id', 50432], ['id', 27122], ['id', 47100], ['id', 36714], ['id', 39618]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.24509084224700928, 0.6056230664253235, 0.37032854557037354, 0.3356349468231201, 0.40258514881134033, 0.3014994263648987, 0.45784610509872437, 0.28086310625076294, 0.3290376663208008, 0.3777640759944916]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.986009418964386})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5273106098175049})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.40418121218681335})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.38045042753219604})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3578032851219177})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.35776272416114807})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3587932288646698})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3651445508003235})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.38955193758010864})
store['active_learning_steps'][22]['training']['best_epoch']=6
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9529, 'crossentropy': 0.35748330078125}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7526776790618896})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4829021096229553})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4144716262817383})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.36360087990760803})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3666709065437317})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.35884425044059753})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.39326992630958557})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.34449055790901184})
store['active_learning_steps'][22]['eval_training']['best_epoch']=8
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 27045], ['id', 4165], ['id', 55496], ['id', 32533], ['id', 49548], ['id', 44335], ['id', 4476], ['id', 27130], ['id', 52138], ['id', 35645]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.5351687073707581, 0.5071106553077698, 0.4823305606842041, 0.4367574453353882, 0.3824225068092346, 0.38129112124443054, 0.5145479440689087, 0.26880404353141785, 0.4755122661590576, 0.4121028184890747]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.120640754699707})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5940828323364258})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4873288571834564})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.43919694423675537})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.39775365591049194})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3982979357242584})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3691084384918213})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4102116823196411})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.42588645219802856})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.37257498502731323})
store['active_learning_steps'][23]['training']['best_epoch']=7
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9556, 'crossentropy': 0.3683271484375}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6978281736373901})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.479128897190094})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.38629552721977234})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.34612035751342773})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.33280569314956665})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2824782133102417})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.33444350957870483})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3166237473487854})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.29883965849876404})
store['active_learning_steps'][23]['eval_training']['best_epoch']=6
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 44432], ['id', 34785], ['id', 48480], ['id', 13794], ['id', 43764], ['id', 22994], ['id', 41816], ['id', 52091], ['id', 32282], ['id', 44286]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.4730950593948364, 0.528735876083374, 0.4896155595779419, 0.46977055072784424, 0.45045679807662964, 0.47405117750167847, 0.4682767391204834, 0.5535159111022949, 0.45989859104156494, 0.3760831356048584]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 1.0424530506134033})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5098296999931335})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.39467328786849976})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3751239776611328})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32051101326942444})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31985870003700256})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3456191420555115})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.35770219564437866})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3743113875389099})
store['active_learning_steps'][24]['training']['best_epoch']=6
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9563, 'crossentropy': 0.3305412353515625}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7323959469795227})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4851585030555725})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3730960488319397})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.327492356300354})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3267310857772827})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30819395184516907})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.275115430355072})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31047356128692627})
store['active_learning_steps'][24]['eval_training']['best_epoch']=7
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 37468], ['id', 57507], ['id', 32426], ['id', 44008], ['id', 36704], ['id', 39818], ['id', 43660], ['id', 18031], ['id', 13156], ['id', 16730]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.47863084077835083, 0.6454591751098633, 0.42397475242614746, 0.44268298149108887, 0.564903736114502, 0.38016802072525024, 0.6083545088768005, 0.48956507444381714, 0.5984972715377808, 0.47263914346694946]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.0077183246612549})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5257860422134399})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4167214035987854})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3680586814880371})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.34516072273254395})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3553099036216736})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29857316613197327})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33518528938293457})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3537248969078064})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.35075515508651733})
store['active_learning_steps'][25]['training']['best_epoch']=7
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9622, 'crossentropy': 0.320727001953125}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6942407488822937})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.48198574781417847})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3744383454322815})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3476283550262451})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33020299673080444})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28464260697364807})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3023757040500641})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2972881495952606})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.29386454820632935})
store['active_learning_steps'][25]['eval_training']['best_epoch']=6
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 41614], ['id', 19586], ['id', 50462], ['id', 30925], ['id', 45944], ['id', 49398], ['id', 36770], ['id', 20756], ['id', 31650], ['id', 55906]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.2681042551994324, 0.40808868408203125, 0.3953901529312134, 0.44558343291282654, 0.3804945945739746, 0.2659686207771301, 0.4886179566383362, 0.3138887882232666, 0.49713677167892456, 0.5278698801994324]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.046468734741211})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5791122317314148})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.41245704889297485})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.38115400075912476})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.36579960584640503})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3593459129333496})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.35772496461868286})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3712480664253235})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.36188024282455444})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.36897575855255127})
store['active_learning_steps'][26]['training']['best_epoch']=7
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9631, 'crossentropy': 0.3325827392578125}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.831881046295166})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5131666660308838})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.38299036026000977})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.32121455669403076})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.322311133146286})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30908215045928955})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3102196455001831})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.31082165241241455})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2670983672142029})
store['active_learning_steps'][26]['eval_training']['best_epoch']=9
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 13998], ['id', 31659], ['id', 57054], ['id', 31738], ['id', 46878], ['id', 14070], ['id', 49082], ['id', 36668], ['id', 58832], ['id', 46324]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4952813982963562, 0.4358701705932617, 0.5611592531204224, 0.5282570719718933, 0.42259424924850464, 0.6794317960739136, 0.3487205505371094, 0.3711036443710327, 0.4804612398147583, 0.470910906791687]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.0389567613601685})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5442250967025757})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.39201968908309937})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3596144914627075})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3783505856990814})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4096751809120178})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.38732150197029114})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.956, 'crossentropy': 0.3583526611328125}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8714647889137268})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5847994089126587})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.43680882453918457})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.43388867378234863})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3974507451057434})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3962763249874115})
store['active_learning_steps'][27]['eval_training']['best_epoch']=6
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 15801], ['id', 43042], ['id', 50469], ['id', 370], ['ood', 45431], ['id', 51048], ['id', 44570], ['id', 22824], ['id', 26638], ['id', 49425]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.40902847051620483, 0.4373873472213745, 0.3817133903503418, 0.38072890043258667, 0.2123088836669922, 0.1794475018978119, 0.5778697729110718, 0.4491656422615051, 0.3499898314476013, 0.42779263854026794]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9555001854896545})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5184991359710693})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.4249553978443146})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.34432080388069153})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3091038465499878})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3226414918899536})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33155837655067444})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2991424798965454})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2979635000228882})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2998810410499573})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.321661114692688})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3251597285270691})
store['active_learning_steps'][28]['training']['best_epoch']=9
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9631, 'crossentropy': 0.288430029296875}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.8289002776145935})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4912891387939453})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4006020426750183})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.34526771306991577})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3184988796710968})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30666106939315796})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2751290202140808})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.28005751967430115})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.24854786694049835})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.25408536195755005})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2518289089202881})
store['active_learning_steps'][28]['eval_training']['best_epoch']=9
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 43897], ['id', 59309], ['id', 38329], ['id', 4909], ['id', 35654], ['id', 41098], ['id', 10690], ['id', 48130], ['id', 58625], ['id', 41772]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5400529503822327, 0.5621069073677063, 0.42470598220825195, 0.45068681240081787, 0.5645957589149475, 0.45283281803131104, 0.6575267314910889, 0.47604256868362427, 0.29169268906116486, 0.5432752370834351]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.094442367553711})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5848389863967896})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4294944405555725})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.41776496171951294})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.34707558155059814})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3653695583343506})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3308684825897217})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3265469968318939})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3337481915950775})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3406292796134949})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3414592742919922})
store['active_learning_steps'][29]['training']['best_epoch']=8
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9624, 'crossentropy': 0.313718115234375}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.8749213218688965})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4906458854675293})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.39359766244888306})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3468690812587738})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32858920097351074})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2916746139526367})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29333508014678955})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2655350863933563})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2975161671638489})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28539860248565674})
store['active_learning_steps'][29]['eval_training']['best_epoch']=8
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 440], ['id', 58101], ['id', 2574], ['id', 24984], ['id', 27235], ['id', 8316], ['id', 16799], ['id', 13078], ['id', 42059], ['id', 46058]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.38137227296829224, 0.4641333818435669, 0.6015345454216003, 0.4434433579444885, 0.385428249835968, 0.29631292819976807, 0.6638451814651489, 0.6111127734184265, 0.24314066767692566, 0.3051682710647583]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.035408616065979})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.49503761529922485})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4211840033531189})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3743080198764801})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32935813069343567})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3294227719306946})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3385887145996094})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3252047002315521})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.325375497341156})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.33392688632011414})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3349152207374573})
store['active_learning_steps'][30]['training']['best_epoch']=8
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9674, 'crossentropy': 0.291533837890625}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8600605726242065})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.44318610429763794})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3387322425842285})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33217722177505493})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3132127523422241})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2903299927711487})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2908259630203247})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2534552812576294})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.24994689226150513})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2584552764892578})
store['active_learning_steps'][30]['eval_training']['best_epoch']=9
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 50317], ['id', 47344], ['id', 23629], ['id', 6269], ['id', 44184], ['id', 8104], ['id', 6918], ['id', 44443], ['id', 41274], ['id', 13388]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7323512434959412, 0.6113268733024597, 0.5380980372428894, 0.5493553876876831, 0.7089113891124725, 0.4926908016204834, 0.46391844749450684, 0.4562927782535553, 0.5049197673797607, 0.4393378496170044]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.0901730060577393})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6072367429733276})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4237087666988373})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3776002526283264})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3096195459365845})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.34283608198165894})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3279600739479065})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30593541264533997})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28510573506355286})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3362022638320923})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2997429370880127})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3112686276435852})
store['active_learning_steps'][31]['training']['best_epoch']=9
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9695, 'crossentropy': 0.27455205078125}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.8225003480911255})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4550221860408783})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3879809081554413})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33984696865081787})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3418934941291809})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.28355902433395386})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.27944672107696533})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2964192032814026})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2552754282951355})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.25838327407836914})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2475772649049759})
store['active_learning_steps'][31]['eval_training']['best_epoch']=11
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 33338], ['id', 20916], ['id', 9340], ['id', 21370], ['id', 20280], ['id', 42698], ['id', 10656], ['id', 47321], ['id', 16528], ['id', 12236]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5464272499084473, 0.4308238625526428, 0.4750545620918274, 0.5203250050544739, 0.4219503402709961, 0.2769337296485901, 0.3844417929649353, 0.5096946954727173, 0.4545789957046509, 0.4547353982925415]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.976718544960022})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4975515902042389})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.40211907029151917})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3541676998138428})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3002229332923889})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3091822862625122})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30208322405815125})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3178696036338806})
store['active_learning_steps'][32]['training']['best_epoch']=5
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9684, 'crossentropy': 0.284081787109375}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.858898937702179})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4453686475753784})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.36670050024986267})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3696584105491638})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.36471039056777954})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3507278561592102})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.32714295387268066})
store['active_learning_steps'][32]['eval_training']['best_epoch']=7
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 41970], ['ood', 46027], ['id', 37648], ['ood', 17526], ['id', 5790], ['id', 19130], ['id', 39377], ['id', 49987], ['id', 9547], ['id', 53732]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5261210799217224, 0.26108670234680176, 0.378886878490448, 0.232946515083313, 0.2881283164024353, 0.32173585891723633, 0.3823232054710388, 0.4177149534225464, 0.27371641993522644, 0.46663618087768555]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.1038111448287964})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5239368081092834})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3636254668235779})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3154575228691101})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3217010498046875})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28717076778411865})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30423086881637573})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29909420013427734})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.30058419704437256})
store['active_learning_steps'][33]['training']['best_epoch']=6
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9681, 'crossentropy': 0.2736994384765625}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8386956453323364})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5438892841339111})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.41096246242523193})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3341232240200043})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3211253881454468})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2975022792816162})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30339908599853516})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3022041916847229})
store['active_learning_steps'][33]['eval_training']['best_epoch']=6
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 24479], ['id', 21894], ['id', 2519], ['id', 53522], ['id', 5000], ['ood', 29306], ['id', 43560], ['id', 4820], ['id', 57557], ['id', 7612]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3665192127227783, 0.3157063126564026, 0.48423153162002563, 0.3863644003868103, 0.5169305205345154, 0.1735457181930542, 0.48869097232818604, 0.35766297578811646, 0.41794371604919434, 0.28328970074653625]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9936463832855225})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5607637166976929})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.36217084527015686})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.33794522285461426})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.281097412109375})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2888931632041931})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30222439765930176})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.34756407141685486})
store['active_learning_steps'][34]['training']['best_epoch']=5
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9664, 'crossentropy': 0.282036181640625}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.8298300504684448})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4930569529533386})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4259880483150482})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3994791507720947})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32459044456481934})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3708345293998718})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3322127163410187})
store['active_learning_steps'][34]['eval_training']['best_epoch']=5
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 24740], ['id', 58560], ['id', 29891], ['id', 17817], ['id', 14749], ['id', 991], ['id', 32864], ['id', 8298], ['ood', 36985], ['id', 57720]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.633057713508606, 0.4981294870376587, 0.4546361565589905, 0.41332119703292847, 0.5813063979148865, 0.5365275740623474, 0.4293801188468933, 0.3118436336517334, 0.43453550338745117, 0.5139858722686768]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 1.0166709423065186})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5724496841430664})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.39587223529815674})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3405234217643738})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2857246994972229})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2688755393028259})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2756618559360504})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27207690477371216})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28827765583992004})
store['active_learning_steps'][35]['training']['best_epoch']=6
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9697, 'crossentropy': 0.246440380859375}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.9054921865463257})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5127320289611816})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.37385183572769165})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34808284044265747})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3221411108970642})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.28137916326522827})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2988412380218506})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3162420094013214})
store['active_learning_steps'][35]['eval_training']['best_epoch']=6
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 788], ['id', 134], ['id', 32918], ['id', 59747], ['id', 32511], ['id', 212], ['id', 9180], ['id', 25246], ['id', 45972], ['id', 42702]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.40347421169281006, 0.32244694232940674, 0.38160479068756104, 0.5255193710327148, 0.3544243574142456, 0.33356159925460815, 0.5534935593605042, 0.40519243478775024, 0.4828031659126282, 0.3213183283805847]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.2108380794525146})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5568937063217163})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.43686503171920776})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.33733612298965454})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.31332817673683167})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32087621092796326})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2842126488685608})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2891853451728821})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3183460235595703})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.3102807104587555})
store['active_learning_steps'][36]['training']['best_epoch']=7
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.969, 'crossentropy': 0.2567244140625}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.8033010959625244})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5365190505981445})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.41648924350738525})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.35318708419799805})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2979661226272583})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29390448331832886})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2853066921234131})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2958824634552002})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27570420503616333})
store['active_learning_steps'][36]['eval_training']['best_epoch']=9
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 2078], ['id', 41322], ['id', 1375], ['id', 5042], ['id', 15602], ['id', 52237], ['ood', 48390], ['id', 51464], ['ood', 58300], ['id', 7015]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.20606935024261475, 0.37504640221595764, 0.362668514251709, 0.460246205329895, 0.37520867586135864, 0.4316374659538269, 0.30506718158721924, 0.2414199709892273, 0.28569841384887695, 0.5134534239768982]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.1933841705322266})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5435220003128052})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.39572983980178833})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.336095929145813})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31033581495285034})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2953619360923767})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29066139459609985})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2714284062385559})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.30480828881263733})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30880483984947205})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.263802707195282})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27392375469207764})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2763397693634033})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.27534887194633484})
store['active_learning_steps'][37]['training']['best_epoch']=11
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9722, 'crossentropy': 0.252124658203125}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.8586574196815491})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5160630941390991})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.39151740074157715})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3392886519432068})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3102564215660095})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28803175687789917})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.27842533588409424})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2526588439941406})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2458159327507019})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26189562678337097})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.25591421127319336})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2277868688106537})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2405669391155243})
store['active_learning_steps'][37]['eval_training']['best_epoch']=12
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 28375], ['id', 28644], ['id', 28775], ['id', 12493], ['id', 34069], ['id', 54586], ['id', 186], ['id', 24030], ['id', 8918], ['id', 30688]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.3862565755844116, 0.36555999517440796, 0.6216428279876709, 0.3332429528236389, 0.40342944860458374, 0.29050856828689575, 0.47367173433303833, 0.5272552967071533, 0.4571388363838196, 0.5057353377342224]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 1.1381959915161133})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5763747692108154})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3668597638607025})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29990121722221375})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31044644117355347})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.254393070936203})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2609814405441284})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2494521588087082})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.25497961044311523})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.25591355562210083})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2663099765777588})
store['active_learning_steps'][38]['training']['best_epoch']=8
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9728, 'crossentropy': 0.235088330078125}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.9311327934265137})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5530263185501099})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3622984290122986})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33552730083465576})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.274416446685791})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2853201627731323})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27238577604293823})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.26480603218078613})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.23449958860874176})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.26928257942199707})
store['active_learning_steps'][38]['eval_training']['best_epoch']=9
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 36337], ['id', 14972], ['id', 21880], ['id', 29530], ['id', 31114], ['id', 7259], ['id', 17234], ['id', 30016], ['id', 9952], ['id', 16964]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.7808632254600525, 0.6067308187484741, 0.5259646773338318, 0.5026944279670715, 0.453788161277771, 0.3431817889213562, 0.4671069383621216, 0.5040692687034607, 0.41063958406448364, 0.48265135288238525]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.0943024158477783})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.6372123956680298})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4218308925628662})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.35172539949417114})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3432667851448059})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3200407028198242})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3129178285598755})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3149435818195343})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3089023530483246})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3092098534107208})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2995765209197998})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.29871270060539246})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2904220223426819})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3043763041496277})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3333045244216919})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3258156180381775})
store['active_learning_steps'][39]['training']['best_epoch']=13
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9718, 'crossentropy': 0.252999267578125}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.9644496440887451})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5549749135971069})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4357665777206421})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3212953209877014})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3215256333351135})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2896997928619385})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2842373847961426})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2757859528064728})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2577860951423645})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.25581076741218567})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.24672117829322815})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.24411329627037048})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2548152804374695})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.23749244213104248})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.23121850192546844})
store['active_learning_steps'][39]['eval_training']['best_epoch']=15
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 26017], ['id', 52319], ['id', 12947], ['id', 26389], ['id', 29294], ['id', 49111], ['id', 1598], ['id', 41998], ['id', 1573], ['id', 37118]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4180179536342621, 0.4023735523223877, 0.5429350733757019, 0.5482480525970459, 0.699496328830719, 0.5514019727706909, 0.443081796169281, 0.3936671316623688, 0.5755785703659058, 0.47767436504364014]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.0864543914794922})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5995523929595947})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4419803023338318})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3281468451023102})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3245026469230652})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3018456995487213})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3062993288040161})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2702016830444336})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30296850204467773})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27754727005958557})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2768372595310211})
store['active_learning_steps'][40]['training']['best_epoch']=8
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9707, 'crossentropy': 0.256762451171875}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9356899261474609})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.44893234968185425})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3958507776260376})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3478376269340515})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.33364641666412354})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29459089040756226})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2912186086177826})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30373990535736084})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2817521393299103})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2666036784648895})
store['active_learning_steps'][40]['eval_training']['best_epoch']=10
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 15912], ['id', 37770], ['id', 24191], ['id', 22320], ['id', 15855], ['id', 8690], ['id', 5129], ['id', 17739], ['id', 27085], ['id', 13173]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.3835570812225342, 0.3817794919013977, 0.256289541721344, 0.515798807144165, 0.37823742628097534, 0.4408160448074341, 0.4200199842453003, 0.6105694770812988, 0.463991641998291, 0.40107792615890503]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.144913911819458})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5358184576034546})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4102001190185547})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3171444833278656})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30613476037979126})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.24753567576408386})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28224706649780273})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2877163290977478})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2847817540168762})
store['active_learning_steps'][41]['training']['best_epoch']=6
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.972, 'crossentropy': 0.2523659423828125}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8667100667953491})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4828326106071472})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4032514691352844})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3292708396911621})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.33525505661964417})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30247485637664795})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.30655401945114136})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.271198570728302})
store['active_learning_steps'][41]['eval_training']['best_epoch']=8
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 27994], ['id', 30884], ['id', 16173], ['id', 4058], ['id', 15486], ['id', 22635], ['id', 14635], ['id', 7192], ['id', 7920], ['id', 17540]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.302295982837677, 0.3519415855407715, 0.3315233588218689, 0.5066155195236206, 0.4064972996711731, 0.46626126766204834, 0.45795512199401855, 0.40645062923431396, 0.4742203950881958, 0.5247118473052979]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.2018951177597046})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6558820605278015})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.41545525193214417})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.35724347829818726})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.326336145401001})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31631016731262207})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2860691547393799})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.29442334175109863})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31105101108551025})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3134413957595825})
store['active_learning_steps'][42]['training']['best_epoch']=7
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9698, 'crossentropy': 0.25135283203125}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8566139936447144})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5164139270782471})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3891783356666565})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3545997738838196})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3386034071445465})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.28563880920410156})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29917699098587036})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2917565107345581})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.27523496747016907})
store['active_learning_steps'][42]['eval_training']['best_epoch']=9
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 37048], ['id', 1293], ['id', 7308], ['id', 28374], ['id', 50224], ['id', 13895], ['id', 27406], ['id', 35688], ['id', 41108], ['id', 23021]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.4954625368118286, 0.3597937822341919, 0.5022786259651184, 0.4773707985877991, 0.47774988412857056, 0.45698654651641846, 0.4508523941040039, 0.4902377724647522, 0.42480039596557617, 0.4042043685913086]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.275747299194336})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5929843187332153})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.4349106252193451})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3496994972229004})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31610268354415894})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.289970338344574})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.28411588072776794})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28295624256134033})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3029312491416931})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2797238826751709})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2874564528465271})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2785852253437042})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2708786129951477})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30078381299972534})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27210116386413574})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.27579617500305176})
store['active_learning_steps'][43]['training']['best_epoch']=13
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9765, 'crossentropy': 0.2322954833984375}
