store = {}
store['timestamp']=1620299231
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=28']
store['commit']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['github_url']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=28
store['worker_id']=28
store['num_workers']=40
store['config']={'seed': 36, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 20, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.Random', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.269864082336426})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.330420732498169})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.940155506134033})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.8919785022735596})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.694, 'crossentropy': 2.022437890625}
store['active_learning_steps'][0]['acquisition']={'indices': [53560, 19059, 30866, 19319, 15813], 'labels': [3, -1, -1, 5, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.802093505859375})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.421037197113037})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 3.1558566093444824})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 3.0730764865875244})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 3.0444817543029785})
store['active_learning_steps'][1]['training']['best_epoch']=2
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7318, 'crossentropy': 2.0314642578125}
store['active_learning_steps'][1]['acquisition']={'indices': [23012, 55273, 4400, 43821, 25163], 'labels': [1, -1, -1, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.546347141265869})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.8788084983825684})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 3.134519577026367})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 3.053677797317505})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.667, 'crossentropy': 2.2826130859375}
store['active_learning_steps'][2]['acquisition']={'indices': [47784, 44518, 667, 6998, 32701], 'labels': [-1, -1, -1, 1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.391860008239746})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.1514267921447754})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.9000444412231445})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 3.106625556945801})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6894, 'crossentropy': 2.0658416015625}
store['active_learning_steps'][3]['acquisition']={'indices': [13372, 9271, 16514, 27466, 59039], 'labels': [-1, -1, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.463735580444336})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.7248082160949707})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.9721875190734863})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 3.1859774589538574})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.6983, 'crossentropy': 2.104609375}
store['active_learning_steps'][4]['acquisition']={'indices': [24742, 51123, 7542, 29505, 44357], 'labels': [7, -1, 1, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.5442323684692383})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.8795833587646484})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.993032455444336})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 3.1829910278320312})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.6723, 'crossentropy': 2.0859931640625}
store['active_learning_steps'][5]['acquisition']={'indices': [47296, 18161, 32010, 58889, 1390], 'labels': [5, -1, -1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.278726816177368})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.723799467086792})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.885805606842041})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.6105103492736816})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.6857, 'crossentropy': 1.9028779296875}
store['active_learning_steps'][6]['acquisition']={'indices': [17026, 38028, 36032, 34373, 45233], 'labels': [3, 6, 3, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.108126640319824})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.6653034687042236})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.5095419883728027})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.996525287628174})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7163, 'crossentropy': 1.704519140625}
store['active_learning_steps'][7]['acquisition']={'indices': [32797, 55651, 56522, 29561, 44065], 'labels': [-1, -1, 0, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.946858286857605})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.5400404930114746})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.5496230125427246})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.7685306072235107})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.7021, 'crossentropy': 1.7459748046875}
store['active_learning_steps'][8]['acquisition']={'indices': [34752, 56425, 52767, 46918, 9412], 'labels': [4, -1, 5, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.0542564392089844})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.554661273956299})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.7947003841400146})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.8426077365875244})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.7358, 'crossentropy': 1.609649609375}
store['active_learning_steps'][9]['acquisition']={'indices': [39928, 55253, 48751, 33517, 11669], 'labels': [-1, -1, 1, 8, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.552384376525879})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 3.2738137245178223})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.931959629058838})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 3.3129048347473145})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.6859, 'crossentropy': 2.074125390625}
store['active_learning_steps'][10]['acquisition']={'indices': [47556, 38152, 11633, 20522, 59946], 'labels': [-1, -1, -1, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.8375675678253174})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 2.056464433670044})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.423696279525757})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 3.3611059188842773})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.7474, 'crossentropy': 1.5237185546875}
store['active_learning_steps'][11]['acquisition']={'indices': [7102, 16521, 27987, 55970, 36767], 'labels': [-1, 9, -1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.0964584350585938})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 3.0521345138549805})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.942732334136963})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.876194477081299})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.7262, 'crossentropy': 1.6280654296875}
store['active_learning_steps'][12]['acquisition']={'indices': [7859, 42037, 57319, 30680, 19784], 'labels': [-1, -1, 2, 6, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.3423776626586914})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 2.3276705741882324})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 2.5470733642578125})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 2.685382843017578})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 3.103501319885254})
store['active_learning_steps'][13]['training']['best_epoch']=2
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.7559, 'crossentropy': 1.9751005859375}
store['active_learning_steps'][13]['acquisition']={'indices': [4341, 43446, 28102, 4459, 8904], 'labels': [2, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.5479323863983154})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.83402681350708})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 2.2947754859924316})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 2.1454215049743652})
store['active_learning_steps'][14]['training']['best_epoch']=1
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.7649, 'crossentropy': 1.3866529296875}
store['active_learning_steps'][14]['acquisition']={'indices': [32700, 6834, 13058, 37548, 37475], 'labels': [7, 1, 5, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.9067211151123047})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 2.168792486190796})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.6545047760009766})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 2.642671823501587})
store['active_learning_steps'][15]['training']['best_epoch']=1
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.7237, 'crossentropy': 1.6901404296875}
store['active_learning_steps'][15]['acquisition']={'indices': [11784, 11023, 34090, 35081, 13471], 'labels': [-1, 4, -1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.869659185409546})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.993659496307373})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 2.0494303703308105})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.4559905529022217})
store['active_learning_steps'][16]['training']['best_epoch']=1
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.7319, 'crossentropy': 1.44139013671875}
store['active_learning_steps'][16]['acquisition']={'indices': [41479, 37148, 34562, 27760, 1790], 'labels': [7, -1, -1, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.784287929534912})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 2.2695224285125732})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 2.296773910522461})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 2.4381349086761475})
store['active_learning_steps'][17]['training']['best_epoch']=1
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.7602, 'crossentropy': 1.446010546875}
store['active_learning_steps'][17]['acquisition']={'indices': [32883, 31859, 57402, 58417, 2169], 'labels': [3, -1, 3, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.659349799156189})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.71575927734375})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 2.059680461883545})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 2.298370838165283})
store['active_learning_steps'][18]['training']['best_epoch']=1
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.7377, 'crossentropy': 1.48985986328125}
store['active_learning_steps'][18]['acquisition']={'indices': [20245, 54079, 38610, 32995, 12409], 'labels': [6, 1, 5, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.6243809461593628})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.9255778789520264})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 2.130624294281006})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 2.303128480911255})
store['active_learning_steps'][19]['training']['best_epoch']=1
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.7545, 'crossentropy': 1.40824453125}
store['active_learning_steps'][19]['acquisition']={'indices': [53150, 34629, 14961, 23298, 14085], 'labels': [8, 3, 7, 3, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.7872419357299805})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.917945384979248})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 2.229898452758789})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 2.3093760013580322})
store['active_learning_steps'][20]['training']['best_epoch']=1
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.7512, 'crossentropy': 1.48369609375}
store['active_learning_steps'][20]['acquisition']={'indices': [20963, 50067, 32815, 8610, 46041], 'labels': [-1, 3, 5, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.707693338394165})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.9578975439071655})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 2.1952383518218994})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 2.260631561279297})
store['active_learning_steps'][21]['training']['best_epoch']=1
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.7607, 'crossentropy': 1.41819306640625}
store['active_learning_steps'][21]['acquisition']={'indices': [6317, 4598, 5168, 54227, 48724], 'labels': [3, 8, 1, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.3147326707839966})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.5240812301635742})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.9422208070755005})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.9172756671905518})
store['active_learning_steps'][22]['training']['best_epoch']=1
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.7872, 'crossentropy': 1.15409150390625}
store['active_learning_steps'][22]['acquisition']={'indices': [11559, 14836, 50772, 20234, 45357], 'labels': [0, 2, -1, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.2094829082489014})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.652103304862976})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.507381796836853})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 2.063633441925049})
store['active_learning_steps'][23]['training']['best_epoch']=1
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.8112, 'crossentropy': 1.0662638671875}
store['active_learning_steps'][23]['acquisition']={'indices': [26245, 19547, 47943, 20804, 14346], 'labels': [2, 0, -1, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.2832785844802856})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.5385956764221191})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.6311562061309814})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.8570979833602905})
store['active_learning_steps'][24]['training']['best_epoch']=1
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.7945, 'crossentropy': 1.1092703125}
store['active_learning_steps'][24]['acquisition']={'indices': [38344, 36682, 14898, 39082, 58724], 'labels': [9, -1, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.287307620048523})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.6954634189605713})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.9715843200683594})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 2.160740613937378})
store['active_learning_steps'][25]['training']['best_epoch']=1
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.8044, 'crossentropy': 1.13533837890625}
store['active_learning_steps'][25]['acquisition']={'indices': [6519, 32885, 51178, 4693, 3231], 'labels': [4, 3, -1, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.2373278141021729})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.5781028270721436})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 2.0795116424560547})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.9185843467712402})
store['active_learning_steps'][26]['training']['best_epoch']=1
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.8283, 'crossentropy': 1.04968369140625}
store['active_learning_steps'][26]['acquisition']={'indices': [22607, 7641, 44286, 11451, 13286], 'labels': [-1, -1, 8, 0, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.1896862983703613})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.4043689966201782})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.5968475341796875})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.670184850692749})
store['active_learning_steps'][27]['training']['best_epoch']=1
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.8215, 'crossentropy': 1.0135072265625}
store['active_learning_steps'][27]['acquisition']={'indices': [37454, 37854, 55949, 20084, 12003], 'labels': [3, -1, 9, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.2562768459320068})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.2071548700332642})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.429703950881958})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.5504342317581177})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.6620498895645142})
store['active_learning_steps'][28]['training']['best_epoch']=2
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.8499, 'crossentropy': 0.99289140625}
store['active_learning_steps'][28]['acquisition']={'indices': [48946, 49858, 24532, 9363, 25826], 'labels': [-1, 4, 3, 3, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.1377673149108887})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.3803653717041016})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.9236154556274414})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.7423665523529053})
store['active_learning_steps'][29]['training']['best_epoch']=1
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.8289, 'crossentropy': 1.00948466796875}
store['active_learning_steps'][29]['acquisition']={'indices': [23782, 25302, 20497, 23801, 40878], 'labels': [-1, -1, 2, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.3082077503204346})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.5260944366455078})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.7017340660095215})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.7931240797042847})
store['active_learning_steps'][30]['training']['best_epoch']=1
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.7819, 'crossentropy': 1.1640849609375}
store['active_learning_steps'][30]['acquisition']={'indices': [9127, 53311, 7002, 43440, 56986], 'labels': [-1, 6, -1, 6, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.2407584190368652})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.5112996101379395})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.5674614906311035})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.6074776649475098})
store['active_learning_steps'][31]['training']['best_epoch']=1
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.8064, 'crossentropy': 1.110870703125}
store['active_learning_steps'][31]['acquisition']={'indices': [30000, 14303, 50370, 39997, 11183], 'labels': [-1, -1, 7, 9, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.135838270187378})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.329517126083374})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.2835609912872314})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.4779257774353027})
store['active_learning_steps'][32]['training']['best_epoch']=1
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.8199, 'crossentropy': 0.97002587890625}
store['active_learning_steps'][32]['acquisition']={'indices': [19134, 13691, 18843, 53753, 42934], 'labels': [-1, -1, 7, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.3009365797042847})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.4313448667526245})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.5048706531524658})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.4684460163116455})
store['active_learning_steps'][33]['training']['best_epoch']=1
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.8162, 'crossentropy': 1.0638884765625}
store['active_learning_steps'][33]['acquisition']={'indices': [14526, 50889, 2713, 57239, 35303], 'labels': [-1, -1, 5, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.0913859605789185})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.1761829853057861})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.430790662765503})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.3550715446472168})
store['active_learning_steps'][34]['training']['best_epoch']=1
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.8337, 'crossentropy': 0.96191513671875}
store['active_learning_steps'][34]['acquisition']={'indices': [50697, 9290, 11605, 15287, 47234], 'labels': [-1, -1, 0, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9981662034988403})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.181065559387207})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.356135368347168})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.4588255882263184})
store['active_learning_steps'][35]['training']['best_epoch']=1
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.8443, 'crossentropy': 0.83460029296875}
store['active_learning_steps'][35]['acquisition']={'indices': [26490, 7211, 14072, 53104, 47160], 'labels': [-1, 4, 6, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.0604054927825928})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.1654893159866333})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.2664680480957031})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.3139402866363525})
store['active_learning_steps'][36]['training']['best_epoch']=1
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.8289, 'crossentropy': 0.92392861328125}
store['active_learning_steps'][36]['acquisition']={'indices': [45723, 29559, 15214, 47487, 31705], 'labels': [-1, -1, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.9944812059402466})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.0971136093139648})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.224254846572876})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.2141422033309937})
store['active_learning_steps'][37]['training']['best_epoch']=1
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.8316, 'crossentropy': 0.92894052734375}
store['active_learning_steps'][37]['acquisition']={'indices': [351, 52970, 50143, 12209, 31109], 'labels': [1, -1, -1, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.0662446022033691})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.2681605815887451})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.4318032264709473})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.4701602458953857})
store['active_learning_steps'][38]['training']['best_epoch']=1
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.8307, 'crossentropy': 0.92781201171875}
store['active_learning_steps'][38]['acquisition']={'indices': [8808, 43427, 19352, 1069, 29838], 'labels': [3, 7, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.1486029624938965})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.2481718063354492})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.3142974376678467})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.5735211372375488})
store['active_learning_steps'][39]['training']['best_epoch']=1
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.8014, 'crossentropy': 1.00859892578125}
store['active_learning_steps'][39]['acquisition']={'indices': [57446, 6476, 41984, 27807, 29320], 'labels': [-1, 7, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.078833818435669})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.1221051216125488})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.0734541416168213})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.415432333946228})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.299553632736206})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.361853837966919})
store['active_learning_steps'][40]['training']['best_epoch']=3
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.8705, 'crossentropy': 0.86660029296875}
store['active_learning_steps'][40]['acquisition']={'indices': [35731, 25705, 11229, 46104, 18125], 'labels': [-1, -1, -1, 4, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.9589325189590454})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.2936060428619385})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.3080462217330933})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.4493892192840576})
store['active_learning_steps'][41]['training']['best_epoch']=1
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.8251, 'crossentropy': 0.90721484375}
store['active_learning_steps'][41]['acquisition']={'indices': [44014, 50334, 31001, 9704, 36626], 'labels': [5, 2, -1, 4, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.1979787349700928})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.2908148765563965})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.2835685014724731})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.3918615579605103})
store['active_learning_steps'][42]['training']['best_epoch']=1
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.8089, 'crossentropy': 1.0626234375}
store['active_learning_steps'][42]['acquisition']={'indices': [28950, 54340, 22702, 43713, 15223], 'labels': [2, 1, -1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.1304025650024414})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.1291027069091797})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.3171749114990234})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.3412598371505737})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.550606608390808})
store['active_learning_steps'][43]['training']['best_epoch']=2
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.8452, 'crossentropy': 0.9730869140625}
store['active_learning_steps'][43]['acquisition']={'indices': [16636, 10015, 44620, 58836, 39545], 'labels': [-1, 5, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.0427320003509521})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.0830539464950562})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.1625967025756836})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.3123666048049927})
store['active_learning_steps'][44]['training']['best_epoch']=1
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.8123, 'crossentropy': 0.9801126953125}
store['active_learning_steps'][44]['acquisition']={'indices': [47195, 57488, 47135, 25554, 53976], 'labels': [3, 3, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.2568423748016357})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.0371065139770508})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.3281331062316895})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.2405354976654053})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.3263763189315796})
store['active_learning_steps'][45]['training']['best_epoch']=2
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.8639, 'crossentropy': 0.9262609375}
store['active_learning_steps'][45]['acquisition']={'indices': [37872, 55635, 12414, 57464, 27995], 'labels': [6, 1, 0, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.239959955215454})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.294373631477356})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.5882680416107178})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.3663594722747803})
store['active_learning_steps'][46]['training']['best_epoch']=1
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.8131, 'crossentropy': 1.02357626953125}
store['active_learning_steps'][46]['acquisition']={'indices': [18021, 25262, 2618, 54053, 28294], 'labels': [-1, 8, 7, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9722316861152649})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.2177352905273438})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.1076750755310059})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.4057466983795166})
store['active_learning_steps'][47]['training']['best_epoch']=1
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.8458, 'crossentropy': 0.82335107421875}
store['active_learning_steps'][47]['acquisition']={'indices': [16928, 46450, 20972, 5847, 40583], 'labels': [0, 8, 4, 5, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.9678394198417664})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.135974407196045})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.1697747707366943})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.2570364475250244})
store['active_learning_steps'][48]['training']['best_epoch']=1
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.8459, 'crossentropy': 0.8275693359375}
store['active_learning_steps'][48]['acquisition']={'indices': [14116, 25444, 46931, 36451, 15477], 'labels': [-1, -1, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.9348948001861572})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.0059142112731934})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.096153736114502})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.1629161834716797})
store['active_learning_steps'][49]['training']['best_epoch']=1
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.8415, 'crossentropy': 0.84763671875}
store['active_learning_steps'][49]['acquisition']={'indices': [24585, 8820, 24668, 53879, 18180], 'labels': [6, -1, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.003836989402771})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.0603992938995361})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.0660977363586426})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.097879409790039})
store['active_learning_steps'][50]['training']['best_epoch']=1
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.8241, 'crossentropy': 0.904087890625}
store['active_learning_steps'][50]['acquisition']={'indices': [53058, 46408, 59382, 3701, 16112], 'labels': [-1, 2, -1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.9407907724380493})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.0598409175872803})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.1379222869873047})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.3139095306396484})
store['active_learning_steps'][51]['training']['best_epoch']=1
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.8374, 'crossentropy': 0.8636021484375}
store['active_learning_steps'][51]['acquisition']={'indices': [18163, 58699, 39780, 46343, 19069], 'labels': [1, -1, 5, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.9790937900543213})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.9974098205566406})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.0123984813690186})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.0636016130447388})
store['active_learning_steps'][52]['training']['best_epoch']=1
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.818, 'crossentropy': 0.91115205078125}
store['active_learning_steps'][52]['acquisition']={'indices': [28048, 49749, 24623, 7692, 53086], 'labels': [-1, -1, -1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.0394953489303589})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.9909673929214478})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.1832890510559082})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.3326566219329834})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.1614255905151367})
store['active_learning_steps'][53]['training']['best_epoch']=2
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.8643, 'crossentropy': 0.848916796875}
store['active_learning_steps'][53]['acquisition']={'indices': [2903, 41206, 14360, 27725, 45471], 'labels': [-1, 4, -1, 9, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.9236915707588196})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.1323999166488647})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.0997278690338135})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.151944875717163})
store['active_learning_steps'][54]['training']['best_epoch']=1
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.8394, 'crossentropy': 0.817513525390625}
store['active_learning_steps'][54]['acquisition']={'indices': [32685, 8214, 21413, 42277, 29724], 'labels': [3, 7, 0, 0, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.7977325916290283})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.90175461769104})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.0886995792388916})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.0049854516983032})
store['active_learning_steps'][55]['training']['best_epoch']=1
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.8554, 'crossentropy': 0.72010537109375}
store['active_learning_steps'][55]['acquisition']={'indices': [20201, 16818, 32835, 13063, 33672], 'labels': [-1, 4, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.8393275141716003})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9318569898605347})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9109320044517517})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.0736011266708374})
store['active_learning_steps'][56]['training']['best_epoch']=1
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.8464, 'crossentropy': 0.78595146484375}
store['active_learning_steps'][56]['acquisition']={'indices': [28592, 10644, 46258, 11940, 44528], 'labels': [9, -1, -1, 8, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.8789817690849304})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.9762648344039917})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9544205665588379})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9616131782531738})
store['active_learning_steps'][57]['training']['best_epoch']=1
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.8502, 'crossentropy': 0.77426142578125}
store['active_learning_steps'][57]['acquisition']={'indices': [17545, 52, 57196, 21933, 43939], 'labels': [8, 7, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8209223747253418})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8142822980880737})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8968756794929504})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9315138459205627})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9713337421417236})
store['active_learning_steps'][58]['training']['best_epoch']=2
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.8784, 'crossentropy': 0.735388720703125}
store['active_learning_steps'][58]['acquisition']={'indices': [48239, 13999, 45920, 8580, 54210], 'labels': [6, 6, 2, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8758996725082397})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.0211634635925293})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 1.0404306650161743})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.942135214805603})
store['active_learning_steps'][59]['training']['best_epoch']=1
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.8568, 'crossentropy': 0.76138310546875}
store['active_learning_steps'][59]['acquisition']={'indices': [44209, 22968, 54011, 15886, 41519], 'labels': [2, -1, 7, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8349545001983643})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7839727401733398})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9426804184913635})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9328128099441528})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.1592259407043457})
store['active_learning_steps'][60]['training']['best_epoch']=2
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.8849, 'crossentropy': 0.667946826171875}
store['active_learning_steps'][60]['acquisition']={'indices': [14704, 54137, 14749, 21876, 54797], 'labels': [-1, 8, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9151530265808105})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.9015619158744812})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.9179483652114868})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.045694351196289})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.1248915195465088})
store['active_learning_steps'][61]['training']['best_epoch']=2
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.8787, 'crossentropy': 0.739871826171875}
store['active_learning_steps'][61]['acquisition']={'indices': [41964, 48148, 26520, 39312, 23565], 'labels': [4, 9, 8, 3, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.7812859416007996})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.756943941116333})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9674479961395264})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8748502731323242})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9161996841430664})
store['active_learning_steps'][62]['training']['best_epoch']=2
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.8901, 'crossentropy': 0.657950146484375}
store['active_learning_steps'][62]['acquisition']={'indices': [25139, 16830, 8680, 55385, 30574], 'labels': [2, 6, -1, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.8903599977493286})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8630521297454834})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9716923236846924})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7946544289588928})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9960905313491821})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.9527463912963867})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.9797791242599487})
store['active_learning_steps'][63]['training']['best_epoch']=4
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.8992, 'crossentropy': 0.749903955078125}
store['active_learning_steps'][63]['acquisition']={'indices': [42602, 20937, 18311, 1495, 10656], 'labels': [1, -1, 8, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.740031361579895})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7968150973320007})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8236945867538452})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9489824771881104})
store['active_learning_steps'][64]['training']['best_epoch']=1
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.8751, 'crossentropy': 0.645771337890625}
store['active_learning_steps'][64]['acquisition']={'indices': [49797, 46072, 27642, 24241, 55250], 'labels': [5, 3, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7774468660354614})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8652269244194031})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8819940090179443})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.915938138961792})
store['active_learning_steps'][65]['training']['best_epoch']=1
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.8691, 'crossentropy': 0.67861103515625}
store['active_learning_steps'][65]['acquisition']={'indices': [54951, 46379, 37742, 3609, 17319], 'labels': [-1, 3, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.8546839356422424})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.849610447883606})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.9333828687667847})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9780566692352295})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.0799927711486816})
store['active_learning_steps'][66]['training']['best_epoch']=2
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.8759, 'crossentropy': 0.754204833984375}
store['active_learning_steps'][66]['acquisition']={'indices': [44450, 17242, 55160, 33577, 35862], 'labels': [-1, 3, 4, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.817320704460144})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7802466154098511})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8766469955444336})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.9383574724197388})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 1.07857346534729})
store['active_learning_steps'][67]['training']['best_epoch']=2
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.8883, 'crossentropy': 0.672064013671875}
store['active_learning_steps'][67]['acquisition']={'indices': [57642, 33091, 30923, 10761, 29578], 'labels': [-1, 1, 0, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7345080971717834})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7784608602523804})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8403669595718384})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.849390983581543})
store['active_learning_steps'][68]['training']['best_epoch']=1
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.8741, 'crossentropy': 0.677285205078125}
store['active_learning_steps'][68]['acquisition']={'indices': [4721, 34060, 59572, 16097, 19332], 'labels': [-1, -1, -1, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7674716711044312})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.753410816192627})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9172927141189575})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8749411106109619})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8278694748878479})
store['active_learning_steps'][69]['training']['best_epoch']=2
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.8907, 'crossentropy': 0.639012060546875}
store['active_learning_steps'][69]['acquisition']={'indices': [46808, 21084, 23802, 20314, 1601], 'labels': [5, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.820993185043335})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7439981698989868})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7775583267211914})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.885033369064331})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8964551687240601})
store['active_learning_steps'][70]['training']['best_epoch']=2
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.8925, 'crossentropy': 0.67809990234375}
store['active_learning_steps'][70]['acquisition']={'indices': [51529, 59892, 5801, 15606, 8453], 'labels': [1, 6, 0, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.8586257696151733})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8810597658157349})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9176760911941528})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.84736168384552})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8591513633728027})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8604950904846191})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 1.072419285774231})
store['active_learning_steps'][71]['training']['best_epoch']=4
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.8934, 'crossentropy': 0.73651904296875}
store['active_learning_steps'][71]['acquisition']={'indices': [48175, 13463, 44994, 26644, 27463], 'labels': [1, 4, 1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8457719087600708})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.840764045715332})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7544081211090088})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9282243251800537})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8145260810852051})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7979632616043091})
store['active_learning_steps'][72]['training']['best_epoch']=3
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.8945, 'crossentropy': 0.6958755859375}
store['active_learning_steps'][72]['acquisition']={'indices': [54529, 56855, 10770, 25575, 32864], 'labels': [7, -1, 5, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.9808506369590759})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7731932401657104})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.9988275766372681})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9175066947937012})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8636350035667419})
store['active_learning_steps'][73]['training']['best_epoch']=2
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.8958, 'crossentropy': 0.67737177734375}
store['active_learning_steps'][73]['acquisition']={'indices': [11726, 5247, 5767, 51059, 14144], 'labels': [-1, -1, 0, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.822128415107727})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.9173803329467773})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8117392659187317})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8675846457481384})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9256513118743896})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 1.0320690870285034})
store['active_learning_steps'][74]['training']['best_epoch']=3
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.8899, 'crossentropy': 0.709776123046875}
store['active_learning_steps'][74]['acquisition']={'indices': [22655, 20039, 32666, 59264, 5555], 'labels': [9, -1, -1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.6974442601203918})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7538319826126099})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.835494875907898})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8093579411506653})
store['active_learning_steps'][75]['training']['best_epoch']=1
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.8756, 'crossentropy': 0.672514404296875}
store['active_learning_steps'][75]['acquisition']={'indices': [48487, 24593, 13446, 52632, 13952], 'labels': [-1, 9, -1, 8, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.8755356073379517})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8305741548538208})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.836310625076294})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8097747564315796})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8572249412536621})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8788462281227112})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.950131356716156})
store['active_learning_steps'][76]['training']['best_epoch']=4
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.8952, 'crossentropy': 0.754638134765625}
store['active_learning_steps'][76]['acquisition']={'indices': [25505, 54678, 41301, 7946, 16988], 'labels': [-1, -1, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7503443956375122})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7085820436477661})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7511191368103027})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8875547647476196})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8685351610183716})
store['active_learning_steps'][77]['training']['best_epoch']=2
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.897, 'crossentropy': 0.605237939453125}
store['active_learning_steps'][77]['acquisition']={'indices': [21092, 39120, 33804, 7191, 46243], 'labels': [-1, 5, 2, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.8985213041305542})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.800927460193634})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9391016960144043})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9912536144256592})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7903151512145996})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.879767894744873})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.9562238454818726})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 1.0356394052505493})
store['active_learning_steps'][78]['training']['best_epoch']=5
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9067, 'crossentropy': 0.687291015625}
store['active_learning_steps'][78]['acquisition']={'indices': [5506, 44452, 40742, 58518, 22806], 'labels': [5, 6, 7, 8, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.795478880405426})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6850818395614624})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7887534499168396})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7744699120521545})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8267604112625122})
store['active_learning_steps'][79]['training']['best_epoch']=2
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.8971, 'crossentropy': 0.58928369140625}
store['active_learning_steps'][79]['acquisition']={'indices': [38328, 44855, 19296, 59373, 43052], 'labels': [-1, 9, -1, 1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7626688480377197})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7573059797286987})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7835417985916138})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7860677242279053})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7687538266181946})
store['active_learning_steps'][80]['training']['best_epoch']=2
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.8886, 'crossentropy': 0.671586376953125}
store['active_learning_steps'][80]['acquisition']={'indices': [13738, 42801, 48860, 10175, 15656], 'labels': [0, -1, 1, 4, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7983353734016418})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7219893336296082})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.713089644908905})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8166849613189697})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8031626343727112})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7815619707107544})
store['active_learning_steps'][81]['training']['best_epoch']=3
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.903, 'crossentropy': 0.598995068359375}
store['active_learning_steps'][81]['acquisition']={'indices': [32345, 22547, 54110, 5468, 58858], 'labels': [-1, 4, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7968149185180664})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8611007928848267})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8548933267593384})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8267751932144165})
store['active_learning_steps'][82]['training']['best_epoch']=1
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.8787, 'crossentropy': 0.668834423828125}
store['active_learning_steps'][82]['acquisition']={'indices': [21510, 18288, 24497, 5037, 54965], 'labels': [-1, 8, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.7760966420173645})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7772300839424133})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7756353616714478})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.725061297416687})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7918083071708679})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 1.0182685852050781})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8405963182449341})
store['active_learning_steps'][83]['training']['best_epoch']=4
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9119, 'crossentropy': 0.607554931640625}
store['active_learning_steps'][83]['acquisition']={'indices': [51326, 32152, 47753, 3418, 36701], 'labels': [-1, -1, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.8458776473999023})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7262107133865356})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8061524629592896})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7564041614532471})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9834911823272705})
store['active_learning_steps'][84]['training']['best_epoch']=2
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.8956, 'crossentropy': 0.6153341796875}
store['active_learning_steps'][84]['acquisition']={'indices': [21108, 47960, 55701, 7209, 7199], 'labels': [-1, -1, 9, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8028473258018494})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6932275295257568})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.776284396648407})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.688917875289917})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8492157459259033})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7606987953186035})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.9111586809158325})
store['active_learning_steps'][85]['training']['best_epoch']=4
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9152, 'crossentropy': 0.601903564453125}
store['active_learning_steps'][85]['acquisition']={'indices': [57223, 21037, 11352, 46732, 26746], 'labels': [-1, 4, 1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7908203601837158})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6918222308158875})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7095382213592529})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7963616847991943})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8267680406570435})
store['active_learning_steps'][86]['training']['best_epoch']=2
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.9033, 'crossentropy': 0.569188427734375}
store['active_learning_steps'][86]['acquisition']={'indices': [26341, 34621, 47974, 1962, 11927], 'labels': [2, 6, 9, 9, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][87]['training']={}
store['active_learning_steps'][87]['training']['epochs']=[]
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.776655375957489})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6810166835784912})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8059672117233276})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7706960439682007})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7547228336334229})
store['active_learning_steps'][87]['training']['best_epoch']=2
store['active_learning_steps'][87]['evaluation_metrics']={'accuracy': 0.9018, 'crossentropy': 0.57429580078125}
store['active_learning_steps'][87]['acquisition']={'indices': [30081, 30710, 36535, 26218, 9781], 'labels': [-1, -1, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][88]['training']={}
store['active_learning_steps'][88]['training']['epochs']=[]
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.7834339141845703})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7838953137397766})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7308517694473267})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8582639694213867})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8541326522827148})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7094192504882812})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.8037809133529663})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8742191791534424})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.8085547685623169})
store['active_learning_steps'][88]['training']['best_epoch']=6
store['active_learning_steps'][88]['evaluation_metrics']={'accuracy': 0.917, 'crossentropy': 0.609646044921875}
store['active_learning_steps'][88]['acquisition']={'indices': [26282, 18391, 50409, 1839, 16795], 'labels': [9, 7, 5, 1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][89]['training']={}
store['active_learning_steps'][89]['training']['epochs']=[]
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8206442594528198})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7287123799324036})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7602495551109314})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9031782150268555})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7601615190505981})
store['active_learning_steps'][89]['training']['best_epoch']=2
store['active_learning_steps'][89]['evaluation_metrics']={'accuracy': 0.901, 'crossentropy': 0.591460498046875}
store['active_learning_steps'][89]['acquisition']={'indices': [19958, 51381, 48476, 29082, 13932], 'labels': [-1, -1, 2, 8, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][90]['training']={}
store['active_learning_steps'][90]['training']['epochs']=[]
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7001153826713562})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.654710054397583})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6986510753631592})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6975467205047607})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6921185255050659})
store['active_learning_steps'][90]['training']['best_epoch']=2
store['active_learning_steps'][90]['evaluation_metrics']={'accuracy': 0.9039, 'crossentropy': 0.57014677734375}
store['active_learning_steps'][90]['acquisition']={'indices': [3307, 11522, 41354, 58803, 11231], 'labels': [2, 1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][91]['training']={}
store['active_learning_steps'][91]['training']['epochs']=[]
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.7941620349884033})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6766694188117981})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6769393086433411})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7684847116470337})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8481457233428955})
store['active_learning_steps'][91]['training']['best_epoch']=2
store['active_learning_steps'][91]['evaluation_metrics']={'accuracy': 0.91, 'crossentropy': 0.546114111328125}
store['active_learning_steps'][91]['acquisition']={'indices': [35948, 7822, 52518, 6117, 15656], 'labels': [-1, 9, 6, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][92]['training']={}
store['active_learning_steps'][92]['training']['epochs']=[]
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7450029850006104})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7652526497840881})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7103630304336548})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7490420937538147})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7954225540161133})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8759670257568359})
store['active_learning_steps'][92]['training']['best_epoch']=3
store['active_learning_steps'][92]['evaluation_metrics']={'accuracy': 0.9037, 'crossentropy': 0.61825}
store['active_learning_steps'][92]['acquisition']={'indices': [14758, 51336, 16353, 45988, 31088], 'labels': [1, 0, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][93]['training']={}
store['active_learning_steps'][93]['training']['epochs']=[]
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.7884000539779663})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6812798976898193})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7684431076049805})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7067950963973999})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7308424115180969})
store['active_learning_steps'][93]['training']['best_epoch']=2
store['active_learning_steps'][93]['evaluation_metrics']={'accuracy': 0.9056, 'crossentropy': 0.58619189453125}
store['active_learning_steps'][93]['acquisition']={'indices': [55350, 49020, 18661, 42744, 35360], 'labels': [-1, -1, 2, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][94]['training']={}
store['active_learning_steps'][94]['training']['epochs']=[]
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.712372362613678})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.697163462638855})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6881241798400879})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7110798358917236})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6724134087562561})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.7223050594329834})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7894638776779175})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.8633166551589966})
store['active_learning_steps'][94]['training']['best_epoch']=5
store['active_learning_steps'][94]['evaluation_metrics']={'accuracy': 0.9158, 'crossentropy': 0.58465244140625}
store['active_learning_steps'][94]['acquisition']={'indices': [11248, 55297, 16440, 12035, 36144], 'labels': [-1, 0, -1, 3, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][95]['training']={}
store['active_learning_steps'][95]['training']['epochs']=[]
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7549688220024109})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6929082870483398})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7358019351959229})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8133975267410278})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7474262118339539})
store['active_learning_steps'][95]['training']['best_epoch']=2
store['active_learning_steps'][95]['evaluation_metrics']={'accuracy': 0.9037, 'crossentropy': 0.59942841796875}
store['active_learning_steps'][95]['acquisition']={'indices': [39730, 36079, 50119, 2609, 15638], 'labels': [4, -1, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][96]['training']={}
store['active_learning_steps'][96]['training']['epochs']=[]
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7779029011726379})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7049442529678345})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7177713513374329})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6932696104049683})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7937576770782471})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.9926635026931763})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8582165241241455})
store['active_learning_steps'][96]['training']['best_epoch']=4
store['active_learning_steps'][96]['evaluation_metrics']={'accuracy': 0.9146, 'crossentropy': 0.589376953125}
store['active_learning_steps'][96]['acquisition']={'indices': [54756, 9741, 7515, 48230, 43784], 'labels': [2, 4, 0, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][97]['training']={}
store['active_learning_steps'][97]['training']['epochs']=[]
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7329296469688416})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6394683718681335})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6563878655433655})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7662725448608398})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7741005420684814})
store['active_learning_steps'][97]['training']['best_epoch']=2
store['active_learning_steps'][97]['evaluation_metrics']={'accuracy': 0.9085, 'crossentropy': 0.544733740234375}
store['active_learning_steps'][97]['acquisition']={'indices': [3143, 14598, 36353, 11828, 19382], 'labels': [0, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][98]['training']={}
store['active_learning_steps'][98]['training']['epochs']=[]
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8068009614944458})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7232131958007812})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7742807865142822})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8108161687850952})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7772371768951416})
store['active_learning_steps'][98]['training']['best_epoch']=2
store['active_learning_steps'][98]['evaluation_metrics']={'accuracy': 0.9032, 'crossentropy': 0.602372607421875}
store['active_learning_steps'][98]['acquisition']={'indices': [14630, 8695, 32653, 9118, 1658], 'labels': [-1, 4, 3, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][99]['training']={}
store['active_learning_steps'][99]['training']['epochs']=[]
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7574065327644348})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7463461756706238})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7147753238677979})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7364450693130493})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7360489368438721})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.8075389862060547})
store['active_learning_steps'][99]['training']['best_epoch']=3
store['active_learning_steps'][99]['evaluation_metrics']={'accuracy': 0.9045, 'crossentropy': 0.61422177734375}
store['active_learning_steps'][99]['acquisition']={'indices': [35174, 50655, 23577, 35415, 53459], 'labels': [-1, -1, 6, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][100]['training']={}
store['active_learning_steps'][100]['training']['epochs']=[]
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.7845057249069214})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6528278589248657})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7282992601394653})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7313331365585327})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7683273553848267})
store['active_learning_steps'][100]['training']['best_epoch']=2
store['active_learning_steps'][100]['evaluation_metrics']={'accuracy': 0.9083, 'crossentropy': 0.5538736328125}
store['active_learning_steps'][100]['acquisition']={'indices': [23441, 24192, 20332, 35067, 57346], 'labels': [-1, -1, 1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][101]['training']={}
store['active_learning_steps'][101]['training']['epochs']=[]
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.7762744426727295})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7112055420875549})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7349506616592407})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7462978959083557})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7733678221702576})
store['active_learning_steps'][101]['training']['best_epoch']=2
store['active_learning_steps'][101]['evaluation_metrics']={'accuracy': 0.894, 'crossentropy': 0.604287353515625}
store['active_learning_steps'][101]['acquisition']={'indices': [47513, 44181, 22433, 28809, 50739], 'labels': [0, -1, 9, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][102]['training']={}
store['active_learning_steps'][102]['training']['epochs']=[]
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7084512710571289})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.635931670665741})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6238078474998474})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6572443246841431})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.659591794013977})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7530187964439392})
store['active_learning_steps'][102]['training']['best_epoch']=3
store['active_learning_steps'][102]['evaluation_metrics']={'accuracy': 0.9176, 'crossentropy': 0.5288392578125}
store['active_learning_steps'][102]['acquisition']={'indices': [40423, 59178, 22144, 3661, 42487], 'labels': [-1, 3, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][103]['training']={}
store['active_learning_steps'][103]['training']['epochs']=[]
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7844972610473633})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7029801607131958})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6753620505332947})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7257936596870422})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8552185893058777})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8130753040313721})
store['active_learning_steps'][103]['training']['best_epoch']=3
store['active_learning_steps'][103]['evaluation_metrics']={'accuracy': 0.9078, 'crossentropy': 0.581693701171875}
store['active_learning_steps'][103]['acquisition']={'indices': [8862, 54272, 16510, 25517, 10276], 'labels': [-1, -1, -1, 2, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][104]['training']={}
store['active_learning_steps'][104]['training']['epochs']=[]
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.763106107711792})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6993411779403687})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7395970225334167})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6850483417510986})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7029362916946411})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6925001740455627})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.8521934151649475})
store['active_learning_steps'][104]['training']['best_epoch']=4
store['active_learning_steps'][104]['evaluation_metrics']={'accuracy': 0.9167, 'crossentropy': 0.587652099609375}
store['active_learning_steps'][104]['acquisition']={'indices': [41156, 15956, 22700, 2294, 5428], 'labels': [-1, 8, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][105]['training']={}
store['active_learning_steps'][105]['training']['epochs']=[]
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.7752794027328491})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6382055878639221})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7785346508026123})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.757516622543335})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6740008592605591})
store['active_learning_steps'][105]['training']['best_epoch']=2
store['active_learning_steps'][105]['evaluation_metrics']={'accuracy': 0.9009, 'crossentropy': 0.578099951171875}
store['active_learning_steps'][105]['acquisition']={'indices': [12129, 43491, 216, 33299, 12458], 'labels': [-1, 7, -1, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][106]['training']={}
store['active_learning_steps'][106]['training']['epochs']=[]
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7023745775222778})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6874411106109619})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7514194250106812})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6287250518798828})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7654867768287659})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7867931127548218})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7551863193511963})
store['active_learning_steps'][106]['training']['best_epoch']=4
store['active_learning_steps'][106]['evaluation_metrics']={'accuracy': 0.9152, 'crossentropy': 0.576125634765625}
store['active_learning_steps'][106]['acquisition']={'indices': [26561, 11696, 34907, 56667, 53070], 'labels': [3, 5, -1, 8, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][107]['training']={}
store['active_learning_steps'][107]['training']['epochs']=[]
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7540266513824463})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6708284616470337})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6535834670066833})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6738424301147461})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.8349988460540771})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7435469627380371})
store['active_learning_steps'][107]['training']['best_epoch']=3
store['active_learning_steps'][107]['evaluation_metrics']={'accuracy': 0.9114, 'crossentropy': 0.5734490234375}
store['active_learning_steps'][107]['acquisition']={'indices': [38314, 16532, 52683, 30736, 26625], 'labels': [-1, 2, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][108]['training']={}
store['active_learning_steps'][108]['training']['epochs']=[]
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7145471572875977})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6286221742630005})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6781869530677795})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7244226932525635})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.802571177482605})
store['active_learning_steps'][108]['training']['best_epoch']=2
store['active_learning_steps'][108]['evaluation_metrics']={'accuracy': 0.9081, 'crossentropy': 0.54643583984375}
store['active_learning_steps'][108]['acquisition']={'indices': [56535, 25786, 32901, 59100, 41501], 'labels': [-1, 1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][109]['training']={}
store['active_learning_steps'][109]['training']['epochs']=[]
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7293051481246948})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.627138078212738})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6585789918899536})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7004725933074951})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7741753458976746})
store['active_learning_steps'][109]['training']['best_epoch']=2
store['active_learning_steps'][109]['evaluation_metrics']={'accuracy': 0.9077, 'crossentropy': 0.5499435546875}
store['active_learning_steps'][109]['acquisition']={'indices': [41016, 51808, 28024, 58931, 40186], 'labels': [-1, 2, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][110]['training']={}
store['active_learning_steps'][110]['training']['epochs']=[]
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7594943046569824})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6613930463790894})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.731724739074707})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.700152575969696})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7637799978256226})
store['active_learning_steps'][110]['training']['best_epoch']=2
store['active_learning_steps'][110]['evaluation_metrics']={'accuracy': 0.9076, 'crossentropy': 0.574677001953125}
store['active_learning_steps'][110]['acquisition']={'indices': [45994, 35013, 6298, 40153, 59485], 'labels': [1, 9, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][111]['training']={}
store['active_learning_steps'][111]['training']['epochs']=[]
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6915274262428284})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.697932779788971})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.687519907951355})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.641960859298706})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7054744958877563})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.724195122718811})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.8435750007629395})
store['active_learning_steps'][111]['training']['best_epoch']=4
store['active_learning_steps'][111]['evaluation_metrics']={'accuracy': 0.9152, 'crossentropy': 0.577348046875}
store['active_learning_steps'][111]['acquisition']={'indices': [56018, 34762, 21599, 5290, 1094], 'labels': [9, -1, 6, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][112]['training']={}
store['active_learning_steps'][112]['training']['epochs']=[]
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7249374389648438})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6284866333007812})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6795334815979004})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6636909246444702})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.725456714630127})
store['active_learning_steps'][112]['training']['best_epoch']=2
store['active_learning_steps'][112]['evaluation_metrics']={'accuracy': 0.9059, 'crossentropy': 0.567628662109375}
store['active_learning_steps'][112]['acquisition']={'indices': [8655, 35041, 8324, 8871, 40414], 'labels': [-1, -1, 8, 6, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][113]['training']={}
store['active_learning_steps'][113]['training']['epochs']=[]
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8056677579879761})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6771236658096313})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6970106959342957})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.68440842628479})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7538358569145203})
store['active_learning_steps'][113]['training']['best_epoch']=2
store['active_learning_steps'][113]['evaluation_metrics']={'accuracy': 0.9015, 'crossentropy': 0.58816162109375}
store['active_learning_steps'][113]['acquisition']={'indices': [38131, 2136, 23103, 11486, 39867], 'labels': [-1, -1, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][114]['training']={}
store['active_learning_steps'][114]['training']['epochs']=[]
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7924713492393494})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6570447683334351})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6644977331161499})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6412578821182251})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6619269847869873})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6198263168334961})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7603293061256409})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7409272193908691})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.7483245134353638})
store['active_learning_steps'][114]['training']['best_epoch']=6
store['active_learning_steps'][114]['evaluation_metrics']={'accuracy': 0.9221, 'crossentropy': 0.565444970703125}
store['active_learning_steps'][114]['acquisition']={'indices': [44481, 44539, 18105, 18763, 9477], 'labels': [-1, 7, -1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][115]['training']={}
store['active_learning_steps'][115]['training']['epochs']=[]
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8085922002792358})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6628909111022949})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.67848801612854})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7396091222763062})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7812538146972656})
store['active_learning_steps'][115]['training']['best_epoch']=2
store['active_learning_steps'][115]['evaluation_metrics']={'accuracy': 0.9018, 'crossentropy': 0.543070556640625}
store['active_learning_steps'][115]['acquisition']={'indices': [38441, 50360, 55184, 53281, 9698], 'labels': [3, 7, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][116]['training']={}
store['active_learning_steps'][116]['training']['epochs']=[]
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7416350841522217})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7605960965156555})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6843082904815674})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7826758623123169})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7830532789230347})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7562891840934753})
store['active_learning_steps'][116]['training']['best_epoch']=3
store['active_learning_steps'][116]['evaluation_metrics']={'accuracy': 0.9103, 'crossentropy': 0.602957080078125}
store['active_learning_steps'][116]['acquisition']={'indices': [1782, 16884, 6738, 39919, 54392], 'labels': [-1, -1, -1, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][117]['training']={}
store['active_learning_steps'][117]['training']['epochs']=[]
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.6882708072662354})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6195052862167358})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6785333752632141})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6188079118728638})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6363365650177002})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.656791090965271})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6824973821640015})
store['active_learning_steps'][117]['training']['best_epoch']=4
store['active_learning_steps'][117]['evaluation_metrics']={'accuracy': 0.9165, 'crossentropy': 0.566693408203125}
store['active_learning_steps'][117]['acquisition']={'indices': [59797, 45702, 47220, 25290, 50982], 'labels': [2, 6, 6, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][118]['training']={}
store['active_learning_steps'][118]['training']['epochs']=[]
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7688045501708984})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6628415584564209})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6972568035125732})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.733788251876831})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6911232471466064})
store['active_learning_steps'][118]['training']['best_epoch']=2
store['active_learning_steps'][118]['evaluation_metrics']={'accuracy': 0.8976, 'crossentropy': 0.5875025390625}
store['active_learning_steps'][118]['acquisition']={'indices': [52047, 51989, 35627, 20314, 14140], 'labels': [0, 5, 6, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][119]['training']={}
store['active_learning_steps'][119]['training']['epochs']=[]
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8429762125015259})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8108365535736084})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.710423469543457})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8189372420310974})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8436503410339355})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.9108952283859253})
store['active_learning_steps'][119]['training']['best_epoch']=3
store['active_learning_steps'][119]['evaluation_metrics']={'accuracy': 0.9041, 'crossentropy': 0.589641552734375}
store['active_learning_steps'][119]['acquisition']={'indices': [26880, 32498, 37940, 29978, 10820], 'labels': [3, 4, -1, 9, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][120]['training']={}
store['active_learning_steps'][120]['training']['epochs']=[]
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.7779014110565186})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.653958261013031})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.682379961013794})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6887447834014893})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7283335328102112})
store['active_learning_steps'][120]['training']['best_epoch']=2
store['active_learning_steps'][120]['evaluation_metrics']={'accuracy': 0.9042, 'crossentropy': 0.555291455078125}
store['active_learning_steps'][120]['acquisition']={'indices': [3456, 29645, 31653, 21180, 36878], 'labels': [-1, -1, -1, 6, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][121]['training']={}
store['active_learning_steps'][121]['training']['epochs']=[]
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7699069976806641})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6962305307388306})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7243576645851135})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.8352364301681519})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8618152737617493})
store['active_learning_steps'][121]['training']['best_epoch']=2
store['active_learning_steps'][121]['evaluation_metrics']={'accuracy': 0.9032, 'crossentropy': 0.586802294921875}
store['active_learning_steps'][121]['acquisition']={'indices': [41265, 44851, 11556, 40650, 40654], 'labels': [-1, 9, -1, 6, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][122]['training']={}
store['active_learning_steps'][122]['training']['epochs']=[]
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7247898578643799})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.744313657283783})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7786015272140503})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6118634939193726})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.740494966506958})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.8335007429122925})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7931709289550781})
store['active_learning_steps'][122]['training']['best_epoch']=4
store['active_learning_steps'][122]['evaluation_metrics']={'accuracy': 0.9099, 'crossentropy': 0.560243115234375}
store['active_learning_steps'][122]['acquisition']={'indices': [7448, 5425, 27039, 15899, 52211], 'labels': [5, 1, -1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][123]['training']={}
store['active_learning_steps'][123]['training']['epochs']=[]
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7880076766014099})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.650009274482727})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.722240149974823})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7084765434265137})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8053494095802307})
store['active_learning_steps'][123]['training']['best_epoch']=2
store['active_learning_steps'][123]['evaluation_metrics']={'accuracy': 0.9029, 'crossentropy': 0.55881875}
store['active_learning_steps'][123]['acquisition']={'indices': [39240, 32972, 30018, 5975, 9371], 'labels': [3, 9, 7, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][124]['training']={}
store['active_learning_steps'][124]['training']['epochs']=[]
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7121000289916992})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6516447067260742})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6652642488479614})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6611783504486084})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7069560289382935})
store['active_learning_steps'][124]['training']['best_epoch']=2
store['active_learning_steps'][124]['evaluation_metrics']={'accuracy': 0.903, 'crossentropy': 0.592316552734375}
store['active_learning_steps'][124]['acquisition']={'indices': [36854, 55023, 16344, 36643, 604], 'labels': [-1, -1, 3, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][125]['training']={}
store['active_learning_steps'][125]['training']['epochs']=[]
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.680882453918457})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6225878000259399})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.649311363697052})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7105776071548462})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7338069081306458})
store['active_learning_steps'][125]['training']['best_epoch']=2
store['active_learning_steps'][125]['evaluation_metrics']={'accuracy': 0.9048, 'crossentropy': 0.528203466796875}
store['active_learning_steps'][125]['acquisition']={'indices': [23748, 56364, 18930, 48271, 34101], 'labels': [-1, -1, -1, 7, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][126]['training']={}
store['active_learning_steps'][126]['training']['epochs']=[]
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.6843529939651489})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.58122718334198})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5856437683105469})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6406806111335754})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6374607682228088})
store['active_learning_steps'][126]['training']['best_epoch']=2
store['active_learning_steps'][126]['evaluation_metrics']={'accuracy': 0.9109, 'crossentropy': 0.519891845703125}
store['active_learning_steps'][126]['acquisition']={'indices': [50320, 14573, 49504, 41272, 29696], 'labels': [5, -1, -1, 6, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][127]['training']={}
store['active_learning_steps'][127]['training']['epochs']=[]
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7353817820549011})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6892897486686707})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7684121131896973})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.649512767791748})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6814327239990234})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7563307285308838})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.720234751701355})
store['active_learning_steps'][127]['training']['best_epoch']=4
store['active_learning_steps'][127]['evaluation_metrics']={'accuracy': 0.9123, 'crossentropy': 0.58484482421875}
store['active_learning_steps'][127]['acquisition']={'indices': [13174, 28326, 3822, 34438, 58544], 'labels': [-1, 6, -1, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][128]['training']={}
store['active_learning_steps'][128]['training']['epochs']=[]
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8191614151000977})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6899973154067993})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6136761903762817})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6747344732284546})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6089999675750732})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7169023156166077})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.757644772529602})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7147783041000366})
store['active_learning_steps'][128]['training']['best_epoch']=5
store['active_learning_steps'][128]['evaluation_metrics']={'accuracy': 0.9145, 'crossentropy': 0.5749666015625}
store['active_learning_steps'][128]['acquisition']={'indices': [29427, 57069, 8949, 49080, 12181], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][129]['training']={}
store['active_learning_steps'][129]['training']['epochs']=[]
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7220168113708496})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7043163776397705})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6508357524871826})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7404747009277344})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.700647234916687})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7783210873603821})
store['active_learning_steps'][129]['training']['best_epoch']=3
store['active_learning_steps'][129]['evaluation_metrics']={'accuracy': 0.9058, 'crossentropy': 0.579572900390625}
store['active_learning_steps'][129]['acquisition']={'indices': [3314, 17439, 32699, 3478, 34016], 'labels': [-1, 2, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][130]['training']={}
store['active_learning_steps'][130]['training']['epochs']=[]
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7060308456420898})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.721662700176239})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7827028036117554})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7388449907302856})
store['active_learning_steps'][130]['training']['best_epoch']=1
store['active_learning_steps'][130]['evaluation_metrics']={'accuracy': 0.8882, 'crossentropy': 0.635828271484375}
store['active_learning_steps'][130]['acquisition']={'indices': [29125, 11108, 2789, 26287, 55399], 'labels': [1, -1, 6, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][131]['training']={}
store['active_learning_steps'][131]['training']['epochs']=[]
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7204419374465942})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6105257272720337})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5794304609298706})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.605969250202179})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6156083345413208})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6268345713615417})
store['active_learning_steps'][131]['training']['best_epoch']=3
store['active_learning_steps'][131]['evaluation_metrics']={'accuracy': 0.9164, 'crossentropy': 0.534480029296875}
store['active_learning_steps'][131]['acquisition']={'indices': [30470, 44127, 48641, 45497, 34164], 'labels': [-1, 0, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][132]['training']={}
store['active_learning_steps'][132]['training']['epochs']=[]
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7515013217926025})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6151636838912964})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5869396924972534})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6483603715896606})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.714771568775177})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6323407888412476})
store['active_learning_steps'][132]['training']['best_epoch']=3
store['active_learning_steps'][132]['evaluation_metrics']={'accuracy': 0.9082, 'crossentropy': 0.583065625}
store['active_learning_steps'][132]['acquisition']={'indices': [14209, 15780, 48460, 39205, 28960], 'labels': [-1, 6, -1, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][133]['training']={}
store['active_learning_steps'][133]['training']['epochs']=[]
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7195754647254944})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6199998259544373})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5330121517181396})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6135525703430176})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6484472751617432})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.69305419921875})
store['active_learning_steps'][133]['training']['best_epoch']=3
store['active_learning_steps'][133]['evaluation_metrics']={'accuracy': 0.9165, 'crossentropy': 0.50920263671875}
store['active_learning_steps'][133]['acquisition']={'indices': [56209, 31625, 26839, 49684, 44073], 'labels': [-1, -1, 9, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][134]['training']={}
store['active_learning_steps'][134]['training']['epochs']=[]
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.775565505027771})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6314902305603027})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6634604334831238})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6488487720489502})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6967787742614746})
store['active_learning_steps'][134]['training']['best_epoch']=2
store['active_learning_steps'][134]['evaluation_metrics']={'accuracy': 0.8977, 'crossentropy': 0.62002177734375}
store['active_learning_steps'][134]['acquisition']={'indices': [40415, 33892, 40247, 16756, 11173], 'labels': [7, -1, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][135]['training']={}
store['active_learning_steps'][135]['training']['epochs']=[]
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8097014427185059})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6381912231445312})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6976542472839355})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.625796914100647})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6559550166130066})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6322290301322937})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7507511377334595})
store['active_learning_steps'][135]['training']['best_epoch']=4
store['active_learning_steps'][135]['evaluation_metrics']={'accuracy': 0.9153, 'crossentropy': 0.559839892578125}
store['active_learning_steps'][135]['acquisition']={'indices': [54948, 26255, 5109, 41130, 25700], 'labels': [6, 7, 5, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][136]['training']={}
store['active_learning_steps'][136]['training']['epochs']=[]
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7420052289962769})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6773113012313843})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6747361421585083})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6393229961395264})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7302647829055786})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7208616137504578})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.7014375925064087})
store['active_learning_steps'][136]['training']['best_epoch']=4
store['active_learning_steps'][136]['evaluation_metrics']={'accuracy': 0.9159, 'crossentropy': 0.583581884765625}
store['active_learning_steps'][136]['acquisition']={'indices': [6777, 47350, 36788, 18637, 43732], 'labels': [-1, -1, -1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][137]['training']={}
store['active_learning_steps'][137]['training']['epochs']=[]
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7436867952346802})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.669216513633728})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7408144474029541})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6989496946334839})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7023246884346008})
store['active_learning_steps'][137]['training']['best_epoch']=2
store['active_learning_steps'][137]['evaluation_metrics']={'accuracy': 0.8957, 'crossentropy': 0.590203076171875}
store['active_learning_steps'][137]['acquisition']={'indices': [23569, 47603, 5600, 45571, 41244], 'labels': [6, -1, -1, 7, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][138]['training']={}
store['active_learning_steps'][138]['training']['epochs']=[]
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7349191308021545})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5940000414848328})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5873246192932129})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6500189304351807})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6797758340835571})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7654927968978882})
store['active_learning_steps'][138]['training']['best_epoch']=3
store['active_learning_steps'][138]['evaluation_metrics']={'accuracy': 0.9178, 'crossentropy': 0.539725390625}
store['active_learning_steps'][138]['acquisition']={'indices': [48259, 24390, 34369, 30682, 14946], 'labels': [7, 2, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][139]['training']={}
store['active_learning_steps'][139]['training']['epochs']=[]
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.7420752048492432})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6179823875427246})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6641659736633301})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8142837285995483})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6591811776161194})
store['active_learning_steps'][139]['training']['best_epoch']=2
store['active_learning_steps'][139]['evaluation_metrics']={'accuracy': 0.905, 'crossentropy': 0.549400537109375}
store['active_learning_steps'][139]['acquisition']={'indices': [6303, 13248, 53902, 50917, 59593], 'labels': [1, 5, 4, 4, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][140]['training']={}
store['active_learning_steps'][140]['training']['epochs']=[]
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7603994011878967})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6551605463027954})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6500467658042908})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6085460782051086})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6799232959747314})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6971555948257446})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6020882725715637})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.8149012327194214})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.8628942966461182})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.7208608388900757})
store['active_learning_steps'][140]['training']['best_epoch']=7
store['active_learning_steps'][140]['evaluation_metrics']={'accuracy': 0.9281, 'crossentropy': 0.52641552734375}
store['active_learning_steps'][140]['acquisition']={'indices': [27704, 44272, 16452, 40710, 44172], 'labels': [6, 8, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][141]['training']={}
store['active_learning_steps'][141]['training']['epochs']=[]
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7236130237579346})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6278764009475708})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6522673964500427})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6036504507064819})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6595531702041626})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6246443390846252})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7089235782623291})
store['active_learning_steps'][141]['training']['best_epoch']=4
store['active_learning_steps'][141]['evaluation_metrics']={'accuracy': 0.9166, 'crossentropy': 0.538250341796875}
store['active_learning_steps'][141]['acquisition']={'indices': [28338, 53798, 555, 41723, 51835], 'labels': [-1, -1, -1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][142]['training']={}
store['active_learning_steps'][142]['training']['epochs']=[]
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7063775062561035})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6145299673080444})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7608180046081543})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6589055061340332})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.643814742565155})
store['active_learning_steps'][142]['training']['best_epoch']=2
store['active_learning_steps'][142]['evaluation_metrics']={'accuracy': 0.9094, 'crossentropy': 0.52335869140625}
store['active_learning_steps'][142]['acquisition']={'indices': [27796, 39383, 42355, 3330, 18547], 'labels': [-1, -1, 3, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][143]['training']={}
store['active_learning_steps'][143]['training']['epochs']=[]
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7199348211288452})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6060730218887329})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6810612678527832})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6404708623886108})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6620136499404907})
store['active_learning_steps'][143]['training']['best_epoch']=2
store['active_learning_steps'][143]['evaluation_metrics']={'accuracy': 0.9056, 'crossentropy': 0.54084921875}
store['active_learning_steps'][143]['acquisition']={'indices': [1715, 32767, 24846, 429, 21660], 'labels': [2, -1, 0, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][144]['training']={}
store['active_learning_steps'][144]['training']['epochs']=[]
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.6996763944625854})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5812203884124756})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6609102487564087})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6260606050491333})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6550077199935913})
store['active_learning_steps'][144]['training']['best_epoch']=2
store['active_learning_steps'][144]['evaluation_metrics']={'accuracy': 0.911, 'crossentropy': 0.50915185546875}
store['active_learning_steps'][144]['acquisition']={'indices': [52072, 23686, 21938, 40421, 43713], 'labels': [-1, -1, -1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][145]['training']={}
store['active_learning_steps'][145]['training']['epochs']=[]
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7564630508422852})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6333237886428833})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6338940858840942})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6376386880874634})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7011765241622925})
store['active_learning_steps'][145]['training']['best_epoch']=2
store['active_learning_steps'][145]['evaluation_metrics']={'accuracy': 0.8995, 'crossentropy': 0.544805078125}
store['active_learning_steps'][145]['acquisition']={'indices': [32749, 55836, 3811, 33971, 20742], 'labels': [-1, 2, 1, 4, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][146]['training']={}
store['active_learning_steps'][146]['training']['epochs']=[]
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6830352544784546})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6662279367446899})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5712452530860901})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6490241289138794})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6406198143959045})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.639911413192749})
store['active_learning_steps'][146]['training']['best_epoch']=3
store['active_learning_steps'][146]['evaluation_metrics']={'accuracy': 0.9118, 'crossentropy': 0.524480517578125}
store['active_learning_steps'][146]['acquisition']={'indices': [17315, 2639, 26443, 1324, 58576], 'labels': [-1, -1, -1, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][147]['training']={}
store['active_learning_steps'][147]['training']['epochs']=[]
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7709786891937256})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5777148604393005})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6239884495735168})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5842170715332031})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5669828653335571})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5664932727813721})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.7184852361679077})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.624167263507843})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6813289523124695})
store['active_learning_steps'][147]['training']['best_epoch']=6
store['active_learning_steps'][147]['evaluation_metrics']={'accuracy': 0.9289, 'crossentropy': 0.50293623046875}
store['active_learning_steps'][147]['acquisition']={'indices': [37061, 55932, 46247, 47154, 54002], 'labels': [1, 3, 3, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][148]['training']={}
store['active_learning_steps'][148]['training']['epochs']=[]
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6722526550292969})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6165528893470764})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5833064913749695})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6132999658584595})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6167595386505127})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6274795532226562})
store['active_learning_steps'][148]['training']['best_epoch']=3
store['active_learning_steps'][148]['evaluation_metrics']={'accuracy': 0.9173, 'crossentropy': 0.49972294921875}
store['active_learning_steps'][148]['acquisition']={'indices': [6058, 51369, 57083, 835, 39688], 'labels': [4, 1, 7, 1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][149]['training']={}
store['active_learning_steps'][149]['training']['epochs']=[]
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7271685600280762})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6956143379211426})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5797648429870605})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6738059520721436})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6210995316505432})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6802064180374146})
store['active_learning_steps'][149]['training']['best_epoch']=3
store['active_learning_steps'][149]['evaluation_metrics']={'accuracy': 0.9143, 'crossentropy': 0.52899091796875}
store['active_learning_steps'][149]['acquisition']={'indices': [2594, 750, 46559, 45425, 11647], 'labels': [1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][150]['training']={}
store['active_learning_steps'][150]['training']['epochs']=[]
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7804087400436401})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7446985244750977})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6032674908638})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6582203507423401})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.624384343624115})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7394760251045227})
store['active_learning_steps'][150]['training']['best_epoch']=3
store['active_learning_steps'][150]['evaluation_metrics']={'accuracy': 0.9149, 'crossentropy': 0.541780322265625}
store['active_learning_steps'][150]['acquisition']={'indices': [20973, 46555, 34159, 47360, 37642], 'labels': [8, 3, -1, 1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][151]['training']={}
store['active_learning_steps'][151]['training']['epochs']=[]
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.7570286989212036})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6504446268081665})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6763166189193726})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7182556390762329})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6908049583435059})
store['active_learning_steps'][151]['training']['best_epoch']=2
store['active_learning_steps'][151]['evaluation_metrics']={'accuracy': 0.9046, 'crossentropy': 0.55724130859375}
store['active_learning_steps'][151]['acquisition']={'indices': [59847, 55243, 58978, 27150, 24196], 'labels': [0, 9, 9, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][152]['training']={}
store['active_learning_steps'][152]['training']['epochs']=[]
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6370951533317566})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5531949400901794})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5230653285980225})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.558594822883606})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5004247426986694})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6893700361251831})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5547890067100525})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.579807460308075})
store['active_learning_steps'][152]['training']['best_epoch']=5
store['active_learning_steps'][152]['evaluation_metrics']={'accuracy': 0.9286, 'crossentropy': 0.487943310546875}
store['active_learning_steps'][152]['acquisition']={'indices': [59347, 52684, 12742, 40112, 44829], 'labels': [6, -1, 7, 4, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][153]['training']={}
store['active_learning_steps'][153]['training']['epochs']=[]
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.7622524499893188})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6176683902740479})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6051027774810791})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6304693818092346})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5835034847259521})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6339687705039978})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6332929730415344})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6445046067237854})
store['active_learning_steps'][153]['training']['best_epoch']=5
store['active_learning_steps'][153]['evaluation_metrics']={'accuracy': 0.9248, 'crossentropy': 0.52673232421875}
store['active_learning_steps'][153]['acquisition']={'indices': [35071, 32924, 25783, 23078, 46751], 'labels': [2, 7, 0, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][154]['training']={}
store['active_learning_steps'][154]['training']['epochs']=[]
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7471472024917603})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6230528950691223})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5954877734184265})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6011478304862976})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5843989253044128})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6061583161354065})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6679242849349976})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6598703861236572})
store['active_learning_steps'][154]['training']['best_epoch']=5
store['active_learning_steps'][154]['evaluation_metrics']={'accuracy': 0.9272, 'crossentropy': 0.52459775390625}
store['active_learning_steps'][154]['acquisition']={'indices': [44917, 55843, 6964, 49218, 6421], 'labels': [0, -1, 9, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][155]['training']={}
store['active_learning_steps'][155]['training']['epochs']=[]
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.7646437883377075})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6153223514556885})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6188308000564575})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5870239734649658})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6104891300201416})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5729091167449951})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6825452446937561})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6383689641952515})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.7214099168777466})
store['active_learning_steps'][155]['training']['best_epoch']=6
store['active_learning_steps'][155]['evaluation_metrics']={'accuracy': 0.9296, 'crossentropy': 0.492411474609375}
store['active_learning_steps'][155]['acquisition']={'indices': [12212, 57759, 59210, 50853, 305], 'labels': [-1, 9, -1, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][156]['training']={}
store['active_learning_steps'][156]['training']['epochs']=[]
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.690362811088562})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.620988130569458})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6342527866363525})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6343289017677307})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6306352615356445})
store['active_learning_steps'][156]['training']['best_epoch']=2
store['active_learning_steps'][156]['evaluation_metrics']={'accuracy': 0.9036, 'crossentropy': 0.577668701171875}
store['active_learning_steps'][156]['acquisition']={'indices': [44405, 24283, 6234, 42646, 5842], 'labels': [-1, -1, 9, 7, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][157]['training']={}
store['active_learning_steps'][157]['training']['epochs']=[]
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6521366834640503})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5254677534103394})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5414671897888184})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5385046005249023})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5522134304046631})
store['active_learning_steps'][157]['training']['best_epoch']=2
store['active_learning_steps'][157]['evaluation_metrics']={'accuracy': 0.9166, 'crossentropy': 0.49111376953125}
store['active_learning_steps'][157]['acquisition']={'indices': [37855, 4084, 1949, 46019, 13731], 'labels': [3, -1, 9, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][158]['training']={}
store['active_learning_steps'][158]['training']['epochs']=[]
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7044156789779663})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6557538509368896})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6565451622009277})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6386310458183289})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5656265020370483})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6126646995544434})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5614719390869141})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5607205629348755})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.6194521188735962})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6435949802398682})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6271803379058838})
store['active_learning_steps'][158]['training']['best_epoch']=8
store['active_learning_steps'][158]['evaluation_metrics']={'accuracy': 0.9336, 'crossentropy': 0.486702734375}
store['active_learning_steps'][158]['acquisition']={'indices': [43669, 38985, 9720, 49338, 37525], 'labels': [-1, -1, 0, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][159]['training']={}
store['active_learning_steps'][159]['training']['epochs']=[]
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6655696630477905})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5725486874580383})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5183964967727661})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5642318725585938})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5601242184638977})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5159808397293091})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5137962102890015})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5896711945533752})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5730180740356445})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5442765951156616})
store['active_learning_steps'][159]['training']['best_epoch']=7
store['active_learning_steps'][159]['evaluation_metrics']={'accuracy': 0.9275, 'crossentropy': 0.51828134765625}
store['active_learning_steps'][159]['acquisition']={'indices': [34066, 55486, 11781, 20950, 43104], 'labels': [-1, 7, -1, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][160]['training']={}
store['active_learning_steps'][160]['training']['epochs']=[]
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7358717918395996})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5909701585769653})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5586664080619812})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6072036027908325})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6305102705955505})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5864031314849854})
store['active_learning_steps'][160]['training']['best_epoch']=3
store['active_learning_steps'][160]['evaluation_metrics']={'accuracy': 0.9258, 'crossentropy': 0.478101806640625}
store['active_learning_steps'][160]['acquisition']={'indices': [34988, 48384, 35321, 18260, 40786], 'labels': [4, 9, 7, 2, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][161]['training']={}
store['active_learning_steps'][161]['training']['epochs']=[]
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.6705242395401001})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5785484313964844})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5774621963500977})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5704392194747925})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5936121940612793})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6067205667495728})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5858083963394165})
store['active_learning_steps'][161]['training']['best_epoch']=4
store['active_learning_steps'][161]['evaluation_metrics']={'accuracy': 0.9283, 'crossentropy': 0.47512109375}
store['active_learning_steps'][161]['acquisition']={'indices': [27202, 41586, 2251, 3785, 49959], 'labels': [1, -1, -1, 9, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][162]['training']={}
store['active_learning_steps'][162]['training']['epochs']=[]
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6743402481079102})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5945169925689697})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5407894253730774})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.684779167175293})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5448516607284546})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5696821212768555})
store['active_learning_steps'][162]['training']['best_epoch']=3
store['active_learning_steps'][162]['evaluation_metrics']={'accuracy': 0.9201, 'crossentropy': 0.4660982421875}
store['active_learning_steps'][162]['acquisition']={'indices': [5317, 22890, 20949, 11948, 1082], 'labels': [-1, 9, 6, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][163]['training']={}
store['active_learning_steps'][163]['training']['epochs']=[]
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.6963237524032593})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5493401288986206})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5502523183822632})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5156528353691101})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5972474813461304})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5586265325546265})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.557523250579834})
store['active_learning_steps'][163]['training']['best_epoch']=4
store['active_learning_steps'][163]['evaluation_metrics']={'accuracy': 0.9258, 'crossentropy': 0.46258740234375}
store['active_learning_steps'][163]['acquisition']={'indices': [20371, 58922, 13505, 42758, 8130], 'labels': [-1, 6, 5, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][164]['training']={}
store['active_learning_steps'][164]['training']['epochs']=[]
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.7606250047683716})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5568078756332397})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5822923183441162})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5997180938720703})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5336065888404846})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4967910349369049})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6019444465637207})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6287876963615417})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5852165222167969})
store['active_learning_steps'][164]['training']['best_epoch']=6
store['active_learning_steps'][164]['evaluation_metrics']={'accuracy': 0.9398, 'crossentropy': 0.440564599609375}
store['active_learning_steps'][164]['acquisition']={'indices': [8595, 42992, 52025, 42650, 5608], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][165]['training']={}
store['active_learning_steps'][165]['training']['epochs']=[]
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.652470588684082})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5491619110107422})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5565968751907349})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5294966101646423})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5128586888313293})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6223376989364624})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6130775213241577})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6573137640953064})
store['active_learning_steps'][165]['training']['best_epoch']=5
store['active_learning_steps'][165]['evaluation_metrics']={'accuracy': 0.9317, 'crossentropy': 0.463087451171875}
store['active_learning_steps'][165]['acquisition']={'indices': [26641, 46983, 21702, 16951, 36999], 'labels': [6, 3, 1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][166]['training']={}
store['active_learning_steps'][166]['training']['epochs']=[]
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7205713391304016})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6201678514480591})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6013810634613037})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6297958493232727})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6899547576904297})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6060641407966614})
store['active_learning_steps'][166]['training']['best_epoch']=3
store['active_learning_steps'][166]['evaluation_metrics']={'accuracy': 0.917, 'crossentropy': 0.4836939453125}
store['active_learning_steps'][166]['acquisition']={'indices': [19232, 59842, 11895, 25431, 28067], 'labels': [-1, 7, 1, 3, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][167]['training']={}
store['active_learning_steps'][167]['training']['epochs']=[]
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6563019156455994})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5491132140159607})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.527380645275116})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5911946296691895})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5279091596603394})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5750538110733032})
store['active_learning_steps'][167]['training']['best_epoch']=3
store['active_learning_steps'][167]['evaluation_metrics']={'accuracy': 0.9257, 'crossentropy': 0.45815244140625}
