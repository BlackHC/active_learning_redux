store = {}
store['timestamp']=1622064901
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=2']
store['commit']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['github_url']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=2
store['worker_id']=2
store['num_workers']=80
store['config']={'seed': 1236, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 16, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('FastFashionMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 3792, 5573, 45567, 10508, 2728, 21423, 396, 49512, 31444]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.1934375762939453})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.6525511741638184})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.6837615966796875})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.813356876373291})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.9517016410827637})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.724815845489502})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.838024854660034})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.9290127754211426})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 3.078594923019409})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 3.1395223140716553})
store['active_learning_steps'][0]['training']['best_epoch']=7
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6974, 'crossentropy': 2.602639453125}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.4161242246627808})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.4024074077606201})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.428210735321045})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.6546146869659424})
store['active_learning_steps'][0]['eval_training']['best_epoch']=1
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 16756], ['id', 47759], ['id', 1314], ['id', 46329], ['ood', 4703]], 'labels': [7, 2, 7, 3, -1], 'scores': [0.9461366267069153, 1.6970775946933099, 2.2032851395443283, 2.5164511119361297, 2.6810033929906885]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.531409740447998})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 3.025850534439087})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.803007125854492})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.091292381286621})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6505, 'crossentropy': 2.2942552734375}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.4166442155838013})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.366565465927124})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.3639769554138184})
store['active_learning_steps'][1]['eval_training']['best_epoch']=2
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 36661], ['id', 6873], ['id', 11191], ['id', 32126], ['id', 37209]], 'labels': [5, 8, 8, 4, 3], 'scores': [0.8222107051007899, 1.4837349655491003, 1.9539256177998006, 2.281399550915606, 2.4988475248392303]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.6041226387023926})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.327788829803467})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.124174118041992})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.689312696456909})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7328, 'crossentropy': 1.48794638671875}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.2430870532989502})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.2246665954589844})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.1545038223266602})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 24630], ['id', 42707], ['id', 28136], ['id', 56362], ['ood', 12568]], 'labels': [5, 3, 8, 0, -1], 'scores': [0.685854754035806, 1.2569673585065195, 1.7458400699747552, 2.093067551900119, 2.307304383380437]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.929215908050537})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.271566867828369})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.6419029235839844})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.707381010055542})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7098, 'crossentropy': 1.62091484375}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.2640141248703003})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.256210446357727})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.1942209005355835})
store['active_learning_steps'][3]['eval_training']['best_epoch']=3
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 4356], ['id', 3730], ['id', 26733], ['id', 9370], ['id', 48319]], 'labels': [0, 8, 2, 4, 6], 'scores': [0.7632878079662611, 1.354907004034088, 1.8042228647169107, 2.142302876323212, 2.3662290257940484]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.623449444770813})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.8646332025527954})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.99748957157135})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 2.1499557495117188})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 2.369647264480591})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 2.262737274169922})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.6953177452087402})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 2.313826560974121})
store['active_learning_steps'][4]['training']['best_epoch']=5
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7571, 'crossentropy': 2.0996158203125}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.7339129447937012})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.595507264137268})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.5236222743988037})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.689195156097412})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.445621132850647})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.5361547470092773})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.590250015258789})
store['active_learning_steps'][4]['eval_training']['best_epoch']=5
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 34758], ['id', 36446], ['id', 46961], ['id', 47753], ['id', 6933]], 'labels': [8, 6, 9, 8, 2], 'scores': [0.8288466863588139, 1.529683362850784, 2.0618961363682367, 2.4367688622548225, 2.6535660399498977]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.6707231998443604})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.7221906185150146})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 2.049431562423706})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.9924001693725586})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 2.0622169971466064})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 2.3602101802825928})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 2.439556121826172})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 2.1733241081237793})
store['active_learning_steps'][5]['training']['best_epoch']=5
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7561, 'crossentropy': 1.9454392578125}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.553354263305664})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.547802448272705})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.462925672531128})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.470552921295166})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.4526664018630981})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.4029362201690674})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.2914891242980957})
store['active_learning_steps'][5]['eval_training']['best_epoch']=5
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 17644], ['id', 31312], ['id', 48968], ['id', 39320], ['id', 25856]], 'labels': [9, 9, 9, 6, 4], 'scores': [0.8327462937887802, 1.457508338856195, 1.9301790075714598, 2.2831330931940093, 2.532443289679862]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.38808274269104})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.6359106302261353})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.8759818077087402})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.78873872756958})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.9915800094604492})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.9848873615264893})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 2.0587358474731445})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 2.1143219470977783})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 2.2326884269714355})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 2.0468087196350098})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 2.2889671325683594})
store['active_learning_steps'][6]['training']['best_epoch']=8
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7902, 'crossentropy': 1.8571091796875}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.17543363571167})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.2320985794067383})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.1832600831985474})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.2518222332000732})
store['active_learning_steps'][6]['eval_training']['best_epoch']=1
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 16219], ['id', 5872], ['id', 56612], ['id', 41708], ['id', 12913]], 'labels': [5, 5, 2, 2, 3], 'scores': [0.6877640235390494, 1.2914011972186819, 1.740304797992287, 2.027668224127914, 2.176957719089783]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.3401398658752441})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.4723025560379028})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.6107385158538818})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.8503000736236572})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.931789517402649})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.8823742866516113})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.8253196477890015})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.897521734237671})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 2.084195613861084})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 2.0837178230285645})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 2.199065923690796})
store['active_learning_steps'][7]['training']['best_epoch']=8
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.805, 'crossentropy': 1.5751287109375}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.2174372673034668})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.3001632690429688})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.2368814945220947})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.3183956146240234})
store['active_learning_steps'][7]['eval_training']['best_epoch']=1
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 40234], ['id', 24165], ['id', 28734], ['id', 8933], ['id', 51759]], 'labels': [4, 6, 3, 8, 3], 'scores': [0.7508582055817279, 1.3717639522725338, 1.8619443851190738, 2.1991886008377186, 2.399824251748578]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.0502337217330933})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.071646809577942})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.3213051557540894})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.218212604522705})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.2843477725982666})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.481630802154541})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.336412787437439})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.27472722530365})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.304657220840454})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.3679169416427612})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.64535391330719})
store['active_learning_steps'][8]['training']['best_epoch']=8
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8522, 'crossentropy': 1.12984111328125}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.0544288158416748})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.9865211844444275})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9062745571136475})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.8987745046615601})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.8792575001716614})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.8914241790771484})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.880545437335968})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.8781405687332153})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.8558351993560791})
store['active_learning_steps'][8]['eval_training']['best_epoch']=6
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 7695], ['id', 21138], ['id', 4153], ['id', 48009], ['id', 50840]], 'labels': [2, 9, 2, 2, 2], 'scores': [0.8485844130464084, 1.5309425688737965, 2.061929678158572, 2.455354352510291, 2.705338185164989]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.1158332824707031})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.2042322158813477})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.4678339958190918})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.4344203472137451})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.5720208883285522})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.4890460968017578})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.5500565767288208})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.5535165071487427})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.6069328784942627})
store['active_learning_steps'][9]['training']['best_epoch']=6
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8308, 'crossentropy': 1.330219140625}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.1212260723114014})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.0728601217269897})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.128861904144287})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.022261619567871})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 0.9848311543464661})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.9333324432373047})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 0.9612756967544556})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.0211130380630493})
store['active_learning_steps'][9]['eval_training']['best_epoch']=6
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 41718], ['id', 18264], ['id', 57097], ['id', 22824], ['id', 12137]], 'labels': [8, 2, 7, 9, 5], 'scores': [0.8634781845117957, 1.5369326109085377, 2.0369198256693766, 2.4198517448956287, 2.6575064644531334]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.1780591011047363})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.2778527736663818})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.3510799407958984})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.4179913997650146})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.343636393547058})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.4860360622406006})
store['active_learning_steps'][10]['training']['best_epoch']=3
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8281, 'crossentropy': 1.1874609375}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.0615581274032593})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 0.9000874757766724})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 0.9119138717651367})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 0.8820478916168213})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.8049913644790649})
store['active_learning_steps'][10]['eval_training']['best_epoch']=5
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 19942], ['id', 37919], ['id', 53344], ['id', 43245], ['id', 14100]], 'labels': [5, 9, 0, 5, 5], 'scores': [0.8246160610244382, 1.4879134788897073, 1.996267053358049, 2.3272423925537815, 2.514465330866396]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.9782717823982239})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.0352622270584106})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.1955066919326782})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.290438175201416})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.3249452114105225})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.2729079723358154})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.399234414100647})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.4492912292480469})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.3852880001068115})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.43500816822052})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.4568098783493042})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.7428057193756104})
store['active_learning_steps'][11]['training']['best_epoch']=9
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8384, 'crossentropy': 1.22399541015625}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.0870145559310913})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.9318007230758667})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9961464405059814})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.9435474276542664})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.973816990852356})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9401384592056274})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.87531578540802})
store['active_learning_steps'][11]['eval_training']['best_epoch']=4
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 2369], ['id', 35679], ['id', 50233], ['id', 46400], ['ood', 35952]], 'labels': [8, 2, 7, 2, -1], 'scores': [0.7232888314989333, 1.3558390806668448, 1.9199250237935086, 2.3168812319421623, 2.5677997553940717]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.1462197303771973})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.0362374782562256})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.3783342838287354})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.3279926776885986})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.303600788116455})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.3444753885269165})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.507153868675232})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.37298583984375})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.6729490756988525})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.3330516815185547})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.4940087795257568})
store['active_learning_steps'][12]['training']['best_epoch']=8
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8446, 'crossentropy': 1.31328193359375}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.0138988494873047})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.0184624195098877})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9923555850982666})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.018614649772644})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.8639136552810669})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.9244406223297119})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9326066970825195})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.8892912268638611})
store['active_learning_steps'][12]['eval_training']['best_epoch']=5
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 22139], ['id', 15494], ['id', 55683], ['id', 48507], ['id', 8715]], 'labels': [2, 7, 8, 6, 6], 'scores': [0.8234195598395626, 1.523802980944906, 2.0857142885632385, 2.4498508202159206, 2.665955837072135]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.0515652894973755})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.1077826023101807})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.1718409061431885})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.3573591709136963})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.2877434492111206})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.3864765167236328})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.439825177192688})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.428848385810852})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.3938870429992676})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.5624573230743408})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.3463631868362427})
store['active_learning_steps'][13]['training']['best_epoch']=8
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8454, 'crossentropy': 1.22249765625}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9597599506378174})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8589751720428467})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.8671699166297913})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.871677041053772})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.761783242225647})
store['active_learning_steps'][13]['eval_training']['best_epoch']=2
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 158], ['id', 35232], ['id', 29880], ['id', 9574], ['id', 40084]], 'labels': [7, 8, 5, 6, 2], 'scores': [0.8117075889163364, 1.5339838691199086, 2.1065540239468366, 2.4907463761033535, 2.7268222402511624]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.0668129920959473})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.0183753967285156})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.0351183414459229})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.0461483001708984})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.1356017589569092})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.3469867706298828})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.2464280128479004})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.3408737182617188})
store['active_learning_steps'][14]['training']['best_epoch']=5
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8547, 'crossentropy': 1.00864208984375}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 0.9889973402023315})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.8999133110046387})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.7841501235961914})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.8049365282058716})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.7825086712837219})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.8556917309761047})
store['active_learning_steps'][14]['eval_training']['best_epoch']=3
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 24462], ['id', 12036], ['id', 49539], ['id', 12363], ['id', 36839]], 'labels': [2, 4, 6, 7, 5], 'scores': [0.6831858125813696, 1.2078725710823441, 1.6658428546371993, 2.0350662593680884, 2.289660432028107]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.0677605867385864})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.9933614730834961})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.0546554327011108})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.4029637575149536})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.2738721370697021})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.2604281902313232})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8408, 'crossentropy': 1.06515654296875}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.0361689329147339})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.8317620754241943})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.8153358101844788})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.7468886375427246})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.8030982613563538})
store['active_learning_steps'][15]['eval_training']['best_epoch']=2
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 16733], ['id', 32537], ['id', 23678], ['id', 46139], ['id', 15629]], 'labels': [5, 5, 7, 0, 8], 'scores': [0.6667368277584944, 1.2625258038578568, 1.7309671289053385, 2.036061968134522, 2.1811961081295195]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.092031717300415})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8645243644714355})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.9147403240203857})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.0260052680969238})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.0475170612335205})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.0618391036987305})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.0066030025482178})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.0229188203811646})
store['active_learning_steps'][16]['training']['best_epoch']=5
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8687, 'crossentropy': 0.8872369140625}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.9201476573944092})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7231317758560181})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7087024450302124})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.6584474444389343})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.6839728951454163})
store['active_learning_steps'][16]['eval_training']['best_epoch']=2
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 1276], ['id', 18872], ['id', 25873], ['id', 6920], ['id', 44350]], 'labels': [5, 8, 8, 3, 3], 'scores': [0.6796189216837212, 1.2824957110157689, 1.7521578892133123, 2.0763014915920657, 2.292884051124254]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.9982188940048218})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8828102946281433})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.9373290538787842})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.0595767498016357})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.0535237789154053})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.1345206499099731})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.1187639236450195})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.089452862739563})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.15095853805542})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9825732111930847})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.1615053415298462})
store['active_learning_steps'][17]['training']['best_epoch']=8
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8674, 'crossentropy': 0.987458203125}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.001469612121582})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.8949852585792542})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7440750598907471})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.712643027305603})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7166546583175659})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7114290595054626})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.7184240818023682})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.6601963043212891})
store['active_learning_steps'][17]['eval_training']['best_epoch']=5
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 44095], ['id', 50368], ['id', 3436], ['id', 10194], ['ood', 21680]], 'labels': [2, 2, 4, 2, -1], 'scores': [0.6866018237046787, 1.262445116650654, 1.7344354026718092, 2.0345339880773095, 2.2462993660016046]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 0.9617395997047424})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8429262638092041})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.947475790977478})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.9703699350357056})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.1024020910263062})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.1760003566741943})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.1146214008331299})
store['active_learning_steps'][18]['training']['best_epoch']=4
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8567, 'crossentropy': 0.91411884765625}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9310733675956726})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7011723518371582})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.647824764251709})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.6490710973739624})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6100636720657349})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.564353346824646})
store['active_learning_steps'][18]['eval_training']['best_epoch']=6
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 11292], ['id', 31456], ['id', 45154], ['id', 26391], ['id', 40268]], 'labels': [1, 9, 6, 3, 5], 'scores': [0.7427819207059434, 1.4151424383020386, 1.9714123902178176, 2.381833518130226, 2.607525305607064]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.1015408039093018})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7985535860061646})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8760483264923096})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.9654964804649353})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8800199031829834})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.9755884408950806})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9731645584106445})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.960079550743103})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.013396978378296})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.2231508493423462})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9480863213539124})
store['active_learning_steps'][19]['training']['best_epoch']=8
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8804, 'crossentropy': 0.8873578125}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.9527158737182617})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7882808446884155})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7707725763320923})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7850654125213623})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7400350570678711})
store['active_learning_steps'][19]['eval_training']['best_epoch']=2
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 18200], ['id', 44308], ['id', 6002], ['id', 17855], ['id', 24274]], 'labels': [4, 8, 1, 6, 4], 'scores': [0.6342271936459292, 1.1784950358647177, 1.6488164358794677, 1.9598813738690755, 2.1660638507520416]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.857451856136322})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.7794040441513062})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.9240325093269348})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9012914896011353})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.0607022047042847})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9703364372253418})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.036908745765686})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9592819213867188})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9282240867614746})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 1.046276569366455})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.0063174962997437})
store['active_learning_steps'][20]['training']['best_epoch']=8
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8831, 'crossentropy': 0.830862890625}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.9004489183425903})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.88034987449646})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8179992437362671})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8551611304283142})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8021887540817261})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8079420924186707})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7342836856842041})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7195556163787842})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.7411613464355469})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.6948813199996948})
store['active_learning_steps'][20]['eval_training']['best_epoch']=7
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 52099], ['id', 34805], ['id', 31197], ['id', 22699], ['id', 5537]], 'labels': [2, 3, 2, 4, 8], 'scores': [0.7433765482393275, 1.3415217961411254, 1.8486235776179023, 2.238960298548565, 2.4727592740383626]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8924350738525391})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8023650646209717})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9245718717575073})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.879395604133606})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.0692552328109741})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.985824704170227})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.111634373664856})
store['active_learning_steps'][21]['training']['best_epoch']=4
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.8741, 'crossentropy': 0.84950966796875}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9502698183059692})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7121803760528564})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7216518521308899})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.6535696983337402})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.6570327877998352})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.6726356148719788})
store['active_learning_steps'][21]['eval_training']['best_epoch']=4
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 16022], ['id', 14722], ['id', 24521], ['id', 52729], ['id', 48899]], 'labels': [8, 0, 8, 4, 2], 'scores': [0.7410283491290277, 1.390959511578925, 1.8879894128815362, 2.2582275904320532, 2.46730393077725]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 0.9735205173492432})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7926750779151917})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8612226843833923})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.9267293214797974})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8517650365829468})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.0256192684173584})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.0362701416015625})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.0652062892913818})
store['active_learning_steps'][22]['training']['best_epoch']=5
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.8792, 'crossentropy': 0.80984375}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.9902381896972656})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7674721479415894})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7439785599708557})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7128722667694092})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.6914983987808228})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6131505966186523})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.6315053701400757})
store['active_learning_steps'][22]['eval_training']['best_epoch']=6
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 59303], ['id', 35628], ['id', 57383], ['id', 58046], ['id', 37460]], 'labels': [8, 5, 5, 8, 8], 'scores': [0.6786524900659539, 1.2620577574326437, 1.6971067452840343, 2.009636908576039, 2.2020071785881337]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.106726884841919})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.79969722032547})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.9402035474777222})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9363102316856384})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.039289951324463})
store['active_learning_steps'][23]['training']['best_epoch']=2
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.8542, 'crossentropy': 0.82543984375}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.9432809352874756})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.6941436529159546})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.6913783550262451})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.6825565099716187})
store['active_learning_steps'][23]['eval_training']['best_epoch']=3
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 32047], ['id', 32104], ['id', 15679], ['id', 10886], ['id', 36226]], 'labels': [9, 7, 2, 1, 4], 'scores': [0.5645918586022767, 1.0411631330901128, 1.4625952944524565, 1.8033666727650859, 2.0338221996886103]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.9590926170349121})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8215447664260864})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8577284216880798})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7742549777030945})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9067071676254272})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9285743236541748})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.9615086317062378})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.8966, 'crossentropy': 0.688943603515625}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.9147875308990479})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.6509997844696045})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.5680637359619141})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.5538443326950073})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.5510293245315552})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.539474368095398})
store['active_learning_steps'][24]['eval_training']['best_epoch']=3
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 42632], ['id', 21880], ['id', 39668], ['id', 27992], ['id', 52140]], 'labels': [0, 2, 8, 6, 4], 'scores': [0.6432648616487597, 1.2066993955780836, 1.6651375618672528, 1.9821783183613677, 2.189855543211376]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.996549129486084})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8542522192001343})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7984639406204224})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8222849369049072})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8567390441894531})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.906708836555481})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8881200551986694})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.9504091739654541})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9817119836807251})
store['active_learning_steps'][25]['training']['best_epoch']=6
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.8938, 'crossentropy': 0.815312939453125}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.893239438533783})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6453564763069153})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6512473821640015})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6068885326385498})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.558152437210083})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.5720592737197876})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.5480933785438538})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.5303232073783875})
store['active_learning_steps'][25]['eval_training']['best_epoch']=5
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 16952], ['id', 12655], ['id', 18501], ['id', 37309], ['id', 49616]], 'labels': [2, 9, 4, 3, 7], 'scores': [0.6735361971948542, 1.3013705712744583, 1.856619955326889, 2.2591192683894374, 2.5414063436706518]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9701942205429077})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7377525568008423})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6802190542221069})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7444458603858948})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.765964150428772})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8300256729125977})
store['active_learning_steps'][26]['training']['best_epoch']=3
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.8979, 'crossentropy': 0.649931396484375}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9146796464920044})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.692468523979187})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6293278932571411})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5700607895851135})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.5850421786308289})
store['active_learning_steps'][26]['eval_training']['best_epoch']=4
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 51544], ['id', 49493], ['id', 35246], ['id', 55739], ['id', 10203]], 'labels': [1, 8, 8, 5, 0], 'scores': [0.5999968475546342, 1.154758574746022, 1.593392309922593, 1.9134939281356802, 2.110815211926173]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.0252251625061035})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6785422563552856})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7033435106277466})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6820720434188843})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7567996978759766})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8236934542655945})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7392998933792114})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9068, 'crossentropy': 0.66099208984375}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8860794305801392})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7131583094596863})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.663214385509491})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.5963478684425354})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5555237531661987})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5259531736373901})
store['active_learning_steps'][27]['eval_training']['best_epoch']=6
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 53324], ['id', 13969], ['id', 24329], ['id', 2942], ['id', 27181]], 'labels': [9, 3, 1, 8, 2], 'scores': [0.661186591603214, 1.2438364586582318, 1.71862722857926, 2.0343259592710536, 2.2377737226038157]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.0081140995025635})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6265170574188232})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6010848879814148})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.574641227722168})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5931034088134766})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6643105745315552})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6043163537979126})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6833852529525757})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.664657473564148})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6530855894088745})
store['active_learning_steps'][28]['training']['best_epoch']=7
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9287, 'crossentropy': 0.539297509765625}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8035023212432861})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5518307089805603})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5299214124679565})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.46282678842544556})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.45009517669677734})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4454759359359741})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.42439189553260803})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.43975621461868286})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4080834984779358})
store['active_learning_steps'][28]['eval_training']['best_epoch']=7
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 47443], ['ood', 50517], ['id', 49563], ['id', 30986], ['ood', 56288]], 'labels': [2, -1, 8, 3, -1], 'scores': [0.8125176559596119, 1.4484934786497914, 1.986093751550059, 2.401796459634798, 2.639798588342021]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.9166553020477295})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6088209748268127})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5308215618133545})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5381996035575867})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.565340518951416})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6327787637710571})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6624508500099182})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6159957647323608})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6970922946929932})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6714681386947632})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6911660432815552})
store['active_learning_steps'][29]['training']['best_epoch']=8
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9277, 'crossentropy': 0.575993359375}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.9451024532318115})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6380957365036011})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.524541974067688})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.4792554974555969})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5127871036529541})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.459550678730011})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.45367807149887085})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4304685592651367})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4182779788970947})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4025534391403198})
store['active_learning_steps'][29]['eval_training']['best_epoch']=9
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 57236], ['ood', 50517], ['ood', 48735], ['id', 31184], ['id', 48454]], 'labels': [9, -1, -1, 9, 1], 'scores': [0.7396418624320655, 1.3966674094754814, 1.9237436963289225, 2.285855120729119, 2.4999673700686085]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.9544318914413452})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6723170280456543})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5973131656646729})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6429145336151123})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6293210983276367})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5520989894866943})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6155850887298584})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.589414119720459})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7539177536964417})
store['active_learning_steps'][30]['training']['best_epoch']=6
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9288, 'crossentropy': 0.530261572265625}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.0481845140457153})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5640355348587036})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5327840447425842})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.46566468477249146})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4922652244567871})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.46030116081237793})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4310612678527832})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4316929578781128})
store['active_learning_steps'][30]['eval_training']['best_epoch']=8
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 25187], ['id', 56662], ['id', 47949], ['id', 43048], ['id', 51562]], 'labels': [3, 0, 5, 5, 5], 'scores': [0.7279562227159198, 1.401763613395997, 1.9007470911312314, 2.2420949853319527, 2.4703049766805645]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.9472427368164062})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6041305065155029})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5670961141586304})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5602293014526367})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5831252932548523})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5497176647186279})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6496149301528931})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5782338976860046})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7011324167251587})
store['active_learning_steps'][31]['training']['best_epoch']=6
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9316, 'crossentropy': 0.518468212890625}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.0271201133728027})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6461009383201599})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5202884078025818})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4587699770927429})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5043186545372009})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4734859764575958})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.45098984241485596})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4428567886352539})
store['active_learning_steps'][31]['eval_training']['best_epoch']=5
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 14896], ['ood', 45084], ['id', 57742], ['ood', 38827], ['ood', 15130]], 'labels': [8, -1, 6, -1, -1], 'scores': [0.6665315703531345, 1.246671843016617, 1.7501892764116143, 2.11256478795527, 2.316700546082682]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.9483301639556885})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5962899923324585})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5961713790893555})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5962442755699158})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.654916524887085})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6258053183555603})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6127902269363403})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6238888502120972})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6847281455993652})
store['active_learning_steps'][32]['training']['best_epoch']=6
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9185, 'crossentropy': 0.60224619140625}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.066235899925232})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5840660333633423})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5109431743621826})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.461622416973114})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4438994824886322})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.4408002197742462})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.4416349530220032})
store['active_learning_steps'][32]['eval_training']['best_epoch']=4
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 38194], ['ood', 50403], ['id', 47513], ['id', 35381], ['id', 16488]], 'labels': [5, -1, 0, 3, 9], 'scores': [0.7310971242685733, 1.3264665617850968, 1.8172180601527992, 2.1612612520125936, 2.3675170177232188]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.064049482345581})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6334724426269531})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6045486927032471})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5966241359710693})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.634204626083374})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6474297046661377})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6959309577941895})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.634970486164093})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.7207432389259338})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6786254644393921})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.668471097946167})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6691564321517944})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6841073036193848})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.7499256134033203})
store['active_learning_steps'][33]['training']['best_epoch']=11
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9356, 'crossentropy': 0.57127265625}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9784934520721436})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6028667688369751})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5467289686203003})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.49027252197265625})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.4897648096084595})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.44041138887405396})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.42142754793167114})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.42907917499542236})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4217257499694824})
store['active_learning_steps'][33]['eval_training']['best_epoch']=6
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 2278], ['id', 51722], ['id', 52690], ['id', 7851], ['id', 43208]], 'labels': [0, 4, 3, 8, 3], 'scores': [0.7140320824738193, 1.3471576697407746, 1.8379769335163685, 2.181492047481349, 2.374566764603684]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.9727128744125366})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5795757174491882})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.534828782081604})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.502381443977356})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5242778062820435})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5790133476257324})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5090604424476624})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5709238052368164})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5718419551849365})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5512509942054749})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5470595359802246})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.630814790725708})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6376187801361084})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6284456849098206})
store['active_learning_steps'][34]['training']['best_epoch']=11
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9385, 'crossentropy': 0.519444189453125}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8800411224365234})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5999609231948853})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.49977391958236694})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.45814093947410583})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.44351398944854736})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4001118242740631})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.43336641788482666})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.41157543659210205})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.38220423460006714})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.414071261882782})
store['active_learning_steps'][34]['eval_training']['best_epoch']=7
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 19877], ['id', 4761], ['id', 15781], ['id', 42479], ['id', 13018]], 'labels': [8, 8, 5, 8, 8], 'scores': [0.6943528727999415, 1.3448972573877767, 1.8851815788720945, 2.2628132685923195, 2.511236189458998]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 0.9493232369422913})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6032019853591919})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.58027583360672})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5279546976089478})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6102265119552612})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.568790078163147})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5993423461914062})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5914497375488281})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6997083425521851})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6617670059204102})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6940820217132568})
store['active_learning_steps'][35]['training']['best_epoch']=8
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9268, 'crossentropy': 0.541452001953125}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.0052424669265747})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6432491540908813})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5737050771713257})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.4953767657279968})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.4733280539512634})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4666077494621277})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.46956712007522583})
store['active_learning_steps'][35]['eval_training']['best_epoch']=4
store['active_learning_steps'][35]['acquisition']={'indices': [['ood', 41966], ['id', 31554], ['id', 31200], ['ood', 31904], ['id', 48927]], 'labels': [-1, 5, 9, -1, 9], 'scores': [0.6500419348800364, 1.2549591182254938, 1.746549797939454, 2.069041500121237, 2.252333839729051]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.0806152820587158})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6004570722579956})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5707206726074219})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5558900833129883})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5903339385986328})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.597027063369751})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5648424625396729})
store['active_learning_steps'][36]['training']['best_epoch']=4
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9265, 'crossentropy': 0.504915576171875}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.0037347078323364})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6594408750534058})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.4848066568374634})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.49719902873039246})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.47386717796325684})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5040040016174316})
store['active_learning_steps'][36]['eval_training']['best_epoch']=3
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 10044], ['id', 18426], ['id', 19188], ['ood', 8544], ['id', 47655]], 'labels': [6, 3, 1, -1, 3], 'scores': [0.5945202483135856, 1.1419956808092249, 1.5997670117989933, 1.9344206127042938, 2.164092073768609]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.9290932416915894})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5602366924285889})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4982147812843323})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5042020082473755})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.565178632736206})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4562793970108032})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5149372816085815})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5683680772781372})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5179563760757446})
store['active_learning_steps'][37]['training']['best_epoch']=6
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9375, 'crossentropy': 0.439586767578125}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9825925827026367})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5926656723022461})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.48496130108833313})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4177893400192261})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.41745951771736145})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3828226625919342})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3869907855987549})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.38032209873199463})
store['active_learning_steps'][37]['eval_training']['best_epoch']=8
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 7160], ['id', 18003], ['id', 11852], ['id', 12566], ['id', 12317]], 'labels': [1, 2, 4, 5, 8], 'scores': [0.6276310583906515, 1.1484624472339, 1.6068199717038572, 1.965207314456345, 2.219541529051801]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.9860556125640869})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.566072940826416})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.49437516927719116})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5306404829025269})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5844880938529968})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5163049697875977})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.641690194606781})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6599444150924683})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6255521774291992})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6361097097396851})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.591749906539917})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6667613983154297})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.6212131977081299})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.6228556632995605})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6731590032577515})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6483968496322632})
store['active_learning_steps'][38]['training']['best_epoch']=13
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9368, 'crossentropy': 0.598819482421875}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.0895440578460693})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6094868183135986})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5905418992042542})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.497043639421463})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5041066408157349})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4456203281879425})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.45716217160224915})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.46460819244384766})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4164140522480011})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4068205952644348})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.41732752323150635})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4008561074733734})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4212940037250519})
store['active_learning_steps'][38]['eval_training']['best_epoch']=10
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 33010], ['id', 40477], ['ood', 46619], ['id', 20792], ['id', 48784]], 'labels': [6, 9, -1, 9, 2], 'scores': [0.7674335872611926, 1.4096969066273177, 1.9237137499056227, 2.3136563613285404, 2.606047559513645]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.9638067483901978})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6460287570953369})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5717253684997559})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.557739794254303})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5620013475418091})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5782312154769897})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5854356288909912})
store['active_learning_steps'][39]['training']['best_epoch']=4
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9213, 'crossentropy': 0.540716845703125}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.0837035179138184})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6409469842910767})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5529133081436157})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.5548052191734314})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5133036375045776})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.4888627529144287})
store['active_learning_steps'][39]['eval_training']['best_epoch']=5
store['active_learning_steps'][39]['acquisition']={'indices': [['ood', 22991], ['ood', 6482], ['ood', 58134], ['id', 30326], ['ood', 6657]], 'labels': [-1, -1, -1, 4, -1], 'scores': [0.829174811925032, 1.5579959792694829, 2.052278498994612, 2.4168018089789562, 2.656648529646551]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.0990514755249023})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6552104353904724})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5642316341400146})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5600783824920654})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5743712186813354})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5546218156814575})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5990906357765198})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6206996440887451})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6195302605628967})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6065476536750793})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6537156105041504})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6303349733352661})
store['active_learning_steps'][40]['training']['best_epoch']=9
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9343, 'crossentropy': 0.537221484375}
