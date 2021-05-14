store = {}
store['timestamp']=1620924251
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=16']
store['commit']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['github_url']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=16
store['worker_id']=16
store['num_workers']=20
store['config']={'seed': 1258, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'evaluation_set_size': 100, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.18837571144104})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.682811737060547})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.9211511611938477})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.765324592590332})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6816, 'crossentropy': 1.994144921875}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.196800947189331})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.1787054538726807})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.1686885356903076})
store['active_learning_steps'][0]['eval_training']['best_epoch']=3
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 15773], ['id', 35878], ['id', 26785], ['id', 22685], ['id', 54433], ['id', 52221], ['id', 30016], ['id', 6503], ['id', 35044], ['id', 35429]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8269203901290894, 0.7328079342842102, 0.7143964171409607, 0.8697605729103088, 0.7816694974899292, 0.8598765134811401, 0.6601625680923462, 0.7547415494918823, 0.6796100735664368, 0.6144307851791382]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.8608489036560059})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 2.089472532272339})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.3963961601257324})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 2.3547143936157227})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7346, 'crossentropy': 1.6948298828125}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.0881468057632446})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.0561474561691284})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.0237253904342651})
store['active_learning_steps'][1]['eval_training']['best_epoch']=3
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 37390], ['id', 32325], ['id', 56920], ['id', 53198], ['id', 31396], ['id', 50236], ['id', 59380], ['id', 49992], ['id', 54602], ['id', 7283]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7534961104393005, 0.8103448748588562, 0.6368497014045715, 0.7914993762969971, 0.6887883543968201, 0.7578996419906616, 0.4795670509338379, 0.7860729098320007, 0.7464779615402222, 0.753892719745636]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.4651954174041748})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 2.0324220657348633})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 2.1657633781433105})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 2.3749852180480957})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7576, 'crossentropy': 1.4075322265625}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.067000389099121})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 0.9417377710342407})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 0.9292794466018677})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 8638], ['id', 30129], ['id', 14761], ['id', 49938], ['id', 29966], ['id', 41334], ['id', 31962], ['id', 10012], ['id', 47683], ['id', 4360]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.6698328256607056, 0.5863626599311829, 0.8333197832107544, 0.7650187611579895, 0.6804066896438599, 0.6743489503860474, 0.6813526749610901, 0.6571487188339233, 0.7286024689674377, 0.8265748620033264]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.4903603792190552})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.7569286823272705})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.8002984523773193})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 2.1220338344573975})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7446, 'crossentropy': 1.4090373046875}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.0904929637908936})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.0543243885040283})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 0.9914612770080566})
store['active_learning_steps'][3]['eval_training']['best_epoch']=3
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 10572], ['id', 49476], ['id', 24472], ['id', 54795], ['id', 45281], ['id', 45203], ['id', 29425], ['id', 52944], ['id', 29624], ['id', 5825]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.49895644187927246, 0.5664404630661011, 0.5253452062606812, 0.6253491640090942, 0.5298480987548828, 0.7180810570716858, 0.5450854301452637, 0.5322936773300171, 0.6960636973381042, 0.41424810886383057]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.2959635257720947})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.5856446027755737})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.5370099544525146})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.7048192024230957})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.8, 'crossentropy': 1.1546759765625}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 0.9523590803146362})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 0.8813210129737854})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.812667965888977})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 22497], ['id', 12498], ['id', 22731], ['id', 47056], ['id', 21333], ['id', 33027], ['id', 10923], ['id', 17972], ['id', 27598], ['ood', 4076]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.5408785343170166, 0.4644860029220581, 0.5469507575035095, 0.7085465788841248, 0.5693919062614441, 0.595301628112793, 0.5286116600036621, 0.6675360202789307, 0.47041910886764526, 0.4140608310699463]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.122150182723999})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.0109763145446777})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.1675370931625366})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.1709154844284058})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.278848648071289})
store['active_learning_steps'][5]['training']['best_epoch']=2
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8332, 'crossentropy': 0.9725826171875}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.8357263803482056})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.772538423538208})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.7167564034461975})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.6978090405464172})
store['active_learning_steps'][5]['eval_training']['best_epoch']=4
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 8835], ['id', 14808], ['id', 56669], ['id', 4058], ['id', 12059], ['id', 51271], ['id', 3658], ['id', 30394], ['id', 47983], ['id', 39395]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5314297676086426, 0.4544370174407959, 0.4663052558898926, 0.39717209339141846, 0.5908392667770386, 0.6295098066329956, 0.3952869176864624, 0.409523069858551, 0.5321140885353088, 0.4575679302215576]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8443896770477295})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7407578825950623})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7555885910987854})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7770413160324097})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.8608691692352295})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8974, 'crossentropy': 0.68151015625}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.739585280418396})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5953071117401123})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5464599132537842})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5208957195281982})
store['active_learning_steps'][6]['eval_training']['best_epoch']=4
store['active_learning_steps'][6]['acquisition']={'indices': [['ood', 22502], ['ood', 59475], ['id', 9368], ['id', 43999], ['id', 10156], ['id', 1981], ['id', 19586], ['id', 16183], ['id', 15769], ['id', 14180]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.26526403427124023, 0.45036137104034424, 0.4405949115753174, 0.3681957721710205, 0.308815062046051, 0.3845630884170532, 0.4689651131629944, 0.6203707456588745, 0.57957923412323, 0.5013142824172974]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.9345531463623047})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7664638757705688})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.9473618865013123})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8393650054931641})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.92515629529953})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8647, 'crossentropy': 0.75760576171875}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7381258606910706})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.5953382253646851})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.6163389682769775})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.585090160369873})
store['active_learning_steps'][7]['eval_training']['best_epoch']=4
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 43609], ['id', 38691], ['id', 14587], ['ood', 14127], ['id', 12650], ['id', 3173], ['id', 16973], ['id', 8289], ['id', 7851], ['id', 906]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4794921875, 0.42773526906967163, 0.3601025938987732, 0.3288770914077759, 0.4532088041305542, 0.39958590269088745, 0.47909873723983765, 0.5127492547035217, 0.5011414885520935, 0.50994873046875]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9115356802940369})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7651205062866211})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7015180587768555})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7968708276748657})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7600668668746948})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7647042274475098})
store['active_learning_steps'][8]['training']['best_epoch']=3
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.897, 'crossentropy': 0.659645849609375}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7085865139961243})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.5587098598480225})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5302070379257202})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5122360587120056})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.4888998866081238})
store['active_learning_steps'][8]['eval_training']['best_epoch']=5
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 54880], ['id', 50210], ['id', 31631], ['id', 44261], ['id', 3415], ['id', 56433], ['id', 41830], ['id', 14679], ['id', 10802], ['id', 30446]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.4515664577484131, 0.686294674873352, 0.43222546577453613, 0.5754475593566895, 0.5013350248336792, 0.3420428931713104, 0.5432630181312561, 0.5271508693695068, 0.533930242061615, 0.39308685064315796]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.860304594039917})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6209611892700195})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6006336808204651})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6374520063400269})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6584423184394836})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6312483549118042})
store['active_learning_steps'][9]['training']['best_epoch']=3
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.9113, 'crossentropy': 0.554809423828125}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7514495849609375})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5133755207061768})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.4915171265602112})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.4799383878707886})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.4524102210998535})
store['active_learning_steps'][9]['eval_training']['best_epoch']=5
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 10965], ['id', 7984], ['id', 32774], ['id', 3082], ['id', 35764], ['id', 19575], ['id', 55103], ['id', 47365], ['id', 53979], ['id', 21456]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.45646458864212036, 0.46750348806381226, 0.5134662985801697, 0.46690094470977783, 0.4563729166984558, 0.5881702303886414, 0.4474388360977173, 0.47762101888656616, 0.5384200215339661, 0.4810571074485779]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8064330816268921})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6608227491378784})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6463539600372314})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6854926347732544})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6730121970176697})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6583400964736938})
store['active_learning_steps'][10]['training']['best_epoch']=3
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.905, 'crossentropy': 0.597398974609375}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7015324234962463})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5743542909622192})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.50331711769104})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.48063671588897705})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.48956847190856934})
store['active_learning_steps'][10]['eval_training']['best_epoch']=4
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 50316], ['id', 52592], ['id', 50926], ['id', 45746], ['ood', 41390], ['ood', 24086], ['id', 21601], ['id', 25686], ['id', 30405], ['id', 35482]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5320035219192505, 0.29366636276245117, 0.2523546814918518, 0.5061990022659302, 0.3791780471801758, 0.445212721824646, 0.3505491018295288, 0.42287033796310425, 0.44905441999435425, 0.5536311864852905]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.9235985279083252})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5829183459281921})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5651463270187378})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5059311389923096})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5230013728141785})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5029482841491699})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.575617790222168})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.491952508687973})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5972089767456055})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5437345504760742})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.6004172563552856})
store['active_learning_steps'][11]['training']['best_epoch']=8
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.9289, 'crossentropy': 0.523307666015625}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7168641090393066})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4866138994693756})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4595206081867218})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.40499579906463623})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3719426095485687})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3954290747642517})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3817611634731293})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.3777766227722168})
store['active_learning_steps'][11]['eval_training']['best_epoch']=5
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 59459], ['id', 47910], ['id', 23681], ['id', 7228], ['id', 16869], ['id', 4309], ['id', 44361], ['id', 54947], ['id', 50054], ['id', 49622]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.35716184973716736, 0.3095715343952179, 0.40714943408966064, 0.6001725792884827, 0.4053915739059448, 0.3593660295009613, 0.6770315170288086, 0.4994354248046875, 0.5097179412841797, 0.2965344190597534]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8221459984779358})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.522741436958313})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5830795764923096})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.596013069152832})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6051375865936279})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9236, 'crossentropy': 0.50748974609375}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7923526763916016})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5512701272964478})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.49343937635421753})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4489212930202484})
store['active_learning_steps'][12]['eval_training']['best_epoch']=4
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 31897], ['id', 42906], ['id', 46447], ['id', 51180], ['id', 3636], ['ood', 10804], ['id', 25910], ['id', 29739], ['id', 30149], ['id', 51038]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.25981009006500244, 0.3457707166671753, 0.486041784286499, 0.5434975028038025, 0.41150569915771484, 0.2696448564529419, 0.5129784941673279, 0.24346774816513062, 0.4597703218460083, 0.2716294527053833]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7233467102050781})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.47236108779907227})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4585701823234558})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4404684007167816})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4361810088157654})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.37758439779281616})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.49683427810668945})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.40644580125808716})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.38936102390289307})
store['active_learning_steps'][13]['training']['best_epoch']=6
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.947, 'crossentropy': 0.38307685546875}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7298054695129395})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4528759717941284})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.3771311044692993})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.339277982711792})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.36278143525123596})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3724685311317444})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.32797950506210327})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.33322545886039734})
store['active_learning_steps'][13]['eval_training']['best_epoch']=7
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 16756], ['id', 43368], ['id', 7833], ['ood', 54085], ['id', 836], ['id', 53872], ['id', 11304], ['id', 59344], ['ood', 5858], ['id', 53019]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5148845314979553, 0.4307582378387451, 0.4690183997154236, 0.29240310192108154, 0.34806495904922485, 0.5882952809333801, 0.7444227337837219, 0.5437725782394409, 0.416659414768219, 0.5223672389984131]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8866525888442993})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.49914395809173584})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4493328332901001})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.44232672452926636})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4620516896247864})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.44777393341064453})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4180561900138855})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4251379370689392})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4209769368171692})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4643322229385376})
store['active_learning_steps'][14]['training']['best_epoch']=7
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.944, 'crossentropy': 0.38829599609375}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7461994290351868})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4818848669528961})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3784501850605011})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3506694436073303})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3410831689834595})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3452967405319214})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3506155014038086})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.322639524936676})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.333995521068573})
store['active_learning_steps'][14]['eval_training']['best_epoch']=8
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 45887], ['id', 36589], ['id', 41622], ['id', 8719], ['ood', 29271], ['id', 55153], ['id', 20055], ['id', 11559], ['id', 51432], ['id', 52892]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.4835398197174072, 0.39921003580093384, 0.44142699241638184, 0.3286001682281494, 0.3090226650238037, 0.6093132495880127, 0.3113934099674225, 0.21703147888183594, 0.4091107249259949, 0.3584338426589966]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.9051669836044312})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5415948629379272})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.46795564889907837})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4529121518135071})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4896806478500366})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4615541696548462})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.46277761459350586})
store['active_learning_steps'][15]['training']['best_epoch']=4
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9259, 'crossentropy': 0.444001220703125}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7227258682250977})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5054053068161011})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.41477304697036743})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4213067293167114})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.380764901638031})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3958837389945984})
store['active_learning_steps'][15]['eval_training']['best_epoch']=5
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 21856], ['id', 48102], ['id', 29096], ['id', 52099], ['id', 12768], ['id', 37358], ['id', 55976], ['id', 22989], ['id', 25860], ['ood', 4147]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.37434959411621094, 0.4622432589530945, 0.28072643280029297, 0.42793506383895874, 0.3949686288833618, 0.4304690957069397, 0.30741047859191895, 0.4080003499984741, 0.4296702742576599, 0.34876692295074463]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.942511260509491})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5110456347465515})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4219723641872406})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.40269914269447327})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.42986392974853516})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4095151424407959})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.39807623624801636})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.41079461574554443})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4889734089374542})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.42264968156814575})
store['active_learning_steps'][16]['training']['best_epoch']=7
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9474, 'crossentropy': 0.36895126953125}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.836305558681488})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4808681011199951})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4105849266052246})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.36444392800331116})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3362356424331665})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3550150990486145})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3345339000225067})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.31219300627708435})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.33399444818496704})
store['active_learning_steps'][16]['eval_training']['best_epoch']=8
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 31608], ['id', 41196], ['id', 30184], ['id', 38698], ['id', 32065], ['id', 37450], ['id', 13878], ['id', 12018], ['id', 9340], ['id', 56330]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.263427734375, 0.694139301776886, 0.459682822227478, 0.4407053589820862, 0.39856433868408203, 0.3193565607070923, 0.4954099655151367, 0.4844190776348114, 0.4965214133262634, 0.50324547290802]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.849947452545166})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4773164391517639})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3874359428882599})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3772498369216919})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.36796244978904724})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.36171624064445496})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.37411242723464966})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4127417206764221})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.40991276502609253})
store['active_learning_steps'][17]['training']['best_epoch']=6
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9463, 'crossentropy': 0.367716162109375}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8244104385375977})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4949392080307007})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4231879413127899})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4102485477924347})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.35678452253341675})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3619142770767212})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3249858617782593})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.32666993141174316})
store['active_learning_steps'][17]['eval_training']['best_epoch']=7
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 22149], ['id', 43897], ['ood', 15397], ['id', 12305], ['id', 21852], ['id', 46776], ['id', 14825], ['id', 47674], ['id', 49635], ['id', 5370]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4832184314727783, 0.39973151683807373, 0.18584740161895752, 0.31884491443634033, 0.4731077253818512, 0.4196876883506775, 0.5238080620765686, 0.42761099338531494, 0.38307181000709534, 0.6864529252052307]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9156723022460938})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5331735014915466})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4823891818523407})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.45119747519493103})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.45804500579833984})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4829307794570923})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.42100581526756287})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4380049705505371})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.451709121465683})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4598434269428253})
store['active_learning_steps'][18]['training']['best_epoch']=7
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9522, 'crossentropy': 0.354719677734375}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7890555262565613})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.48065924644470215})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.42671293020248413})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3832959532737732})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.335470050573349})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.31928321719169617})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.33185791969299316})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3159923553466797})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3210591673851013})
store['active_learning_steps'][18]['eval_training']['best_epoch']=8
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 55893], ['id', 13742], ['id', 44732], ['id', 30474], ['id', 4164], ['id', 46673], ['id', 52358], ['id', 17178], ['id', 24577], ['id', 22191]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.47908079624176025, 0.4736218750476837, 0.5389262437820435, 0.31546181440353394, 0.588936448097229, 0.6581327319145203, 0.3860471248626709, 0.48540621995925903, 0.6027761101722717, 0.43819642066955566]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9041571021080017})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.453782856464386})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4170265793800354})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3763774633407593})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3694186210632324})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.38857632875442505})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.39931249618530273})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.41894859075546265})
store['active_learning_steps'][19]['training']['best_epoch']=5
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9541, 'crossentropy': 0.325858544921875}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7662733197212219})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4719555974006653})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.39550819993019104})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.37824809551239014})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3578634262084961})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.36065173149108887})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.331665575504303})
store['active_learning_steps'][19]['eval_training']['best_epoch']=7
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 27876], ['id', 27336], ['id', 49781], ['id', 19612], ['id', 4646], ['id', 12978], ['id', 16961], ['id', 6418], ['id', 29810], ['id', 42199]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.20835834741592407, 0.30806684494018555, 0.5101760029792786, 0.44107967615127563, 0.5625320076942444, 0.2398747205734253, 0.4533165693283081, 0.4247199296951294, 0.35989248752593994, 0.4381452798843384]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9435219168663025})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.47530829906463623})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.39861077070236206})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35647860169410706})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.37029680609703064})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3419995903968811})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.35378748178482056})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.36383292078971863})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3842719793319702})
store['active_learning_steps'][20]['training']['best_epoch']=6
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.961, 'crossentropy': 0.304542431640625}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7332183718681335})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4363640248775482})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.369962215423584})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.33516979217529297})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.33203378319740295})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.34223753213882446})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3015338182449341})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.29265540838241577})
store['active_learning_steps'][20]['eval_training']['best_epoch']=8
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 46285], ['id', 1772], ['id', 31738], ['id', 24457], ['id', 12268], ['id', 11858], ['id', 16799], ['id', 39865], ['id', 55310], ['id', 1518]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.5252202153205872, 0.4843904376029968, 0.4399142265319824, 0.6430351138114929, 0.5006576180458069, 0.47594404220581055, 0.5074709057807922, 0.4878811240196228, 0.5731033682823181, 0.5004487037658691]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9336515665054321})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4455506503582001})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4109598696231842})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3678438365459442})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3802022933959961})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32292869687080383})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.36017167568206787})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33573365211486816})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.36851781606674194})
store['active_learning_steps'][21]['training']['best_epoch']=6
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9593, 'crossentropy': 0.302397216796875}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7647905349731445})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.47590160369873047})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.39229634404182434})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.32578325271606445})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2952909469604492})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3196863532066345})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.30832719802856445})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2857053279876709})
store['active_learning_steps'][21]['eval_training']['best_epoch']=8
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 11822], ['id', 20206], ['id', 5000], ['id', 20039], ['id', 43372], ['id', 8614], ['id', 17698], ['id', 48584], ['id', 57334], ['id', 51988]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.4349878430366516, 0.37517988681793213, 0.5840756893157959, 0.42926502227783203, 0.4883766174316406, 0.45651912689208984, 0.5027152895927429, 0.37186241149902344, 0.5652171969413757, 0.4229488968849182]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.0269562005996704})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.48584094643592834})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4157169461250305})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.36393094062805176})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3840962052345276})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.40468332171440125})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4362061321735382})
store['active_learning_steps'][22]['training']['best_epoch']=4
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9485, 'crossentropy': 0.35167890625}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8453537225723267})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5469229221343994})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.43063080310821533})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.39169400930404663})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3758160173892975})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3858542740345001})
store['active_learning_steps'][22]['eval_training']['best_epoch']=5
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 1033], ['id', 17738], ['id', 29863], ['id', 51337], ['id', 47142], ['id', 46432], ['id', 16485], ['id', 27829], ['id', 18572], ['id', 18519]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.35108697414398193, 0.41640377044677734, 0.4578820466995239, 0.42107582092285156, 0.2858320474624634, 0.35428953170776367, 0.536994457244873, 0.5786154866218567, 0.36978697776794434, 0.3838658332824707]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8261046409606934})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4664028584957123})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.335419237613678})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3466520309448242})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3657209873199463})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3435670733451843})
store['active_learning_steps'][23]['training']['best_epoch']=3
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9549, 'crossentropy': 0.3178845458984375}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7610229253768921})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4821462631225586})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.42753052711486816})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3672560155391693})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3557213246822357})
store['active_learning_steps'][23]['eval_training']['best_epoch']=5
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 11864], ['ood', 27521], ['id', 33824], ['id', 22436], ['id', 2092], ['id', 8649], ['id', 41016], ['id', 9147], ['id', 32776], ['id', 2343]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3189049959182739, 0.21162426471710205, 0.43407928943634033, 0.4530603885650635, 0.41178226470947266, 0.36863547563552856, 0.33350950479507446, 0.5164895057678223, 0.4038625955581665, 0.1751599907875061]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8834726214408875})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.513305127620697})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.41376644372940063})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3786541223526001})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3526439070701599})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.35883593559265137})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3374060392379761})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3578462600708008})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3699299097061157})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4205848276615143})
store['active_learning_steps'][24]['training']['best_epoch']=7
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9602, 'crossentropy': 0.2930052734375}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8418495655059814})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4375413656234741})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.37438368797302246})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2919121980667114})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3170187175273895})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2856292724609375})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2914467453956604})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2983959913253784})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.29926955699920654})
store['active_learning_steps'][24]['eval_training']['best_epoch']=6
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 12012], ['id', 14025], ['id', 18589], ['id', 16036], ['id', 10044], ['id', 20714], ['id', 52060], ['id', 25346], ['id', 28200], ['id', 43943]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5435774326324463, 0.37684276700019836, 0.5481207072734833, 0.500109076499939, 0.38546425104141235, 0.5905974507331848, 0.32186222076416016, 0.4129353165626526, 0.3204103112220764, 0.4007854461669922]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8161017894744873})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4299960434436798})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.35322630405426025})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32202422618865967})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.33464014530181885})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3250250518321991})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3252401351928711})
store['active_learning_steps'][25]['training']['best_epoch']=4
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9607, 'crossentropy': 0.2838343994140625}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7844109535217285})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.49905574321746826})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4170619547367096})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3403923511505127})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.34650322794914246})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.36936360597610474})
store['active_learning_steps'][25]['eval_training']['best_epoch']=4
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 32668], ['ood', 53668], ['ood', 33635], ['id', 51942], ['id', 8857], ['id', 18598], ['id', 5155], ['id', 6974], ['id', 56014], ['id', 45056]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5205891728401184, 0.237138032913208, 0.17153573036193848, 0.2925564646720886, 0.279213011264801, 0.37582993507385254, 0.38466787338256836, 0.14793002605438232, 0.3421117067337036, 0.3311527967453003]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.9981590509414673})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.48173603415489197})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.38873016834259033})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.34973451495170593})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.344776451587677})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.35142865777015686})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3311370015144348})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.37452542781829834})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.34540536999702454})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3279306888580322})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35814160108566284})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3483728766441345})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.388461172580719})
store['active_learning_steps'][26]['training']['best_epoch']=10
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9646, 'crossentropy': 0.292381591796875}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8444111347198486})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.496995747089386})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.39874136447906494})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3552584648132324})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3294733166694641})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.28907686471939087})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.30338990688323975})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.28368109464645386})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2998853027820587})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.27608272433280945})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2899009585380554})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2819669246673584})
store['active_learning_steps'][26]['eval_training']['best_epoch']=10
store['active_learning_steps'][26]['acquisition']={'indices': [['ood', 10894], ['id', 53844], ['id', 22734], ['id', 20881], ['id', 50728], ['id', 33304], ['id', 9008], ['id', 28030], ['id', 29821], ['id', 13524]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.29880034923553467, 0.516169548034668, 0.28445059061050415, 0.4270264506340027, 0.43427836894989014, 0.3947393596172333, 0.6498041152954102, 0.4603552222251892, 0.3355771005153656, 0.5287507772445679]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8931964635848999})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5412180423736572})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.38243114948272705})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3241451382637024})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3419066071510315})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3530825972557068})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3394102454185486})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9612, 'crossentropy': 0.3032521484375}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8146167993545532})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.48626112937927246})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.39209556579589844})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.35846439003944397})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.33836638927459717})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.30185872316360474})
store['active_learning_steps'][27]['eval_training']['best_epoch']=6
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 47403], ['id', 11104], ['id', 50905], ['id', 41779], ['id', 39822], ['id', 30646], ['id', 49493], ['id', 11541], ['id', 15945], ['id', 224]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.39902687072753906, 0.3955736756324768, 0.38100898265838623, 0.24790418148040771, 0.39840757846832275, 0.32502996921539307, 0.302609384059906, 0.24466148018836975, 0.2948076128959656, 0.38847076892852783]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.1146271228790283})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5410555005073547})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3930298089981079})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3601894676685333})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.320324182510376})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3329622149467468})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3482820987701416})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3638930320739746})
store['active_learning_steps'][28]['training']['best_epoch']=5
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.963, 'crossentropy': 0.293579150390625}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7948508262634277})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.456720769405365})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3612217903137207})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.327505886554718})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.32046079635620117})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.29140734672546387})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2948685884475708})
store['active_learning_steps'][28]['eval_training']['best_epoch']=6
store['active_learning_steps'][28]['acquisition']={'indices': [['ood', 4115], ['id', 22484], ['id', 10867], ['id', 21306], ['id', 51856], ['id', 2765], ['id', 1682], ['id', 31444], ['id', 33013], ['id', 48507]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.23073434829711914, 0.40503036975860596, 0.3149402141571045, 0.3164113163948059, 0.37033629417419434, 0.45758056640625, 0.5303024053573608, 0.47376924753189087, 0.36948084831237793, 0.4343335032463074]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.0529752969741821})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.49425408244132996})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3857441544532776})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33132386207580566})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31579840183258057})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2997925281524658})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.33408331871032715})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.296993613243103})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3083066940307617})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3513561487197876})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3382500410079956})
store['active_learning_steps'][29]['training']['best_epoch']=8
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9644, 'crossentropy': 0.2802710693359375}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.9139111042022705})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4834152162075043})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3859463334083557})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.32146352529525757})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32817065715789795})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.30090048909187317})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.31494343280792236})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.31335753202438354})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.260797917842865})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.23779112100601196})
store['active_learning_steps'][29]['eval_training']['best_epoch']=10
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 6302], ['ood', 9962], ['id', 31185], ['id', 30238], ['id', 4822], ['id', 17501], ['id', 7259], ['id', 33198], ['id', 46814], ['id', 33152]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.57931749522686, 0.20584475994110107, 0.2970846891403198, 0.42619484663009644, 0.5143295526504517, 0.632718563079834, 0.47545796632766724, 0.4217461943626404, 0.4825552701950073, 0.4263719916343689]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.0951318740844727})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5666993856430054})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.37593144178390503})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3743728995323181})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.36088910698890686})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3328983187675476})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3167943060398102})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3044249713420868})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.31639420986175537})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3284785747528076})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3532979488372803})
store['active_learning_steps'][30]['training']['best_epoch']=8
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9653, 'crossentropy': 0.270435009765625}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8353671431541443})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.49726229906082153})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3911261558532715})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3531358242034912})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3289034366607666})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2687720060348511})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2998355031013489})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.283999502658844})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.26104092597961426})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.27997028827667236})
store['active_learning_steps'][30]['eval_training']['best_epoch']=9
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 38559], ['id', 25246], ['id', 19495], ['id', 55368], ['id', 19089], ['id', 29150], ['id', 35406], ['id', 33892], ['id', 37584], ['id', 40022]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.4322352409362793, 0.5699293613433838, 0.4463673233985901, 0.42259103059768677, 0.571452260017395, 0.4273149371147156, 0.3970727324485779, 0.5737822651863098, 0.6137241125106812, 0.44564545154571533]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 1.0026901960372925})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.5186918377876282})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35319429636001587})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3195476531982422})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.30948108434677124})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2805343270301819})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.31512290239334106})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3003239631652832})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3193376064300537})
store['active_learning_steps'][31]['training']['best_epoch']=6
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9677, 'crossentropy': 0.254325830078125}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8091025948524475})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.43539959192276})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3557698130607605})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3409375548362732})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3346748352050781})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3350074887275696})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30479252338409424})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2713501751422882})
store['active_learning_steps'][31]['eval_training']['best_epoch']=8
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 31014], ['id', 30692], ['id', 26733], ['id', 17292], ['id', 21896], ['id', 8790], ['id', 40138], ['id', 48494], ['ood', 19614], ['id', 8680]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5987968444824219, 0.41010403633117676, 0.42204582691192627, 0.37654703855514526, 0.41157233715057373, 0.38823020458221436, 0.5530314445495605, 0.40443962812423706, 0.21934008598327637, 0.5673704743385315]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.1350007057189941})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5947170853614807})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3751816749572754})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.35254010558128357})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.3092038631439209})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3239033818244934})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2913264036178589})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27652400732040405})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2877982258796692})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3161323070526123})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30408698320388794})
store['active_learning_steps'][32]['training']['best_epoch']=8
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9689, 'crossentropy': 0.2519882080078125}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8826904892921448})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.45178836584091187})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3174824118614197})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2918955683708191})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.256949245929718})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2758749723434448})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2770501375198364})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.254096120595932})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2511081099510193})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.262785404920578})
store['active_learning_steps'][32]['eval_training']['best_epoch']=9
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 41382], ['id', 18525], ['id', 13854], ['id', 53884], ['id', 31981], ['id', 42121], ['id', 14852], ['id', 36982], ['id', 13153], ['id', 22083]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6072062849998474, 0.5392372608184814, 0.5145010948181152, 0.5379443168640137, 0.41331255435943604, 0.5687925815582275, 0.4832139015197754, 0.5880065560340881, 0.3495154082775116, 0.5338498950004578]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.1885297298431396})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5293542146682739})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3665838837623596})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3126290440559387})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3237394392490387})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.27146899700164795})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2982668876647949})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32176870107650757})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27073150873184204})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29362213611602783})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31104180216789246})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.30309760570526123})
store['active_learning_steps'][33]['training']['best_epoch']=9
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9677, 'crossentropy': 0.262437255859375}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9248705506324768})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5591533184051514})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.39078909158706665})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3446378707885742})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3167775273323059})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.27757203578948975})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2892700135707855})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2895439863204956})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2904624342918396})
store['active_learning_steps'][33]['eval_training']['best_epoch']=6
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 19502], ['id', 19868], ['id', 32880], ['id', 37934], ['id', 25008], ['id', 30962], ['id', 11074], ['id', 39384], ['id', 17139], ['id', 51300]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.33929750323295593, 0.6478025913238525, 0.5138373374938965, 0.3460932970046997, 0.3910254240036011, 0.48321232199668884, 0.32864150404930115, 0.3132917284965515, 0.23404940962791443, 0.3001716732978821]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.1693179607391357})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5148870944976807})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3917269706726074})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.34096193313598633})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3346213102340698})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.300709992647171})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2866276502609253})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2896186411380768})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2827610969543457})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2715263366699219})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.30299603939056396})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2923465371131897})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28669315576553345})
store['active_learning_steps'][34]['training']['best_epoch']=10
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9683, 'crossentropy': 0.2702664794921875}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.9891622066497803})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5716073513031006})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.39241641759872437})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.34089434146881104})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2890715003013611})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2712540030479431})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2917628884315491})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.23776578903198242})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.23272299766540527})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.244604229927063})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.25100672245025635})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.22891253232955933})
store['active_learning_steps'][34]['eval_training']['best_epoch']=12
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 50369], ['id', 1032], ['id', 40350], ['id', 54994], ['id', 15337], ['id', 33505], ['id', 1075], ['id', 46148], ['id', 9346], ['id', 28876]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.35593730211257935, 0.3735613226890564, 0.4169861674308777, 0.36291611194610596, 0.4229786694049835, 0.564494252204895, 0.644952118396759, 0.6673314571380615, 0.6960877776145935, 0.3846927285194397]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.189344048500061})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5916503667831421})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.39094704389572144})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3240880072116852})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3271332383155823})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.27983230352401733})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2739645540714264})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2926740050315857})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30346769094467163})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2972605228424072})
store['active_learning_steps'][35]['training']['best_epoch']=7
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9664, 'crossentropy': 0.2614041259765625}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.8998088836669922})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5000343918800354})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.36756935715675354})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3348325490951538})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2764379382133484})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2776796817779541})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.294526070356369})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2847040593624115})
store['active_learning_steps'][35]['eval_training']['best_epoch']=5
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 59490], ['id', 57575], ['id', 51870], ['id', 37696], ['id', 52953], ['id', 44484], ['id', 55958], ['id', 43702], ['id', 28826], ['id', 7655]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4222133457660675, 0.43134188652038574, 0.2762915790081024, 0.4933362603187561, 0.35654813051223755, 0.4669710397720337, 0.363529771566391, 0.37557196617126465, 0.2305983006954193, 0.46316513419151306]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.2485778331756592})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5659114122390747})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.34923696517944336})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3376288414001465})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.330363392829895})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3091873526573181})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.30591508746147156})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3001008629798889})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3246475160121918})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.31477493047714233})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.33758148550987244})
store['active_learning_steps'][36]['training']['best_epoch']=8
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9714, 'crossentropy': 0.242739013671875}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.9358941316604614})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4745357632637024})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34915226697921753})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3546340763568878})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2817535102367401})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2695397138595581})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.26597365736961365})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26320600509643555})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2529093623161316})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.26448625326156616})
store['active_learning_steps'][36]['eval_training']['best_epoch']=9
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 26738], ['id', 54067], ['id', 24649], ['id', 14373], ['id', 24884], ['id', 53567], ['id', 42799], ['id', 48198], ['id', 35326], ['id', 59726]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3219733238220215, 0.45297157764434814, 0.36708253622055054, 0.5049943327903748, 0.2741878032684326, 0.47981730103492737, 0.5812760591506958, 0.270036518573761, 0.4682571291923523, 0.4986691474914551]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.1594339609146118})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5256688594818115})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3913165032863617})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3323777914047241})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3187851905822754})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3106462359428406})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3108379542827606})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2973436117172241})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2923436760902405})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3051919937133789})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2918272018432617})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29251283407211304})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30251824855804443})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3138914108276367})
store['active_learning_steps'][37]['training']['best_epoch']=11
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9706, 'crossentropy': 0.2481168212890625}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.9303070306777954})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.5129776000976562})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3819177746772766})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31178492307662964})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.29835212230682373})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27670377492904663})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.261711061000824})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2856515645980835})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.25967085361480713})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2671641707420349})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.26009663939476013})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.25909334421157837})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.25443267822265625})
store['active_learning_steps'][37]['eval_training']['best_epoch']=13
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 4349], ['id', 30080], ['id', 56454], ['id', 16676], ['id', 36072], ['id', 18813], ['id', 9431], ['id', 58871], ['ood', 47734], ['id', 40976]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.39396411180496216, 0.4520232081413269, 0.5617320537567139, 0.3847543001174927, 0.604438304901123, 0.3652004301548004, 0.5800439119338989, 0.4517329931259155, 0.19237613677978516, 0.5644610226154327]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.4744027853012085})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6514461040496826})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5044920444488525})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.39053821563720703})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.38439467549324036})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3378370404243469})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3253343999385834})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34187278151512146})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3548401892185211})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3382722735404968})
store['active_learning_steps'][38]['training']['best_epoch']=7
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9641, 'crossentropy': 0.2869200439453125}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.9596021175384521})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5030121207237244})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4037133753299713})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.34516283869743347})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3232493996620178})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.27381691336631775})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.304440975189209})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3029947876930237})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30703699588775635})
store['active_learning_steps'][38]['eval_training']['best_epoch']=6
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 37460], ['id', 47322], ['id', 20150], ['id', 11406], ['id', 16043], ['id', 47520], ['id', 11639], ['id', 34650], ['ood', 47545], ['id', 18510]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.48360276222229004, 0.44648289680480957, 0.2560464143753052, 0.2862504720687866, 0.525063693523407, 0.35924720764160156, 0.5058575868606567, 0.4112497568130493, 0.2890690565109253, 0.33886682987213135]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.3187847137451172})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6340966820716858})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.37952810525894165})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3393374979496002})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.30241405963897705})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30996036529541016})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28927934169769287})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.319119930267334})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2736722528934479})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2543865442276001})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3122144341468811})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.29973018169403076})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.29755014181137085})
store['active_learning_steps'][39]['training']['best_epoch']=10
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9682, 'crossentropy': 0.254209033203125}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.9932770729064941})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.49989110231399536})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4183034300804138})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31862273812294006})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2487882673740387})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2781674861907959})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.267061710357666})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2611420154571533})
store['active_learning_steps'][39]['eval_training']['best_epoch']=5
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 49672], ['id', 32054], ['id', 16951], ['id', 32926], ['id', 2450], ['id', 46339], ['id', 23441], ['id', 47235], ['id', 30041], ['id', 14982]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.2829137444496155, 0.47543179988861084, 0.5054894685745239, 0.4027038812637329, 0.46574684977531433, 0.45997193455696106, 0.3999147415161133, 0.4604048728942871, 0.41038262844085693, 0.2929442226886749]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.1580629348754883})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.6488436460494995})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4359949231147766})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3485528528690338})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2827623188495636})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.270383358001709})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.24928054213523865})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2843163013458252})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2770835757255554})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2773818373680115})
store['active_learning_steps'][40]['training']['best_epoch']=7
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9733, 'crossentropy': 0.225782470703125}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8810573220252991})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.48279517889022827})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.35297468304634094})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3165120780467987})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.277602881193161})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.24321503937244415})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2543153166770935})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2690001428127289})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2702525854110718})
store['active_learning_steps'][40]['eval_training']['best_epoch']=6
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 29751], ['id', 56358], ['id', 31068], ['id', 39848], ['id', 57808], ['id', 22144], ['id', 13729], ['id', 36818], ['id', 56190], ['id', 33536]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3772583603858948, 0.31119900941848755, 0.3209487795829773, 0.32218509912490845, 0.41794002056121826, 0.35668665170669556, 0.5842565298080444, 0.4170991778373718, 0.3108491599559784, 0.27626946568489075]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.2665212154388428})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.661217212677002})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.41892415285110474})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29622793197631836})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2983267903327942})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2633454203605652})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.284878671169281})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2900620698928833})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2456209808588028})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.24848975241184235})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2405194342136383})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2682889997959137})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27261418104171753})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2829136848449707})
store['active_learning_steps'][41]['training']['best_epoch']=11
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9731, 'crossentropy': 0.2269478271484375}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.9377951622009277})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4524414539337158})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3512157201766968})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.286980003118515})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.28775444626808167})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.24843399226665497})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.268416166305542})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.24593909084796906})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2651655972003937})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.23942041397094727})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.23837631940841675})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.22409221529960632})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.22562915086746216})
store['active_learning_steps'][41]['eval_training']['best_epoch']=12
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 2426], ['id', 42573], ['id', 52086], ['ood', 1007], ['id', 39778], ['id', 6995], ['id', 39208], ['id', 2030], ['ood', 46395], ['id', 44849]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.47492456436157227, 0.41791093349456787, 0.5368582606315613, 0.2349681854248047, 0.5407578945159912, 0.3907451629638672, 0.6507859826087952, 0.5091509222984314, 0.23813748359680176, 0.4555211067199707]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.197129487991333})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5316653251647949})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3556407690048218})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.28137436509132385})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2836531698703766})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27401405572891235})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.25509586930274963})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.24711695313453674})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2408764660358429})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27142736315727234})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.26259785890579224})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2622922658920288})
store['active_learning_steps'][42]['training']['best_epoch']=9
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9704, 'crossentropy': 0.233568310546875}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.9742892980575562})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.504868745803833})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.38495945930480957})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33011147379875183})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.31700846552848816})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2622174024581909})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28446444869041443})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.24669067561626434})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2766386866569519})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.25441303849220276})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2722029387950897})
store['active_learning_steps'][42]['eval_training']['best_epoch']=8
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 31275], ['id', 50469], ['id', 43462], ['id', 43048], ['id', 54932], ['id', 28150], ['id', 38165], ['id', 13969], ['id', 37489], ['id', 8552]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.281113862991333, 0.3783513307571411, 0.5269114971160889, 0.2997787594795227, 0.41392040252685547, 0.45410144329071045, 0.5274204015731812, 0.3699617385864258, 0.4036363363265991, 0.3344341516494751]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.1782212257385254})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5126423835754395})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33358559012413025})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31061142683029175})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31315648555755615})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2952672839164734})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2667611241340637})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27456265687942505})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2638477087020874})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.23972922563552856})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2557753026485443})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2607795298099518})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2529945969581604})
store['active_learning_steps'][43]['training']['best_epoch']=10
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9732, 'crossentropy': 0.217217724609375}
