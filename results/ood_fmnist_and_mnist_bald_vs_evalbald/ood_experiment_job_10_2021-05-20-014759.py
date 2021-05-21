store = {}
store['timestamp']=1621471679
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=10']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=10
store['worker_id']=10
store['num_workers']=80
store['config']={'seed': 1244, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 16, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('FastFashionMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 3792, 5573, 45567, 10508, 2728, 21423, 396, 49512, 31444]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.3093056678771973})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.505469560623169})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.7020537853240967})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.962874412536621})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 3.1163411140441895})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 3.166698932647705})
store['active_learning_steps'][0]['training']['best_epoch']=3
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.7011, 'crossentropy': 2.4685431640625}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 12377], ['id', 30064], ['id', 50321], ['id', 59698], ['id', 1324]], 'labels': [3, 2, 5, 2, 5], 'scores': [1.2697088904757496, 2.30810862137481, 3.1505082501040267, 3.744573167514126, 4.107547919775725]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 2.74021577835083})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.775904417037964})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.0891947746276855})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.979304313659668})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.4963159561157227})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.9676480293273926})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.711670398712158})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.436000347137451})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.64394474029541})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 3.404204845428467})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 3.6479766368865967})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 3.6914596557617188})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 3.221839666366577})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.6492981910705566})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 3.2489662170410156})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 3.509131908416748})
store['active_learning_steps'][1]['training']['best_epoch']=13
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6969, 'crossentropy': 2.817673828125}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 25415], ['id', 54556], ['id', 56792], ['id', 48469], ['id', 7843]], 'labels': [8, 2, 9, 5, 4], 'scores': [1.2785198190110465, 2.4150427827184737, 3.306612280295986, 3.838233633302136, 4.183486688761778]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.111048936843872})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.375235080718994})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.599043369293213})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.6186532974243164})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 3.159769058227539})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.999371290206909})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 3.1163368225097656})
store['active_learning_steps'][2]['training']['best_epoch']=4
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7038, 'crossentropy': 2.2823384765625}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 30079], ['id', 34226], ['id', 50320], ['id', 16155], ['id', 39198]], 'labels': [4, 2, 5, 4, 2], 'scores': [1.3481344897031673, 2.3888820662351833, 3.230372418369324, 3.7856293918313195, 4.139881115521033]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.2161011695861816})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.482705593109131})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.7101192474365234})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.7880940437316895})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.192932605743408})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.728456497192383})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.880390167236328})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 3.3610191345214844})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.9026315212249756})
store['active_learning_steps'][3]['training']['best_epoch']=6
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6985, 'crossentropy': 2.48334140625}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 57570], ['id', 45256], ['id', 43833], ['id', 42707], ['id', 10038]], 'labels': [7, 5, 3, 3, 9], 'scores': [1.236986382196313, 2.331425149140972, 3.2077899939002137, 3.803183281427553, 4.164931025858083]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.6619956493377686})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 2.0062897205352783})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.3415420055389404})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.4043827056884766})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.9424242973327637})
store['active_learning_steps'][4]['training']['best_epoch']=2
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7421, 'crossentropy': 1.6660744140625}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 49438], ['id', 18984], ['id', 5545], ['id', 20388], ['id', 22483]], 'labels': [8, 9, 2, 0, 8], 'scores': [1.0794056964945207, 2.0462659663725686, 2.864406768763881, 3.503019454892292, 3.912431470838677]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.5944628715515137})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.863908052444458})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.8798818588256836})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.9905974864959717})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.1735148429870605})
store['active_learning_steps'][5]['training']['best_epoch']=2
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7685, 'crossentropy': 1.59857470703125}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 34332], ['id', 969], ['id', 8847], ['id', 42570], ['id', 38908]], 'labels': [9, 7, 9, 6, 7], 'scores': [1.1394585076785675, 2.182940559574165, 3.0029109888695302, 3.5972966919206772, 3.9859722665212978]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.3109424114227295})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.5629005432128906})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 2.086611032485962})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.8497865200042725})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.9772573709487915})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 2.2940566539764404})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 2.3867549896240234})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.619818687438965})
store['active_learning_steps'][6]['training']['best_epoch']=5
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.788, 'crossentropy': 1.60755322265625}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 55698], ['id', 17658], ['id', 12497], ['id', 3719], ['id', 33221]], 'labels': [3, 8, 0, 2, 5], 'scores': [1.1409357016125963, 2.1707614708309118, 3.0283226114454944, 3.668638555118924, 4.077215527957082]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.2315338850021362})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.4786375761032104})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.641937494277954})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.68855619430542})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.82456636428833})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.9720964431762695})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 2.172922134399414})
store['active_learning_steps'][7]['training']['best_epoch']=4
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8148, 'crossentropy': 1.41699111328125}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 19423], ['id', 15893], ['id', 18739], ['id', 7851], ['id', 19505]], 'labels': [2, 5, 3, 8, 2], 'scores': [1.1484331320887369, 2.146836960331241, 2.9807710567749846, 3.6163192200497614, 4.0520099071729785]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.1693434715270996})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.4998810291290283})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.4851787090301514})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.4697656631469727})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.9466392993927002})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.8196680545806885})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.8542382717132568})
store['active_learning_steps'][8]['training']['best_epoch']=4
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.826, 'crossentropy': 1.2432208984375}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 17756], ['id', 21307], ['id', 49767], ['id', 8958], ['id', 14773]], 'labels': [8, 4, 9, 3, 0], 'scores': [1.1405788825877, 2.14384418581213, 2.988570418290818, 3.634313408497162, 4.0455894096508285]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.2298206090927124})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.552415370941162})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.651850700378418})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.6922308206558228})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.9133256673812866})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 2.044257164001465})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.9185391664505005})
store['active_learning_steps'][9]['training']['best_epoch']=4
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8096, 'crossentropy': 1.4751943359375}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 18171], ['id', 18190], ['id', 19942], ['id', 7621], ['id', 22144]], 'labels': [0, 4, 5, 7, 0], 'scores': [1.2661733466750094, 2.3810852429381884, 3.2142237369944286, 3.79130169547627, 4.137779993446016]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.0523598194122314})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.182596206665039})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.3764543533325195})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.3835619688034058})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.503221035003662})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8433, 'crossentropy': 0.9925185546875}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 41602], ['id', 17494], ['id', 34594], ['id', 50058], ['id', 56213]], 'labels': [5, 5, 8, 6, 2], 'scores': [1.1186845251652637, 2.098982899797849, 2.90297666942096, 3.4683751572978982, 3.875380806846162]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.2497373819351196})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.0622495412826538})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.2922554016113281})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.4211186170578003})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.341357707977295})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8436, 'crossentropy': 0.891037109375}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 26434], ['id', 16379], ['id', 32126], ['id', 13370], ['id', 16860]], 'labels': [2, 7, 4, 2, 8], 'scores': [0.9613617715019556, 1.807442547209683, 2.5543945937051333, 3.1598278099809587, 3.6107214852758993]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.0258567333221436})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.0486946105957031})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.0564370155334473})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.2866714000701904})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.2018224000930786})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.1876684427261353})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.2832248210906982})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.4056446552276611})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.3992465734481812})
store['active_learning_steps'][12]['training']['best_epoch']=6
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8679, 'crossentropy': 1.02916884765625}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 41572], ['id', 31301], ['id', 47936], ['id', 2856], ['id', 47626]], 'labels': [6, 5, 8, 4, -1], 'scores': [1.1969126242414416, 2.255771910224099, 3.0837729891608667, 3.6761482661325218, 4.071722217255328]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.9509382247924805})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.9598589539527893})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.135120153427124})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.1210572719573975})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.2144758701324463})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.365547776222229})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.4283751249313354})
store['active_learning_steps'][13]['training']['best_epoch']=4
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8547, 'crossentropy': 0.96314521484375}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 51298], ['id', 33505], ['id', 16692], ['id', 40766], ['id', 40595]], 'labels': [5, 2, 5, 4, 8], 'scores': [1.0613429468508304, 1.9755265649507283, 2.7795490199133006, 3.4043449015102727, 3.845912013208313]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.9640809297561646})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8575512170791626})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.9579827785491943})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.0763038396835327})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.1451306343078613})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8625, 'crossentropy': 0.784515869140625}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 5684], ['id', 7924], ['id', 17409], ['id', 35326], ['id', 59468]], 'labels': [6, 8, 3, 5, 7], 'scores': [0.9146410548328836, 1.7638163569755396, 2.46861873581598, 3.0714781430240095, 3.509451099428775]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.0676863193511963})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.9181072115898132})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.0735198259353638})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.1347726583480835})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.0549577474594116})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.1274986267089844})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.1545073986053467})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.1858317852020264})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.280864953994751})
store['active_learning_steps'][15]['training']['best_epoch']=6
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8804, 'crossentropy': 0.914066796875}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 49487], ['id', 5315], ['id', 32747], ['id', 52099], ['id', 57728]], 'labels': [8, 3, 8, 2, 9], 'scores': [1.1726406145739454, 2.1846698356793057, 3.029799095921561, 3.6454586294144793, 4.04915542952398]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.1189320087432861})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8397336602210999})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.0181357860565186})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.0682377815246582})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.1255230903625488})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8734, 'crossentropy': 0.750444775390625}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 33812], ['id', 8691], ['id', 4820], ['id', 41453], ['id', 2761]], 'labels': [6, 2, 5, 3, 8], 'scores': [0.9206967618530124, 1.746167534469707, 2.4595271018151568, 3.0496314685969175, 3.480057379462191]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.1417245864868164})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7573127746582031})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9284588098526001})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.05839204788208})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9714944362640381})
store['active_learning_steps'][17]['training']['best_epoch']=2
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8877, 'crossentropy': 0.6904400390625}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 42020], ['id', 48006], ['id', 52358], ['id', 49354], ['id', 51508]], 'labels': [9, 6, 2, 0, 6], 'scores': [0.9173325054872707, 1.706615512746132, 2.417904866294867, 2.9896870278616117, 3.43177047110383]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.0667624473571777})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7287953495979309})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8272144794464111})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8468567132949829})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9032687544822693})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.9393267631530762})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.915922999382019})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.118037223815918})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9749438762664795})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.071320652961731})
store['active_learning_steps'][18]['training']['best_epoch']=7
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8934, 'crossentropy': 0.86814697265625}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 42703], ['id', 30952], ['id', 2636], ['id', 9180], ['id', 34829]], 'labels': [0, 7, 8, 3, 5], 'scores': [1.1766893134985206, 2.2602464367514745, 3.1581028785376555, 3.8050742830538606, 4.16242130475927]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.1993095874786377})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8475949168205261})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7988592386245728})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8662919998168945})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9553009271621704})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 1.0066101551055908})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9275434017181396})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.0172779560089111})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.20369291305542})
store['active_learning_steps'][19]['training']['best_epoch']=6
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8901, 'crossentropy': 0.866748828125}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 20746], ['id', 26184], ['id', 28838], ['id', 48360], ['id', 32880]], 'labels': [1, 0, 9, 3, 0], 'scores': [1.1031331965676947, 2.1275829976860976, 2.982490882564619, 3.61845195971154, 4.0252218393792685]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.0125927925109863})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6930178999900818})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7239675521850586})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7800000905990601})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8215340375900269})
store['active_learning_steps'][20]['training']['best_epoch']=2
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8974, 'crossentropy': 0.625614208984375}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 9118], ['id', 35449], ['id', 26072], ['id', 1518], ['id', 40390]], 'labels': [9, 0, 1, 9, 0], 'scores': [0.8596472472113146, 1.6286889748092421, 2.3357201129114653, 2.8926425299827683, 3.3448469451034075]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.0176407098770142})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7228364944458008})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7491403818130493})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7942191958427429})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8638646602630615})
store['active_learning_steps'][21]['training']['best_epoch']=2
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.894, 'crossentropy': 0.6555080078125}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 5129], ['id', 12913], ['id', 39411], ['id', 7168], ['id', 42793]], 'labels': [2, 3, 2, 8, 4], 'scores': [0.8506053340233084, 1.6469195547963507, 2.359349735714199, 2.9589301251738584, 3.4245312266797256]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.1155622005462646})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7096618413925171})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8248006105422974})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7738573551177979})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9066812992095947})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.843775749206543})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.0488898754119873})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9512061476707458})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.9284184575080872})
store['active_learning_steps'][22]['training']['best_epoch']=6
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.8994, 'crossentropy': 0.783995751953125}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 50916], ['id', 42265], ['id', 47561], ['id', 58258], ['id', 46247]], 'labels': [4, 7, 6, 7, 3], 'scores': [1.0841252789130702, 2.0835849886780764, 2.9598278302281233, 3.6026408689560068, 4.0242917129566]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.1548378467559814})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.657517671585083})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6504837274551392})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6726831793785095})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7276814579963684})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7800558805465698})
store['active_learning_steps'][23]['training']['best_epoch']=3
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9151, 'crossentropy': 0.56605498046875}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 29087], ['id', 59314], ['id', 45446], ['id', 4822], ['id', 43176]], 'labels': [1, 9, 7, 4, 2], 'scores': [0.9558556885849683, 1.8393995548838076, 2.598475279369188, 3.192335403410988, 3.6467407516535717]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.1203527450561523})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6326957941055298})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7204827070236206})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6241370439529419})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6758413314819336})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8192344307899475})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.743891716003418})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.922, 'crossentropy': 0.561454052734375}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 4165], ['id', 42078], ['id', 45602], ['id', 42199], ['id', 16628]], 'labels': [2, 4, 5, 3, 9], 'scores': [1.0332680004889165, 1.9999968116991411, 2.8054372618028323, 3.4320349895188205, 3.8828125599136634]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.068240761756897})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.609298825263977})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6229065656661987})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6268024444580078})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6470780968666077})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7174019813537598})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6526278257369995})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7271595001220703})
store['active_learning_steps'][25]['training']['best_epoch']=5
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9225, 'crossentropy': 0.56856513671875}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 39818], ['id', 33057], ['id', 11208], ['id', 18487], ['id', 51180]], 'labels': [1, 7, 9, 4, 7], 'scores': [1.057665612629104, 1.9990291546811285, 2.8429034307159275, 3.4876280797108343, 3.92061472793159]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.0183213949203491})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6284612417221069})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5649346709251404})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6101504564285278})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5828105211257935})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7619104385375977})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6615893840789795})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7275383472442627})
store['active_learning_steps'][26]['training']['best_epoch']=5
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9236, 'crossentropy': 0.531079736328125}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 17055], ['id', 41933], ['id', 8762], ['id', 23463], ['id', 32776]], 'labels': [8, 5, 3, 9, 4], 'scores': [1.0084108460102197, 1.9346961501608848, 2.7359120281803104, 3.3890032133583663, 3.837765886427153]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.1604459285736084})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6673545837402344})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5582641363143921})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6025567054748535})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5588219165802002})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.698843240737915})
store['active_learning_steps'][27]['training']['best_epoch']=3
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9194, 'crossentropy': 0.557889453125}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 52169], ['id', 51464], ['id', 44255], ['id', 22193], ['id', 56391]], 'labels': [2, 0, 6, 5, 3], 'scores': [0.9859852407446072, 1.826241334294827, 2.5836070152525323, 3.2016245049201144, 3.6469445768706317]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.0898056030273438})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6000673770904541})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6278122663497925})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5828208923339844})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.776129961013794})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6686629056930542})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6203192472457886})
store['active_learning_steps'][28]['training']['best_epoch']=4
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9331, 'crossentropy': 0.51475439453125}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 1541], ['id', 55372], ['id', 52462], ['id', 34314], ['id', 27085]], 'labels': [4, 6, 9, 7, 8], 'scores': [0.9652650313268252, 1.835056421914226, 2.634523300993881, 3.259056927511063, 3.7291923966537617]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.2772282361984253})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7088896036148071})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5728646516799927})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5778456926345825})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.567211389541626})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6132088899612427})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5923655033111572})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5716910362243652})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5690072774887085})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6938880681991577})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.6060749888420105})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5509070158004761})
store['active_learning_steps'][29]['training']['best_epoch']=9
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.934, 'crossentropy': 0.516276220703125}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 55778], ['id', 13524], ['id', 35269], ['id', 8765], ['id', 52140]], 'labels': [-1, 3, -1, 3, 4], 'scores': [1.0520281000713663, 2.050616721471618, 2.8896210161059432, 3.5417726947660704, 3.973681676481741]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.1970645189285278})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6344934701919556})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5682839751243591})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5179268717765808})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5349500179290771})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5456569194793701})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5863367319107056})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5563212633132935})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5905464887619019})
store['active_learning_steps'][30]['training']['best_epoch']=6
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9339, 'crossentropy': 0.50039306640625}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 37469], ['id', 9340], ['id', 53990], ['id', 14305], ['id', 43200]], 'labels': [2, 5, -1, 8, -1], 'scores': [1.0482443277012523, 1.9845908681799083, 2.782857759688012, 3.4236517873258965, 3.867982743871597]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.213702917098999})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6487569808959961})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5309481024742126})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5751670598983765})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5436557531356812})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5270692706108093})
store['active_learning_steps'][31]['training']['best_epoch']=3
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9292, 'crossentropy': 0.522869189453125}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 57342], ['id', 12767], ['id', 32445], ['id', 28745], ['id', 37688]], 'labels': [2, 9, 5, 7, 9], 'scores': [0.8834689621030947, 1.6980206278027703, 2.414470009456057, 3.008985846192301, 3.4806819860957265]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.2720346450805664})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6073716878890991})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5971626043319702})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5194395780563354})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5317202806472778})
store['active_learning_steps'][32]['training']['best_epoch']=2
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.93, 'crossentropy': 0.56876259765625}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 51492], ['id', 27644], ['id', 11572], ['id', 15948], ['id', 3030]], 'labels': [5, 3, 5, 2, 9], 'scores': [0.7060405693105753, 1.3506045235993032, 1.9339294229838373, 2.452805166851194, 2.900469521947107]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.0701136589050293})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6456844806671143})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.494772732257843})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4923129081726074})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.531046986579895})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5018597841262817})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.565484881401062})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5746981501579285})
store['active_learning_steps'][33]['training']['best_epoch']=5
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9394, 'crossentropy': 0.463673291015625}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 26358], ['id', 50743], ['id', 34328], ['id', 17540], ['id', 21900]], 'labels': [3, 7, 8, 1, 6], 'scores': [1.0763272891265185, 2.0354162893715615, 2.8630605740801744, 3.492236557925204, 3.936433726466988]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.1407177448272705})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6175591945648193})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5247544050216675})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5240802764892578})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5072660446166992})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4877152144908905})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4873216450214386})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5445493459701538})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5404108762741089})
store['active_learning_steps'][34]['training']['best_epoch']=6
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9384, 'crossentropy': 0.4901947265625}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 49223], ['id', 7949], ['id', 43212], ['id', 49525], ['id', 42472]], 'labels': [9, -1, 5, 8, 2], 'scores': [1.076619568346084, 2.0387579001068663, 2.8835402196196824, 3.5309716848381667, 3.9642256820847166]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.0990521907806396})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6473087668418884})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5511616468429565})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.568069577217102})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5361975431442261})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.566913366317749})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6015328764915466})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6526724696159363})
store['active_learning_steps'][35]['training']['best_epoch']=5
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9332, 'crossentropy': 0.49738740234375}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 18598], ['id', 30884], ['id', 29132], ['id', 2801], ['id', 46356]], 'labels': [9, 2, 8, 4, 7], 'scores': [1.0143789490538946, 1.9550156155309981, 2.76723552321082, 3.393060041982073, 3.840411061083489]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.3913326263427734})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7133779525756836})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5520138740539551})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5906722545623779})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5076619386672974})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5517171621322632})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5331305265426636})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5152246952056885})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5892986059188843})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5642533898353577})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.48118856549263})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.49068915843963623})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.559140145778656})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5369396209716797})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5388440489768982})
store['active_learning_steps'][36]['training']['best_epoch']=12
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9485, 'crossentropy': 0.48057802734375}
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 7949], ['id', 22932], ['id', 39208], ['id', 41307], ['id', 109]], 'labels': [-1, 0, 5, 4, 2], 'scores': [1.3091870950423563, 2.4187924143709796, 3.2878388783460384, 3.881791147813817, 4.231910073312859]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.246091365814209})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6801453828811646})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5690194368362427})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5235081911087036})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4814046025276184})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.47194766998291016})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.48902904987335205})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5035051703453064})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4550008177757263})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5019083023071289})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5413427352905273})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5006889700889587})
store['active_learning_steps'][37]['training']['best_epoch']=9
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9412, 'crossentropy': 0.493417919921875}
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 43950], ['id', 59720], ['id', 16756], ['id', 39561], ['id', 37161]], 'labels': [9, 2, 7, 2, 3], 'scores': [1.1035805370141962, 2.109839944306696, 2.9848560463070237, 3.625392734882686, 4.047201684280385]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.2804248332977295})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6426324844360352})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5197849273681641})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5368396043777466})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.619092583656311})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5334649085998535})
store['active_learning_steps'][38]['training']['best_epoch']=3
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9318, 'crossentropy': 0.493305517578125}
