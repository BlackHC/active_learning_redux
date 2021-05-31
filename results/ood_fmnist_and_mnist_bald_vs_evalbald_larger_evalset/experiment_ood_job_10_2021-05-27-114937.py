store = {}
store['timestamp']=1622112577
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=10']
store['commit']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['github_url']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
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
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.505469799041748})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.7020537853240967})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.962874412536621})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 3.1163411140441895})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 3.166698932647705})
store['active_learning_steps'][0]['training']['best_epoch']=3
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.7011, 'crossentropy': 2.4685431640625}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 12377], ['id', 30064], ['id', 50321], ['id', 59698], ['id', 1324]], 'labels': [3, 2, 5, 2, 5], 'scores': [1.2697090082271862, 2.308108722718882, 3.1505083435565595, 3.744573258135979, 4.107548006609116]}
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
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 3.6914594173431396})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 3.221839427947998})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.6492981910705566})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 3.2489662170410156})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 3.5091323852539062})
store['active_learning_steps'][1]['training']['best_epoch']=13
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6969, 'crossentropy': 2.817673828125}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 25415], ['id', 54556], ['id', 56792], ['id', 48469], ['id', 7843]], 'labels': [8, 2, 9, 5, 4], 'scores': [1.278519820071798, 2.4150427872637095, 3.306612286971413, 3.838233630832944, 4.183486689926562]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.111049175262451})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.375235080718994})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.599043369293213})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.6186530590057373})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 3.159769058227539})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.99937105178833})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 3.1163368225097656})
store['active_learning_steps'][2]['training']['best_epoch']=4
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7038, 'crossentropy': 2.2823384765625}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 30079], ['id', 34226], ['id', 50320], ['id', 16155], ['id', 39198]], 'labels': [4, 2, 5, 4, 2], 'scores': [1.3481344886640574, 2.3888820603318672, 3.230372411911053, 3.785629381302585, 4.139881111400009]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.2161014080047607})
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
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 57570], ['id', 45256], ['id', 43833], ['id', 42707], ['id', 10038]], 'labels': [7, 5, 3, 3, 9], 'scores': [1.236986381174251, 2.331425137205443, 3.207789977165664, 3.803183257738697, 4.16493100350908]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.6619956493377686})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 2.0062897205352783})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.3415420055389404})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.4043827056884766})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.9424240589141846})
store['active_learning_steps'][4]['training']['best_epoch']=2
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7421, 'crossentropy': 1.6660744140625}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 49438], ['id', 18984], ['id', 5545], ['id', 20388], ['id', 22483]], 'labels': [8, 9, 2, 0, 8], 'scores': [1.079405696121616, 2.0462659045304443, 2.864406701934678, 3.5030193778260275, 3.912431372539281]}
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
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 34332], ['id', 969], ['id', 8847], ['id', 42570], ['id', 38908]], 'labels': [9, 7, 9, 6, 7], 'scores': [1.1394585076697323, 2.182940559919568, 3.002910978457881, 3.5972966616358075, 3.9859722238651827]}
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
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.6198184490203857})
store['active_learning_steps'][6]['training']['best_epoch']=5
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.788, 'crossentropy': 1.60755322265625}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 55698], ['id', 17658], ['id', 12497], ['id', 3719], ['id', 33221]], 'labels': [3, 8, 0, 2, 5], 'scores': [1.1409357005675589, 2.1707614613120754, 3.028322601522885, 3.668638541592472, 4.07721549395515]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.2315337657928467})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.4786375761032104})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.641937494277954})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.6885560750961304})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.82456636428833})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.9720964431762695})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 2.172922134399414})
store['active_learning_steps'][7]['training']['best_epoch']=4
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8148, 'crossentropy': 1.41699111328125}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 19423], ['id', 15893], ['id', 18739], ['id', 7851], ['id', 19505]], 'labels': [2, 5, 3, 8, 2], 'scores': [1.1484331330623105, 2.146836955156699, 2.98077104473147, 3.6163192038878824, 4.052009872374313]}
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
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 17756], ['id', 21307], ['id', 49767], ['id', 8958], ['id', 14773]], 'labels': [8, 4, 9, 3, 0], 'scores': [1.1405788808304196, 2.1438441879150023, 2.988570418126609, 3.6343133835350088, 4.045589378125194]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.2298204898834229})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.552415370941162})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.651850700378418})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.6922308206558228})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.9133256673812866})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 2.0442569255828857})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.91853928565979})
store['active_learning_steps'][9]['training']['best_epoch']=4
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8096, 'crossentropy': 1.4751943359375}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 18171], ['id', 18190], ['id', 19942], ['id', 7621], ['id', 22144]], 'labels': [0, 4, 5, 7, 0], 'scores': [1.2661733439238771, 2.3810852301557093, 3.21422371552074, 3.7913016693008164, 4.137779956335957]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.052359938621521})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.182596206665039})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.3764543533325195})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.3835619688034058})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.503221035003662})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8433, 'crossentropy': 0.9925185546875}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 41602], ['id', 17494], ['id', 34594], ['id', 50058], ['id', 56213]], 'labels': [5, 5, 8, 6, 2], 'scores': [1.1186846432412356, 2.098983006644794, 2.9029767655495373, 3.468375243667813, 3.8753808793958653]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.24973726272583})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.0622495412826538})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.2922554016113281})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.4211187362670898})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.341357707977295})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8436, 'crossentropy': 0.891037109375}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 26434], ['id', 16379], ['id', 32126], ['id', 13370], ['id', 16860]], 'labels': [2, 7, 4, 2, 8], 'scores': [0.961361769981979, 1.8074425426532628, 2.55439457213366, 3.1598277760971483, 3.610721434018373]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.0258567333221436})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.0486946105957031})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.0564371347427368})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.2866714000701904})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.2018224000930786})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.1876684427261353})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.2832248210906982})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.4056445360183716})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.3992465734481812})
store['active_learning_steps'][12]['training']['best_epoch']=6
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8679, 'crossentropy': 1.02916884765625}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 41572], ['id', 31301], ['id', 47936], ['id', 2856], ['ood', 47626]], 'labels': [6, 5, 8, 4, -1], 'scores': [1.1969126251121267, 2.2557719092108384, 3.0837729813921886, 3.6761482356064317, 4.071722170662072]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.9509382247924805})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.9598588943481445})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.135120153427124})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.1210572719573975})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.2144758701324463})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.3655478954315186})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.428375244140625})
store['active_learning_steps'][13]['training']['best_epoch']=4
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8547, 'crossentropy': 0.96314521484375}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 51298], ['id', 33505], ['id', 16692], ['id', 40766], ['id', 40595]], 'labels': [5, 2, 5, 4, 8], 'scores': [1.0613429463911892, 1.9755265545187481, 2.779549001721578, 3.404344879611026, 3.8459119917562363]}
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
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 5684], ['id', 7924], ['id', 17409], ['id', 35326], ['id', 59468]], 'labels': [6, 8, 3, 5, 7], 'scores': [0.9146410559791387, 1.7638163611434363, 2.4686187277775256, 3.071478127474915, 3.5094510716288028]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.0676863193511963})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.9181071519851685})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.0735198259353638})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.1347726583480835})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.0549578666687012})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.1274986267089844})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.1545073986053467})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.1858317852020264})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.280864953994751})
store['active_learning_steps'][15]['training']['best_epoch']=6
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8804, 'crossentropy': 0.914066796875}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 49487], ['id', 5315], ['id', 32747], ['id', 52099], ['id', 57728]], 'labels': [8, 3, 8, 2, 9], 'scores': [1.1726406168168861, 2.1846698398862223, 3.029799096624866, 3.645458634070506, 4.049155440394712]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.1189320087432861})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8397336602210999})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.0181357860565186})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.0682376623153687})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.1255230903625488})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8734, 'crossentropy': 0.75044482421875}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 33812], ['id', 8691], ['id', 4820], ['id', 41453], ['id', 2761]], 'labels': [6, 2, 5, 3, 8], 'scores': [0.920696759744327, 1.7461675211988625, 2.459527074822102, 3.049631417134008, 3.4800573220933586]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.141724705696106})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7573127746582031})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9284588098526001})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.05839204788208})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9714944362640381})
store['active_learning_steps'][17]['training']['best_epoch']=2
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8877, 'crossentropy': 0.6904400390625}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 42020], ['id', 48006], ['id', 52358], ['id', 49354], ['id', 51508]], 'labels': [9, 6, 2, 0, 6], 'scores': [0.9173325043618661, 1.7066155046726594, 2.417904854781254, 2.9896870091976746, 3.431770437289008]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.0667624473571777})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7287954092025757})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8272144794464111})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8468567132949829})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9032686948776245})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.9393267035484314})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.9159229397773743})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.118037223815918})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9749438166618347})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.071320652961731})
store['active_learning_steps'][18]['training']['best_epoch']=7
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8934, 'crossentropy': 0.86814697265625}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 42703], ['id', 30952], ['id', 2636], ['id', 9180], ['id', 34829]], 'labels': [0, 7, 8, 3, 5], 'scores': [1.1766893099528963, 2.2602464237083764, 3.158102851783931, 3.8050742487247033, 4.162421250066522]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.1993095874786377})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8475949764251709})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.798859179019928})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8662919998168945})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9553009271621704})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 1.0066101551055908})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9275433421134949})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.0172779560089111})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.20369291305542})
store['active_learning_steps'][19]['training']['best_epoch']=6
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8901, 'crossentropy': 0.866748828125}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 20746], ['id', 26184], ['id', 28838], ['id', 48360], ['id', 32880]], 'labels': [1, 0, 9, 3, 0], 'scores': [1.1031333164669237, 2.127583113069518, 2.9824909970649998, 3.6184520560631777, 4.025221929080904]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.0125927925109863})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6930178999900818})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7239674925804138})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7800000905990601})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8215339779853821})
store['active_learning_steps'][20]['training']['best_epoch']=2
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8974, 'crossentropy': 0.625614208984375}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 9118], ['id', 35449], ['id', 26072], ['id', 1518], ['id', 40390]], 'labels': [9, 0, 1, 9, 0], 'scores': [0.8596472473627226, 1.628688974030748, 2.3357201133878167, 2.8926425204828075, 3.3448469304107267]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.0176407098770142})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7228364944458008})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7491403818130493})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7942192554473877})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8638646006584167})
store['active_learning_steps'][21]['training']['best_epoch']=2
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.894, 'crossentropy': 0.655507958984375}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 5129], ['id', 12913], ['id', 39411], ['id', 7168], ['id', 42793]], 'labels': [2, 3, 2, 8, 4], 'scores': [0.8506052143490144, 1.6469194302827836, 2.359349597199637, 2.958929922804261, 3.424531004106721]}
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
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9512062072753906})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.9284184575080872})
store['active_learning_steps'][22]['training']['best_epoch']=6
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.8994, 'crossentropy': 0.78399580078125}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 50916], ['id', 42265], ['id', 47561], ['id', 58258], ['id', 46247]], 'labels': [4, 7, 6, 7, 3], 'scores': [1.084125278529212, 2.0835849892266163, 2.9598278268334477, 3.6026408495571838, 4.024291679765433]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.1548378467559814})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.657517671585083})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6504837274551392})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6726832389831543})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7276813983917236})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7800558805465698})
store['active_learning_steps'][23]['training']['best_epoch']=3
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9151, 'crossentropy': 0.56605498046875}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 29087], ['id', 59314], ['id', 45446], ['id', 4822], ['id', 43176]], 'labels': [1, 9, 7, 4, 2], 'scores': [0.955855688759389, 1.8393995471812348, 2.5984752699969045, 3.192335391084862, 3.646740732697742]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.1203527450561523})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6326958537101746})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7204827070236206})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6241370439529419})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6758413314819336})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8192344903945923})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.743891716003418})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.922, 'crossentropy': 0.561454052734375}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 4165], ['id', 42078], ['id', 45602], ['id', 42199], ['id', 16628]], 'labels': [2, 4, 5, 3, 9], 'scores': [1.0332679987147189, 1.999996802697038, 2.8054372303394324, 3.432034942322752, 3.882812500048346]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.068240761756897})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.609298825263977})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6229065656661987})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6268023252487183})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6470780968666077})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7174019813537598})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6526278257369995})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7271595001220703})
store['active_learning_steps'][25]['training']['best_epoch']=5
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9225, 'crossentropy': 0.56856513671875}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 39818], ['id', 33057], ['id', 11208], ['id', 18487], ['id', 51180]], 'labels': [1, 7, 9, 4, 7], 'scores': [1.0576656114394465, 1.9990291454290272, 2.8429034125372583, 3.487628053495393, 3.9206146907357606]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.0183213949203491})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6284612417221069})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5649346709251404})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6101504564285278})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5828105211257935})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7619104385375977})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6615894436836243})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7275383472442627})
store['active_learning_steps'][26]['training']['best_epoch']=5
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9236, 'crossentropy': 0.5310796875}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 17055], ['id', 41933], ['id', 8762], ['id', 23463], ['id', 32776]], 'labels': [8, 5, 3, 9, 4], 'scores': [1.0084108473931732, 1.9346961517182897, 2.735912023417985, 3.389003197122822, 3.8377658576838023]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.1604459285736084})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6673545837402344})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5582641363143921})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6025567054748535})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.558821976184845})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.698843240737915})
store['active_learning_steps'][27]['training']['best_epoch']=3
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9194, 'crossentropy': 0.557889453125}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 52169], ['id', 51464], ['id', 44255], ['id', 22193], ['id', 56391]], 'labels': [2, 0, 6, 5, 3], 'scores': [0.98598530002819, 1.8262413916865823, 2.5836070749747613, 3.2016245589976666, 3.646944614618185]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.0898056030273438})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6000672578811646})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6278122663497925})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5828208327293396})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7761299014091492})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6686629056930542})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6203192472457886})
store['active_learning_steps'][28]['training']['best_epoch']=4
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9331, 'crossentropy': 0.51475439453125}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 1541], ['id', 55372], ['id', 52462], ['id', 34314], ['id', 27085]], 'labels': [4, 6, 9, 7, 8], 'scores': [0.9652649713059922, 1.8350563586578623, 2.634523221834516, 3.2590568432896703, 3.729192302567486]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.2772283554077148})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7088896036148071})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5728647112846375})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5778456926345825})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.567211389541626})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6132088899612427})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5923655033111572})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5716910362243652})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5690072774887085})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6938881278038025})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.6060749888420105})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5509070158004761})
store['active_learning_steps'][29]['training']['best_epoch']=9
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.934, 'crossentropy': 0.516276220703125}
store['active_learning_steps'][29]['acquisition']={'indices': [['ood', 55778], ['id', 13524], ['ood', 35269], ['id', 8765], ['id', 52140]], 'labels': [-1, 3, -1, 3, 4], 'scores': [1.05202810065011, 2.050616717637888, 2.889621001078968, 3.5417726699696113, 3.9736816453863275]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.1970645189285278})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6344934105873108})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5682839751243591})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5179268717765808})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5349500179290771})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5456569194793701})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5863367915153503})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5563212037086487})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5905464887619019})
store['active_learning_steps'][30]['training']['best_epoch']=6
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9339, 'crossentropy': 0.50039306640625}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 37469], ['id', 9340], ['ood', 53990], ['id', 14305], ['ood', 43200]], 'labels': [2, 5, -1, 8, -1], 'scores': [1.0482443276826234, 1.9845908631446063, 2.782857748544467, 3.423651767239983, 3.8679827152526407]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.213702917098999})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6487569808959961})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5309481024742126})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5751670598983765})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5436558127403259})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5270692110061646})
store['active_learning_steps'][31]['training']['best_epoch']=3
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9292, 'crossentropy': 0.522869189453125}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 57342], ['id', 12767], ['id', 32445], ['id', 28745], ['id', 37688]], 'labels': [2, 9, 5, 7, 9], 'scores': [0.8834690797606461, 1.6980207350535164, 2.4144701050930726, 3.008985940880745, 3.4806820688413165]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.2720346450805664})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6073716878890991})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5971626043319702})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5194396376609802})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5317202806472778})
store['active_learning_steps'][32]['training']['best_epoch']=2
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.93, 'crossentropy': 0.56876259765625}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 51492], ['id', 27644], ['id', 11572], ['id', 15948], ['id', 3030]], 'labels': [5, 3, 5, 2, 9], 'scores': [0.7060405695600835, 1.3506045200585404, 1.9339294106802267, 2.4528051468127874, 2.9004694854042308]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.0701136589050293})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6456844806671143})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.494772732257843})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.49231287837028503})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5310470461845398})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5018598437309265})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.565484881401062})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5746980905532837})
store['active_learning_steps'][33]['training']['best_epoch']=5
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9394, 'crossentropy': 0.46367333984375}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 26358], ['id', 50743], ['id', 34328], ['id', 17540], ['id', 21900]], 'labels': [3, 7, 8, 1, 6], 'scores': [1.0763272883421404, 2.0354162846579533, 2.8630605604876864, 3.4922365417397483, 3.9364336984834063]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.1407177448272705})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6175591945648193})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5247544050216675})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.524080216884613})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5072660446166992})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4877152144908905})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4873216152191162})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5445494055747986})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5404108762741089})
store['active_learning_steps'][34]['training']['best_epoch']=6
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9384, 'crossentropy': 0.4901947265625}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 49223], ['ood', 7949], ['id', 43212], ['id', 49525], ['id', 42472]], 'labels': [9, -1, 5, 8, 2], 'scores': [1.0766195691229687, 2.0387579009529353, 2.8835402116355366, 3.5309716622534992, 3.9642256592086564]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.09905207157135})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6473087668418884})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5511616468429565})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.568069577217102})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5361974835395813})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.566913366317749})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6015329360961914})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6526724100112915})
store['active_learning_steps'][35]['training']['best_epoch']=5
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9332, 'crossentropy': 0.49738740234375}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 18598], ['id', 30884], ['id', 29132], ['id', 2801], ['id', 46356]], 'labels': [9, 2, 8, 4, 7], 'scores': [1.0143789503804859, 1.9550156107841854, 2.767235502497644, 3.3930600086449303, 3.840411025385399]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.3913326263427734})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7133779525756836})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5520138740539551})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5906722545623779})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5076619982719421})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.551717221736908})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5331305265426636})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.515224814414978})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5892986059188843})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5642533898353577})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4811885356903076})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.49068915843963623})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.559140145778656})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5369396805763245})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5388440489768982})
store['active_learning_steps'][36]['training']['best_epoch']=12
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9485, 'crossentropy': 0.48057802734375}
store['active_learning_steps'][36]['acquisition']={'indices': [['ood', 7949], ['id', 22932], ['id', 39208], ['id', 41307], ['id', 109]], 'labels': [-1, 0, 5, 4, 2], 'scores': [1.309187094309474, 2.41879241982995, 3.2878388853343647, 3.8817911534202203, 4.231910076568577]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.246091365814209})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6801455020904541})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5690194368362427})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5235081911087036})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4814046025276184})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.47194766998291016})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.48902904987335205})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5035051703453064})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4550008177757263})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5019083023071289})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5413427948951721})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5006890296936035})
store['active_learning_steps'][37]['training']['best_epoch']=9
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9412, 'crossentropy': 0.493417919921875}
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 43950], ['id', 59720], ['id', 16756], ['id', 39561], ['id', 37161]], 'labels': [9, 2, 7, 2, 3], 'scores': [1.1035805357792632, 2.1098399367418663, 2.9848560223523295, 3.625392694628874, 4.04720161467462]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.2804248332977295})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6426324844360352})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5197849273681641})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5368396043777466})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.619092583656311})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5334649682044983})
store['active_learning_steps'][38]['training']['best_epoch']=3
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9318, 'crossentropy': 0.49330546875}
