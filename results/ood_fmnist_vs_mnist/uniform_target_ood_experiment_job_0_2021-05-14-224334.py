store = {}
store['timestamp']=1621028614
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=0']
store['commit']='5f7c992432b59cee0eb3a035912cbb6cccf9ff9a'
store['github_url']='5f7c992432b59cee0eb3a035912cbb6cccf9ff9a'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=0
store['worker_id']=0
store['num_workers']=30
store['config']={'seed': 1234, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'evaluation_set_size': 100, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.EvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset: FastMNIST (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastFashionMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 40646, 10110, 32775, 33736, 27254, 306, 37354, 19689, 57811, 14640, 39579, 5573, 5715, 47420, 27135, 26129, 16927, 39050, 42295, 45567, 2728, 1774, 33486, 43252, 43803, 50036, 46861, 53831, 54003, 52801, 15969, 57520, 36797, 34198, 27145, 3029, 37047, 31965, 26501, 53689, 31444, 29950, 44803, 396, 56990, 24052, 12108, 54426, 42320, 801, 48031, 2206, 2404, 58741, 29079, 49986, 46464, 17659, 30072, 55187, 34588, 38725, 50466, 40018, 37115, 20801, 23496, 4321, 42102, 26479, 43321, 44048, 45974, 15675, 10508, 49549, 28991, 13074, 9574, 50997, 48032, 40334, 21423, 46870, 18137, 4701, 18693, 17506, 6968, 3792, 10664, 5616, 32972, 30013, 19757, 49169, 47417, 38430, 41512]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.3959145545959473})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.009756565093994})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.3468470573425293})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.5752663612365723})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.5779, 'crossentropy': 2.625590234375}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.358462929725647})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 1.3103251457214355})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.303393840789795})
store['active_learning_steps'][0]['eval_training']['best_epoch']=3
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 47252], ['ood', 45148], ['ood', 42566], ['ood', 46456], ['ood', 55516], ['ood', 14582], ['ood', 45243], ['ood', 4789], ['ood', 43832], ['ood', 3222]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [1.2257462739944458, 1.1764904856681824, 1.1649401783943176, 1.1542161107063293, 1.1469126343727112, 1.1419536471366882, 1.1235126852989197, 1.120550513267517, 1.111819863319397, 1.1047712564468384]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.564453125, 'crossentropy': 2.22113037109375})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 3.1437413692474365})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5595703125, 'crossentropy': 3.5668911933898926})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 3.544548273086548})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.5501, 'crossentropy': 2.385484375}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.57421875, 'crossentropy': 1.4064369201660156})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.5693359375, 'crossentropy': 1.369092345237732})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.576171875, 'crossentropy': 1.3055768013000488})
store['active_learning_steps'][1]['eval_training']['best_epoch']=3
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 35776], ['id', 9302], ['id', 40979], ['id', 43426], ['id', 30693], ['id', 58220], ['id', 23416], ['id', 4689], ['id', 59627], ['id', 16154]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7229611873626709, 0.7222020626068115, 0.7090809941291809, 0.7043580412864685, 0.6951416730880737, 0.6888877153396606, 0.6886236071586609, 0.6816051006317139, 0.6811914443969727, 0.6764780282974243]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.464298129081726})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.422269344329834})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.2858262062072754})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.753396511077881})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6107, 'crossentropy': 1.50541064453125}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 1.2361645698547363})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.1505837440490723})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.1579670906066895})
store['active_learning_steps'][2]['eval_training']['best_epoch']=2
store['active_learning_steps'][2]['acquisition']={'indices': [['ood', 40418], ['ood', 1873], ['ood', 41877], ['ood', 22634], ['ood', 25917], ['ood', 15848], ['ood', 5409], ['ood', 41937], ['ood', 58046], ['ood', 53469]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.6624612808227539, 0.6600583791732788, 0.6490464210510254, 0.6373553276062012, 0.6362165212631226, 0.6290936470031738, 0.6248502731323242, 0.6219731569290161, 0.6203081607818604, 0.61855149269104]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.3611340522766113})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.7630245685577393})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.175781488418579})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.4028592109680176})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6136, 'crossentropy': 1.3653265625}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.2804020643234253})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.2127892971038818})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.2148854732513428})
store['active_learning_steps'][3]['eval_training']['best_epoch']=2
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 22232], ['id', 12430], ['id', 14700], ['id', 1033], ['id', 7492], ['id', 50774], ['id', 56058], ['id', 58300], ['id', 3194], ['id', 20656]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.40900659561157227, 0.40591180324554443, 0.4042321443557739, 0.40262508392333984, 0.40025579929351807, 0.39544910192489624, 0.3923720121383667, 0.3912597894668579, 0.39123499393463135, 0.3902759552001953]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 1.3227832317352295})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.4060537815093994})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.655777931213379})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.1133296489715576})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.5647, 'crossentropy': 1.36738173828125}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.5595703125, 'crossentropy': 1.3175768852233887})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 1.32447350025177})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.2792489528656006})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 50487], ['id', 3976], ['id', 49461], ['id', 22412], ['id', 36627], ['id', 45708], ['id', 52229], ['id', 28110], ['id', 20578], ['id', 41641]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.40274202823638916, 0.3814358115196228, 0.3797089457511902, 0.3790976405143738, 0.36932212114334106, 0.3679264187812805, 0.3670980930328369, 0.36702466011047363, 0.364788293838501, 0.36341726779937744]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.385502815246582})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.365959644317627})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.7665053606033325})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.0389859676361084})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.8603930473327637})
store['active_learning_steps'][5]['training']['best_epoch']=2
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.6399, 'crossentropy': 1.41386767578125}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.2254199981689453})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.1086574792861938})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.1010018587112427})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.0618488788604736})
store['active_learning_steps'][5]['eval_training']['best_epoch']=4
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 6572], ['id', 59682], ['id', 1350], ['id', 55078], ['id', 29629], ['id', 42210], ['id', 57000], ['id', 54053], ['id', 47772], ['id', 38696]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5072638988494873, 0.506495475769043, 0.4958608150482178, 0.49349403381347656, 0.493272066116333, 0.4927457571029663, 0.48758769035339355, 0.4854457378387451, 0.4834860563278198, 0.48275840282440186]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.3390345573425293})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.2505528926849365})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.506472110748291})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.6824696063995361})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.8323848247528076})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.6515, 'crossentropy': 1.290834765625}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.1570665836334229})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.048163890838623})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.0417802333831787})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.0303301811218262})
store['active_learning_steps'][6]['eval_training']['best_epoch']=4
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 40549], ['id', 52590], ['id', 27719], ['id', 27863], ['id', 2434], ['id', 53054], ['id', 23401], ['id', 33801], ['id', 29255], ['id', 28218]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5228146314620972, 0.4963189363479614, 0.4918729066848755, 0.4833589792251587, 0.4763460159301758, 0.4708077311515808, 0.46434491872787476, 0.45886677503585815, 0.4569716453552246, 0.45029687881469727]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.5693359375, 'crossentropy': 1.3648159503936768})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.382707118988037})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.4634101390838623})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.8092572689056396})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.5482, 'crossentropy': 1.36951416015625}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.515625, 'crossentropy': 1.4148510694503784})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.5419921875, 'crossentropy': 1.3179938793182373})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.5390625, 'crossentropy': 1.3159667253494263})
store['active_learning_steps'][7]['eval_training']['best_epoch']=3
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 10251], ['id', 36293], ['id', 9862], ['id', 19398], ['id', 59806], ['id', 23087], ['id', 29125], ['id', 18814], ['id', 1799], ['id', 3913]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.34035539627075195, 0.3356863260269165, 0.3346543312072754, 0.33300673961639404, 0.33257853984832764, 0.32857322692871094, 0.3278486728668213, 0.3272141218185425, 0.3261357545852661, 0.31979143619537354]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.5498046875, 'crossentropy': 1.4637887477874756})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.4405457973480225})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.5759568214416504})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.8104276657104492})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.8668614625930786})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.5988, 'crossentropy': 1.43897119140625}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.5478515625, 'crossentropy': 1.2763723134994507})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.1606022119522095})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.1513992547988892})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.1631255149841309})
store['active_learning_steps'][8]['eval_training']['best_epoch']=3
store['active_learning_steps'][8]['acquisition']={'indices': [['ood', 5236], ['ood', 51786], ['ood', 58182], ['ood', 220], ['ood', 22958], ['ood', 35832], ['ood', 28920], ['ood', 4360], ['ood', 37613], ['ood', 33010]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.47349441051483154, 0.452514111995697, 0.4505186080932617, 0.4453237056732178, 0.44158780574798584, 0.43159759044647217, 0.4306703805923462, 0.42626941204071045, 0.4237098693847656, 0.4191274642944336]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.5205078125, 'crossentropy': 1.5007096529006958})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.3171250820159912})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.4364745616912842})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.7054060697555542})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.8172733783721924})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.595, 'crossentropy': 1.359037890625}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.3355703353881836})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 1.2182331085205078})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.2176934480667114})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.1937263011932373})
store['active_learning_steps'][9]['eval_training']['best_epoch']=4
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 19800], ['id', 34425], ['id', 6657], ['id', 22139], ['id', 48811], ['id', 43644], ['id', 52334], ['id', 14647], ['id', 1776], ['id', 43543]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.4233335256576538, 0.40448129177093506, 0.39993274211883545, 0.3942503333091736, 0.3909297585487366, 0.39060521125793457, 0.38862109184265137, 0.38756561279296875, 0.38525938987731934, 0.385092556476593]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.5068359375, 'crossentropy': 1.498782992362976})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.3026853799819946})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.3892509937286377})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.4527963399887085})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.669715404510498})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.6255, 'crossentropy': 1.3028427734375}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.3193551301956177})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.2011604309082031})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.198345422744751})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.1476640701293945})
store['active_learning_steps'][10]['eval_training']['best_epoch']=4
store['active_learning_steps'][10]['acquisition']={'indices': [['ood', 31173], ['ood', 14944], ['id', 22547], ['id', 57392], ['id', 39750], ['ood', 18412], ['ood', 1590], ['ood', 34514], ['id', 57751], ['ood', 24461]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.4078104496002197, 0.4036763310432434, 0.3995780944824219, 0.39454150199890137, 0.393057644367218, 0.3921504616737366, 0.3920139670372009, 0.3917475938796997, 0.3893672823905945, 0.388147234916687]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.5166015625, 'crossentropy': 1.4640932083129883})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.2823286056518555})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.425417423248291})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.52179753780365})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.5276380777359009})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.6051, 'crossentropy': 1.31324248046875}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.5478515625, 'crossentropy': 1.3165031671524048})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.1818666458129883})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.158433437347412})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.1548713445663452})
store['active_learning_steps'][11]['eval_training']['best_epoch']=4
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 20686], ['id', 56747], ['id', 1488], ['id', 5535], ['id', 38188], ['id', 34458], ['id', 45126], ['id', 55037], ['id', 3852], ['id', 6565]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.45949411392211914, 0.42479652166366577, 0.41992270946502686, 0.4168604612350464, 0.4123849868774414, 0.4105139374732971, 0.4095337390899658, 0.4089759588241577, 0.40710514783859253, 0.4043201208114624]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.4912109375, 'crossentropy': 1.5431928634643555})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 1.3501636981964111})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.2512931823730469})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.3474557399749756})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.4138140678405762})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.4984138011932373})
store['active_learning_steps'][12]['training']['best_epoch']=3
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.638, 'crossentropy': 1.28870146484375}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 1.31436288356781})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.1903762817382812})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.1047812700271606})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.114135980606079})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.1339976787567139})
store['active_learning_steps'][12]['eval_training']['best_epoch']=3
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 38889], ['id', 34920], ['id', 34821], ['id', 53015], ['id', 47471], ['id', 17205], ['id', 35711], ['id', 3282], ['id', 4623], ['id', 49039]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.4712461233139038, 0.39837849140167236, 0.39496636390686035, 0.37186121940612793, 0.37028419971466064, 0.36858928203582764, 0.36758577823638916, 0.36386919021606445, 0.36035335063934326, 0.3597341775894165]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.4716796875, 'crossentropy': 1.5229475498199463})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 1.3469184637069702})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.288694143295288})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.366300344467163})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.5229294300079346})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.6088812351226807})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6347, 'crossentropy': 1.29975517578125}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 1.2670174837112427})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.1612927913665771})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.1397626399993896})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.124443769454956})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.0828635692596436})
store['active_learning_steps'][13]['eval_training']['best_epoch']=5
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 27800], ['id', 10886], ['id', 27712], ['id', 59348], ['id', 18754], ['id', 47079], ['id', 42858], ['id', 43636], ['id', 59054], ['id', 11510]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.49190497398376465, 0.45245760679244995, 0.4458523988723755, 0.44564783573150635, 0.44483482837677, 0.44286584854125977, 0.44196462631225586, 0.4418737590312958, 0.4296605587005615, 0.42659515142440796]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5107421875, 'crossentropy': 1.557334065437317})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.2740797996520996})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.2316359281539917})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.2245874404907227})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.3443553447723389})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.3472623825073242})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.4541174173355103})
store['active_learning_steps'][14]['training']['best_epoch']=4
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.6824, 'crossentropy': 1.22562607421875}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.253873348236084})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.0899834632873535})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.1002600193023682})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.0516173839569092})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.040963888168335})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.0335575342178345})
store['active_learning_steps'][14]['eval_training']['best_epoch']=6
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 31557], ['id', 18292], ['id', 59646], ['id', 39951], ['id', 35971], ['id', 12241], ['id', 46619], ['id', 15599], ['ood', 56289], ['id', 57174]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.6240140199661255, 0.5593172311782837, 0.5417921543121338, 0.5224747061729431, 0.5155056715011597, 0.4958588778972626, 0.49113136529922485, 0.48482000827789307, 0.483736515045166, 0.4750971794128418]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.4580078125, 'crossentropy': 1.6157472133636475})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.3278566598892212})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.3007107973098755})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.2650115489959717})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.4098396301269531})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.451362133026123})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.3806617259979248})
store['active_learning_steps'][15]['training']['best_epoch']=4
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.6698, 'crossentropy': 1.27767529296875}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.2639284133911133})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.1324764490127563})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.090301752090454})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.08158540725708})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.0711909532546997})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.050703763961792})
store['active_learning_steps'][15]['eval_training']['best_epoch']=6
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 14529], ['id', 47764], ['id', 37709], ['id', 46050], ['id', 25738], ['id', 8278], ['id', 52722], ['id', 25290], ['id', 26568], ['id', 18207]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5117974877357483, 0.4965684413909912, 0.4927225112915039, 0.4891098141670227, 0.4890066385269165, 0.48872166872024536, 0.487160325050354, 0.48652493953704834, 0.48055410385131836, 0.48014771938323975]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.4853515625, 'crossentropy': 1.5896377563476562})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.282109022140503})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.1627304553985596})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.153550386428833})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.161522388458252})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.270355463027954})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.4439709186553955})
store['active_learning_steps'][16]['training']['best_epoch']=4
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.6827, 'crossentropy': 1.1514150390625}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.231589436531067})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.0864405632019043})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.0648243427276611})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0208492279052734})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.0085225105285645})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 0.9778388738632202})
store['active_learning_steps'][16]['eval_training']['best_epoch']=6
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 4148], ['id', 38782], ['id', 26219], ['id', 56948], ['ood', 54066], ['ood', 47613], ['ood', 31699], ['id', 23425], ['id', 326], ['id', 15357]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.4677177667617798, 0.4529803395271301, 0.44429636001586914, 0.44212937355041504, 0.4376477003097534, 0.4167991876602173, 0.41402363777160645, 0.4132845997810364, 0.4106866717338562, 0.4072195887565613]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.48046875, 'crossentropy': 1.4585245847702026})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.1519074440002441})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.153540015220642})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.1605284214019775})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.147288203239441})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.3314573764801025})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.3545395135879517})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.3392493724822998})
store['active_learning_steps'][17]['training']['best_epoch']=5
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.6779, 'crossentropy': 1.18223115234375}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 1.3037898540496826})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.0805683135986328})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.0301686525344849})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.0431709289550781})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 0.9828649759292603})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 0.9728461503982544})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 0.9882580041885376})
store['active_learning_steps'][17]['eval_training']['best_epoch']=6
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 56635], ['id', 7577], ['id', 57582], ['id', 40572], ['id', 26871], ['id', 20624], ['id', 59953], ['id', 41358], ['id', 40968], ['id', 52602]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.4669252038002014, 0.4500313401222229, 0.43268489837646484, 0.4269574284553528, 0.40191876888275146, 0.40013134479522705, 0.39616119861602783, 0.39409029483795166, 0.38622236251831055, 0.3803791403770447]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.49609375, 'crossentropy': 1.5243337154388428})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.2608118057250977})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.15311861038208})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.1429409980773926})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.1847524642944336})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.3301243782043457})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.3285417556762695})
store['active_learning_steps'][18]['training']['best_epoch']=4
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6795, 'crossentropy': 1.13450615234375}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.2417895793914795})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.0632097721099854})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.0618622303009033})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 0.9897421598434448})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.0247288942337036})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.0119143724441528})
store['active_learning_steps'][18]['eval_training']['best_epoch']=4
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 44011], ['ood', 37074], ['id', 13846], ['id', 38613], ['id', 22780], ['id', 46632], ['id', 36022], ['id', 35995], ['id', 30119], ['id', 36843]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.40748846530914307, 0.40548741817474365, 0.39669978618621826, 0.3961724042892456, 0.3948780298233032, 0.39137375354766846, 0.38994431495666504, 0.3875514268875122, 0.38028252124786377, 0.37984126806259155]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.50390625, 'crossentropy': 1.5179188251495361})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.2384934425354004})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.1537292003631592})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.114546775817871})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.170755386352539})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.178155779838562})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.233703374862671})
store['active_learning_steps'][19]['training']['best_epoch']=4
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6695, 'crossentropy': 1.11044931640625}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.2592108249664307})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.0899744033813477})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.0600343942642212})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.0084903240203857})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 0.9961702823638916})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 0.9807124137878418})
store['active_learning_steps'][19]['eval_training']['best_epoch']=6
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 19185], ['id', 18584], ['id', 10953], ['id', 23637], ['id', 30476], ['id', 13598], ['id', 19138], ['id', 28962], ['id', 12467], ['id', 55765]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5628138780593872, 0.45978742837905884, 0.4503161907196045, 0.44451117515563965, 0.4353095293045044, 0.42515575885772705, 0.4217637777328491, 0.4217336177825928, 0.4207252264022827, 0.41849589347839355]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.4892578125, 'crossentropy': 1.511746883392334})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.248138189315796})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.1021041870117188})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.0804941654205322})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.032670259475708})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.0520870685577393})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.0971555709838867})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.233304738998413})
store['active_learning_steps'][20]['training']['best_epoch']=5
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.6861, 'crossentropy': 1.08636376953125}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.199242353439331})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.0957977771759033})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.0230088233947754})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 0.9580690264701843})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 0.9380249977111816})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 0.9658375978469849})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 0.9487464427947998})
store['active_learning_steps'][20]['eval_training']['best_epoch']=5
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 36294], ['id', 37480], ['id', 32171], ['id', 13530], ['id', 50381], ['id', 54600], ['id', 35874], ['id', 43337], ['id', 35500], ['id', 45306]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.46107667684555054, 0.45579469203948975, 0.45517194271087646, 0.45446479320526123, 0.4416983127593994, 0.4382694959640503, 0.43482714891433716, 0.42767423391342163, 0.4272708296775818, 0.4230351448059082]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.466796875, 'crossentropy': 1.5237572193145752})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.2003741264343262})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.1180531978607178})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.0048457384109497})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.030029296875})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.1509236097335815})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.1950808763504028})
store['active_learning_steps'][21]['training']['best_epoch']=4
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.6878, 'crossentropy': 1.0206263671875}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.3011013269424438})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.091869592666626})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.0576266050338745})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 0.9994262456893921})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 0.9864311218261719})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 0.9531769752502441})
store['active_learning_steps'][21]['eval_training']['best_epoch']=6
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 52509], ['id', 7420], ['id', 4436], ['id', 31037], ['id', 26058], ['id', 25963], ['id', 28173], ['id', 8485], ['id', 6049], ['id', 23980]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.40137970447540283, 0.38741040229797363, 0.38530635833740234, 0.37524735927581787, 0.36671555042266846, 0.3620191812515259, 0.3618279695510864, 0.3602389097213745, 0.3572828769683838, 0.35599470138549805]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.4208984375, 'crossentropy': 1.6622331142425537})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.5263671875, 'crossentropy': 1.3347901105880737})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.201792597770691})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.1614291667938232})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.118780255317688})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.1406112909317017})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.2298860549926758})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.1061732769012451})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.2456729412078857})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.1592684984207153})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.2508726119995117})
store['active_learning_steps'][22]['training']['best_epoch']=8
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.7249, 'crossentropy': 1.117569921875}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.2210075855255127})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.0150578022003174})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 0.960984468460083})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 0.9129085540771484})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 0.9171142578125})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 0.9005054235458374})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 0.8908700942993164})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 0.8883699178695679})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 0.8894883394241333})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 0.8815084099769592})
store['active_learning_steps'][22]['eval_training']['best_epoch']=10
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 24108], ['id', 43039], ['id', 51156], ['id', 1182], ['id', 2759], ['id', 52098], ['id', 22465], ['id', 32286], ['id', 51152], ['id', 48435]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5943421125411987, 0.5926966667175293, 0.587112307548523, 0.580696702003479, 0.574094295501709, 0.5724552869796753, 0.5583729147911072, 0.5412958860397339, 0.5409635901451111, 0.5346555709838867]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.45703125, 'crossentropy': 1.6130441427230835})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.5244140625, 'crossentropy': 1.3491331338882446})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.544921875, 'crossentropy': 1.336665153503418})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.1947872638702393})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.1335575580596924})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.1706645488739014})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.2030086517333984})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.2545263767242432})
store['active_learning_steps'][23]['training']['best_epoch']=5
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.681, 'crossentropy': 1.09753681640625}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 1.2842994928359985})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.1016860008239746})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.0761208534240723})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0278400182724})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0170048475265503})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.0074937343597412})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.0080831050872803})
store['active_learning_steps'][23]['eval_training']['best_epoch']=6
store['active_learning_steps'][23]['acquisition']={'indices': [['ood', 1160], ['id', 14040], ['id', 42673], ['id', 17831], ['id', 2369], ['id', 39373], ['ood', 48107], ['ood', 56440], ['id', 5974], ['id', 30274]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.3862968683242798, 0.3809792995452881, 0.37074846029281616, 0.3702888488769531, 0.36620527505874634, 0.36597365140914917, 0.35980749130249023, 0.35671067237854004, 0.3566351532936096, 0.3520115315914154]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.439453125, 'crossentropy': 1.6247612237930298})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.5546875, 'crossentropy': 1.282731533050537})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.1235778331756592})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.0923001766204834})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.1188185214996338})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.094264268875122})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.0776968002319336})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.2471094131469727})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.1650195121765137})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.2271876335144043})
store['active_learning_steps'][24]['training']['best_epoch']=7
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.7249, 'crossentropy': 1.07011337890625}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.2970552444458008})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.137445092201233})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 0.9767733812332153})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 0.9237380027770996})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 0.9173427224159241})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 0.9341965317726135})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 0.8911291360855103})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 0.9175697565078735})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 0.9013924598693848})
store['active_learning_steps'][24]['eval_training']['best_epoch']=7
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 7656], ['id', 50471], ['id', 28065], ['id', 58639], ['id', 58963], ['id', 37387], ['id', 46249], ['id', 41102], ['id', 810], ['id', 22291]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5738944411277771, 0.5682661533355713, 0.5639311075210571, 0.5571069121360779, 0.5548079609870911, 0.553983211517334, 0.5527969002723694, 0.5526958703994751, 0.5525092482566833, 0.5475829839706421]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.4296875, 'crossentropy': 1.6008126735687256})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 1.2917897701263428})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.1773529052734375})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.1523038148880005})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.1531152725219727})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.1396839618682861})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.1082602739334106})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.241397738456726})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.3182134628295898})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.2596582174301147})
store['active_learning_steps'][25]['training']['best_epoch']=7
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.7233, 'crossentropy': 1.0564103515625}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.192427396774292})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.069413661956787})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 0.9737546443939209})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 0.9405121803283691})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 0.9558501243591309})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 0.9168447852134705})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 0.917640209197998})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 0.8853198289871216})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 0.9475858211517334})
store['active_learning_steps'][25]['eval_training']['best_epoch']=8
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 2731], ['ood', 51436], ['ood', 50094], ['id', 4194], ['id', 35305], ['id', 50770], ['id', 44051], ['ood', 49927], ['id', 29450], ['id', 16872]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.5443716049194336, 0.5254909992218018, 0.4924989938735962, 0.48708152770996094, 0.4797205924987793, 0.47629737854003906, 0.464050829410553, 0.46204912662506104, 0.4579455852508545, 0.45719587802886963]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.5146484375, 'crossentropy': 1.5221807956695557})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.560546875, 'crossentropy': 1.2819113731384277})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.1525604724884033})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.079545259475708})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 0.9922913908958435})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.035347580909729})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.1294505596160889})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.126342535018921})
store['active_learning_steps'][26]['training']['best_epoch']=5
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.7221, 'crossentropy': 0.98420830078125}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.5283203125, 'crossentropy': 1.373116135597229})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.1610881090164185})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.1012704372406006})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.0274295806884766})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.0432238578796387})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.0208970308303833})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 0.9895758628845215})
store['active_learning_steps'][26]['eval_training']['best_epoch']=7
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 58130], ['id', 38058], ['id', 18729], ['id', 55157], ['id', 31662], ['id', 48671], ['id', 28159], ['id', 48293], ['id', 25382], ['id', 19682]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.381477952003479, 0.37522852420806885, 0.37368738651275635, 0.35729002952575684, 0.3437539339065552, 0.3373647928237915, 0.3367271423339844, 0.3327535390853882, 0.33251291513442993, 0.3289825916290283]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.4541015625, 'crossentropy': 1.6090750694274902})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.5390625, 'crossentropy': 1.2824640274047852})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.106985092163086})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.081996202468872})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 0.9788607358932495})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.0543546676635742})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.0212485790252686})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 0.9680213928222656})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.157186508178711})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.0941548347473145})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.1304566860198975})
store['active_learning_steps'][27]['training']['best_epoch']=8
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.7485, 'crossentropy': 0.998009375}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.281281590461731})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.1000105142593384})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.0272605419158936})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 0.9963955879211426})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 0.9313327074050903})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 0.9190993309020996})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 0.9119889736175537})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 0.91553795337677})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 0.916475772857666})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 0.8936219215393066})
store['active_learning_steps'][27]['eval_training']['best_epoch']=10
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 42897], ['id', 2372], ['id', 11953], ['id', 32261], ['id', 28543], ['id', 11651], ['id', 16841], ['ood', 2898], ['id', 36185], ['id', 35424]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.49977636337280273, 0.49608129262924194, 0.48413705825805664, 0.4766152501106262, 0.46120762825012207, 0.4454631805419922, 0.4453020691871643, 0.4355272650718689, 0.4338971972465515, 0.4266786575317383]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.4384765625, 'crossentropy': 1.6689715385437012})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.5361328125, 'crossentropy': 1.2909495830535889})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 1.1911661624908447})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.1627719402313232})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.1000828742980957})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.1193108558654785})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.0639362335205078})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.066264033317566})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.1831350326538086})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.2277635335922241})
store['active_learning_steps'][28]['training']['best_epoch']=7
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.7238, 'crossentropy': 1.0604931640625}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.2414581775665283})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.0638099908828735})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.0043061971664429})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.0111641883850098})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 0.9546558856964111})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 0.9649468660354614})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 0.922214150428772})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 0.923984706401825})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 0.9041891098022461})
store['active_learning_steps'][28]['eval_training']['best_epoch']=9
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 27400], ['id', 8455], ['id', 49135], ['id', 30443], ['id', 44860], ['id', 14436], ['id', 32204], ['id', 32110], ['id', 29206], ['id', 59105]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.45722877979278564, 0.45565879344940186, 0.44376271963119507, 0.44367992877960205, 0.4399530291557312, 0.4396030306816101, 0.436853289604187, 0.4230705499649048, 0.4191586971282959, 0.4190126061439514]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.4501953125, 'crossentropy': 1.6264203786849976})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.501953125, 'crossentropy': 1.3094370365142822})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.1695804595947266})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.0614397525787354})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.0398600101470947})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.0612962245941162})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.1689696311950684})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.1081596612930298})
store['active_learning_steps'][29]['training']['best_epoch']=5
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.6918, 'crossentropy': 1.05957666015625}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.56640625, 'crossentropy': 1.275820016860962})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.0926756858825684})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.0669528245925903})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.0231187343597412})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 0.9675883054733276})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 0.9782508611679077})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 0.9697573184967041})
store['active_learning_steps'][29]['eval_training']['best_epoch']=5
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 10252], ['id', 55165], ['ood', 54913], ['id', 29652], ['ood', 54949], ['id', 59835], ['id', 27212], ['id', 2427], ['id', 40210], ['id', 32856]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3875999450683594, 0.37031257152557373, 0.36148011684417725, 0.36140191555023193, 0.3589463233947754, 0.3573274612426758, 0.3572286367416382, 0.3489685654640198, 0.348818302154541, 0.3478353023529053]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.4384765625, 'crossentropy': 1.603955626487732})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.5341796875, 'crossentropy': 1.318744421005249})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.1032812595367432})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.0974233150482178})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.0587937831878662})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.0740643739700317})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.1120359897613525})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.0830276012420654})
store['active_learning_steps'][30]['training']['best_epoch']=5
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.653, 'crossentropy': 1.07335234375}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.5205078125, 'crossentropy': 1.3119266033172607})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.5751953125, 'crossentropy': 1.108012080192566})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.0776931047439575})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.0476980209350586})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.024592399597168})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.0074632167816162})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 0.9931761026382446})
store['active_learning_steps'][30]['eval_training']['best_epoch']=7
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 19842], ['id', 46507], ['id', 36647], ['id', 18913], ['id', 13384], ['id', 6256], ['ood', 52586], ['ood', 27772], ['ood', 9658], ['id', 70]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.39280402660369873, 0.3604327440261841, 0.3505845069885254, 0.3439524173736572, 0.34352290630340576, 0.34008729457855225, 0.33729636669158936, 0.33276045322418213, 0.3319293260574341, 0.32837462425231934]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.521484375, 'crossentropy': 1.6265387535095215})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.564453125, 'crossentropy': 1.3264808654785156})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 1.2009177207946777})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 1.1575040817260742})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.138092041015625})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.0961480140686035})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.103654384613037})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.127920389175415})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.1991475820541382})
store['active_learning_steps'][31]['training']['best_epoch']=6
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.7032, 'crossentropy': 1.0678796875}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.5380859375, 'crossentropy': 1.3172838687896729})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.1602504253387451})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.0749268531799316})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.0442016124725342})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.0180790424346924})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 0.9986003041267395})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 0.9816608428955078})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 0.9744935035705566})
store['active_learning_steps'][31]['eval_training']['best_epoch']=8
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 16457], ['id', 18079], ['id', 54835], ['ood', 10319], ['id', 22718], ['id', 29501], ['id', 28352], ['id', 20141], ['id', 3929], ['id', 56592]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.452595055103302, 0.43323051929473877, 0.4305293560028076, 0.42842280864715576, 0.42229998111724854, 0.4137084484100342, 0.412888765335083, 0.4124199151992798, 0.40268945693969727, 0.40267813205718994]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.509765625, 'crossentropy': 1.6362779140472412})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.5185546875, 'crossentropy': 1.4236894845962524})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.568359375, 'crossentropy': 1.2506908178329468})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.1444069147109985})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.10444176197052})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.138350248336792})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.1100045442581177})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.0941087007522583})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.0905039310455322})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.1076910495758057})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.063209056854248})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.1227169036865234})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.1578340530395508})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.2078888416290283})
store['active_learning_steps'][32]['training']['best_epoch']=11
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.7331, 'crossentropy': 1.080069921875}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 1.3743305206298828})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.1444705724716187})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.0502617359161377})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 0.963533878326416})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 0.9337620735168457})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 0.9370944499969482})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 0.915382981300354})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 0.9193714261054993})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 0.895021915435791})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 0.8994645476341248})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 0.8672174215316772})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 0.9199018478393555})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 0.8683908581733704})
store['active_learning_steps'][32]['eval_training']['best_epoch']=11
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 49864], ['id', 6212], ['id', 41623], ['id', 54405], ['id', 1935], ['id', 49891], ['id', 11958], ['id', 2298], ['id', 1752], ['id', 35215]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5954798460006714, 0.5080977082252502, 0.49535828828811646, 0.4913559556007385, 0.490473210811615, 0.48167628049850464, 0.48111069202423096, 0.4778589606285095, 0.4716538190841675, 0.4713444709777832]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.44921875, 'crossentropy': 1.717907428741455})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.5654296875, 'crossentropy': 1.3754924535751343})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.1985862255096436})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.1164307594299316})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.1050159931182861})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.0372990369796753})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.0787081718444824})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.0722999572753906})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.130746841430664})
store['active_learning_steps'][33]['training']['best_epoch']=6
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.7208, 'crossentropy': 1.007840234375}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.3050353527069092})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.1323356628417969})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.0897207260131836})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.0145387649536133})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 0.9985731840133667})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 0.9758260250091553})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 0.9897880554199219})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 0.9569669961929321})
store['active_learning_steps'][33]['eval_training']['best_epoch']=8
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 33141], ['id', 47163], ['id', 15841], ['id', 58841], ['id', 35376], ['id', 13107], ['id', 51236], ['id', 34238], ['id', 47904], ['id', 41355]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.48510146141052246, 0.4128413200378418, 0.38672661781311035, 0.3859955668449402, 0.3758019208908081, 0.37532222270965576, 0.3709886074066162, 0.36979687213897705, 0.3667137622833252, 0.3666236400604248]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.443359375, 'crossentropy': 1.6789617538452148})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.5263671875, 'crossentropy': 1.3333446979522705})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.552734375, 'crossentropy': 1.179091215133667})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.1253018379211426})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.0776643753051758})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0406930446624756})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.0781278610229492})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.1386239528656006})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.069710612297058})
store['active_learning_steps'][34]['training']['best_epoch']=6
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.7238, 'crossentropy': 1.00588388671875}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 1.3629968166351318})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.1566290855407715})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.061903476715088})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 0.9897680878639221})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 0.9960395097732544})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 0.9584771394729614})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.0005379915237427})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 0.9258224964141846})
store['active_learning_steps'][34]['eval_training']['best_epoch']=8
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 43663], ['id', 12078], ['id', 49890], ['id', 33502], ['id', 45176], ['id', 53488], ['id', 6818], ['id', 5708], ['id', 26759], ['id', 25420]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.4359778165817261, 0.43143945932388306, 0.41616177558898926, 0.4158110022544861, 0.41505444049835205, 0.4138491749763489, 0.41114604473114014, 0.4074937701225281, 0.4071849584579468, 0.407063364982605]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.41015625, 'crossentropy': 1.6900081634521484})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.525390625, 'crossentropy': 1.3331698179244995})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.572265625, 'crossentropy': 1.18744695186615})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.121919870376587})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.0991342067718506})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.1136515140533447})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.0113866329193115})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.075297236442566})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.1053917407989502})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.050173044204712})
store['active_learning_steps'][35]['training']['best_epoch']=7
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.702, 'crossentropy': 1.00337978515625}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.5458984375, 'crossentropy': 1.341833472251892})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.0878918170928955})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.064647912979126})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 0.9934777021408081})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 0.9901392459869385})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 0.9415220022201538})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 0.984350860118866})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 0.9208494424819946})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 0.9092888832092285})
store['active_learning_steps'][35]['eval_training']['best_epoch']=9
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 33377], ['id', 16858], ['id', 16996], ['id', 17122], ['id', 11095], ['id', 20968], ['id', 16608], ['id', 32863], ['id', 14622], ['id', 41609]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.43504172563552856, 0.42420756816864014, 0.42014485597610474, 0.41850149631500244, 0.39982306957244873, 0.39963608980178833, 0.3994155526161194, 0.3976735472679138, 0.3965533971786499, 0.393871545791626]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.5263671875, 'crossentropy': 1.542513370513916})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.55859375, 'crossentropy': 1.2797520160675049})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.1002774238586426})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.0186030864715576})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 0.9725801348686218})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 0.9889088869094849})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 0.979172945022583})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 0.981398344039917})
store['active_learning_steps'][36]['training']['best_epoch']=5
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.7228, 'crossentropy': 0.96517646484375}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.270892858505249})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.1181210279464722})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.0451810359954834})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.0419588088989258})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 0.9797322154045105})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 0.9969533681869507})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 0.9680472612380981})
store['active_learning_steps'][36]['eval_training']['best_epoch']=7
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 55098], ['id', 46820], ['id', 40827], ['id', 30790], ['id', 46563], ['id', 13899], ['id', 16969], ['id', 17991], ['id', 24832], ['id', 15226]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.3889620304107666, 0.3692120313644409, 0.3562406301498413, 0.3509625196456909, 0.3502308130264282, 0.34649860858917236, 0.346410870552063, 0.3434904217720032, 0.3409966826438904, 0.3389458656311035]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.455078125, 'crossentropy': 1.598539113998413})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.5556640625, 'crossentropy': 1.2630459070205688})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.102097988128662})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.0716943740844727})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.028534173965454})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 0.9692826271057129})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 0.9903985261917114})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 0.9929419755935669})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.0363805294036865})
store['active_learning_steps'][37]['training']['best_epoch']=6
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.7164, 'crossentropy': 0.98750107421875}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.568359375, 'crossentropy': 1.353941559791565})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.0822298526763916})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.0268185138702393})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 0.9428066611289978})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 0.9655129909515381})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 0.9287408590316772})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 0.93748939037323})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 0.9236451387405396})
store['active_learning_steps'][37]['eval_training']['best_epoch']=8
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 5479], ['ood', 7409], ['id', 8763], ['id', 726], ['id', 52142], ['id', 16349], ['id', 9473], ['id', 26095], ['id', 18809], ['id', 5944]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4337824583053589, 0.42970168590545654, 0.42518138885498047, 0.42314326763153076, 0.41524362564086914, 0.4151182174682617, 0.41126298904418945, 0.4105473756790161, 0.4066042900085449, 0.40405434370040894]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.4697265625, 'crossentropy': 1.5530343055725098})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.2817888259887695})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.0985939502716064})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.0878000259399414})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 0.9951621890068054})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 0.9717273712158203})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 0.9528136253356934})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.0027683973312378})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 0.9718681573867798})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.0537984371185303})
store['active_learning_steps'][38]['training']['best_epoch']=7
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.7446, 'crossentropy': 0.924168359375}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.251136064529419})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.0800433158874512})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 0.9777840375900269})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 0.9268736839294434})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 0.9114405512809753})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 0.9111044406890869})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 0.8823091983795166})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 0.872016191482544})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 0.9000037908554077})
store['active_learning_steps'][38]['eval_training']['best_epoch']=8
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 20009], ['id', 54813], ['id', 18681], ['id', 18278], ['id', 46129], ['id', 42939], ['id', 33525], ['id', 38743], ['id', 51163], ['id', 14145]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4493985176086426, 0.41819220781326294, 0.4089949131011963, 0.3892836570739746, 0.3859140872955322, 0.3798847198486328, 0.373684287071228, 0.3643989562988281, 0.36404842138290405, 0.36146533489227295]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.5283203125, 'crossentropy': 1.603057861328125})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 1.2775160074234009})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.0873832702636719})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.0684973001480103})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 0.9818987846374512})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 0.9291818141937256})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 0.9597448110580444})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 0.9337005615234375})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 0.9219714403152466})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 0.9926933646202087})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.077844500541687})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.003368854522705})
store['active_learning_steps'][39]['training']['best_epoch']=9
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.757, 'crossentropy': 0.89663759765625}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.3213977813720703})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.0622344017028809})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 0.9731380939483643})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 0.9182100296020508})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 0.8924695253372192})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 0.8406169414520264})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 0.858376681804657})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 0.8226751685142517})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 0.8497699499130249})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 0.8337074518203735})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 0.8245817422866821})
store['active_learning_steps'][39]['eval_training']['best_epoch']=8
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 18183], ['id', 1381], ['id', 52498], ['id', 47350], ['id', 49839], ['id', 49811], ['id', 48541], ['id', 55586], ['id', 58583], ['id', 55576]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5086575150489807, 0.4446154236793518, 0.43246567249298096, 0.4242990016937256, 0.42080026865005493, 0.4083450436592102, 0.4071999788284302, 0.39510542154312134, 0.3926524519920349, 0.3922621011734009]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.5361328125, 'crossentropy': 1.5794707536697388})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.1759276390075684})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.0607826709747314})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 0.9552315473556519})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 0.915591835975647})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 0.8915983438491821})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 0.90435791015625})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 0.9011527299880981})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 0.922752857208252})
store['active_learning_steps'][40]['training']['best_epoch']=6
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.7536, 'crossentropy': 0.86832724609375}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.265803575515747})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.0332419872283936})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 0.9726070761680603})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 0.9299243092536926})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 0.8814551830291748})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 0.8874918818473816})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 0.8634012937545776})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 0.8493712544441223})
store['active_learning_steps'][40]['eval_training']['best_epoch']=8
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 9692], ['id', 37251], ['id', 3301], ['id', 59012], ['id', 46216], ['id', 17481], ['ood', 8552], ['id', 22946], ['id', 33674], ['id', 17383]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.40843313932418823, 0.3700345754623413, 0.36422866582870483, 0.36204755306243896, 0.35799407958984375, 0.35092735290527344, 0.3460402488708496, 0.3440800905227661, 0.3431583642959595, 0.3418009281158447]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.525390625, 'crossentropy': 1.5702366828918457})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.2130719423294067})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.0519943237304688})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 0.9319523572921753})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 0.9278324246406555})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 0.8922863602638245})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 0.9151389598846436})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 0.9325491189956665})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 0.943312406539917})
store['active_learning_steps'][41]['training']['best_epoch']=6
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.7522, 'crossentropy': 0.88344345703125}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.2848920822143555})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.1020455360412598})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 0.9696889519691467})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 0.9358810186386108})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 0.895704984664917})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 0.9088894128799438})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 0.9068174362182617})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 0.8502227067947388})
store['active_learning_steps'][41]['eval_training']['best_epoch']=8
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 24627], ['id', 6866], ['id', 5135], ['id', 14784], ['id', 24609], ['id', 44939], ['id', 43854], ['id', 38121], ['id', 40742], ['id', 14265]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4348670244216919, 0.4341124892234802, 0.4272632598876953, 0.4235217571258545, 0.41563379764556885, 0.41553378105163574, 0.4123431444168091, 0.41217750310897827, 0.40897083282470703, 0.40413355827331543]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.5615234375, 'crossentropy': 1.5070056915283203})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.269419550895691})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.1300445795059204})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.0556361675262451})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 0.9588766098022461})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 0.9698852300643921})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 0.9418768286705017})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 0.918636679649353})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.0019936561584473})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 0.9867415428161621})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 0.9765320420265198})
store['active_learning_steps'][42]['training']['best_epoch']=8
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.7401, 'crossentropy': 0.91744736328125}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.2807176113128662})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.0708656311035156})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 0.993812084197998})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 0.8893707990646362})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 0.9198893904685974})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 0.8945667743682861})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 0.9445890188217163})
store['active_learning_steps'][42]['eval_training']['best_epoch']=4
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 56754], ['id', 41044], ['id', 11473], ['id', 30784], ['id', 38374], ['id', 58751], ['id', 48303], ['id', 6478], ['id', 11992], ['id', 47257]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.45956093072891235, 0.449428915977478, 0.4308955669403076, 0.4202982187271118, 0.41500556468963623, 0.4134249687194824, 0.40632015466690063, 0.4011784791946411, 0.4002692699432373, 0.3989967107772827]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.4921875, 'crossentropy': 1.5011684894561768})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.2525854110717773})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.0444319248199463})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 0.9593393802642822})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 0.9049926400184631})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 0.9140703678131104})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 0.9007415771484375})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 0.8976545333862305})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 0.9417262077331543})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 0.99342942237854})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 0.9647570848464966})
store['active_learning_steps'][43]['training']['best_epoch']=8
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.7546, 'crossentropy': 0.88595537109375}
