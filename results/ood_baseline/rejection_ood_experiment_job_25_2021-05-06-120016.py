store = {}
store['timestamp']=1620298816
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=25']
store['commit']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['github_url']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=25
store['worker_id']=25
store['num_workers']=40
store['config']={'seed': 30, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 20, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.Random', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.6353745460510254})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.6310830116271973})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.5534510612487793})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.824211359024048})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.03212308883667})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.9762306213378906})
store['active_learning_steps'][0]['training']['best_epoch']=3
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6929, 'crossentropy': 2.40249921875}
store['active_learning_steps'][0]['acquisition']={'indices': [18679, 26120, 5702, 24909, 27468], 'labels': [-1, 2, 3, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.924136996269226})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.2545158863067627})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.3022241592407227})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.6784987449645996})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7213, 'crossentropy': 1.740809375}
store['active_learning_steps'][1]['acquisition']={'indices': [16113, 2767, 6060, 56617, 30288], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.0582332611083984})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.3648409843444824})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.668548345565796})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.5926222801208496})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7006, 'crossentropy': 1.9748142578125}
store['active_learning_steps'][2]['acquisition']={'indices': [49078, 13030, 25458, 5281, 9615], 'labels': [-1, -1, 7, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.12101149559021})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.576272487640381})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.709747314453125})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.7086753845214844})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7001, 'crossentropy': 2.0408861328125}
store['active_learning_steps'][3]['acquisition']={'indices': [33239, 52723, 18532, 25049, 43010], 'labels': [3, -1, 7, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.89424729347229})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.279386043548584})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.4768242835998535})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.3457956314086914})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7174, 'crossentropy': 1.828346484375}
store['active_learning_steps'][4]['acquisition']={'indices': [11530, 14822, 46296, 46375, 12229], 'labels': [-1, 9, 3, 0, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.9875164031982422})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.2928524017333984})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.528947591781616})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.4860615730285645})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7034, 'crossentropy': 1.79252265625}
store['active_learning_steps'][5]['acquisition']={'indices': [52918, 6380, 58833, 40924, 3355], 'labels': [6, 1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.9679546356201172})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.4056243896484375})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.4558095932006836})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.4338207244873047})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7068, 'crossentropy': 1.8371189453125}
store['active_learning_steps'][6]['acquisition']={'indices': [241, 43153, 43760, 21158, 50522], 'labels': [-1, -1, -1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.949317216873169})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.6237199306488037})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.6747188568115234})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.889132499694824})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.716, 'crossentropy': 1.8067294921875}
store['active_learning_steps'][7]['acquisition']={'indices': [31215, 59158, 49385, 20776, 56021], 'labels': [-1, -1, 7, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.9476399421691895})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.274651527404785})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 2.5749287605285645})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.6342151165008545})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.7081, 'crossentropy': 1.89123515625}
store['active_learning_steps'][8]['acquisition']={'indices': [45067, 40757, 33386, 50683, 44429], 'labels': [6, -1, -1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.7054164409637451})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 2.158609390258789})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 2.4636988639831543})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 2.67175555229187})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.7459, 'crossentropy': 1.6995556640625}
store['active_learning_steps'][9]['acquisition']={'indices': [51636, 36859, 39732, 27092, 27021], 'labels': [-1, -1, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.741370677947998})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 2.0059070587158203})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 2.345520496368408})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 2.3765530586242676})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.7444, 'crossentropy': 1.6672501953125}
store['active_learning_steps'][10]['acquisition']={'indices': [55138, 52468, 846, 59452, 21326], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.8367466926574707})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 2.190173625946045})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 2.3179268836975098})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 2.628737449645996})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.7263, 'crossentropy': 1.7626015625}
store['active_learning_steps'][11]['acquisition']={'indices': [37130, 14062, 43941, 9063, 1115], 'labels': [-1, 8, -1, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.060640811920166})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.4306130409240723})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.58317494392395})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 3.0233194828033447})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.6763, 'crossentropy': 2.1182818359375}
store['active_learning_steps'][12]['acquisition']={'indices': [48210, 16689, 6999, 12683, 10805], 'labels': [0, -1, 9, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.7890504598617554})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 2.145611047744751})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 2.102170944213867})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 2.2282638549804688})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.7272, 'crossentropy': 1.65983984375}
store['active_learning_steps'][13]['acquisition']={'indices': [37830, 28370, 54667, 7953, 19788], 'labels': [5, 2, 9, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.7083160877227783})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.1106088161468506})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.446967124938965})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.3181562423706055})
store['active_learning_steps'][14]['training']['best_epoch']=1
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.7169, 'crossentropy': 1.71628046875}
store['active_learning_steps'][14]['acquisition']={'indices': [3217, 44304, 39627, 53213, 912], 'labels': [4, -1, 2, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.382758378982544})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.6518139839172363})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 2.042128562927246})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.9178876876831055})
store['active_learning_steps'][15]['training']['best_epoch']=1
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.7513, 'crossentropy': 1.3351083984375}
store['active_learning_steps'][15]['acquisition']={'indices': [7314, 30713, 9847, 24159, 28934], 'labels': [-1, 7, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.4069777727127075})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.6334799528121948})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.735126256942749})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 2.011411666870117})
store['active_learning_steps'][16]['training']['best_epoch']=1
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.7566, 'crossentropy': 1.37438388671875}
store['active_learning_steps'][16]['acquisition']={'indices': [1956, 54728, 13800, 2057, 26666], 'labels': [0, 0, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.5154414176940918})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.860562801361084})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.7879440784454346})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.7130892276763916})
store['active_learning_steps'][17]['training']['best_epoch']=1
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.7388, 'crossentropy': 1.54949990234375}
store['active_learning_steps'][17]['acquisition']={'indices': [17637, 40754, 48132, 58715, 25077], 'labels': [-1, -1, 5, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.2987074851989746})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.6410995721817017})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.6286022663116455})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.6758540868759155})
store['active_learning_steps'][18]['training']['best_epoch']=1
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.7857, 'crossentropy': 1.24069765625}
store['active_learning_steps'][18]['acquisition']={'indices': [25231, 47027, 12565, 27750, 25640], 'labels': [3, 3, 8, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.1191797256469727})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.3398075103759766})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.3535363674163818})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.305006504058838})
store['active_learning_steps'][19]['training']['best_epoch']=1
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8207, 'crossentropy': 1.07373232421875}
store['active_learning_steps'][19]['acquisition']={'indices': [3219, 49095, 20104, 33927, 36795], 'labels': [-1, -1, -1, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.1179237365722656})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.1975475549697876})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.3389467000961304})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.2543728351593018})
store['active_learning_steps'][20]['training']['best_epoch']=1
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8159, 'crossentropy': 1.0978658203125}
store['active_learning_steps'][20]['acquisition']={'indices': [38431, 7784, 57775, 21682, 782], 'labels': [-1, 3, 1, 1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.9146449565887451})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.964238166809082})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.1256673336029053})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.1156466007232666})
store['active_learning_steps'][21]['training']['best_epoch']=1
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.8501, 'crossentropy': 0.851290234375}
store['active_learning_steps'][21]['acquisition']={'indices': [37537, 49621, 2776, 33176, 34139], 'labels': [-1, 0, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.9380922317504883})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.0348711013793945})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 1.0098329782485962})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.1576234102249146})
store['active_learning_steps'][22]['training']['best_epoch']=1
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.7997, 'crossentropy': 0.9626666015625}
store['active_learning_steps'][22]['acquisition']={'indices': [3747, 59116, 55735, 30483, 38677], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.9018865823745728})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9652523994445801})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.1676931381225586})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.142399549484253})
store['active_learning_steps'][23]['training']['best_epoch']=1
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.8316, 'crossentropy': 0.8975021484375}
store['active_learning_steps'][23]['acquisition']={'indices': [59085, 46818, 10760, 53436, 11450], 'labels': [-1, 0, 3, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.00862717628479})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.1274091005325317})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.1064376831054688})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.1326711177825928})
store['active_learning_steps'][24]['training']['best_epoch']=1
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.8363, 'crossentropy': 0.9357560546875}
store['active_learning_steps'][24]['acquisition']={'indices': [51527, 49323, 50168, 6629, 59932], 'labels': [9, 8, 6, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.0278854370117188})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9570907950401306})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9408762454986572})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 1.0166412591934204})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.098934292793274})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.2760342359542847})
store['active_learning_steps'][25]['training']['best_epoch']=3
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.8612, 'crossentropy': 0.94783994140625}
store['active_learning_steps'][25]['acquisition']={'indices': [40218, 5167, 685, 41439, 29051], 'labels': [0, 0, -1, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.0382380485534668})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.0596845149993896})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.1857739686965942})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.2109497785568237})
store['active_learning_steps'][26]['training']['best_epoch']=1
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.8121, 'crossentropy': 1.09233828125}
store['active_learning_steps'][26]['acquisition']={'indices': [20384, 19095, 27906, 37488, 16098], 'labels': [1, 6, 7, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.087856650352478})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.092667818069458})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.3705275058746338})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.3395040035247803})
store['active_learning_steps'][27]['training']['best_epoch']=1
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.8171, 'crossentropy': 1.0180833984375}
store['active_learning_steps'][27]['acquisition']={'indices': [17588, 33650, 45501, 16325, 12774], 'labels': [3, -1, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.9263546466827393})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8284815549850464})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9644008278846741})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.0836323499679565})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 1.0369322299957275})
store['active_learning_steps'][28]['training']['best_epoch']=2
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.872, 'crossentropy': 0.8473384765625}
store['active_learning_steps'][28]['acquisition']={'indices': [47671, 17576, 1505, 44891, 34952], 'labels': [9, -1, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8802229762077332})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9754214286804199})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.136358618736267})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.1697615385055542})
store['active_learning_steps'][29]['training']['best_epoch']=1
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.8427, 'crossentropy': 0.90960634765625}
store['active_learning_steps'][29]['acquisition']={'indices': [28370, 54337, 32453, 24010, 19920], 'labels': [-1, -1, 8, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.9507964253425598})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9790394306182861})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.1531084775924683})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.1025056838989258})
store['active_learning_steps'][30]['training']['best_epoch']=1
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.8427, 'crossentropy': 0.90394150390625}
store['active_learning_steps'][30]['acquisition']={'indices': [2034, 15993, 27337, 42614, 2862], 'labels': [-1, -1, 5, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9272600412368774})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.9117176532745361})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.953961968421936})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9818594455718994})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.170495867729187})
store['active_learning_steps'][31]['training']['best_epoch']=2
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.8523, 'crossentropy': 0.93644560546875}
store['active_learning_steps'][31]['acquisition']={'indices': [53968, 34046, 34104, 27530, 43210], 'labels': [-1, -1, 9, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.956648051738739})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.9355214834213257})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.9912849068641663})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.1395775079727173})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.0941821336746216})
store['active_learning_steps'][32]['training']['best_epoch']=2
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.8498, 'crossentropy': 0.95450224609375}
store['active_learning_steps'][32]['acquisition']={'indices': [41130, 3121, 13720, 27318, 27905], 'labels': [-1, -1, 9, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8750179409980774})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.97630774974823})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.955292820930481})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.1396195888519287})
store['active_learning_steps'][33]['training']['best_epoch']=1
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.8546, 'crossentropy': 0.82362275390625}
store['active_learning_steps'][33]['acquisition']={'indices': [51484, 52225, 39163, 53083, 22890], 'labels': [8, -1, 9, 3, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.0245029926300049})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.048736572265625})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.4003785848617554})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.2653403282165527})
store['active_learning_steps'][34]['training']['best_epoch']=1
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.8065, 'crossentropy': 0.95436044921875}
store['active_learning_steps'][34]['acquisition']={'indices': [21438, 47966, 21317, 59980, 48142], 'labels': [2, 2, 9, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9618406891822815})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9707351922988892})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.1432348489761353})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.0982741117477417})
store['active_learning_steps'][35]['training']['best_epoch']=1
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.8148, 'crossentropy': 0.96053173828125}
store['active_learning_steps'][35]['acquisition']={'indices': [40031, 40852, 6462, 55748, 54056], 'labels': [-1, 8, 4, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.0006433725357056})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.0667240619659424})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.0381118059158325})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.206555724143982})
store['active_learning_steps'][36]['training']['best_epoch']=1
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.8068, 'crossentropy': 0.977051953125}
store['active_learning_steps'][36]['acquisition']={'indices': [48723, 33529, 32211, 45894, 38883], 'labels': [8, 3, 6, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8940207958221436})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.9012451767921448})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9568095207214355})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.0783395767211914})
store['active_learning_steps'][37]['training']['best_epoch']=1
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.8412, 'crossentropy': 0.8432884765625}
store['active_learning_steps'][37]['acquisition']={'indices': [59565, 17335, 20075, 36610, 2800], 'labels': [-1, 0, 9, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8203259706497192})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.960618257522583})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9288547039031982})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.947113037109375})
store['active_learning_steps'][38]['training']['best_epoch']=1
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.8618, 'crossentropy': 0.804594775390625}
store['active_learning_steps'][38]['acquisition']={'indices': [5529, 3813, 55311, 16003, 49392], 'labels': [2, 2, 8, 3, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.8796892166137695})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.9862487316131592})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.0400948524475098})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.9917973875999451})
store['active_learning_steps'][39]['training']['best_epoch']=1
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.8247, 'crossentropy': 0.87745771484375}
store['active_learning_steps'][39]['acquisition']={'indices': [54501, 29737, 18276, 37510, 28725], 'labels': [-1, 9, -1, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.0123765468597412})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8988155126571655})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.052830696105957})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.1385836601257324})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.218550682067871})
store['active_learning_steps'][40]['training']['best_epoch']=2
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.8597, 'crossentropy': 0.8755298828125}
store['active_learning_steps'][40]['acquisition']={'indices': [36423, 26887, 51768, 39893, 8881], 'labels': [2, -1, -1, 6, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.9552463293075562})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.0687259435653687})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.047839879989624})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.0080896615982056})
store['active_learning_steps'][41]['training']['best_epoch']=1
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.8332, 'crossentropy': 0.9048140625}
store['active_learning_steps'][41]['acquisition']={'indices': [46367, 4361, 52139, 37139, 43966], 'labels': [4, 4, 9, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.9181413650512695})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8801422119140625})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.066149353981018})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.008939504623413})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.005906581878662})
store['active_learning_steps'][42]['training']['best_epoch']=2
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.866, 'crossentropy': 0.812466162109375}
store['active_learning_steps'][42]['acquisition']={'indices': [11387, 22027, 12678, 22973, 51978], 'labels': [-1, -1, 7, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.9420725107192993})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8862314820289612})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9243172407150269})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.022824764251709})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.2961641550064087})
store['active_learning_steps'][43]['training']['best_epoch']=2
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.8773, 'crossentropy': 0.8095658203125}
store['active_learning_steps'][43]['acquisition']={'indices': [1017, 59044, 45727, 30858, 55635], 'labels': [-1, -1, -1, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8627825975418091})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.80399489402771})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.897215723991394})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.059550404548645})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.1674693822860718})
store['active_learning_steps'][44]['training']['best_epoch']=2
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.8745, 'crossentropy': 0.793741455078125}
store['active_learning_steps'][44]['acquisition']={'indices': [22633, 1365, 50049, 29968, 245], 'labels': [-1, 1, -1, 1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.1166356801986694})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.9253617525100708})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8962835073471069})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.947779655456543})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 1.043445348739624})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9783722162246704})
store['active_learning_steps'][45]['training']['best_epoch']=3
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.8755, 'crossentropy': 0.89144990234375}
store['active_learning_steps'][45]['acquisition']={'indices': [41434, 46254, 43276, 40921, 5093], 'labels': [-1, -1, -1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.8821516036987305})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.0167237520217896})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8684214353561401})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9781942367553711})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.032257080078125})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9344077110290527})
store['active_learning_steps'][46]['training']['best_epoch']=3
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.8686, 'crossentropy': 0.85881728515625}
store['active_learning_steps'][46]['acquisition']={'indices': [16495, 23808, 50456, 26627, 23954], 'labels': [1, -1, -1, 4, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.0103957653045654})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.934272050857544})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.953526496887207})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.0566604137420654})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.060559630393982})
store['active_learning_steps'][47]['training']['best_epoch']=2
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.8631, 'crossentropy': 0.89827197265625}
store['active_learning_steps'][47]['acquisition']={'indices': [41503, 48452, 25820, 43223, 39623], 'labels': [-1, -1, 3, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.9418222904205322})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7761085629463196})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.9818719625473022})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.1122875213623047})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.117522954940796})
store['active_learning_steps'][48]['training']['best_epoch']=2
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.8821, 'crossentropy': 0.7451865234375}
store['active_learning_steps'][48]['acquisition']={'indices': [30902, 38652, 46589, 37117, 2404], 'labels': [7, 2, 9, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8488298654556274})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8495776653289795})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.753591001033783})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9504294395446777})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8753269910812378})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 1.0230302810668945})
store['active_learning_steps'][49]['training']['best_epoch']=3
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.8937, 'crossentropy': 0.73680693359375}
store['active_learning_steps'][49]['acquisition']={'indices': [21053, 3459, 23257, 13865, 36152], 'labels': [-1, 4, -1, 6, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.9559072256088257})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9092251062393188})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.0040128231048584})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.105320930480957})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9484383463859558})
store['active_learning_steps'][50]['training']['best_epoch']=2
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.8774, 'crossentropy': 0.793050830078125}
store['active_learning_steps'][50]['acquisition']={'indices': [18277, 38942, 45230, 39057, 2362], 'labels': [-1, 8, 0, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8697781562805176})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8871320486068726})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8686457276344299})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9901442527770996})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9928646087646484})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.9064209461212158})
store['active_learning_steps'][51]['training']['best_epoch']=3
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.8785, 'crossentropy': 0.828575}
store['active_learning_steps'][51]['acquisition']={'indices': [23339, 25424, 19018, 38529, 43810], 'labels': [4, 6, -1, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8180089592933655})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.9106752872467041})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9573299884796143})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9600880146026611})
store['active_learning_steps'][52]['training']['best_epoch']=1
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.8523, 'crossentropy': 0.815854736328125}
store['active_learning_steps'][52]['acquisition']={'indices': [14348, 158, 48807, 59951, 44067], 'labels': [-1, -1, 0, 4, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8167173266410828})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8649505376815796})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9373434782028198})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.9085451364517212})
store['active_learning_steps'][53]['training']['best_epoch']=1
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.8504, 'crossentropy': 0.797044873046875}
store['active_learning_steps'][53]['acquisition']={'indices': [9609, 8256, 48088, 50238, 5706], 'labels': [-1, 7, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8622134923934937})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8739528656005859})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8552849292755127})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.925851583480835})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.940654993057251})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.141771674156189})
store['active_learning_steps'][54]['training']['best_epoch']=3
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.8816, 'crossentropy': 0.81524306640625}
store['active_learning_steps'][54]['acquisition']={'indices': [27262, 33841, 22724, 56118, 36154], 'labels': [-1, 1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7795106172561646})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8636693358421326})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9001434445381165})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.98259437084198})
store['active_learning_steps'][55]['training']['best_epoch']=1
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.856, 'crossentropy': 0.75720751953125}
store['active_learning_steps'][55]['acquisition']={'indices': [40113, 323, 46911, 14083, 53137], 'labels': [-1, 6, 3, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.8929225206375122})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8130090832710266})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8346553444862366})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9486279487609863})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 1.1224870681762695})
store['active_learning_steps'][56]['training']['best_epoch']=2
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.8793, 'crossentropy': 0.76767099609375}
store['active_learning_steps'][56]['acquisition']={'indices': [31626, 21911, 48416, 58033, 35920], 'labels': [-1, 2, 7, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8515740633010864})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8180930018424988})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8888649940490723})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9446925520896912})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.9306123852729797})
store['active_learning_steps'][57]['training']['best_epoch']=2
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.8843, 'crossentropy': 0.7398228515625}
store['active_learning_steps'][57]['acquisition']={'indices': [29104, 9003, 8832, 43658, 40072], 'labels': [-1, -1, 4, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8608317375183105})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8022655844688416})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9452908039093018})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8902095556259155})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9998801946640015})
store['active_learning_steps'][58]['training']['best_epoch']=2
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.8873, 'crossentropy': 0.746040283203125}
store['active_learning_steps'][58]['acquisition']={'indices': [2219, 11807, 37727, 8733, 1431], 'labels': [9, -1, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8536790609359741})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9039992094039917})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8982366323471069})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9127058982849121})
store['active_learning_steps'][59]['training']['best_epoch']=1
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.8504, 'crossentropy': 0.8272994140625}
store['active_learning_steps'][59]['acquisition']={'indices': [15432, 43007, 3139, 56766, 50441], 'labels': [-1, 1, -1, 0, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.9197412729263306})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7986961603164673})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.793880820274353})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8465616703033447})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8599705696105957})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.9708970785140991})
store['active_learning_steps'][60]['training']['best_epoch']=3
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.8966, 'crossentropy': 0.76287138671875}
store['active_learning_steps'][60]['acquisition']={'indices': [14706, 48199, 14689, 31584, 50934], 'labels': [-1, 6, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7672139406204224})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7812511324882507})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8069369792938232})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.859038770198822})
store['active_learning_steps'][61]['training']['best_epoch']=1
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.874, 'crossentropy': 0.709183935546875}
store['active_learning_steps'][61]['acquisition']={'indices': [11687, 18524, 30624, 29150, 59078], 'labels': [7, 1, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.8905855417251587})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7783488035202026})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9517542123794556})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.9546993970870972})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9434041976928711})
store['active_learning_steps'][62]['training']['best_epoch']=2
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.8873, 'crossentropy': 0.72489990234375}
store['active_learning_steps'][62]['acquisition']={'indices': [42806, 42337, 12514, 47729, 48362], 'labels': [-1, -1, 2, 1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.7951866388320923})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8530659079551697})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7605855464935303})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8294012546539307})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9180365800857544})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8285761475563049})
store['active_learning_steps'][63]['training']['best_epoch']=3
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.8975, 'crossentropy': 0.758807958984375}
store['active_learning_steps'][63]['acquisition']={'indices': [7120, 22765, 14512, 54862, 21395], 'labels': [-1, 9, 5, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8148365020751953})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.775507926940918})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8769091367721558})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7741652131080627})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.9096263647079468})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8449535369873047})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.9861363768577576})
store['active_learning_steps'][64]['training']['best_epoch']=4
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.9019, 'crossentropy': 0.69306572265625}
store['active_learning_steps'][64]['acquisition']={'indices': [33762, 12131, 33406, 52524, 29678], 'labels': [-1, -1, 7, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8818429708480835})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8326064944267273})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.943333625793457})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9813125729560852})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 1.113209843635559})
store['active_learning_steps'][65]['training']['best_epoch']=2
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.8802, 'crossentropy': 0.7952515625}
store['active_learning_steps'][65]['acquisition']={'indices': [53886, 27649, 11717, 27420, 46114], 'labels': [-1, 3, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8260756134986877})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8215377926826477})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9508330225944519})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9568436145782471})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9776549935340881})
store['active_learning_steps'][66]['training']['best_epoch']=2
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.8786, 'crossentropy': 0.728379296875}
store['active_learning_steps'][66]['acquisition']={'indices': [15530, 26398, 52794, 19931, 21620], 'labels': [0, -1, 3, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8738548159599304})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8806267976760864})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9131560921669006})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.9748535752296448})
store['active_learning_steps'][67]['training']['best_epoch']=1
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.8517, 'crossentropy': 0.801330615234375}
store['active_learning_steps'][67]['acquisition']={'indices': [13283, 28591, 38276, 58198, 35008], 'labels': [-1, 6, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7829588651657104})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8283853530883789})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8494755029678345})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9085192680358887})
store['active_learning_steps'][68]['training']['best_epoch']=1
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.8605, 'crossentropy': 0.785852783203125}
store['active_learning_steps'][68]['acquisition']={'indices': [38444, 59105, 30566, 7625, 36291], 'labels': [6, -1, -1, 3, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.8760504722595215})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.832646369934082})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7248410582542419})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8847588300704956})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.9455811977386475})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8971576690673828})
store['active_learning_steps'][69]['training']['best_epoch']=3
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9022, 'crossentropy': 0.72441103515625}
store['active_learning_steps'][69]['acquisition']={'indices': [30137, 18827, 6948, 35783, 24217], 'labels': [-1, -1, 2, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7791841626167297})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7362985610961914})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8582155704498291})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.935266375541687})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8512855172157288})
store['active_learning_steps'][70]['training']['best_epoch']=2
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.8954, 'crossentropy': 0.6705146484375}
store['active_learning_steps'][70]['acquisition']={'indices': [38359, 36098, 15785, 52836, 25368], 'labels': [2, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.9120631217956543})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7737431526184082})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7336318492889404})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8401490449905396})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.9686193466186523})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.9063366055488586})
store['active_learning_steps'][71]['training']['best_epoch']=3
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.8941, 'crossentropy': 0.682816748046875}
store['active_learning_steps'][71]['acquisition']={'indices': [7836, 32496, 39712, 16054, 22022], 'labels': [-1, -1, 7, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8398037552833557})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7631673812866211})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7359633445739746})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8041261434555054})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8179930448532104})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7592167258262634})
store['active_learning_steps'][72]['training']['best_epoch']=3
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.8954, 'crossentropy': 0.669455029296875}
store['active_learning_steps'][72]['acquisition']={'indices': [17245, 39689, 26652, 4851, 46569], 'labels': [-1, -1, 4, 2, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7414029836654663})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6894221901893616})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6883043050765991})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7630044221878052})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7798956632614136})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8516066074371338})
store['active_learning_steps'][73]['training']['best_epoch']=3
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.8998, 'crossentropy': 0.651649951171875}
store['active_learning_steps'][73]['acquisition']={'indices': [22779, 44203, 58363, 39726, 55010], 'labels': [5, 8, 9, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7792361974716187})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7013792991638184})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7163932919502258})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8069547414779663})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8409998416900635})
store['active_learning_steps'][74]['training']['best_epoch']=2
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.8947, 'crossentropy': 0.640760595703125}
store['active_learning_steps'][74]['acquisition']={'indices': [45626, 53366, 42843, 43812, 19331], 'labels': [7, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.780448853969574})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6616389751434326})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6934096813201904})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7085339426994324})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7963085174560547})
store['active_learning_steps'][75]['training']['best_epoch']=2
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9034, 'crossentropy': 0.597008349609375}
store['active_learning_steps'][75]['acquisition']={'indices': [44658, 49287, 3781, 39487, 229], 'labels': [7, 3, -1, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7912552356719971})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6896560788154602})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6555246114730835})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.716463565826416})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8136157989501953})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7251635789871216})
store['active_learning_steps'][76]['training']['best_epoch']=3
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9148, 'crossentropy': 0.616369384765625}
store['active_learning_steps'][76]['acquisition']={'indices': [7209, 20960, 193, 27782, 2070], 'labels': [-1, 2, 7, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.814927339553833})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7764469385147095})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7894426584243774})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8620650172233582})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.852886438369751})
store['active_learning_steps'][77]['training']['best_epoch']=2
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.8901, 'crossentropy': 0.66119365234375}
store['active_learning_steps'][77]['acquisition']={'indices': [3587, 7090, 26379, 38891, 433], 'labels': [-1, 4, 8, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7535451650619507})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8005844354629517})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6850557327270508})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.737319827079773})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7750606536865234})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.8172539472579956})
store['active_learning_steps'][78]['training']['best_epoch']=3
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9053, 'crossentropy': 0.605260791015625}
store['active_learning_steps'][78]['acquisition']={'indices': [8327, 26980, 25965, 3525, 56698], 'labels': [-1, -1, 9, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6956093311309814})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6676952242851257})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6696217060089111})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6716628074645996})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7409951686859131})
store['active_learning_steps'][79]['training']['best_epoch']=2
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.8943, 'crossentropy': 0.607207275390625}
store['active_learning_steps'][79]['acquisition']={'indices': [2422, 32986, 59990, 10648, 25732], 'labels': [6, 1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7498915791511536})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7032430171966553})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.717122495174408})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7711712121963501})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7971073985099792})
store['active_learning_steps'][80]['training']['best_epoch']=2
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.8895, 'crossentropy': 0.628409619140625}
store['active_learning_steps'][80]['acquisition']={'indices': [44828, 19899, 12630, 43700, 28983], 'labels': [2, -1, -1, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7194260358810425})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7454853653907776})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7454913854598999})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7218840718269348})
store['active_learning_steps'][81]['training']['best_epoch']=1
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.8656, 'crossentropy': 0.68290947265625}
store['active_learning_steps'][81]['acquisition']={'indices': [7523, 30242, 37613, 17381, 22658], 'labels': [-1, 8, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7222070693969727})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6690788865089417})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7049709558486938})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7575856447219849})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7848566770553589})
store['active_learning_steps'][82]['training']['best_epoch']=2
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9035, 'crossentropy': 0.610898974609375}
store['active_learning_steps'][82]['acquisition']={'indices': [4654, 33540, 45298, 38055, 34182], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7495981454849243})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.748169481754303})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7465475797653198})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7612261772155762})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8501921892166138})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8179116249084473})
store['active_learning_steps'][83]['training']['best_epoch']=3
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9004, 'crossentropy': 0.6297642578125}
store['active_learning_steps'][83]['acquisition']={'indices': [92, 8770, 2555, 57708, 55274], 'labels': [4, -1, 8, 4, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8219703435897827})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7118332386016846})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8143092393875122})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8895225524902344})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7497073411941528})
store['active_learning_steps'][84]['training']['best_epoch']=2
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.8945, 'crossentropy': 0.627320263671875}
store['active_learning_steps'][84]['acquisition']={'indices': [57345, 15653, 12040, 13734, 33748], 'labels': [-1, 9, -1, 0, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7347954511642456})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7011144161224365})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7555553913116455})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8170604705810547})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.801697850227356})
store['active_learning_steps'][85]['training']['best_epoch']=2
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.8941, 'crossentropy': 0.64618515625}
store['active_learning_steps'][85]['acquisition']={'indices': [8950, 10687, 21325, 16804, 49747], 'labels': [4, -1, 3, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7318708896636963})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6864253878593445})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7404541969299316})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7737374305725098})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8186960220336914})
store['active_learning_steps'][86]['training']['best_epoch']=2
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.8942, 'crossentropy': 0.667239794921875}
store['active_learning_steps'][86]['acquisition']={'indices': [18765, 33235, 40428, 2064, 35001], 'labels': [3, -1, -1, 7, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][87]['training']={}
store['active_learning_steps'][87]['training']['epochs']=[]
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.825270414352417})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6936733722686768})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7440767288208008})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8439508676528931})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8601360321044922})
store['active_learning_steps'][87]['training']['best_epoch']=2
store['active_learning_steps'][87]['evaluation_metrics']={'accuracy': 0.8958, 'crossentropy': 0.646318505859375}
store['active_learning_steps'][87]['acquisition']={'indices': [23727, 18950, 5430, 30384, 22490], 'labels': [-1, 7, -1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][88]['training']={}
store['active_learning_steps'][88]['training']['epochs']=[]
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7305906414985657})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6908375024795532})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6851952075958252})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7013775110244751})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.701643705368042})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7068589925765991})
store['active_learning_steps'][88]['training']['best_epoch']=3
store['active_learning_steps'][88]['evaluation_metrics']={'accuracy': 0.9088, 'crossentropy': 0.62322685546875}
store['active_learning_steps'][88]['acquisition']={'indices': [16255, 57345, 24258, 22199, 54549], 'labels': [-1, -1, -1, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][89]['training']={}
store['active_learning_steps'][89]['training']['epochs']=[]
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7626593112945557})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6600710153579712})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6572104692459106})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6865516901016235})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8147492408752441})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7013939619064331})
store['active_learning_steps'][89]['training']['best_epoch']=3
store['active_learning_steps'][89]['evaluation_metrics']={'accuracy': 0.9105, 'crossentropy': 0.5887837890625}
store['active_learning_steps'][89]['acquisition']={'indices': [19528, 4036, 36508, 34336, 44637], 'labels': [1, -1, 5, 6, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][90]['training']={}
store['active_learning_steps'][90]['training']['epochs']=[]
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7685188055038452})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6496686339378357})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7880086898803711})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7361704111099243})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7212674021720886})
store['active_learning_steps'][90]['training']['best_epoch']=2
store['active_learning_steps'][90]['evaluation_metrics']={'accuracy': 0.8997, 'crossentropy': 0.600807666015625}
store['active_learning_steps'][90]['acquisition']={'indices': [18563, 8607, 15659, 28933, 23434], 'labels': [-1, -1, -1, 7, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][91]['training']={}
store['active_learning_steps'][91]['training']['epochs']=[]
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7015474438667297})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6554967164993286})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7566744089126587})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6575732231140137})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6942079663276672})
store['active_learning_steps'][91]['training']['best_epoch']=2
store['active_learning_steps'][91]['evaluation_metrics']={'accuracy': 0.8961, 'crossentropy': 0.6046361328125}
store['active_learning_steps'][91]['acquisition']={'indices': [33677, 3794, 8974, 29547, 26573], 'labels': [-1, -1, 6, 9, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][92]['training']={}
store['active_learning_steps'][92]['training']['epochs']=[]
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.6880090236663818})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5947903394699097})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6845458745956421})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6746523380279541})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6797477006912231})
store['active_learning_steps'][92]['training']['best_epoch']=2
store['active_learning_steps'][92]['evaluation_metrics']={'accuracy': 0.904, 'crossentropy': 0.585361865234375}
store['active_learning_steps'][92]['acquisition']={'indices': [23206, 35560, 59178, 3318, 51063], 'labels': [3, 7, -1, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][93]['training']={}
store['active_learning_steps'][93]['training']['epochs']=[]
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.7921843528747559})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6843562126159668})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7545537948608398})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7962701916694641})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.8372998237609863})
store['active_learning_steps'][93]['training']['best_epoch']=2
store['active_learning_steps'][93]['evaluation_metrics']={'accuracy': 0.8871, 'crossentropy': 0.623813671875}
store['active_learning_steps'][93]['acquisition']={'indices': [17133, 17933, 57887, 50347, 41319], 'labels': [0, 6, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][94]['training']={}
store['active_learning_steps'][94]['training']['epochs']=[]
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8219192028045654})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7527427673339844})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7470070123672485})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.783126711845398})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.8011766672134399})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8324680328369141})
store['active_learning_steps'][94]['training']['best_epoch']=3
store['active_learning_steps'][94]['evaluation_metrics']={'accuracy': 0.9045, 'crossentropy': 0.64203564453125}
store['active_learning_steps'][94]['acquisition']={'indices': [23595, 49042, 41312, 36491, 30409], 'labels': [4, -1, 5, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][95]['training']={}
store['active_learning_steps'][95]['training']['epochs']=[]
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7562600374221802})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6794806122779846})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6578798294067383})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7234634160995483})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7286738157272339})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.8630405068397522})
store['active_learning_steps'][95]['training']['best_epoch']=3
store['active_learning_steps'][95]['evaluation_metrics']={'accuracy': 0.909, 'crossentropy': 0.58467861328125}
store['active_learning_steps'][95]['acquisition']={'indices': [4196, 42157, 28162, 47891, 14693], 'labels': [3, 0, 6, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][96]['training']={}
store['active_learning_steps'][96]['training']['epochs']=[]
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6867339015007019})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5620789527893066})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6470175981521606})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6380887031555176})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7180556058883667})
store['active_learning_steps'][96]['training']['best_epoch']=2
store['active_learning_steps'][96]['evaluation_metrics']={'accuracy': 0.911, 'crossentropy': 0.5019037109375}
store['active_learning_steps'][96]['acquisition']={'indices': [55556, 57964, 8326, 56904, 12932], 'labels': [-1, 2, 6, 6, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][97]['training']={}
store['active_learning_steps'][97]['training']['epochs']=[]
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.7964791059494019})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6702306270599365})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6878660321235657})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6933690309524536})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6976370811462402})
store['active_learning_steps'][97]['training']['best_epoch']=2
store['active_learning_steps'][97]['evaluation_metrics']={'accuracy': 0.9013, 'crossentropy': 0.563930419921875}
store['active_learning_steps'][97]['acquisition']={'indices': [44065, 51540, 56700, 10553, 9647], 'labels': [-1, -1, -1, 6, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][98]['training']={}
store['active_learning_steps'][98]['training']['epochs']=[]
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7535756230354309})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5842448472976685})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6778190732002258})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7427815198898315})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7019271850585938})
store['active_learning_steps'][98]['training']['best_epoch']=2
store['active_learning_steps'][98]['evaluation_metrics']={'accuracy': 0.9073, 'crossentropy': 0.548893505859375}
store['active_learning_steps'][98]['acquisition']={'indices': [37272, 40290, 7152, 36554, 47372], 'labels': [4, 5, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][99]['training']={}
store['active_learning_steps'][99]['training']['epochs']=[]
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6971657276153564})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6620025634765625})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7276139259338379})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7150533199310303})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7363607883453369})
store['active_learning_steps'][99]['training']['best_epoch']=2
store['active_learning_steps'][99]['evaluation_metrics']={'accuracy': 0.9012, 'crossentropy': 0.58084169921875}
store['active_learning_steps'][99]['acquisition']={'indices': [29409, 5737, 16004, 54344, 51422], 'labels': [-1, -1, 7, 8, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][100]['training']={}
store['active_learning_steps'][100]['training']['epochs']=[]
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7060590982437134})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6737935543060303})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6288599967956543})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7308447360992432})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.8019120693206787})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7798850536346436})
store['active_learning_steps'][100]['training']['best_epoch']=3
store['active_learning_steps'][100]['evaluation_metrics']={'accuracy': 0.918, 'crossentropy': 0.525630810546875}
store['active_learning_steps'][100]['acquisition']={'indices': [46833, 34761, 16174, 6135, 24569], 'labels': [-1, -1, -1, 1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][101]['training']={}
store['active_learning_steps'][101]['training']['epochs']=[]
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7476657629013062})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6566916108131409})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6491546630859375})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7138790488243103})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7366985082626343})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7336733341217041})
store['active_learning_steps'][101]['training']['best_epoch']=3
store['active_learning_steps'][101]['evaluation_metrics']={'accuracy': 0.9109, 'crossentropy': 0.5876865234375}
store['active_learning_steps'][101]['acquisition']={'indices': [41935, 42756, 39324, 17289, 6089], 'labels': [-1, 5, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][102]['training']={}
store['active_learning_steps'][102]['training']['epochs']=[]
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6740777492523193})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5649961233139038})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7434276342391968})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6638088226318359})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6474335789680481})
store['active_learning_steps'][102]['training']['best_epoch']=2
store['active_learning_steps'][102]['evaluation_metrics']={'accuracy': 0.9124, 'crossentropy': 0.50823349609375}
store['active_learning_steps'][102]['acquisition']={'indices': [27553, 15349, 53012, 20778, 32775], 'labels': [-1, 9, 1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][103]['training']={}
store['active_learning_steps'][103]['training']['epochs']=[]
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7001878023147583})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6434333324432373})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5958091020584106})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7313210964202881})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6490452289581299})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.695928692817688})
store['active_learning_steps'][103]['training']['best_epoch']=3
store['active_learning_steps'][103]['evaluation_metrics']={'accuracy': 0.9199, 'crossentropy': 0.517614453125}
store['active_learning_steps'][103]['acquisition']={'indices': [51890, 33262, 2777, 22611, 52645], 'labels': [-1, 4, 6, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][104]['training']={}
store['active_learning_steps'][104]['training']['epochs']=[]
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7150167226791382})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.600618839263916})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6373031139373779})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6634013652801514})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6920174956321716})
store['active_learning_steps'][104]['training']['best_epoch']=2
store['active_learning_steps'][104]['evaluation_metrics']={'accuracy': 0.9085, 'crossentropy': 0.5572484375}
store['active_learning_steps'][104]['acquisition']={'indices': [49065, 46009, 58986, 41732, 59182], 'labels': [0, -1, 4, 1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][105]['training']={}
store['active_learning_steps'][105]['training']['epochs']=[]
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8023828864097595})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6005401611328125})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.641539454460144})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6721633672714233})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7236541509628296})
store['active_learning_steps'][105]['training']['best_epoch']=2
store['active_learning_steps'][105]['evaluation_metrics']={'accuracy': 0.8968, 'crossentropy': 0.555807275390625}
store['active_learning_steps'][105]['acquisition']={'indices': [49662, 36719, 28715, 18529, 16467], 'labels': [-1, -1, 9, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][106]['training']={}
store['active_learning_steps'][106]['training']['epochs']=[]
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7561267614364624})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6277775764465332})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6146976947784424})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6624637842178345})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6885918378829956})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7696901559829712})
store['active_learning_steps'][106]['training']['best_epoch']=3
store['active_learning_steps'][106]['evaluation_metrics']={'accuracy': 0.9121, 'crossentropy': 0.556855859375}
store['active_learning_steps'][106]['acquisition']={'indices': [33232, 27542, 48006, 28847, 52819], 'labels': [-1, -1, -1, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][107]['training']={}
store['active_learning_steps'][107]['training']['epochs']=[]
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.722856879234314})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6202820539474487})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6825620532035828})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6791667938232422})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7268372774124146})
store['active_learning_steps'][107]['training']['best_epoch']=2
store['active_learning_steps'][107]['evaluation_metrics']={'accuracy': 0.9033, 'crossentropy': 0.57030673828125}
store['active_learning_steps'][107]['acquisition']={'indices': [54973, 3671, 43874, 36481, 9892], 'labels': [-1, 6, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][108]['training']={}
store['active_learning_steps'][108]['training']['epochs']=[]
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7323784828186035})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6711583137512207})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6163312196731567})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7009546756744385})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7063955068588257})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.804863452911377})
store['active_learning_steps'][108]['training']['best_epoch']=3
store['active_learning_steps'][108]['evaluation_metrics']={'accuracy': 0.9149, 'crossentropy': 0.549592236328125}
store['active_learning_steps'][108]['acquisition']={'indices': [43143, 5663, 33334, 45342, 9733], 'labels': [7, 7, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][109]['training']={}
store['active_learning_steps'][109]['training']['epochs']=[]
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7515836358070374})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6503781080245972})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6956063508987427})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6871199607849121})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7602159976959229})
store['active_learning_steps'][109]['training']['best_epoch']=2
store['active_learning_steps'][109]['evaluation_metrics']={'accuracy': 0.9028, 'crossentropy': 0.581635546875}
store['active_learning_steps'][109]['acquisition']={'indices': [13752, 41799, 17203, 4680, 52244], 'labels': [9, 1, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][110]['training']={}
store['active_learning_steps'][110]['training']['epochs']=[]
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7188452482223511})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6601063013076782})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6379603147506714})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.671918511390686})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6974742412567139})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.717315673828125})
store['active_learning_steps'][110]['training']['best_epoch']=3
store['active_learning_steps'][110]['evaluation_metrics']={'accuracy': 0.9143, 'crossentropy': 0.54412265625}
store['active_learning_steps'][110]['acquisition']={'indices': [42056, 6571, 1559, 34119, 58255], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][111]['training']={}
store['active_learning_steps'][111]['training']['epochs']=[]
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7673377990722656})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6212891340255737})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6154680848121643})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6730218529701233})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6812283992767334})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6498644948005676})
store['active_learning_steps'][111]['training']['best_epoch']=3
store['active_learning_steps'][111]['evaluation_metrics']={'accuracy': 0.9125, 'crossentropy': 0.556447998046875}
store['active_learning_steps'][111]['acquisition']={'indices': [9613, 6001, 10585, 52645, 32516], 'labels': [9, -1, 3, 6, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][112]['training']={}
store['active_learning_steps'][112]['training']['epochs']=[]
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7283576726913452})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6486072540283203})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6299667358398438})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6871124505996704})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6739286184310913})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6987210512161255})
store['active_learning_steps'][112]['training']['best_epoch']=3
store['active_learning_steps'][112]['evaluation_metrics']={'accuracy': 0.9051, 'crossentropy': 0.570746044921875}
store['active_learning_steps'][112]['acquisition']={'indices': [3274, 43851, 55346, 20779, 13407], 'labels': [-1, 2, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][113]['training']={}
store['active_learning_steps'][113]['training']['epochs']=[]
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7191951274871826})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5885396599769592})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5830944180488586})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5628786087036133})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.7207472920417786})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6100683212280273})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6219318509101868})
store['active_learning_steps'][113]['training']['best_epoch']=4
store['active_learning_steps'][113]['evaluation_metrics']={'accuracy': 0.9232, 'crossentropy': 0.51980751953125}
store['active_learning_steps'][113]['acquisition']={'indices': [50057, 2369, 35857, 24134, 7718], 'labels': [0, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][114]['training']={}
store['active_learning_steps'][114]['training']['epochs']=[]
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7761176228523254})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6183783411979675})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6654759049415588})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6799033880233765})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6545989513397217})
store['active_learning_steps'][114]['training']['best_epoch']=2
store['active_learning_steps'][114]['evaluation_metrics']={'accuracy': 0.9094, 'crossentropy': 0.56590146484375}
store['active_learning_steps'][114]['acquisition']={'indices': [34385, 56886, 22436, 19847, 52372], 'labels': [-1, -1, -1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][115]['training']={}
store['active_learning_steps'][115]['training']['epochs']=[]
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7646050453186035})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6539642810821533})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6402576565742493})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6895557045936584})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6615055799484253})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7007851600646973})
store['active_learning_steps'][115]['training']['best_epoch']=3
store['active_learning_steps'][115]['evaluation_metrics']={'accuracy': 0.9059, 'crossentropy': 0.573064501953125}
store['active_learning_steps'][115]['acquisition']={'indices': [41352, 57284, 16981, 21522, 28746], 'labels': [0, 2, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][116]['training']={}
store['active_learning_steps'][116]['training']['epochs']=[]
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7188988924026489})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5801289081573486})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.649644136428833})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6103978157043457})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6888910531997681})
store['active_learning_steps'][116]['training']['best_epoch']=2
store['active_learning_steps'][116]['evaluation_metrics']={'accuracy': 0.9175, 'crossentropy': 0.521630419921875}
store['active_learning_steps'][116]['acquisition']={'indices': [55043, 13446, 29817, 3762, 19600], 'labels': [-1, -1, -1, 8, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][117]['training']={}
store['active_learning_steps'][117]['training']['epochs']=[]
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7119388580322266})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6190322637557983})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5965713262557983})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5996469259262085})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7408630847930908})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7258539199829102})
store['active_learning_steps'][117]['training']['best_epoch']=3
store['active_learning_steps'][117]['evaluation_metrics']={'accuracy': 0.9216, 'crossentropy': 0.528650146484375}
store['active_learning_steps'][117]['acquisition']={'indices': [30845, 13009, 49788, 54098, 25495], 'labels': [9, 4, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][118]['training']={}
store['active_learning_steps'][118]['training']['epochs']=[]
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6761599779129028})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5885759592056274})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6463111639022827})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.618925154209137})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6568971872329712})
store['active_learning_steps'][118]['training']['best_epoch']=2
store['active_learning_steps'][118]['evaluation_metrics']={'accuracy': 0.9047, 'crossentropy': 0.55083056640625}
store['active_learning_steps'][118]['acquisition']={'indices': [31274, 35383, 48389, 31814, 32011], 'labels': [-1, -1, 4, 4, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][119]['training']={}
store['active_learning_steps'][119]['training']['epochs']=[]
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.8194899559020996})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6005537509918213})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6745916604995728})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.698448657989502})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7061039209365845})
store['active_learning_steps'][119]['training']['best_epoch']=2
store['active_learning_steps'][119]['evaluation_metrics']={'accuracy': 0.9076, 'crossentropy': 0.54613662109375}
store['active_learning_steps'][119]['acquisition']={'indices': [33163, 36666, 58886, 57643, 31782], 'labels': [-1, -1, 1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][120]['training']={}
store['active_learning_steps'][120]['training']['epochs']=[]
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.6918125152587891})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6902403831481934})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5537002086639404})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6600183248519897})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6439929008483887})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.689129114151001})
store['active_learning_steps'][120]['training']['best_epoch']=3
store['active_learning_steps'][120]['evaluation_metrics']={'accuracy': 0.9212, 'crossentropy': 0.498385205078125}
store['active_learning_steps'][120]['acquisition']={'indices': [43624, 41637, 17646, 29502, 17769], 'labels': [0, -1, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][121]['training']={}
store['active_learning_steps'][121]['training']['epochs']=[]
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7522018551826477})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5866619348526001})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6117244958877563})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5771927833557129})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6357132196426392})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6581244468688965})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6684706211090088})
store['active_learning_steps'][121]['training']['best_epoch']=4
store['active_learning_steps'][121]['evaluation_metrics']={'accuracy': 0.922, 'crossentropy': 0.537547705078125}
store['active_learning_steps'][121]['acquisition']={'indices': [57942, 50853, 52305, 35868, 58590], 'labels': [-1, 5, 0, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][122]['training']={}
store['active_learning_steps'][122]['training']['epochs']=[]
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7080857753753662})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6335676312446594})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7190622091293335})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6861644983291626})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7295711040496826})
store['active_learning_steps'][122]['training']['best_epoch']=2
store['active_learning_steps'][122]['evaluation_metrics']={'accuracy': 0.8971, 'crossentropy': 0.564532470703125}
store['active_learning_steps'][122]['acquisition']={'indices': [25523, 27979, 2084, 19093, 18259], 'labels': [-1, -1, 0, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][123]['training']={}
store['active_learning_steps'][123]['training']['epochs']=[]
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6508550047874451})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.611164927482605})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5907570123672485})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5635383725166321})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.636738657951355})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5638493299484253})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6708358526229858})
store['active_learning_steps'][123]['training']['best_epoch']=4
store['active_learning_steps'][123]['evaluation_metrics']={'accuracy': 0.9275, 'crossentropy': 0.492419921875}
store['active_learning_steps'][123]['acquisition']={'indices': [42924, 3389, 37629, 51266, 53803], 'labels': [9, -1, 1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][124]['training']={}
store['active_learning_steps'][124]['training']['epochs']=[]
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7328532934188843})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5909736156463623})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.578031063079834})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6290624141693115})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5990713834762573})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6667688488960266})
store['active_learning_steps'][124]['training']['best_epoch']=3
store['active_learning_steps'][124]['evaluation_metrics']={'accuracy': 0.9212, 'crossentropy': 0.518964404296875}
store['active_learning_steps'][124]['acquisition']={'indices': [42932, 58573, 25254, 36351, 49863], 'labels': [1, 8, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][125]['training']={}
store['active_learning_steps'][125]['training']['epochs']=[]
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7235807180404663})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5855597853660583})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6116775870323181})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6783519387245178})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6357940435409546})
store['active_learning_steps'][125]['training']['best_epoch']=2
store['active_learning_steps'][125]['evaluation_metrics']={'accuracy': 0.9105, 'crossentropy': 0.535588330078125}
store['active_learning_steps'][125]['acquisition']={'indices': [21489, 2179, 30657, 53074, 25483], 'labels': [5, 3, 7, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][126]['training']={}
store['active_learning_steps'][126]['training']['epochs']=[]
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7407026290893555})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6337633728981018})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6365025043487549})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6634232997894287})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.657018780708313})
store['active_learning_steps'][126]['training']['best_epoch']=2
store['active_learning_steps'][126]['evaluation_metrics']={'accuracy': 0.9068, 'crossentropy': 0.578809423828125}
store['active_learning_steps'][126]['acquisition']={'indices': [41772, 45414, 11773, 37838, 7320], 'labels': [5, -1, 9, 2, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][127]['training']={}
store['active_learning_steps'][127]['training']['epochs']=[]
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7043106555938721})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5943527817726135})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.597257137298584})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5794968605041504})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5916473269462585})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6053248643875122})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6679912805557251})
store['active_learning_steps'][127]['training']['best_epoch']=4
store['active_learning_steps'][127]['evaluation_metrics']={'accuracy': 0.9273, 'crossentropy': 0.515588330078125}
store['active_learning_steps'][127]['acquisition']={'indices': [1093, 8944, 5965, 27186, 35104], 'labels': [-1, 4, 2, 2, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][128]['training']={}
store['active_learning_steps'][128]['training']['epochs']=[]
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7486562728881836})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6437196731567383})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.57558274269104})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6004412770271301})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5861378908157349})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.64104163646698})
store['active_learning_steps'][128]['training']['best_epoch']=3
store['active_learning_steps'][128]['evaluation_metrics']={'accuracy': 0.9215, 'crossentropy': 0.51331806640625}
store['active_learning_steps'][128]['acquisition']={'indices': [13092, 51156, 55268, 8376, 45942], 'labels': [5, -1, 8, 6, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][129]['training']={}
store['active_learning_steps'][129]['training']['epochs']=[]
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7055631279945374})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6109955310821533})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5364833474159241})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5674169659614563})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6211180686950684})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6383237838745117})
store['active_learning_steps'][129]['training']['best_epoch']=3
store['active_learning_steps'][129]['evaluation_metrics']={'accuracy': 0.9255, 'crossentropy': 0.480173779296875}
store['active_learning_steps'][129]['acquisition']={'indices': [48974, 39529, 20215, 22680, 19611], 'labels': [3, -1, -1, 5, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][130]['training']={}
store['active_learning_steps'][130]['training']['epochs']=[]
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7368274927139282})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.655714750289917})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6206332445144653})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.602908730506897})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6338585615158081})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6299271583557129})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.7093369364738464})
store['active_learning_steps'][130]['training']['best_epoch']=4
store['active_learning_steps'][130]['evaluation_metrics']={'accuracy': 0.9223, 'crossentropy': 0.513633935546875}
store['active_learning_steps'][130]['acquisition']={'indices': [9421, 25361, 32518, 29774, 56135], 'labels': [6, -1, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][131]['training']={}
store['active_learning_steps'][131]['training']['epochs']=[]
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.6780246496200562})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5797727108001709})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5540292263031006})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6368545889854431})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5822819471359253})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6289975047111511})
store['active_learning_steps'][131]['training']['best_epoch']=3
store['active_learning_steps'][131]['evaluation_metrics']={'accuracy': 0.9251, 'crossentropy': 0.504461865234375}
store['active_learning_steps'][131]['acquisition']={'indices': [29592, 39588, 40862, 45649, 22742], 'labels': [-1, -1, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][132]['training']={}
store['active_learning_steps'][132]['training']['epochs']=[]
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.6728876233100891})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5231449007987976})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5937727093696594})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6721119284629822})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6173311471939087})
store['active_learning_steps'][132]['training']['best_epoch']=2
store['active_learning_steps'][132]['evaluation_metrics']={'accuracy': 0.92, 'crossentropy': 0.469515966796875}
store['active_learning_steps'][132]['acquisition']={'indices': [28688, 1143, 54676, 30963, 12795], 'labels': [7, 2, -1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][133]['training']={}
store['active_learning_steps'][133]['training']['epochs']=[]
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7103819847106934})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5896080732345581})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5661876201629639})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6217620372772217})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.594272255897522})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6368799209594727})
store['active_learning_steps'][133]['training']['best_epoch']=3
store['active_learning_steps'][133]['evaluation_metrics']={'accuracy': 0.9196, 'crossentropy': 0.502854833984375}
store['active_learning_steps'][133]['acquisition']={'indices': [3344, 19709, 9005, 18798, 58958], 'labels': [1, 0, 0, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][134]['training']={}
store['active_learning_steps'][134]['training']['epochs']=[]
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6918817758560181})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5342137217521667})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5302249193191528})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5884673595428467})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6167831420898438})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6172040700912476})
store['active_learning_steps'][134]['training']['best_epoch']=3
store['active_learning_steps'][134]['evaluation_metrics']={'accuracy': 0.9306, 'crossentropy': 0.47568779296875}
store['active_learning_steps'][134]['acquisition']={'indices': [1456, 19685, 26272, 38272, 91], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][135]['training']={}
store['active_learning_steps'][135]['training']['epochs']=[]
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.708082914352417})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5647450089454651})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5899726748466492})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6216858625411987})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6307098865509033})
store['active_learning_steps'][135]['training']['best_epoch']=2
store['active_learning_steps'][135]['evaluation_metrics']={'accuracy': 0.9112, 'crossentropy': 0.49356025390625}
store['active_learning_steps'][135]['acquisition']={'indices': [4790, 58585, 47143, 29062, 12741], 'labels': [1, -1, -1, 1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][136]['training']={}
store['active_learning_steps'][136]['training']['epochs']=[]
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.755177915096283})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5591848492622375})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6067217588424683})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6449397206306458})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6046912670135498})
store['active_learning_steps'][136]['training']['best_epoch']=2
store['active_learning_steps'][136]['evaluation_metrics']={'accuracy': 0.9088, 'crossentropy': 0.51725517578125}
store['active_learning_steps'][136]['acquisition']={'indices': [6012, 47290, 22825, 972, 27642], 'labels': [2, -1, 3, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][137]['training']={}
store['active_learning_steps'][137]['training']['epochs']=[]
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6990929841995239})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5324221253395081})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5230463147163391})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5904737114906311})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6515972018241882})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6984490752220154})
store['active_learning_steps'][137]['training']['best_epoch']=3
store['active_learning_steps'][137]['evaluation_metrics']={'accuracy': 0.9239, 'crossentropy': 0.4889515625}
store['active_learning_steps'][137]['acquisition']={'indices': [7881, 30334, 48423, 18247, 12404], 'labels': [3, -1, 2, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][138]['training']={}
store['active_learning_steps'][138]['training']['epochs']=[]
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6264692544937134})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4848215579986572})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5110592246055603})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5375804901123047})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5340354442596436})
store['active_learning_steps'][138]['training']['best_epoch']=2
store['active_learning_steps'][138]['evaluation_metrics']={'accuracy': 0.9232, 'crossentropy': 0.4711341796875}
store['active_learning_steps'][138]['acquisition']={'indices': [21922, 19666, 55498, 13349, 58986], 'labels': [-1, 4, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][139]['training']={}
store['active_learning_steps'][139]['training']['epochs']=[]
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6990521550178528})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5614750981330872})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.623070478439331})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5676904916763306})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5801470279693604})
store['active_learning_steps'][139]['training']['best_epoch']=2
store['active_learning_steps'][139]['evaluation_metrics']={'accuracy': 0.9074, 'crossentropy': 0.533994287109375}
store['active_learning_steps'][139]['acquisition']={'indices': [20584, 35379, 40748, 58373, 32542], 'labels': [0, 3, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][140]['training']={}
store['active_learning_steps'][140]['training']['epochs']=[]
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6963645219802856})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6069894433021545})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5597270727157593})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6210854053497314})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6128548383712769})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6376001834869385})
store['active_learning_steps'][140]['training']['best_epoch']=3
store['active_learning_steps'][140]['evaluation_metrics']={'accuracy': 0.923, 'crossentropy': 0.4963044921875}
store['active_learning_steps'][140]['acquisition']={'indices': [45201, 50713, 37102, 48396, 16440], 'labels': [9, -1, -1, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][141]['training']={}
store['active_learning_steps'][141]['training']['epochs']=[]
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6481096148490906})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6255444884300232})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.54847252368927})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6434364318847656})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5781365036964417})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5702968239784241})
store['active_learning_steps'][141]['training']['best_epoch']=3
store['active_learning_steps'][141]['evaluation_metrics']={'accuracy': 0.9208, 'crossentropy': 0.488585302734375}
store['active_learning_steps'][141]['acquisition']={'indices': [36656, 27452, 27215, 6479, 14639], 'labels': [8, -1, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][142]['training']={}
store['active_learning_steps'][142]['training']['epochs']=[]
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.690575897693634})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6479687690734863})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6349274516105652})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6039141416549683})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.749833345413208})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6232245564460754})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6242924928665161})
store['active_learning_steps'][142]['training']['best_epoch']=4
store['active_learning_steps'][142]['evaluation_metrics']={'accuracy': 0.9193, 'crossentropy': 0.490788232421875}
store['active_learning_steps'][142]['acquisition']={'indices': [13363, 5120, 23477, 12526, 57066], 'labels': [4, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][143]['training']={}
store['active_learning_steps'][143]['training']['epochs']=[]
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7418054342269897})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5590970516204834})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6500760316848755})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6327074766159058})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6230440139770508})
store['active_learning_steps'][143]['training']['best_epoch']=2
store['active_learning_steps'][143]['evaluation_metrics']={'accuracy': 0.9117, 'crossentropy': 0.50123681640625}
store['active_learning_steps'][143]['acquisition']={'indices': [28267, 10809, 16593, 7786, 43944], 'labels': [5, -1, -1, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][144]['training']={}
store['active_learning_steps'][144]['training']['epochs']=[]
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6922532320022583})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5724309682846069})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5345815420150757})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5819641947746277})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.59193354845047})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6515383720397949})
store['active_learning_steps'][144]['training']['best_epoch']=3
store['active_learning_steps'][144]['evaluation_metrics']={'accuracy': 0.9273, 'crossentropy': 0.466291015625}
store['active_learning_steps'][144]['acquisition']={'indices': [20410, 58013, 57100, 13631, 24415], 'labels': [-1, -1, 9, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][145]['training']={}
store['active_learning_steps'][145]['training']['epochs']=[]
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7585644125938416})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.60390704870224})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6086202263832092})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6044261455535889})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6308450102806091})
store['active_learning_steps'][145]['training']['best_epoch']=2
store['active_learning_steps'][145]['evaluation_metrics']={'accuracy': 0.914, 'crossentropy': 0.51170107421875}
store['active_learning_steps'][145]['acquisition']={'indices': [1595, 32362, 28585, 11646, 52283], 'labels': [-1, 5, 6, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][146]['training']={}
store['active_learning_steps'][146]['training']['epochs']=[]
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7114197611808777})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5872027277946472})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5928070545196533})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5633623600006104})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5912253856658936})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5857491493225098})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.573609471321106})
store['active_learning_steps'][146]['training']['best_epoch']=4
store['active_learning_steps'][146]['evaluation_metrics']={'accuracy': 0.9221, 'crossentropy': 0.4872603515625}
store['active_learning_steps'][146]['acquisition']={'indices': [20265, 47227, 17676, 29656, 47248], 'labels': [-1, 9, 3, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][147]['training']={}
store['active_learning_steps'][147]['training']['epochs']=[]
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7590914368629456})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6685276031494141})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6190453171730042})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6235771775245667})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7297071218490601})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7664897441864014})
store['active_learning_steps'][147]['training']['best_epoch']=3
store['active_learning_steps'][147]['evaluation_metrics']={'accuracy': 0.9193, 'crossentropy': 0.503790478515625}
store['active_learning_steps'][147]['acquisition']={'indices': [15848, 6019, 57338, 33867, 26743], 'labels': [3, -1, 2, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][148]['training']={}
store['active_learning_steps'][148]['training']['epochs']=[]
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.791382908821106})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.579126238822937})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6438816785812378})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6351525187492371})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.642026960849762})
store['active_learning_steps'][148]['training']['best_epoch']=2
store['active_learning_steps'][148]['evaluation_metrics']={'accuracy': 0.9124, 'crossentropy': 0.51932919921875}
store['active_learning_steps'][148]['acquisition']={'indices': [32973, 9205, 30239, 26573, 3880], 'labels': [-1, 5, -1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][149]['training']={}
store['active_learning_steps'][149]['training']['epochs']=[]
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7109750509262085})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5528762340545654})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5567020177841187})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5935251116752625})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6197659969329834})
store['active_learning_steps'][149]['training']['best_epoch']=2
store['active_learning_steps'][149]['evaluation_metrics']={'accuracy': 0.9177, 'crossentropy': 0.487284326171875}
store['active_learning_steps'][149]['acquisition']={'indices': [21310, 22714, 42184, 26207, 34942], 'labels': [8, 4, 1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][150]['training']={}
store['active_learning_steps'][150]['training']['epochs']=[]
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7239073514938354})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5832176208496094})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5915595889091492})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6151328682899475})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6418927907943726})
store['active_learning_steps'][150]['training']['best_epoch']=2
store['active_learning_steps'][150]['evaluation_metrics']={'accuracy': 0.9127, 'crossentropy': 0.49051162109375}
store['active_learning_steps'][150]['acquisition']={'indices': [11603, 3227, 23197, 9422, 39720], 'labels': [9, 9, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][151]['training']={}
store['active_learning_steps'][151]['training']['epochs']=[]
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7964894771575928})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5696549415588379})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6488954424858093})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5950003862380981})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6120748519897461})
store['active_learning_steps'][151]['training']['best_epoch']=2
store['active_learning_steps'][151]['evaluation_metrics']={'accuracy': 0.9103, 'crossentropy': 0.5425287109375}
store['active_learning_steps'][151]['acquisition']={'indices': [11839, 46126, 54804, 27113, 22851], 'labels': [-1, -1, -1, 2, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][152]['training']={}
store['active_learning_steps'][152]['training']['epochs']=[]
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7074207067489624})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.575849711894989})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6026848554611206})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5739198923110962})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6082188487052917})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6314828991889954})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.604473888874054})
store['active_learning_steps'][152]['training']['best_epoch']=4
store['active_learning_steps'][152]['evaluation_metrics']={'accuracy': 0.9251, 'crossentropy': 0.4930826171875}
store['active_learning_steps'][152]['acquisition']={'indices': [20259, 5458, 17519, 58483, 10801], 'labels': [-1, 3, 0, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][153]['training']={}
store['active_learning_steps'][153]['training']['epochs']=[]
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7146497964859009})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5623447895050049})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5554394125938416})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5514074563980103})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6544121503829956})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6235196590423584})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7116638422012329})
store['active_learning_steps'][153]['training']['best_epoch']=4
store['active_learning_steps'][153]['evaluation_metrics']={'accuracy': 0.9292, 'crossentropy': 0.49247314453125}
store['active_learning_steps'][153]['acquisition']={'indices': [15761, 49004, 39288, 579, 3062], 'labels': [0, 6, -1, 5, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][154]['training']={}
store['active_learning_steps'][154]['training']['epochs']=[]
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7093355655670166})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6202659606933594})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5784428119659424})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.547714352607727})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5666353702545166})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6840993165969849})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6190944910049438})
store['active_learning_steps'][154]['training']['best_epoch']=4
store['active_learning_steps'][154]['evaluation_metrics']={'accuracy': 0.9274, 'crossentropy': 0.465157373046875}
store['active_learning_steps'][154]['acquisition']={'indices': [7280, 41050, 34299, 59658, 13765], 'labels': [4, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][155]['training']={}
store['active_learning_steps'][155]['training']['epochs']=[]
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7216376066207886})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6255261898040771})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5894410014152527})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6627618074417114})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6336223483085632})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6653681993484497})
store['active_learning_steps'][155]['training']['best_epoch']=3
store['active_learning_steps'][155]['evaluation_metrics']={'accuracy': 0.9202, 'crossentropy': 0.501493212890625}
store['active_learning_steps'][155]['acquisition']={'indices': [55500, 5623, 52966, 11427, 4578], 'labels': [-1, -1, 3, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][156]['training']={}
store['active_learning_steps'][156]['training']['epochs']=[]
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.6959218978881836})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5538557767868042})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5747107267379761})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5649500489234924})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5954570174217224})
store['active_learning_steps'][156]['training']['best_epoch']=2
store['active_learning_steps'][156]['evaluation_metrics']={'accuracy': 0.9108, 'crossentropy': 0.48468447265625}
store['active_learning_steps'][156]['acquisition']={'indices': [23921, 38446, 18200, 48540, 45127], 'labels': [-1, 0, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][157]['training']={}
store['active_learning_steps'][157]['training']['epochs']=[]
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6462643146514893})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5964683294296265})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5189369916915894})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5458731055259705})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5073251724243164})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6383858323097229})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6088436841964722})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6471609473228455})
store['active_learning_steps'][157]['training']['best_epoch']=5
store['active_learning_steps'][157]['evaluation_metrics']={'accuracy': 0.9299, 'crossentropy': 0.4615537109375}
store['active_learning_steps'][157]['acquisition']={'indices': [47640, 9068, 45945, 34670, 3989], 'labels': [7, 6, 3, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][158]['training']={}
store['active_learning_steps'][158]['training']['epochs']=[]
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.6742314696311951})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5861225128173828})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5690956115722656})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6397982835769653})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6612162590026855})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5958126187324524})
store['active_learning_steps'][158]['training']['best_epoch']=3
store['active_learning_steps'][158]['evaluation_metrics']={'accuracy': 0.9214, 'crossentropy': 0.483335009765625}
store['active_learning_steps'][158]['acquisition']={'indices': [42267, 48698, 9630, 34001, 45627], 'labels': [5, 2, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][159]['training']={}
store['active_learning_steps'][159]['training']['epochs']=[]
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.6923254728317261})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5603646636009216})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5674939155578613})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6086035966873169})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5661274194717407})
store['active_learning_steps'][159]['training']['best_epoch']=2
store['active_learning_steps'][159]['evaluation_metrics']={'accuracy': 0.9157, 'crossentropy': 0.487015966796875}
store['active_learning_steps'][159]['acquisition']={'indices': [24550, 3125, 38268, 37493, 32174], 'labels': [-1, -1, -1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][160]['training']={}
store['active_learning_steps'][160]['training']['epochs']=[]
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6809356212615967})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6400963068008423})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6591353416442871})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5604884624481201})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6044187545776367})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6625033617019653})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7365709543228149})
store['active_learning_steps'][160]['training']['best_epoch']=4
store['active_learning_steps'][160]['evaluation_metrics']={'accuracy': 0.9298, 'crossentropy': 0.430961572265625}
store['active_learning_steps'][160]['acquisition']={'indices': [12889, 32486, 40840, 54775, 31146], 'labels': [9, -1, 5, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][161]['training']={}
store['active_learning_steps'][161]['training']['epochs']=[]
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.6598083972930908})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.616039514541626})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5892580151557922})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5532602071762085})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6522700190544128})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6911036968231201})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.7181190252304077})
store['active_learning_steps'][161]['training']['best_epoch']=4
store['active_learning_steps'][161]['evaluation_metrics']={'accuracy': 0.9301, 'crossentropy': 0.458335498046875}
store['active_learning_steps'][161]['acquisition']={'indices': [14853, 40082, 22981, 25806, 4382], 'labels': [-1, -1, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][162]['training']={}
store['active_learning_steps'][162]['training']['epochs']=[]
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7180920839309692})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5329093337059021})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5580248832702637})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5471466183662415})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5828251838684082})
store['active_learning_steps'][162]['training']['best_epoch']=2
store['active_learning_steps'][162]['evaluation_metrics']={'accuracy': 0.9275, 'crossentropy': 0.46748447265625}
store['active_learning_steps'][162]['acquisition']={'indices': [38846, 48320, 22921, 12276, 16859], 'labels': [-1, 2, 7, 0, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][163]['training']={}
store['active_learning_steps'][163]['training']['epochs']=[]
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7269425988197327})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5175303220748901})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5676187872886658})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5857089161872864})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5821083188056946})
store['active_learning_steps'][163]['training']['best_epoch']=2
store['active_learning_steps'][163]['evaluation_metrics']={'accuracy': 0.9188, 'crossentropy': 0.465678466796875}
store['active_learning_steps'][163]['acquisition']={'indices': [5203, 59744, 19478, 18236, 51372], 'labels': [-1, 6, 4, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][164]['training']={}
store['active_learning_steps'][164]['training']['epochs']=[]
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6519548892974854})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5680468082427979})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5772264003753662})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5705418586730957})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5877922773361206})
store['active_learning_steps'][164]['training']['best_epoch']=2
store['active_learning_steps'][164]['evaluation_metrics']={'accuracy': 0.9135, 'crossentropy': 0.492485498046875}
store['active_learning_steps'][164]['acquisition']={'indices': [3262, 2370, 44561, 55373, 25398], 'labels': [-1, -1, 1, 2, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][165]['training']={}
store['active_learning_steps'][165]['training']['epochs']=[]
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.703363299369812})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6184180974960327})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5587348937988281})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5585229396820068})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5554945468902588})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5854132175445557})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6636905670166016})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6169999837875366})
store['active_learning_steps'][165]['training']['best_epoch']=5
store['active_learning_steps'][165]['evaluation_metrics']={'accuracy': 0.9288, 'crossentropy': 0.45638095703125}
store['active_learning_steps'][165]['acquisition']={'indices': [44236, 19579, 31112, 36677, 52663], 'labels': [9, 3, 0, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][166]['training']={}
store['active_learning_steps'][166]['training']['epochs']=[]
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7758800983428955})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6764246225357056})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5751174688339233})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5751034617424011})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6019467115402222})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6019769906997681})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6412402391433716})
store['active_learning_steps'][166]['training']['best_epoch']=4
store['active_learning_steps'][166]['evaluation_metrics']={'accuracy': 0.9264, 'crossentropy': 0.45165478515625}
store['active_learning_steps'][166]['acquisition']={'indices': [3059, 49453, 36926, 42487, 23791], 'labels': [7, 8, 7, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][167]['training']={}
store['active_learning_steps'][167]['training']['epochs']=[]
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6887255907058716})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5698843002319336})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5201446413993835})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5722734928131104})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.595375657081604})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5617607831954956})
store['active_learning_steps'][167]['training']['best_epoch']=3
store['active_learning_steps'][167]['evaluation_metrics']={'accuracy': 0.9269, 'crossentropy': 0.462477001953125}
store['active_learning_steps'][167]['acquisition']={'indices': [5334, 41800, 13435, 50116, 9721], 'labels': [6, -1, 9, 8, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][168]['training']={}
store['active_learning_steps'][168]['training']['epochs']=[]
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.6977083683013916})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5320247411727905})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5337299704551697})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.480053186416626})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5424814224243164})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6436135172843933})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6203295588493347})
store['active_learning_steps'][168]['training']['best_epoch']=4
store['active_learning_steps'][168]['evaluation_metrics']={'accuracy': 0.9306, 'crossentropy': 0.444482861328125}
store['active_learning_steps'][168]['acquisition']={'indices': [35693, 53015, 58512, 35985, 48061], 'labels': [-1, 5, 2, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][169]['training']={}
store['active_learning_steps'][169]['training']['epochs']=[]
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.6824830174446106})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6160093545913696})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5636583566665649})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5412967801094055})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.622650682926178})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5737613439559937})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5653432011604309})
store['active_learning_steps'][169]['training']['best_epoch']=4
store['active_learning_steps'][169]['evaluation_metrics']={'accuracy': 0.9294, 'crossentropy': 0.4406078125}
store['active_learning_steps'][169]['acquisition']={'indices': [10228, 771, 50019, 53149, 16145], 'labels': [-1, -1, 5, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][170]['training']={}
store['active_learning_steps'][170]['training']['epochs']=[]
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6610046625137329})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5664428472518921})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5362106561660767})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5190542936325073})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.547873854637146})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6012176275253296})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5957513451576233})
store['active_learning_steps'][170]['training']['best_epoch']=4
store['active_learning_steps'][170]['evaluation_metrics']={'accuracy': 0.9314, 'crossentropy': 0.428907177734375}
store['active_learning_steps'][170]['acquisition']={'indices': [23667, 42757, 18234, 18875, 24648], 'labels': [-1, -1, -1, 5, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][171]['training']={}
store['active_learning_steps'][171]['training']['epochs']=[]
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.6919556856155396})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5590664148330688})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5683512687683105})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6562665700912476})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6388481855392456})
store['active_learning_steps'][171]['training']['best_epoch']=2
store['active_learning_steps'][171]['evaluation_metrics']={'accuracy': 0.9074, 'crossentropy': 0.499664208984375}
store['active_learning_steps'][171]['acquisition']={'indices': [55270, 16564, 37958, 18842, 37856], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][172]['training']={}
store['active_learning_steps'][172]['training']['epochs']=[]
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6332826614379883})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5328941941261292})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5593863725662231})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.48460161685943604})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5159178972244263})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5350890159606934})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5118787288665771})
store['active_learning_steps'][172]['training']['best_epoch']=4
store['active_learning_steps'][172]['evaluation_metrics']={'accuracy': 0.9377, 'crossentropy': 0.420798095703125}
store['active_learning_steps'][172]['acquisition']={'indices': [4652, 39874, 17476, 53530, 12442], 'labels': [8, 0, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][173]['training']={}
store['active_learning_steps'][173]['training']['epochs']=[]
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6574474573135376})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.60957932472229})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6010098457336426})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5849002003669739})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6333626508712769})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6221026182174683})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5610613822937012})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.7281016111373901})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6473851799964905})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6464192867279053})
store['active_learning_steps'][173]['training']['best_epoch']=7
store['active_learning_steps'][173]['evaluation_metrics']={'accuracy': 0.9312, 'crossentropy': 0.4816591796875}
store['active_learning_steps'][173]['acquisition']={'indices': [50854, 40955, 43863, 28135, 26661], 'labels': [9, 4, 9, 2, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][174]['training']={}
store['active_learning_steps'][174]['training']['epochs']=[]
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6742087006568909})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5364865064620972})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.49309784173965454})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.513317346572876})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5372769236564636})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5477598309516907})
store['active_learning_steps'][174]['training']['best_epoch']=3
store['active_learning_steps'][174]['evaluation_metrics']={'accuracy': 0.9241, 'crossentropy': 0.450379296875}
store['active_learning_steps'][174]['acquisition']={'indices': [30715, 23603, 43261, 17917, 25929], 'labels': [-1, 7, 1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][175]['training']={}
store['active_learning_steps'][175]['training']['epochs']=[]
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7362157106399536})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6021003127098083})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5045856237411499})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4868427813053131})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5440160036087036})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5826176404953003})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5173469185829163})
store['active_learning_steps'][175]['training']['best_epoch']=4
store['active_learning_steps'][175]['evaluation_metrics']={'accuracy': 0.9326, 'crossentropy': 0.4237865234375}
store['active_learning_steps'][175]['acquisition']={'indices': [55231, 57644, 24409, 24408, 40135], 'labels': [-1, 1, 7, 5, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][176]['training']={}
store['active_learning_steps'][176]['training']['epochs']=[]
store['active_learning_steps'][176]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6912278532981873})
store['active_learning_steps'][176]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6178537607192993})
store['active_learning_steps'][176]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5624858140945435})
store['active_learning_steps'][176]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5595031976699829})
store['active_learning_steps'][176]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5827499628067017})
store['active_learning_steps'][176]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5849090814590454})
store['active_learning_steps'][176]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5940800309181213})
store['active_learning_steps'][176]['training']['best_epoch']=4
store['active_learning_steps'][176]['evaluation_metrics']={'accuracy': 0.9225, 'crossentropy': 0.4864791015625}
store['active_learning_steps'][176]['acquisition']={'indices': [56451, 51790, 44259, 48272, 43996], 'labels': [7, 3, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][177]['training']={}
store['active_learning_steps'][177]['training']['epochs']=[]
store['active_learning_steps'][177]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7075817584991455})
store['active_learning_steps'][177]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5765141248703003})
store['active_learning_steps'][177]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5672748684883118})
store['active_learning_steps'][177]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5452194213867188})
store['active_learning_steps'][177]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5418843030929565})
store['active_learning_steps'][177]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5771746039390564})
store['active_learning_steps'][177]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.608671247959137})
store['active_learning_steps'][177]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6637592315673828})
store['active_learning_steps'][177]['training']['best_epoch']=5
store['active_learning_steps'][177]['evaluation_metrics']={'accuracy': 0.9247, 'crossentropy': 0.47258759765625}
store['active_learning_steps'][177]['acquisition']={'indices': [55650, 18451, 54650, 34820, 26802], 'labels': [-1, 1, 4, 8, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][178]['training']={}
store['active_learning_steps'][178]['training']['epochs']=[]
store['active_learning_steps'][178]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6716854572296143})
store['active_learning_steps'][178]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5440261363983154})
store['active_learning_steps'][178]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4713943600654602})
store['active_learning_steps'][178]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5547016263008118})
store['active_learning_steps'][178]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5186585187911987})
store['active_learning_steps'][178]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5565053224563599})
store['active_learning_steps'][178]['training']['best_epoch']=3
store['active_learning_steps'][178]['evaluation_metrics']={'accuracy': 0.9288, 'crossentropy': 0.4577173828125}
