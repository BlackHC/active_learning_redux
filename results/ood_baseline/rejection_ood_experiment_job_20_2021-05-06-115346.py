store = {}
store['timestamp']=1620298426
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=20']
store['commit']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['github_url']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=20
store['worker_id']=20
store['num_workers']=40
store['config']={'seed': 20, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 20, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.Random', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.356658458709717})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.65586519241333})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.6641464233398438})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 3.126467704772949})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6829, 'crossentropy': 2.0237904296875}
store['active_learning_steps'][0]['acquisition']={'indices': [23340, 34873, 17271, 46832, 50355], 'labels': [-1, 3, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.0872840881347656})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.624028444290161})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.935842990875244})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.854290008544922})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6804, 'crossentropy': 2.0226126953125}
store['active_learning_steps'][1]['acquisition']={'indices': [8914, 57817, 54683, 45480, 39636], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.9952051639556885})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.2613353729248047})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.7760512828826904})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.7819690704345703})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7119, 'crossentropy': 1.9240890625}
store['active_learning_steps'][2]['acquisition']={'indices': [41229, 26371, 12134, 36888, 49588], 'labels': [3, 0, -1, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.345069408416748})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.7292723655700684})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.96877384185791})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.9408974647521973})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6997, 'crossentropy': 2.0716046875}
store['active_learning_steps'][3]['acquisition']={'indices': [29282, 14076, 47418, 58671, 24661], 'labels': [7, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.2144503593444824})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.225994110107422})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.570316791534424})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.7777609825134277})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.6848, 'crossentropy': 2.0051703125}
store['active_learning_steps'][4]['acquisition']={'indices': [46573, 57351, 9815, 50692, 13784], 'labels': [-1, -1, 1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.9681429862976074})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.6539759635925293})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.5651965141296387})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.6992435455322266})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7231, 'crossentropy': 1.8255646484375}
store['active_learning_steps'][5]['acquisition']={'indices': [36236, 30593, 39739, 32534, 50319], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 2.041563034057617})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.4742136001586914})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.3116044998168945})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 3.1629700660705566})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7314, 'crossentropy': 1.818528515625}
store['active_learning_steps'][6]['acquisition']={'indices': [30666, 30449, 30578, 35892, 47460], 'labels': [4, 7, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.052323341369629})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.434117317199707})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.6373815536499023})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.756103515625})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7241, 'crossentropy': 1.89940078125}
store['active_learning_steps'][7]['acquisition']={'indices': [7008, 28212, 42693, 12094, 52896], 'labels': [-1, 2, 2, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.7647264003753662})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.966078519821167})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 2.1157093048095703})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.8033032417297363})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.7292, 'crossentropy': 1.6797998046875}
store['active_learning_steps'][8]['acquisition']={'indices': [56443, 59346, 47880, 51023, 3827], 'labels': [9, -1, 1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.5563902854919434})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.1490559577941895})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.526585817337036})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 2.2994580268859863})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.7444, 'crossentropy': 1.5842798828125}
store['active_learning_steps'][9]['acquisition']={'indices': [16106, 10782, 38312, 52954, 42058], 'labels': [-1, -1, 9, 8, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.878098964691162})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.0371739864349365})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.419179916381836})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.4416894912719727})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.7303, 'crossentropy': 1.6926234375}
store['active_learning_steps'][10]['acquisition']={'indices': [50389, 56000, 31951, 30053, 31625], 'labels': [-1, -1, -1, 1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.4809578657150269})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.9511516094207764})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 2.0772502422332764})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 2.328753709793091})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.7543, 'crossentropy': 1.45408037109375}
store['active_learning_steps'][11]['acquisition']={'indices': [27640, 18449, 9773, 57645, 3278], 'labels': [-1, 7, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.625757098197937})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 2.231457471847534})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.967785120010376})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 2.154597520828247})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.7564, 'crossentropy': 1.5162939453125}
store['active_learning_steps'][12]['acquisition']={'indices': [28824, 34557, 25751, 28968, 9037], 'labels': [0, -1, -1, 0, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.519347071647644})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.036320686340332})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 2.0447797775268555})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 2.3854317665100098})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.7502, 'crossentropy': 1.45187685546875}
store['active_learning_steps'][13]['acquisition']={'indices': [9752, 3055, 46453, 1638, 5510], 'labels': [9, -1, 5, 5, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.1203895807266235})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.6813995838165283})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.7578259706497192})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 2.045175075531006})
store['active_learning_steps'][14]['training']['best_epoch']=1
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.7989, 'crossentropy': 1.12203564453125}
store['active_learning_steps'][14]['acquisition']={'indices': [43822, 25416, 32092, 50203, 14650], 'labels': [6, -1, 0, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.5206074714660645})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.7218542098999023})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 2.018548011779785})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.8939704895019531})
store['active_learning_steps'][15]['training']['best_epoch']=1
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.7665, 'crossentropy': 1.33323515625}
store['active_learning_steps'][15]['acquisition']={'indices': [21119, 46147, 52683, 28926, 48283], 'labels': [4, -1, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.202130913734436})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.4450883865356445})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.4895957708358765})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.525719404220581})
store['active_learning_steps'][16]['training']['best_epoch']=1
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8138, 'crossentropy': 1.06209345703125}
store['active_learning_steps'][16]['acquisition']={'indices': [9071, 27133, 35032, 27285, 54029], 'labels': [-1, 3, -1, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.3551056385040283})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.433021903038025})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.546267032623291})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.5884861946105957})
store['active_learning_steps'][17]['training']['best_epoch']=1
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.7883, 'crossentropy': 1.23470498046875}
store['active_learning_steps'][17]['acquisition']={'indices': [10392, 9056, 58126, 32448, 6945], 'labels': [7, -1, 2, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.0621453523635864})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.3907380104064941})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.3888272047042847})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.4703019857406616})
store['active_learning_steps'][18]['training']['best_epoch']=1
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8249, 'crossentropy': 0.96443212890625}
store['active_learning_steps'][18]['acquisition']={'indices': [55742, 46322, 29298, 19586, 30088], 'labels': [6, 5, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.2558352947235107})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.4444929361343384})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.4795405864715576})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.5523396730422974})
store['active_learning_steps'][19]['training']['best_epoch']=1
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8086, 'crossentropy': 1.11533447265625}
store['active_learning_steps'][19]['acquisition']={'indices': [56265, 36416, 8291, 43004, 46511], 'labels': [3, 6, -1, 8, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.1084824800491333})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.2714015245437622})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.5056045055389404})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.3908021450042725})
store['active_learning_steps'][20]['training']['best_epoch']=1
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8263, 'crossentropy': 0.97891357421875}
store['active_learning_steps'][20]['acquisition']={'indices': [8781, 16429, 46190, 44451, 5907], 'labels': [-1, -1, -1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.1124142408370972})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.2758431434631348})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.5368216037750244})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.540603756904602})
store['active_learning_steps'][21]['training']['best_epoch']=1
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.8194, 'crossentropy': 1.03139384765625}
store['active_learning_steps'][21]['acquisition']={'indices': [8032, 1772, 36904, 21869, 14403], 'labels': [1, -1, 2, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.2812319993972778})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.3961721658706665})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.5741331577301025})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.717817783355713})
store['active_learning_steps'][22]['training']['best_epoch']=1
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.8036, 'crossentropy': 1.1612318359375}
store['active_learning_steps'][22]['acquisition']={'indices': [44971, 18581, 56509, 23592, 4577], 'labels': [7, 0, -1, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.0729243755340576})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.2054173946380615})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.3128255605697632})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.5972014665603638})
store['active_learning_steps'][23]['training']['best_epoch']=1
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.8178, 'crossentropy': 0.9792203125}
store['active_learning_steps'][23]['acquisition']={'indices': [7035, 49782, 54109, 38880, 31094], 'labels': [8, 2, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.073965311050415})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.1908056735992432})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.5238163471221924})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.4984396696090698})
store['active_learning_steps'][24]['training']['best_epoch']=1
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.8203, 'crossentropy': 1.011384765625}
store['active_learning_steps'][24]['acquisition']={'indices': [14628, 42343, 4755, 10789, 45913], 'labels': [5, 3, -1, 4, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.9757440090179443})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.2988862991333008})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.2657499313354492})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.2793173789978027})
store['active_learning_steps'][25]['training']['best_epoch']=1
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.8379, 'crossentropy': 0.89425390625}
store['active_learning_steps'][25]['acquisition']={'indices': [22828, 50661, 34343, 40938, 44073], 'labels': [-1, -1, 6, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.0741984844207764})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.1848828792572021})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.2411162853240967})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.4852840900421143})
store['active_learning_steps'][26]['training']['best_epoch']=1
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.8295, 'crossentropy': 0.97718662109375}
store['active_learning_steps'][26]['acquisition']={'indices': [56592, 48780, 40580, 21460, 59801], 'labels': [-1, -1, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.1726000308990479})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.292431116104126})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.2673149108886719})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.6382770538330078})
store['active_learning_steps'][27]['training']['best_epoch']=1
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.8167, 'crossentropy': 1.0167482421875}
store['active_learning_steps'][27]['acquisition']={'indices': [43138, 30359, 1779, 53349, 25363], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.133005142211914})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.2794982194900513})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.3570929765701294})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.4344995021820068})
store['active_learning_steps'][28]['training']['best_epoch']=1
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.8225, 'crossentropy': 1.0040234375}
store['active_learning_steps'][28]['acquisition']={'indices': [18545, 36077, 53304, 10957, 14104], 'labels': [1, -1, 1, 2, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.0209945440292358})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.222036600112915})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.2076616287231445})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.2516530752182007})
store['active_learning_steps'][29]['training']['best_epoch']=1
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.8342, 'crossentropy': 0.94220634765625}
store['active_learning_steps'][29]['acquisition']={'indices': [52359, 38005, 9513, 14106, 20952], 'labels': [-1, -1, 4, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.0982837677001953})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.1297968626022339})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.329418659210205})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.4323394298553467})
store['active_learning_steps'][30]['training']['best_epoch']=1
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.8196, 'crossentropy': 1.0005958984375}
store['active_learning_steps'][30]['acquisition']={'indices': [3105, 37809, 21991, 57750, 52838], 'labels': [2, 1, -1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.2842202186584473})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.242014765739441})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.4644982814788818})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.6192958354949951})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.5068998336791992})
store['active_learning_steps'][31]['training']['best_epoch']=2
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.8327, 'crossentropy': 1.043541796875}
store['active_learning_steps'][31]['acquisition']={'indices': [1349, 17988, 6459, 56306, 10393], 'labels': [0, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.0377099514007568})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.2135967016220093})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.2922377586364746})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.3753453493118286})
store['active_learning_steps'][32]['training']['best_epoch']=1
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.8345, 'crossentropy': 0.93805810546875}
store['active_learning_steps'][32]['acquisition']={'indices': [54741, 28157, 32844, 58839, 17179], 'labels': [8, -1, 7, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.04569411277771})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.0964637994766235})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.3919390439987183})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.389060378074646})
store['active_learning_steps'][33]['training']['best_epoch']=1
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.8305, 'crossentropy': 0.9599228515625}
store['active_learning_steps'][33]['acquisition']={'indices': [850, 25676, 33222, 42035, 43639], 'labels': [4, 0, 5, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9068566560745239})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.2151384353637695})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.0178046226501465})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.2423721551895142})
store['active_learning_steps'][34]['training']['best_epoch']=1
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.8516, 'crossentropy': 0.84882685546875}
store['active_learning_steps'][34]['acquisition']={'indices': [24875, 32330, 39661, 29249, 46900], 'labels': [8, 3, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.9128581881523132})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.9159867763519287})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.1096736192703247})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.2215588092803955})
store['active_learning_steps'][35]['training']['best_epoch']=1
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.8417, 'crossentropy': 0.83979453125}
store['active_learning_steps'][35]['acquisition']={'indices': [26478, 42356, 47696, 16076, 42565], 'labels': [-1, 9, -1, 1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.9202158451080322})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.9857190847396851})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.0767838954925537})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.0501408576965332})
store['active_learning_steps'][36]['training']['best_epoch']=1
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.8521, 'crossentropy': 0.8202095703125}
store['active_learning_steps'][36]['acquisition']={'indices': [13993, 34964, 35877, 42231, 38704], 'labels': [3, 2, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.9401372671127319})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.0673179626464844})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.167639970779419})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.2525643110275269})
store['active_learning_steps'][37]['training']['best_epoch']=1
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.8463, 'crossentropy': 0.862158203125}
store['active_learning_steps'][37]['acquisition']={'indices': [28509, 51072, 4530, 25671, 59932], 'labels': [4, 5, 7, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8602828979492188})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.0045044422149658})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9622118473052979})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.0966999530792236})
store['active_learning_steps'][38]['training']['best_epoch']=1
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.8506, 'crossentropy': 0.781270263671875}
store['active_learning_steps'][38]['acquisition']={'indices': [34762, 16486, 30039, 40021, 20808], 'labels': [-1, 8, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.7983453273773193})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.919954776763916})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8643931150436401})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.1347112655639648})
store['active_learning_steps'][39]['training']['best_epoch']=1
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.8587, 'crossentropy': 0.751441162109375}
store['active_learning_steps'][39]['acquisition']={'indices': [43846, 17837, 36513, 37946, 8556], 'labels': [8, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.839111328125})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.0252927541732788})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.0889025926589966})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9997810125350952})
store['active_learning_steps'][40]['training']['best_epoch']=1
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.8564, 'crossentropy': 0.78403828125}
store['active_learning_steps'][40]['acquisition']={'indices': [54159, 54713, 10592, 43411, 28707], 'labels': [5, 9, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8983137607574463})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8655593991279602})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.044443964958191})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9802506566047668})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.1257466077804565})
store['active_learning_steps'][41]['training']['best_epoch']=2
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.8741, 'crossentropy': 0.819081396484375}
store['active_learning_steps'][41]['acquisition']={'indices': [12590, 57140, 19237, 37048, 971], 'labels': [-1, 6, 8, 9, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8718782663345337})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8655683398246765})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9041907787322998})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.1149306297302246})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.09893798828125})
store['active_learning_steps'][42]['training']['best_epoch']=2
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.8799, 'crossentropy': 0.783078125}
store['active_learning_steps'][42]['acquisition']={'indices': [10787, 575, 16101, 54297, 41756], 'labels': [3, 8, -1, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8302983641624451})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.88145911693573})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9188867211341858})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9776759743690491})
store['active_learning_steps'][43]['training']['best_epoch']=1
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.8704, 'crossentropy': 0.75820380859375}
store['active_learning_steps'][43]['acquisition']={'indices': [35231, 31653, 4760, 45676, 58309], 'labels': [-1, 9, -1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8504414558410645})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8937788009643555})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.920698881149292})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 1.0666948556900024})
store['active_learning_steps'][44]['training']['best_epoch']=1
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.8582, 'crossentropy': 0.7999974609375}
store['active_learning_steps'][44]['acquisition']={'indices': [31552, 23154, 26053, 19542, 49375], 'labels': [4, 0, -1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8247702121734619})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8644323348999023})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 1.0175628662109375})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9811444878578186})
store['active_learning_steps'][45]['training']['best_epoch']=1
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.849, 'crossentropy': 0.782580224609375}
store['active_learning_steps'][45]['acquisition']={'indices': [50129, 38668, 38702, 49103, 33214], 'labels': [7, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7915445566177368})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8910641670227051})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8970838785171509})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9506455659866333})
store['active_learning_steps'][46]['training']['best_epoch']=1
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.8726, 'crossentropy': 0.713379931640625}
store['active_learning_steps'][46]['acquisition']={'indices': [42870, 51883, 57270, 28458, 13183], 'labels': [-1, 0, 2, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8429553508758545})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8943020105361938})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8542356491088867})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9891055226325989})
store['active_learning_steps'][47]['training']['best_epoch']=1
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.8638, 'crossentropy': 0.77724443359375}
store['active_learning_steps'][47]['acquisition']={'indices': [1991, 28781, 41855, 32082, 31774], 'labels': [-1, 7, 9, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7853066921234131})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.80198734998703})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.9463768005371094})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.938596785068512})
store['active_learning_steps'][48]['training']['best_epoch']=1
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.861, 'crossentropy': 0.77156630859375}
store['active_learning_steps'][48]['acquisition']={'indices': [1593, 38091, 12282, 52367, 59246], 'labels': [-1, -1, 8, 9, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8347644805908203})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8650805950164795})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.0426719188690186})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9428062438964844})
store['active_learning_steps'][49]['training']['best_epoch']=1
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.8725, 'crossentropy': 0.804018310546875}
store['active_learning_steps'][49]['acquisition']={'indices': [45754, 59726, 19176, 13803, 24691], 'labels': [-1, 5, 1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8173173666000366})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7800806760787964})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8060041069984436})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.879947304725647})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8161805272102356})
store['active_learning_steps'][50]['training']['best_epoch']=2
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.8955, 'crossentropy': 0.698206005859375}
store['active_learning_steps'][50]['acquisition']={'indices': [33492, 26526, 48198, 35636, 45300], 'labels': [-1, 3, 4, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7812304496765137})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8513408303260803})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8929551839828491})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8446766138076782})
store['active_learning_steps'][51]['training']['best_epoch']=1
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.8735, 'crossentropy': 0.735719921875}
store['active_learning_steps'][51]['acquisition']={'indices': [42368, 4241, 26606, 20894, 2696], 'labels': [7, -1, -1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8355422019958496})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7416626811027527})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.813715934753418})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9288959503173828})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.9154465198516846})
store['active_learning_steps'][52]['training']['best_epoch']=2
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.8876, 'crossentropy': 0.7169224609375}
store['active_learning_steps'][52]['acquisition']={'indices': [21877, 52198, 40528, 35199, 25884], 'labels': [3, -1, 9, 7, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7798309326171875})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8618969321250916})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7351586818695068})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9513812065124512})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8972034454345703})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 1.012295126914978})
store['active_learning_steps'][53]['training']['best_epoch']=3
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.8985, 'crossentropy': 0.706171337890625}
store['active_learning_steps'][53]['acquisition']={'indices': [42468, 36602, 35997, 6338, 22005], 'labels': [-1, 5, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8280670046806335})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.800169825553894})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8115918636322021})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8730723261833191})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9274910688400269})
store['active_learning_steps'][54]['training']['best_epoch']=2
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.8842, 'crossentropy': 0.749992236328125}
store['active_learning_steps'][54]['acquisition']={'indices': [5049, 25269, 56196, 39305, 8711], 'labels': [7, 1, -1, 7, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8021150231361389})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7694650888442993})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8430495262145996})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9858574867248535})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8893318176269531})
store['active_learning_steps'][55]['training']['best_epoch']=2
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.8931, 'crossentropy': 0.705474267578125}
store['active_learning_steps'][55]['acquisition']={'indices': [46056, 15408, 16355, 14670, 15744], 'labels': [2, 8, 0, 5, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7712604999542236})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7337229251861572})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7609371542930603})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8286420106887817})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8588479161262512})
store['active_learning_steps'][56]['training']['best_epoch']=2
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.8787, 'crossentropy': 0.716666064453125}
store['active_learning_steps'][56]['acquisition']={'indices': [49840, 18621, 42621, 48671, 5924], 'labels': [1, 7, -1, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7526795268058777})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7763952016830444})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7648521065711975})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.888445258140564})
store['active_learning_steps'][57]['training']['best_epoch']=1
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.8686, 'crossentropy': 0.731867236328125}
store['active_learning_steps'][57]['acquisition']={'indices': [24162, 9811, 48713, 11979, 7425], 'labels': [6, 8, 9, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7595007419586182})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7628989219665527})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7340801954269409})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8076253533363342})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8771382570266724})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.9426393508911133})
store['active_learning_steps'][58]['training']['best_epoch']=3
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.9026, 'crossentropy': 0.699480517578125}
store['active_learning_steps'][58]['acquisition']={'indices': [41375, 47972, 2705, 29638, 51947], 'labels': [-1, 5, 3, 4, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7498332858085632})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.778701663017273})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8130442500114441})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8962960243225098})
store['active_learning_steps'][59]['training']['best_epoch']=1
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.8814, 'crossentropy': 0.6968896484375}
store['active_learning_steps'][59]['acquisition']={'indices': [12201, 42120, 42022, 51642, 30914], 'labels': [-1, -1, -1, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7227106094360352})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7386719584465027})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8288148641586304})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.765910267829895})
store['active_learning_steps'][60]['training']['best_epoch']=1
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.8847, 'crossentropy': 0.658883251953125}
store['active_learning_steps'][60]['acquisition']={'indices': [58043, 24939, 45786, 53660, 32366], 'labels': [6, -1, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7515652179718018})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7672293186187744})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7786797285079956})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7688940763473511})
store['active_learning_steps'][61]['training']['best_epoch']=1
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.8737, 'crossentropy': 0.683453466796875}
store['active_learning_steps'][61]['acquisition']={'indices': [22857, 45969, 43026, 18376, 10698], 'labels': [-1, 9, -1, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8245863318443298})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7044224739074707})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8047646284103394})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8580617904663086})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.972175121307373})
store['active_learning_steps'][62]['training']['best_epoch']=2
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.8954, 'crossentropy': 0.621081787109375}
store['active_learning_steps'][62]['acquisition']={'indices': [28831, 27492, 44499, 41899, 55116], 'labels': [-1, 0, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7862624526023865})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7675094604492188})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8296109437942505})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.9348300695419312})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8415067195892334})
store['active_learning_steps'][63]['training']['best_epoch']=2
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.8893, 'crossentropy': 0.685106494140625}
store['active_learning_steps'][63]['acquisition']={'indices': [45594, 44342, 41128, 10027, 29064], 'labels': [-1, -1, 9, 1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8189212083816528})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7710735201835632})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8288712501525879})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8291120529174805})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8365875482559204})
store['active_learning_steps'][64]['training']['best_epoch']=2
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.8875, 'crossentropy': 0.698371337890625}
store['active_learning_steps'][64]['acquisition']={'indices': [5265, 22319, 39273, 25948, 5670], 'labels': [4, 9, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7268773317337036})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7160605192184448})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8287349939346313})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8664486408233643})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.9304158687591553})
store['active_learning_steps'][65]['training']['best_epoch']=2
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.8985, 'crossentropy': 0.622843798828125}
store['active_learning_steps'][65]['acquisition']={'indices': [34694, 10408, 50942, 3039, 35645], 'labels': [9, -1, 7, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7781186103820801})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6872975826263428})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7718133926391602})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8893730044364929})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.9540635347366333})
store['active_learning_steps'][66]['training']['best_epoch']=2
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.8918, 'crossentropy': 0.667310986328125}
store['active_learning_steps'][66]['acquisition']={'indices': [34595, 8121, 30426, 59577, 5045], 'labels': [-1, -1, -1, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7871860265731812})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7791630029678345})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7535299062728882})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.856742262840271})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9193609952926636})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8993316888809204})
store['active_learning_steps'][67]['training']['best_epoch']=3
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.8972, 'crossentropy': 0.669837548828125}
store['active_learning_steps'][67]['acquisition']={'indices': [39614, 8120, 36831, 32428, 58774], 'labels': [9, 3, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.733068585395813})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6700090169906616})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8151146769523621})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8221448659896851})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.819403886795044})
store['active_learning_steps'][68]['training']['best_epoch']=2
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.9024, 'crossentropy': 0.60110927734375}
store['active_learning_steps'][68]['acquisition']={'indices': [51033, 16590, 331, 46477, 51490], 'labels': [1, 6, 6, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8098368644714355})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7810568809509277})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7321144938468933})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7500904202461243})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8268598318099976})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.9375200867652893})
store['active_learning_steps'][69]['training']['best_epoch']=3
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9076, 'crossentropy': 0.6197326171875}
store['active_learning_steps'][69]['acquisition']={'indices': [25235, 20595, 31674, 40145, 57822], 'labels': [-1, -1, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7514221668243408})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.746337890625})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7738741636276245})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8882548213005066})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8554725050926208})
store['active_learning_steps'][70]['training']['best_epoch']=2
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.8861, 'crossentropy': 0.669433935546875}
store['active_learning_steps'][70]['acquisition']={'indices': [57888, 20999, 54980, 15937, 12609], 'labels': [-1, 4, 0, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8036333918571472})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6939711570739746})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8021656274795532})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7607002258300781})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.876516580581665})
store['active_learning_steps'][71]['training']['best_epoch']=2
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.8976, 'crossentropy': 0.645007666015625}
store['active_learning_steps'][71]['acquisition']={'indices': [58608, 34947, 6185, 18012, 50981], 'labels': [-1, -1, -1, 8, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7537250518798828})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7883425951004028})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7728151082992554})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.750533938407898})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8839473724365234})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7397069931030273})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8394403457641602})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.884367823600769})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.9101262092590332})
store['active_learning_steps'][72]['training']['best_epoch']=6
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.9108, 'crossentropy': 0.663977490234375}
store['active_learning_steps'][72]['acquisition']={'indices': [24018, 28424, 52747, 24062, 8527], 'labels': [4, -1, -1, 9, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7811716794967651})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7890005707740784})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7889606356620789})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7665970325469971})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7990166544914246})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8805912733078003})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.8437145948410034})
store['active_learning_steps'][73]['training']['best_epoch']=4
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9042, 'crossentropy': 0.653941259765625}
store['active_learning_steps'][73]['acquisition']={'indices': [16671, 30237, 35059, 29621, 37027], 'labels': [5, -1, -1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7051202058792114})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.782559871673584})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7660197615623474})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7406008243560791})
store['active_learning_steps'][74]['training']['best_epoch']=1
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.8873, 'crossentropy': 0.652513671875}
store['active_learning_steps'][74]['acquisition']={'indices': [8079, 33770, 22348, 8842, 34175], 'labels': [-1, 8, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7442097067832947})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.840543270111084})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8122625946998596})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7795169353485107})
store['active_learning_steps'][75]['training']['best_epoch']=1
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.8791, 'crossentropy': 0.678054736328125}
store['active_learning_steps'][75]['acquisition']={'indices': [214, 38898, 34148, 3424, 59637], 'labels': [7, 4, -1, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7351350784301758})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7488547563552856})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7716917991638184})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7986999750137329})
store['active_learning_steps'][76]['training']['best_epoch']=1
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.8789, 'crossentropy': 0.700662939453125}
store['active_learning_steps'][76]['acquisition']={'indices': [5457, 29634, 44801, 33939, 19543], 'labels': [9, 8, -1, 3, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.780544638633728})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.751986026763916})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6933314204216003})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7524634599685669})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7072151899337769})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.8596802949905396})
store['active_learning_steps'][77]['training']['best_epoch']=3
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9099, 'crossentropy': 0.620874169921875}
store['active_learning_steps'][77]['acquisition']={'indices': [38648, 14138, 52176, 1342, 59961], 'labels': [5, 7, -1, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.853797435760498})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.727397084236145})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7335213422775269})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7241412997245789})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8982765078544617})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8145550489425659})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7203742265701294})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.9140485525131226})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7862627506256104})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.8542187809944153})
store['active_learning_steps'][78]['training']['best_epoch']=7
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9088, 'crossentropy': 0.681211376953125}
store['active_learning_steps'][78]['acquisition']={'indices': [4007, 33937, 10979, 40876, 25553], 'labels': [-1, -1, -1, 9, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7073941230773926})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7032015323638916})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7965556383132935})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7531066536903381})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.697740375995636})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7335554361343384})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.8061147928237915})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7911714315414429})
store['active_learning_steps'][79]['training']['best_epoch']=5
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9077, 'crossentropy': 0.68631962890625}
store['active_learning_steps'][79]['acquisition']={'indices': [39974, 15062, 44373, 47494, 40581], 'labels': [-1, 7, 3, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7585891485214233})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.733714759349823})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7522979974746704})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7499289512634277})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7922557592391968})
store['active_learning_steps'][80]['training']['best_epoch']=2
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.8965, 'crossentropy': 0.635506884765625}
store['active_learning_steps'][80]['acquisition']={'indices': [43885, 4329, 7116, 37634, 21924], 'labels': [-1, -1, -1, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7327909469604492})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6880986094474792})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6185493469238281})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6770893335342407})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7263737916946411})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7301037311553955})
store['active_learning_steps'][81]['training']['best_epoch']=3
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9115, 'crossentropy': 0.563339990234375}
store['active_learning_steps'][81]['acquisition']={'indices': [10757, 14703, 18964, 4119, 19326], 'labels': [3, -1, -1, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7450931668281555})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7265433073043823})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6646637916564941})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8161582946777344})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8366333842277527})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.8736399412155151})
store['active_learning_steps'][82]['training']['best_epoch']=3
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9103, 'crossentropy': 0.5981708984375}
store['active_learning_steps'][82]['acquisition']={'indices': [53147, 46513, 23167, 26056, 44160], 'labels': [1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7577361464500427})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7510533928871155})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7420974969863892})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7419916987419128})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7701706886291504})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8825218677520752})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7491263747215271})
store['active_learning_steps'][83]['training']['best_epoch']=4
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9035, 'crossentropy': 0.67767255859375}
store['active_learning_steps'][83]['acquisition']={'indices': [4587, 39811, 36990, 32455, 25959], 'labels': [6, 0, 3, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7250753045082092})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7218038439750671})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6805305480957031})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7163894176483154})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7476648092269897})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7887855768203735})
store['active_learning_steps'][84]['training']['best_epoch']=3
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9104, 'crossentropy': 0.61053408203125}
store['active_learning_steps'][84]['acquisition']={'indices': [6159, 30579, 48256, 29974, 41006], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8300630450248718})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6678392887115479})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.694178581237793})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6890684366226196})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.732705295085907})
store['active_learning_steps'][85]['training']['best_epoch']=2
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.8915, 'crossentropy': 0.643985986328125}
store['active_learning_steps'][85]['acquisition']={'indices': [30498, 38969, 7420, 33441, 22478], 'labels': [9, -1, 7, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7847607135772705})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.752336859703064})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.681445837020874})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7417950630187988})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6858341097831726})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7207963466644287})
store['active_learning_steps'][86]['training']['best_epoch']=3
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.9057, 'crossentropy': 0.60713876953125}
store['active_learning_steps'][86]['acquisition']={'indices': [40743, 15041, 3589, 751, 26715], 'labels': [3, 5, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][87]['training']={}
store['active_learning_steps'][87]['training']['epochs']=[]
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7289435863494873})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6186034679412842})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6911643743515015})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6792408227920532})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6911332607269287})
store['active_learning_steps'][87]['training']['best_epoch']=2
store['active_learning_steps'][87]['evaluation_metrics']={'accuracy': 0.9084, 'crossentropy': 0.574734423828125}
store['active_learning_steps'][87]['acquisition']={'indices': [37207, 35436, 24758, 53123, 52359], 'labels': [-1, -1, -1, 3, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][88]['training']={}
store['active_learning_steps'][88]['training']['epochs']=[]
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7809154391288757})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6690373420715332})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6916429996490479})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7758927941322327})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7870225310325623})
store['active_learning_steps'][88]['training']['best_epoch']=2
store['active_learning_steps'][88]['evaluation_metrics']={'accuracy': 0.9037, 'crossentropy': 0.589632080078125}
store['active_learning_steps'][88]['acquisition']={'indices': [32228, 30761, 30934, 49097, 14439], 'labels': [6, 5, 3, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][89]['training']={}
store['active_learning_steps'][89]['training']['epochs']=[]
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7402477860450745})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7043309807777405})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6619550585746765})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6599552631378174})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.688148021697998})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7418248653411865})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7758406400680542})
store['active_learning_steps'][89]['training']['best_epoch']=4
store['active_learning_steps'][89]['evaluation_metrics']={'accuracy': 0.9138, 'crossentropy': 0.582623388671875}
store['active_learning_steps'][89]['acquisition']={'indices': [20681, 48313, 56819, 43536, 7898], 'labels': [-1, -1, -1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][90]['training']={}
store['active_learning_steps'][90]['training']['epochs']=[]
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7150224447250366})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.667515754699707})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6998164057731628})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6718962788581848})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6934959888458252})
store['active_learning_steps'][90]['training']['best_epoch']=2
store['active_learning_steps'][90]['evaluation_metrics']={'accuracy': 0.907, 'crossentropy': 0.586554345703125}
store['active_learning_steps'][90]['acquisition']={'indices': [32205, 2718, 19703, 52592, 33565], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][91]['training']={}
store['active_learning_steps'][91]['training']['epochs']=[]
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7001928091049194})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6943469047546387})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7163585424423218})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7209219336509705})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.840477705001831})
store['active_learning_steps'][91]['training']['best_epoch']=2
store['active_learning_steps'][91]['evaluation_metrics']={'accuracy': 0.8998, 'crossentropy': 0.6188314453125}
store['active_learning_steps'][91]['acquisition']={'indices': [45425, 59258, 31319, 49269, 35791], 'labels': [-1, -1, 7, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][92]['training']={}
store['active_learning_steps'][92]['training']['epochs']=[]
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7282921075820923})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.664980411529541})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7488218545913696})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8488688468933105})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8002394437789917})
store['active_learning_steps'][92]['training']['best_epoch']=2
store['active_learning_steps'][92]['evaluation_metrics']={'accuracy': 0.8985, 'crossentropy': 0.5985765625}
store['active_learning_steps'][92]['acquisition']={'indices': [9183, 8362, 26427, 34234, 56719], 'labels': [3, -1, -1, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][93]['training']={}
store['active_learning_steps'][93]['training']['epochs']=[]
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8001025915145874})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.669969916343689})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.700898289680481})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.755104124546051})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6959704756736755})
store['active_learning_steps'][93]['training']['best_epoch']=2
store['active_learning_steps'][93]['evaluation_metrics']={'accuracy': 0.8937, 'crossentropy': 0.63233759765625}
store['active_learning_steps'][93]['acquisition']={'indices': [46586, 15023, 1392, 26518, 20857], 'labels': [-1, 4, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][94]['training']={}
store['active_learning_steps'][94]['training']['epochs']=[]
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7438657879829407})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6889961957931519})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.713423490524292})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7675915956497192})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7836424112319946})
store['active_learning_steps'][94]['training']['best_epoch']=2
store['active_learning_steps'][94]['evaluation_metrics']={'accuracy': 0.9063, 'crossentropy': 0.609302587890625}
store['active_learning_steps'][94]['acquisition']={'indices': [34469, 51536, 6944, 13827, 20559], 'labels': [-1, 3, -1, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][95]['training']={}
store['active_learning_steps'][95]['training']['epochs']=[]
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7919298410415649})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7036094665527344})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6560728549957275})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6729778051376343})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7171684503555298})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7233803868293762})
store['active_learning_steps'][95]['training']['best_epoch']=3
store['active_learning_steps'][95]['evaluation_metrics']={'accuracy': 0.9069, 'crossentropy': 0.6143845703125}
store['active_learning_steps'][95]['acquisition']={'indices': [37275, 51309, 57918, 20734, 41093], 'labels': [5, -1, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][96]['training']={}
store['active_learning_steps'][96]['training']['epochs']=[]
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.644748866558075})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6122335195541382})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6970987915992737})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.638323187828064})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6640336513519287})
store['active_learning_steps'][96]['training']['best_epoch']=2
store['active_learning_steps'][96]['evaluation_metrics']={'accuracy': 0.9088, 'crossentropy': 0.547139404296875}
store['active_learning_steps'][96]['acquisition']={'indices': [42389, 10119, 16580, 55911, 16623], 'labels': [-1, 0, -1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][97]['training']={}
store['active_learning_steps'][97]['training']['epochs']=[]
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7035916447639465})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6770132780075073})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6153429746627808})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6324606537818909})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6329666972160339})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.691875696182251})
store['active_learning_steps'][97]['training']['best_epoch']=3
store['active_learning_steps'][97]['evaluation_metrics']={'accuracy': 0.9175, 'crossentropy': 0.53129150390625}
store['active_learning_steps'][97]['acquisition']={'indices': [7156, 38572, 10899, 17702, 21005], 'labels': [3, -1, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][98]['training']={}
store['active_learning_steps'][98]['training']['epochs']=[]
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7299859523773193})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7573201060295105})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6482465267181396})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7817119359970093})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6220681667327881})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6934045553207397})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7384666204452515})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.751977801322937})
store['active_learning_steps'][98]['training']['best_epoch']=5
store['active_learning_steps'][98]['evaluation_metrics']={'accuracy': 0.9165, 'crossentropy': 0.571772607421875}
store['active_learning_steps'][98]['acquisition']={'indices': [45168, 10117, 57156, 51086, 48600], 'labels': [-1, 2, 5, 5, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][99]['training']={}
store['active_learning_steps'][99]['training']['epochs']=[]
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6853945255279541})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5531630516052246})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5990527868270874})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6897778511047363})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6886265277862549})
store['active_learning_steps'][99]['training']['best_epoch']=2
store['active_learning_steps'][99]['evaluation_metrics']={'accuracy': 0.9153, 'crossentropy': 0.54377236328125}
store['active_learning_steps'][99]['acquisition']={'indices': [50276, 40805, 2665, 31347, 59110], 'labels': [-1, 3, 4, 3, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][100]['training']={}
store['active_learning_steps'][100]['training']['epochs']=[]
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7222143411636353})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.619173526763916})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.603009819984436})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6186224222183228})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6391369104385376})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6866694688796997})
store['active_learning_steps'][100]['training']['best_epoch']=3
store['active_learning_steps'][100]['evaluation_metrics']={'accuracy': 0.9247, 'crossentropy': 0.53147431640625}
store['active_learning_steps'][100]['acquisition']={'indices': [13934, 21548, 9556, 3575, 45631], 'labels': [-1, 5, 6, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][101]['training']={}
store['active_learning_steps'][101]['training']['epochs']=[]
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7478014230728149})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6291673183441162})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6903599500656128})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6816232204437256})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.608575701713562})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7547672390937805})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6743433475494385})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6787828207015991})
store['active_learning_steps'][101]['training']['best_epoch']=5
store['active_learning_steps'][101]['evaluation_metrics']={'accuracy': 0.9144, 'crossentropy': 0.57368095703125}
store['active_learning_steps'][101]['acquisition']={'indices': [21708, 55758, 23938, 767, 5750], 'labels': [-1, 3, -1, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][102]['training']={}
store['active_learning_steps'][102]['training']['epochs']=[]
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8013519048690796})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6441590785980225})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6900142431259155})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6657775640487671})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6843411922454834})
store['active_learning_steps'][102]['training']['best_epoch']=2
store['active_learning_steps'][102]['evaluation_metrics']={'accuracy': 0.9067, 'crossentropy': 0.56704248046875}
store['active_learning_steps'][102]['acquisition']={'indices': [1480, 47719, 26271, 33298, 31409], 'labels': [-1, -1, -1, 1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][103]['training']={}
store['active_learning_steps'][103]['training']['epochs']=[]
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7159183025360107})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6261724233627319})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6465049982070923})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6508198976516724})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6978340744972229})
store['active_learning_steps'][103]['training']['best_epoch']=2
store['active_learning_steps'][103]['evaluation_metrics']={'accuracy': 0.9042, 'crossentropy': 0.54196630859375}
store['active_learning_steps'][103]['acquisition']={'indices': [30091, 23294, 17380, 1111, 41171], 'labels': [-1, 3, -1, 5, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][104]['training']={}
store['active_learning_steps'][104]['training']['epochs']=[]
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.695899486541748})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6839972734451294})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6583912968635559})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.718040943145752})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7688174843788147})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6946449279785156})
store['active_learning_steps'][104]['training']['best_epoch']=3
store['active_learning_steps'][104]['evaluation_metrics']={'accuracy': 0.9158, 'crossentropy': 0.5320513671875}
store['active_learning_steps'][104]['acquisition']={'indices': [53436, 44461, 879, 23401, 32580], 'labels': [-1, 5, -1, 0, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][105]['training']={}
store['active_learning_steps'][105]['training']['epochs']=[]
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7013310194015503})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5729477405548096})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.662582278251648})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6607068777084351})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6146277189254761})
store['active_learning_steps'][105]['training']['best_epoch']=2
store['active_learning_steps'][105]['evaluation_metrics']={'accuracy': 0.9105, 'crossentropy': 0.539704248046875}
store['active_learning_steps'][105]['acquisition']={'indices': [17856, 8568, 32869, 20675, 43136], 'labels': [-1, 3, 0, 3, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][106]['training']={}
store['active_learning_steps'][106]['training']['epochs']=[]
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6795481443405151})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6794155836105347})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5759320259094238})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7016476392745972})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.8201199769973755})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6540239453315735})
store['active_learning_steps'][106]['training']['best_epoch']=3
store['active_learning_steps'][106]['evaluation_metrics']={'accuracy': 0.9203, 'crossentropy': 0.517519287109375}
store['active_learning_steps'][106]['acquisition']={'indices': [21128, 21696, 50486, 640, 45383], 'labels': [-1, 6, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][107]['training']={}
store['active_learning_steps'][107]['training']['epochs']=[]
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7904379367828369})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6028240323066711})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7587299942970276})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6644147038459778})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.646380603313446})
store['active_learning_steps'][107]['training']['best_epoch']=2
store['active_learning_steps'][107]['evaluation_metrics']={'accuracy': 0.9167, 'crossentropy': 0.524313330078125}
store['active_learning_steps'][107]['acquisition']={'indices': [43549, 19818, 44342, 55434, 4639], 'labels': [-1, -1, 4, 5, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][108]['training']={}
store['active_learning_steps'][108]['training']['epochs']=[]
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.724810779094696})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.600574254989624})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6697250008583069})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6710828542709351})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6467506885528564})
store['active_learning_steps'][108]['training']['best_epoch']=2
store['active_learning_steps'][108]['evaluation_metrics']={'accuracy': 0.9113, 'crossentropy': 0.535964208984375}
store['active_learning_steps'][108]['acquisition']={'indices': [38529, 24866, 4391, 38673, 12482], 'labels': [-1, 4, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][109]['training']={}
store['active_learning_steps'][109]['training']['epochs']=[]
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7917433977127075})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6571604013442993})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7011235356330872})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7375014424324036})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6878138780593872})
store['active_learning_steps'][109]['training']['best_epoch']=2
store['active_learning_steps'][109]['evaluation_metrics']={'accuracy': 0.9031, 'crossentropy': 0.563477783203125}
store['active_learning_steps'][109]['acquisition']={'indices': [12897, 42513, 10289, 8777, 35891], 'labels': [0, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][110]['training']={}
store['active_learning_steps'][110]['training']['epochs']=[]
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7504462599754333})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6193549633026123})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6919097900390625})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7500689625740051})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6508172154426575})
store['active_learning_steps'][110]['training']['best_epoch']=2
store['active_learning_steps'][110]['evaluation_metrics']={'accuracy': 0.9085, 'crossentropy': 0.52480419921875}
store['active_learning_steps'][110]['acquisition']={'indices': [48788, 56279, 10282, 51837, 41234], 'labels': [-1, -1, -1, 3, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][111]['training']={}
store['active_learning_steps'][111]['training']['epochs']=[]
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7424613237380981})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6681276559829712})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6337077617645264})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7097897529602051})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6629306674003601})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7370221018791199})
store['active_learning_steps'][111]['training']['best_epoch']=3
store['active_learning_steps'][111]['evaluation_metrics']={'accuracy': 0.9059, 'crossentropy': 0.580350244140625}
store['active_learning_steps'][111]['acquisition']={'indices': [1512, 43969, 55874, 48095, 3691], 'labels': [0, 7, -1, 7, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][112]['training']={}
store['active_learning_steps'][112]['training']['epochs']=[]
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7184548377990723})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6140821576118469})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5994568467140198})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6823453903198242})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6568185091018677})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6561167240142822})
store['active_learning_steps'][112]['training']['best_epoch']=3
store['active_learning_steps'][112]['evaluation_metrics']={'accuracy': 0.9225, 'crossentropy': 0.51917919921875}
store['active_learning_steps'][112]['acquisition']={'indices': [50559, 40151, 4106, 31992, 31685], 'labels': [-1, 2, 0, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][113]['training']={}
store['active_learning_steps'][113]['training']['epochs']=[]
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6913823485374451})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.596298336982727})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5729727745056152})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.565367579460144})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.585911214351654})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.641725480556488})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5845487117767334})
store['active_learning_steps'][113]['training']['best_epoch']=4
store['active_learning_steps'][113]['evaluation_metrics']={'accuracy': 0.9262, 'crossentropy': 0.5047533203125}
store['active_learning_steps'][113]['acquisition']={'indices': [58357, 1633, 21922, 36677, 57086], 'labels': [5, -1, -1, 8, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][114]['training']={}
store['active_learning_steps'][114]['training']['epochs']=[]
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7559845447540283})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7352694869041443})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6017042398452759})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6790069937705994})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.634506106376648})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6853036880493164})
store['active_learning_steps'][114]['training']['best_epoch']=3
store['active_learning_steps'][114]['evaluation_metrics']={'accuracy': 0.9158, 'crossentropy': 0.571368896484375}
store['active_learning_steps'][114]['acquisition']={'indices': [37134, 19340, 4465, 42907, 59293], 'labels': [-1, 4, 0, 3, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][115]['training']={}
store['active_learning_steps'][115]['training']['epochs']=[]
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7817425727844238})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5903595685958862})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6607412099838257})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6102464199066162})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6871877312660217})
store['active_learning_steps'][115]['training']['best_epoch']=2
store['active_learning_steps'][115]['evaluation_metrics']={'accuracy': 0.9078, 'crossentropy': 0.544082666015625}
store['active_learning_steps'][115]['acquisition']={'indices': [10259, 55291, 2109, 47063, 14152], 'labels': [-1, 7, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][116]['training']={}
store['active_learning_steps'][116]['training']['epochs']=[]
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6825695633888245})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5618395805358887})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5793647766113281})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6588153839111328})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5636768937110901})
store['active_learning_steps'][116]['training']['best_epoch']=2
store['active_learning_steps'][116]['evaluation_metrics']={'accuracy': 0.9162, 'crossentropy': 0.49102548828125}
store['active_learning_steps'][116]['acquisition']={'indices': [50243, 43664, 21391, 11069, 18050], 'labels': [4, 1, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][117]['training']={}
store['active_learning_steps'][117]['training']['epochs']=[]
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7708530426025391})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5965173840522766})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6028063297271729})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6511729955673218})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6058448553085327})
store['active_learning_steps'][117]['training']['best_epoch']=2
store['active_learning_steps'][117]['evaluation_metrics']={'accuracy': 0.9098, 'crossentropy': 0.524300341796875}
store['active_learning_steps'][117]['acquisition']={'indices': [57780, 25462, 24941, 22495, 1457], 'labels': [1, -1, 4, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][118]['training']={}
store['active_learning_steps'][118]['training']['epochs']=[]
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.74718177318573})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.681701123714447})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5620496273040771})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.631824254989624})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6584776639938354})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7378023862838745})
store['active_learning_steps'][118]['training']['best_epoch']=3
store['active_learning_steps'][118]['evaluation_metrics']={'accuracy': 0.9128, 'crossentropy': 0.56112490234375}
store['active_learning_steps'][118]['acquisition']={'indices': [50571, 6763, 52994, 6323, 11193], 'labels': [8, -1, 3, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][119]['training']={}
store['active_learning_steps'][119]['training']['epochs']=[]
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8035857677459717})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6005440950393677})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6905463933944702})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6589971780776978})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6399164199829102})
store['active_learning_steps'][119]['training']['best_epoch']=2
store['active_learning_steps'][119]['evaluation_metrics']={'accuracy': 0.9112, 'crossentropy': 0.52930615234375}
store['active_learning_steps'][119]['acquisition']={'indices': [36463, 4131, 46567, 39938, 27934], 'labels': [2, 7, 6, 8, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][120]['training']={}
store['active_learning_steps'][120]['training']['epochs']=[]
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7230933904647827})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.586402177810669})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6029807925224304})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6283035278320312})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5968015193939209})
store['active_learning_steps'][120]['training']['best_epoch']=2
store['active_learning_steps'][120]['evaluation_metrics']={'accuracy': 0.921, 'crossentropy': 0.481960107421875}
store['active_learning_steps'][120]['acquisition']={'indices': [3900, 38620, 25804, 38654, 28098], 'labels': [1, -1, -1, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][121]['training']={}
store['active_learning_steps'][121]['training']['epochs']=[]
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7464210391044617})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5638976097106934})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6036943197250366})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.636759340763092})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5833818912506104})
store['active_learning_steps'][121]['training']['best_epoch']=2
store['active_learning_steps'][121]['evaluation_metrics']={'accuracy': 0.9182, 'crossentropy': 0.500901123046875}
store['active_learning_steps'][121]['acquisition']={'indices': [57706, 48499, 58157, 15507, 22402], 'labels': [4, 3, -1, 1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][122]['training']={}
store['active_learning_steps'][122]['training']['epochs']=[]
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6746963262557983})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5521492958068848})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.552899956703186})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6144716739654541})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6414707899093628})
store['active_learning_steps'][122]['training']['best_epoch']=2
store['active_learning_steps'][122]['evaluation_metrics']={'accuracy': 0.9138, 'crossentropy': 0.5044408203125}
store['active_learning_steps'][122]['acquisition']={'indices': [39788, 42180, 38819, 47634, 39869], 'labels': [0, 0, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][123]['training']={}
store['active_learning_steps'][123]['training']['epochs']=[]
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7122358083724976})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6587344408035278})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5928592681884766})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5841114521026611})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6565896272659302})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6065751314163208})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6160460710525513})
store['active_learning_steps'][123]['training']['best_epoch']=4
store['active_learning_steps'][123]['evaluation_metrics']={'accuracy': 0.9218, 'crossentropy': 0.504363232421875}
store['active_learning_steps'][123]['acquisition']={'indices': [47315, 808, 16058, 32646, 30717], 'labels': [-1, 3, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][124]['training']={}
store['active_learning_steps'][124]['training']['epochs']=[]
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7502070665359497})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6604430675506592})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6427594423294067})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6229754686355591})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.706944465637207})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6962096691131592})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5847402811050415})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6277236938476562})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6847130656242371})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6268681287765503})
store['active_learning_steps'][124]['training']['best_epoch']=7
store['active_learning_steps'][124]['evaluation_metrics']={'accuracy': 0.9299, 'crossentropy': 0.529158447265625}
store['active_learning_steps'][124]['acquisition']={'indices': [8208, 29179, 30219, 52251, 20902], 'labels': [-1, 8, 8, 2, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][125]['training']={}
store['active_learning_steps'][125]['training']['epochs']=[]
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7253671884536743})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5824495553970337})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5401151776313782})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6019660234451294})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5746614933013916})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5514248609542847})
store['active_learning_steps'][125]['training']['best_epoch']=3
store['active_learning_steps'][125]['evaluation_metrics']={'accuracy': 0.9241, 'crossentropy': 0.47598583984375}
store['active_learning_steps'][125]['acquisition']={'indices': [53887, 27850, 38784, 58137, 32445], 'labels': [-1, 6, 2, 2, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][126]['training']={}
store['active_learning_steps'][126]['training']['epochs']=[]
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7413554787635803})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6400479674339294})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5643385052680969})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6223828792572021})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.618566632270813})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6946597099304199})
store['active_learning_steps'][126]['training']['best_epoch']=3
store['active_learning_steps'][126]['evaluation_metrics']={'accuracy': 0.9283, 'crossentropy': 0.482918701171875}
store['active_learning_steps'][126]['acquisition']={'indices': [20582, 56821, 28859, 9988, 2397], 'labels': [-1, -1, -1, 7, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][127]['training']={}
store['active_learning_steps'][127]['training']['epochs']=[]
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6852378845214844})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5401848554611206})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.530633807182312})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.557459831237793})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5885919332504272})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5733760595321655})
store['active_learning_steps'][127]['training']['best_epoch']=3
store['active_learning_steps'][127]['evaluation_metrics']={'accuracy': 0.925, 'crossentropy': 0.489137060546875}
store['active_learning_steps'][127]['acquisition']={'indices': [32358, 9208, 58389, 19653, 11081], 'labels': [1, -1, -1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][128]['training']={}
store['active_learning_steps'][128]['training']['epochs']=[]
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7312867641448975})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5725707411766052})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.516281247138977})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5261765718460083})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5908166170120239})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6142738461494446})
store['active_learning_steps'][128]['training']['best_epoch']=3
store['active_learning_steps'][128]['evaluation_metrics']={'accuracy': 0.9217, 'crossentropy': 0.4774919921875}
store['active_learning_steps'][128]['acquisition']={'indices': [19701, 2488, 59182, 16907, 16157], 'labels': [-1, -1, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][129]['training']={}
store['active_learning_steps'][129]['training']['epochs']=[]
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6420478224754333})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5802894830703735})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5587645769119263})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5291091203689575})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5638487339019775})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5865741968154907})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.588517427444458})
store['active_learning_steps'][129]['training']['best_epoch']=4
store['active_learning_steps'][129]['evaluation_metrics']={'accuracy': 0.926, 'crossentropy': 0.480794091796875}
store['active_learning_steps'][129]['acquisition']={'indices': [43709, 53514, 41848, 41875, 31345], 'labels': [4, -1, 6, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][130]['training']={}
store['active_learning_steps'][130]['training']['epochs']=[]
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.713158130645752})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.583080530166626})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5851203203201294})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5664635896682739})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5677114129066467})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5759917497634888})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5466758012771606})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6414796710014343})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6250046491622925})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6642105579376221})
store['active_learning_steps'][130]['training']['best_epoch']=7
store['active_learning_steps'][130]['evaluation_metrics']={'accuracy': 0.9298, 'crossentropy': 0.51371005859375}
store['active_learning_steps'][130]['acquisition']={'indices': [54907, 1931, 24829, 45367, 20931], 'labels': [6, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][131]['training']={}
store['active_learning_steps'][131]['training']['epochs']=[]
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.721611738204956})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.575799822807312})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5564050674438477})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6228265762329102})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.540786862373352})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5825287103652954})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.586082935333252})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5679476261138916})
store['active_learning_steps'][131]['training']['best_epoch']=5
store['active_learning_steps'][131]['evaluation_metrics']={'accuracy': 0.9355, 'crossentropy': 0.46062412109375}
store['active_learning_steps'][131]['acquisition']={'indices': [25295, 36486, 31699, 27372, 14333], 'labels': [-1, 9, -1, 8, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][132]['training']={}
store['active_learning_steps'][132]['training']['epochs']=[]
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7341961860656738})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5593671798706055})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5370336771011353})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5633018016815186})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5259252190589905})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5867130756378174})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6415727138519287})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.6243034601211548})
store['active_learning_steps'][132]['training']['best_epoch']=5
store['active_learning_steps'][132]['evaluation_metrics']={'accuracy': 0.9304, 'crossentropy': 0.48515283203125}
store['active_learning_steps'][132]['acquisition']={'indices': [2178, 8196, 19272, 23020, 17633], 'labels': [-1, 7, 6, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][133]['training']={}
store['active_learning_steps'][133]['training']['epochs']=[]
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6886501312255859})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6123272776603699})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5393552780151367})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5866165161132812})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5765000581741333})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5886543989181519})
store['active_learning_steps'][133]['training']['best_epoch']=3
store['active_learning_steps'][133]['evaluation_metrics']={'accuracy': 0.9244, 'crossentropy': 0.466440625}
store['active_learning_steps'][133]['acquisition']={'indices': [57494, 48337, 56062, 6108, 17822], 'labels': [0, -1, 9, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][134]['training']={}
store['active_learning_steps'][134]['training']['epochs']=[]
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6441936492919922})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6124952435493469})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6143338680267334})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5638493895530701})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5916661024093628})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6394925117492676})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6407178640365601})
store['active_learning_steps'][134]['training']['best_epoch']=4
store['active_learning_steps'][134]['evaluation_metrics']={'accuracy': 0.923, 'crossentropy': 0.52577177734375}
store['active_learning_steps'][134]['acquisition']={'indices': [23704, 48107, 48579, 59487, 50380], 'labels': [7, 2, 3, 0, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][135]['training']={}
store['active_learning_steps'][135]['training']['epochs']=[]
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6704323291778564})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5576770305633545})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5891798734664917})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6117468476295471})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5455570220947266})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5668297410011292})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5817936062812805})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6014010310173035})
store['active_learning_steps'][135]['training']['best_epoch']=5
store['active_learning_steps'][135]['evaluation_metrics']={'accuracy': 0.9325, 'crossentropy': 0.472500537109375}
store['active_learning_steps'][135]['acquisition']={'indices': [58910, 46216, 23615, 13893, 21686], 'labels': [2, -1, -1, 9, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][136]['training']={}
store['active_learning_steps'][136]['training']['epochs']=[]
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7302392721176147})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5498721599578857})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5880165100097656})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5784837007522583})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5914204120635986})
store['active_learning_steps'][136]['training']['best_epoch']=2
store['active_learning_steps'][136]['evaluation_metrics']={'accuracy': 0.9142, 'crossentropy': 0.50578310546875}
store['active_learning_steps'][136]['acquisition']={'indices': [23024, 53290, 1819, 47899, 37281], 'labels': [-1, -1, -1, 9, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][137]['training']={}
store['active_learning_steps'][137]['training']['epochs']=[]
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7503295540809631})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5344083309173584})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5096675753593445})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5416616201400757})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5334944128990173})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5109182000160217})
store['active_learning_steps'][137]['training']['best_epoch']=3
store['active_learning_steps'][137]['evaluation_metrics']={'accuracy': 0.9234, 'crossentropy': 0.4566791015625}
store['active_learning_steps'][137]['acquisition']={'indices': [7650, 15643, 34749, 9210, 32699], 'labels': [-1, -1, -1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][138]['training']={}
store['active_learning_steps'][138]['training']['epochs']=[]
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6858292818069458})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5330241918563843})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5163862705230713})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5383968949317932})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5615071058273315})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5552655458450317})
store['active_learning_steps'][138]['training']['best_epoch']=3
store['active_learning_steps'][138]['evaluation_metrics']={'accuracy': 0.9302, 'crossentropy': 0.44011162109375}
store['active_learning_steps'][138]['acquisition']={'indices': [26565, 19116, 11713, 12915, 12952], 'labels': [0, 3, -1, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][139]['training']={}
store['active_learning_steps'][139]['training']['epochs']=[]
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6818382740020752})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4858940839767456})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5054816007614136})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4929048418998718})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.48236823081970215})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.529032289981842})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5419559478759766})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5914243459701538})
store['active_learning_steps'][139]['training']['best_epoch']=5
store['active_learning_steps'][139]['evaluation_metrics']={'accuracy': 0.9383, 'crossentropy': 0.438524267578125}
store['active_learning_steps'][139]['acquisition']={'indices': [9759, 15254, 12743, 54826, 10578], 'labels': [-1, 7, 1, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][140]['training']={}
store['active_learning_steps'][140]['training']['epochs']=[]
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7052239775657654})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5318914651870728})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5508016347885132})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5631361603736877})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4966799318790436})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5502687692642212})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.523471474647522})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5013264417648315})
store['active_learning_steps'][140]['training']['best_epoch']=5
store['active_learning_steps'][140]['evaluation_metrics']={'accuracy': 0.9355, 'crossentropy': 0.435961328125}
store['active_learning_steps'][140]['acquisition']={'indices': [21420, 44366, 16511, 58830, 22349], 'labels': [3, 1, 5, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][141]['training']={}
store['active_learning_steps'][141]['training']['epochs']=[]
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7446763515472412})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5509265065193176})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.4900747835636139})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5082528591156006})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5945150852203369})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6283990740776062})
store['active_learning_steps'][141]['training']['best_epoch']=3
store['active_learning_steps'][141]['evaluation_metrics']={'accuracy': 0.9248, 'crossentropy': 0.461830615234375}
store['active_learning_steps'][141]['acquisition']={'indices': [48244, 21240, 16358, 4358, 59540], 'labels': [-1, -1, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][142]['training']={}
store['active_learning_steps'][142]['training']['epochs']=[]
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7194162607192993})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5024744272232056})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5626226663589478})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5787094235420227})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.49968644976615906})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5245659351348877})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5173263549804688})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5631755590438843})
store['active_learning_steps'][142]['training']['best_epoch']=5
store['active_learning_steps'][142]['evaluation_metrics']={'accuracy': 0.9346, 'crossentropy': 0.440583935546875}
store['active_learning_steps'][142]['acquisition']={'indices': [23910, 57910, 37787, 55052, 50840], 'labels': [-1, 2, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][143]['training']={}
store['active_learning_steps'][143]['training']['epochs']=[]
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6359958052635193})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5064784288406372})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5333737730979919})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5381492972373962})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.49607741832733154})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.537158727645874})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5248759984970093})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5610098838806152})
store['active_learning_steps'][143]['training']['best_epoch']=5
store['active_learning_steps'][143]['evaluation_metrics']={'accuracy': 0.9322, 'crossentropy': 0.46545986328125}
store['active_learning_steps'][143]['acquisition']={'indices': [4846, 13589, 47231, 47357, 12643], 'labels': [2, 0, -1, 5, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][144]['training']={}
store['active_learning_steps'][144]['training']['epochs']=[]
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7339032888412476})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5814002752304077})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5163838267326355})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4877302646636963})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5054190158843994})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.45858973264694214})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5222114324569702})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5049505233764648})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5624712705612183})
store['active_learning_steps'][144]['training']['best_epoch']=6
store['active_learning_steps'][144]['evaluation_metrics']={'accuracy': 0.9354, 'crossentropy': 0.431651220703125}
store['active_learning_steps'][144]['acquisition']={'indices': [13, 36509, 20564, 13033, 37414], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][145]['training']={}
store['active_learning_steps'][145]['training']['epochs']=[]
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6844615936279297})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4904502034187317})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4609186053276062})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4723755121231079})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4411553144454956})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4838581681251526})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.49380311369895935})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5550210475921631})
store['active_learning_steps'][145]['training']['best_epoch']=5
store['active_learning_steps'][145]['evaluation_metrics']={'accuracy': 0.9384, 'crossentropy': 0.42453369140625}
store['active_learning_steps'][145]['acquisition']={'indices': [46278, 3483, 38082, 20896, 47140], 'labels': [-1, -1, -1, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][146]['training']={}
store['active_learning_steps'][146]['training']['epochs']=[]
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6967178583145142})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5284825563430786})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5037331581115723})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4593019485473633})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.49849870800971985})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5161457061767578})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5709182024002075})
store['active_learning_steps'][146]['training']['best_epoch']=4
store['active_learning_steps'][146]['evaluation_metrics']={'accuracy': 0.9333, 'crossentropy': 0.4331583984375}
store['active_learning_steps'][146]['acquisition']={'indices': [25812, 13158, 9670, 33413, 38783], 'labels': [1, -1, 3, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][147]['training']={}
store['active_learning_steps'][147]['training']['epochs']=[]
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6805744767189026})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5501437187194824})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5170477628707886})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.46329066157341003})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5102656483650208})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5797793865203857})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5153989195823669})
store['active_learning_steps'][147]['training']['best_epoch']=4
store['active_learning_steps'][147]['evaluation_metrics']={'accuracy': 0.9343, 'crossentropy': 0.444504150390625}
store['active_learning_steps'][147]['acquisition']={'indices': [40986, 14522, 14209, 8337, 5787], 'labels': [-1, 7, -1, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][148]['training']={}
store['active_learning_steps'][148]['training']['epochs']=[]
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6183030009269714})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5023040771484375})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4946441054344177})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5256916284561157})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5265011191368103})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5305693745613098})
store['active_learning_steps'][148]['training']['best_epoch']=3
store['active_learning_steps'][148]['evaluation_metrics']={'accuracy': 0.932, 'crossentropy': 0.452189697265625}
store['active_learning_steps'][148]['acquisition']={'indices': [46638, 23273, 2834, 53419, 28680], 'labels': [7, -1, 3, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][149]['training']={}
store['active_learning_steps'][149]['training']['epochs']=[]
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6223920583724976})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5472028851509094})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.48306265473365784})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4438542127609253})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5389100313186646})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4791375696659088})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4619978070259094})
store['active_learning_steps'][149]['training']['best_epoch']=4
store['active_learning_steps'][149]['evaluation_metrics']={'accuracy': 0.9346, 'crossentropy': 0.412448388671875}
store['active_learning_steps'][149]['acquisition']={'indices': [59548, 38182, 52881, 9849, 5571], 'labels': [-1, -1, -1, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][150]['training']={}
store['active_learning_steps'][150]['training']['epochs']=[]
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7460476160049438})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5673143863677979})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5192636251449585})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4937548339366913})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5102343559265137})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.575151801109314})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5194106101989746})
store['active_learning_steps'][150]['training']['best_epoch']=4
store['active_learning_steps'][150]['evaluation_metrics']={'accuracy': 0.9314, 'crossentropy': 0.442104248046875}
store['active_learning_steps'][150]['acquisition']={'indices': [22062, 4675, 48346, 15558, 37335], 'labels': [-1, 8, -1, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][151]['training']={}
store['active_learning_steps'][151]['training']['epochs']=[]
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6757466197013855})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4911382496356964})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5146993398666382})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4748918414115906})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.493373841047287})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5079724192619324})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5295052528381348})
store['active_learning_steps'][151]['training']['best_epoch']=4
store['active_learning_steps'][151]['evaluation_metrics']={'accuracy': 0.9358, 'crossentropy': 0.42403173828125}
store['active_learning_steps'][151]['acquisition']={'indices': [30697, 3308, 34, 11430, 40898], 'labels': [-1, 2, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][152]['training']={}
store['active_learning_steps'][152]['training']['epochs']=[]
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6454403400421143})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4804394543170929})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4629189074039459})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.45436346530914307})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.46200770139694214})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4614035487174988})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5395011901855469})
store['active_learning_steps'][152]['training']['best_epoch']=4
store['active_learning_steps'][152]['evaluation_metrics']={'accuracy': 0.9338, 'crossentropy': 0.4287130859375}
store['active_learning_steps'][152]['acquisition']={'indices': [8383, 23446, 34550, 19437, 38816], 'labels': [-1, 9, 4, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][153]['training']={}
store['active_learning_steps'][153]['training']['epochs']=[]
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7237385511398315})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5322598218917847})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.513978123664856})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5070109963417053})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.547710657119751})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5366953611373901})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4821825623512268})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5906403660774231})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5532259941101074})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5780521631240845})
store['active_learning_steps'][153]['training']['best_epoch']=7
store['active_learning_steps'][153]['evaluation_metrics']={'accuracy': 0.9386, 'crossentropy': 0.444466943359375}
store['active_learning_steps'][153]['acquisition']={'indices': [46295, 22152, 27342, 10987, 47899], 'labels': [3, -1, 9, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][154]['training']={}
store['active_learning_steps'][154]['training']['epochs']=[]
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6558483839035034})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5601065158843994})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5078737139701843})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5430644750595093})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5272163152694702})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.48404747247695923})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5691416263580322})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5192420482635498})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5192407369613647})
store['active_learning_steps'][154]['training']['best_epoch']=6
store['active_learning_steps'][154]['evaluation_metrics']={'accuracy': 0.94, 'crossentropy': 0.4247955078125}
store['active_learning_steps'][154]['acquisition']={'indices': [28784, 14928, 11716, 54530, 26238], 'labels': [0, -1, -1, 3, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][155]['training']={}
store['active_learning_steps'][155]['training']['epochs']=[]
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6651296019554138})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5259659290313721})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4782005548477173})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4929650127887726})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5384016036987305})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4841868579387665})
store['active_learning_steps'][155]['training']['best_epoch']=3
store['active_learning_steps'][155]['evaluation_metrics']={'accuracy': 0.9288, 'crossentropy': 0.425802587890625}
store['active_learning_steps'][155]['acquisition']={'indices': [51117, 52315, 48454, 35102, 58850], 'labels': [-1, 9, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][156]['training']={}
store['active_learning_steps'][156]['training']['epochs']=[]
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6347722411155701})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4988476634025574})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4706045389175415})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.47156471014022827})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.479167103767395})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5229414701461792})
store['active_learning_steps'][156]['training']['best_epoch']=3
store['active_learning_steps'][156]['evaluation_metrics']={'accuracy': 0.9286, 'crossentropy': 0.44398828125}
store['active_learning_steps'][156]['acquisition']={'indices': [50644, 58752, 53921, 43279, 50689], 'labels': [3, 8, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][157]['training']={}
store['active_learning_steps'][157]['training']['epochs']=[]
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7138313055038452})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5840877890586853})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4640079140663147})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.47877755761146545})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4971145987510681})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5026952624320984})
store['active_learning_steps'][157]['training']['best_epoch']=3
store['active_learning_steps'][157]['evaluation_metrics']={'accuracy': 0.9301, 'crossentropy': 0.442808203125}
store['active_learning_steps'][157]['acquisition']={'indices': [13057, 13827, 22939, 38317, 7764], 'labels': [9, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][158]['training']={}
store['active_learning_steps'][158]['training']['epochs']=[]
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7283427119255066})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5091619491577148})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4734371304512024})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4686572551727295})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4945294260978699})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4672573208808899})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5139979124069214})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4617166817188263})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.46250206232070923})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5335057973861694})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5699092745780945})
store['active_learning_steps'][158]['training']['best_epoch']=8
store['active_learning_steps'][158]['evaluation_metrics']={'accuracy': 0.9403, 'crossentropy': 0.442722216796875}
store['active_learning_steps'][158]['acquisition']={'indices': [20643, 42451, 57563, 38769, 18331], 'labels': [1, 7, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][159]['training']={}
store['active_learning_steps'][159]['training']['epochs']=[]
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.720096230506897})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5287233591079712})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.49133604764938354})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.46698296070098877})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.48980653285980225})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5554152727127075})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4878760576248169})
store['active_learning_steps'][159]['training']['best_epoch']=4
store['active_learning_steps'][159]['evaluation_metrics']={'accuracy': 0.9267, 'crossentropy': 0.456304248046875}
store['active_learning_steps'][159]['acquisition']={'indices': [14722, 29003, 58422, 13268, 42132], 'labels': [-1, -1, -1, 0, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][160]['training']={}
store['active_learning_steps'][160]['training']['epochs']=[]
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.6780561804771423})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5498138666152954})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5038137435913086})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5387294292449951})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5130537748336792})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5469416379928589})
store['active_learning_steps'][160]['training']['best_epoch']=3
store['active_learning_steps'][160]['evaluation_metrics']={'accuracy': 0.9316, 'crossentropy': 0.420656689453125}
store['active_learning_steps'][160]['acquisition']={'indices': [45538, 22702, 15151, 31361, 626], 'labels': [-1, 6, -1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][161]['training']={}
store['active_learning_steps'][161]['training']['epochs']=[]
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6774226427078247})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5232766270637512})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4599500894546509})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5112684369087219})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.45830464363098145})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4392089247703552})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.44972696900367737})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4883708357810974})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.46487361192703247})
store['active_learning_steps'][161]['training']['best_epoch']=6
store['active_learning_steps'][161]['evaluation_metrics']={'accuracy': 0.9439, 'crossentropy': 0.406184521484375}
store['active_learning_steps'][161]['acquisition']={'indices': [46101, 59022, 42875, 47994, 43803], 'labels': [6, 5, 1, 1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][162]['training']={}
store['active_learning_steps'][162]['training']['epochs']=[]
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7484374046325684})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5929242968559265})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5055366158485413})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5140793323516846})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5506856441497803})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5457592010498047})
store['active_learning_steps'][162]['training']['best_epoch']=3
store['active_learning_steps'][162]['evaluation_metrics']={'accuracy': 0.9143, 'crossentropy': 0.5017771484375}
store['active_learning_steps'][162]['acquisition']={'indices': [10988, 48487, 5608, 46727, 58498], 'labels': [-1, 4, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][163]['training']={}
store['active_learning_steps'][163]['training']['epochs']=[]
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6816587448120117})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.489676296710968})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.44593143463134766})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4724999666213989})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4940029978752136})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5206637978553772})
store['active_learning_steps'][163]['training']['best_epoch']=3
store['active_learning_steps'][163]['evaluation_metrics']={'accuracy': 0.9314, 'crossentropy': 0.418165087890625}
store['active_learning_steps'][163]['acquisition']={'indices': [33808, 50046, 42157, 9235, 29464], 'labels': [-1, -1, 0, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][164]['training']={}
store['active_learning_steps'][164]['training']['epochs']=[]
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.703241229057312})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.595524787902832})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5291582345962524})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5282196998596191})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5143439173698425})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5595855712890625})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5991041660308838})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.590944766998291})
store['active_learning_steps'][164]['training']['best_epoch']=5
store['active_learning_steps'][164]['evaluation_metrics']={'accuracy': 0.9329, 'crossentropy': 0.48412021484375}
store['active_learning_steps'][164]['acquisition']={'indices': [8296, 12896, 19934, 2389, 31349], 'labels': [-1, -1, 9, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][165]['training']={}
store['active_learning_steps'][165]['training']['epochs']=[]
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7488846778869629})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5597509145736694})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.49017468094825745})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4775571823120117})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.49610018730163574})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.45439988374710083})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4429864287376404})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5280815958976746})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5507370233535767})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4992505609989166})
store['active_learning_steps'][165]['training']['best_epoch']=7
store['active_learning_steps'][165]['evaluation_metrics']={'accuracy': 0.9458, 'crossentropy': 0.4251861328125}
store['active_learning_steps'][165]['acquisition']={'indices': [33890, 57355, 15321, 2231, 54386], 'labels': [8, 8, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][166]['training']={}
store['active_learning_steps'][166]['training']['epochs']=[]
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.688733696937561})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5549696683883667})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5245013236999512})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5483393669128418})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.48221099376678467})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5418553352355957})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5848597288131714})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5097841024398804})
store['active_learning_steps'][166]['training']['best_epoch']=5
store['active_learning_steps'][166]['evaluation_metrics']={'accuracy': 0.9364, 'crossentropy': 0.439081298828125}
store['active_learning_steps'][166]['acquisition']={'indices': [9862, 42135, 2281, 44817, 12926], 'labels': [2, 2, 5, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][167]['training']={}
store['active_learning_steps'][167]['training']['epochs']=[]
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6268099546432495})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5261633396148682})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4436572194099426})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4907878637313843})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.47644567489624023})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5409321784973145})
store['active_learning_steps'][167]['training']['best_epoch']=3
store['active_learning_steps'][167]['evaluation_metrics']={'accuracy': 0.9322, 'crossentropy': 0.42481025390625}
store['active_learning_steps'][167]['acquisition']={'indices': [14774, 26972, 7675, 21675, 55300], 'labels': [-1, -1, -1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][168]['training']={}
store['active_learning_steps'][168]['training']['epochs']=[]
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6674007773399353})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.519406259059906})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5152523517608643})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5163493156433105})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.47770917415618896})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.559798002243042})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5060226321220398})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4984649419784546})
store['active_learning_steps'][168]['training']['best_epoch']=5
store['active_learning_steps'][168]['evaluation_metrics']={'accuracy': 0.9328, 'crossentropy': 0.459446630859375}
store['active_learning_steps'][168]['acquisition']={'indices': [51178, 33355, 51332, 5584, 33450], 'labels': [-1, -1, 3, 7, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][169]['training']={}
store['active_learning_steps'][169]['training']['epochs']=[]
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6794103384017944})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5013921856880188})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5124021768569946})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.49525386095046997})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4474163055419922})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.49362534284591675})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5089784264564514})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4970054626464844})
store['active_learning_steps'][169]['training']['best_epoch']=5
store['active_learning_steps'][169]['evaluation_metrics']={'accuracy': 0.9378, 'crossentropy': 0.422317724609375}
store['active_learning_steps'][169]['acquisition']={'indices': [11304, 14075, 7320, 45837, 11355], 'labels': [0, 8, 8, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][170]['training']={}
store['active_learning_steps'][170]['training']['epochs']=[]
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6368634700775146})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.49462345242500305})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4960683584213257})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.48103445768356323})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5044493675231934})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5319724082946777})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5409626960754395})
store['active_learning_steps'][170]['training']['best_epoch']=4
store['active_learning_steps'][170]['evaluation_metrics']={'accuracy': 0.932, 'crossentropy': 0.437862841796875}
store['active_learning_steps'][170]['acquisition']={'indices': [34170, 56027, 7333, 55467, 20481], 'labels': [3, 2, 4, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][171]['training']={}
store['active_learning_steps'][171]['training']['epochs']=[]
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.660529375076294})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5170507431030273})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.46595126390457153})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4913645386695862})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5100917816162109})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5095380544662476})
store['active_learning_steps'][171]['training']['best_epoch']=3
store['active_learning_steps'][171]['evaluation_metrics']={'accuracy': 0.9364, 'crossentropy': 0.3993651611328125}
store['active_learning_steps'][171]['acquisition']={'indices': [50435, 33499, 59106, 22875, 3942], 'labels': [-1, -1, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][172]['training']={}
store['active_learning_steps'][172]['training']['epochs']=[]
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6556876301765442})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5092576742172241})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.47850751876831055})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5002476572990417})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.48056793212890625})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5849449038505554})
store['active_learning_steps'][172]['training']['best_epoch']=3
store['active_learning_steps'][172]['evaluation_metrics']={'accuracy': 0.9294, 'crossentropy': 0.442716650390625}
store['active_learning_steps'][172]['acquisition']={'indices': [38886, 22871, 23065, 59506, 4487], 'labels': [-1, 7, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][173]['training']={}
store['active_learning_steps'][173]['training']['epochs']=[]
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6638095378875732})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5140597224235535})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5227092504501343})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5401979684829712})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5098507404327393})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5353095531463623})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5338459610939026})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.520683765411377})
store['active_learning_steps'][173]['training']['best_epoch']=5
store['active_learning_steps'][173]['evaluation_metrics']={'accuracy': 0.9331, 'crossentropy': 0.473829345703125}
store['active_learning_steps'][173]['acquisition']={'indices': [45581, 30546, 50141, 25417, 43115], 'labels': [-1, 8, 3, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][174]['training']={}
store['active_learning_steps'][174]['training']['epochs']=[]
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6846964359283447})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5388442873954773})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.49192988872528076})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.46189752221107483})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4563911557197571})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5418881177902222})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4744623303413391})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4886716604232788})
store['active_learning_steps'][174]['training']['best_epoch']=5
store['active_learning_steps'][174]['evaluation_metrics']={'accuracy': 0.9386, 'crossentropy': 0.4174765625}
store['active_learning_steps'][174]['acquisition']={'indices': [54091, 3237, 19648, 10096, 56456], 'labels': [-1, -1, 7, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][175]['training']={}
store['active_learning_steps'][175]['training']['epochs']=[]
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6826034784317017})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5623242259025574})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5047515034675598})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5084877610206604})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5121570825576782})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5575849413871765})
store['active_learning_steps'][175]['training']['best_epoch']=3
store['active_learning_steps'][175]['evaluation_metrics']={'accuracy': 0.9284, 'crossentropy': 0.435543994140625}
store['active_learning_steps'][175]['acquisition']={'indices': [15140, 55971, 37613, 59399, 39837], 'labels': [-1, 7, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][176]['training']={}
store['active_learning_steps'][176]['training']['epochs']=[]
store['active_learning_steps'][176]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7158535718917847})
store['active_learning_steps'][176]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5130367875099182})
store['active_learning_steps'][176]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.47336816787719727})
store['active_learning_steps'][176]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4432108998298645})
store['active_learning_steps'][176]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5227264165878296})
store['active_learning_steps'][176]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5122250318527222})
store['active_learning_steps'][176]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5071423649787903})
store['active_learning_steps'][176]['training']['best_epoch']=4
store['active_learning_steps'][176]['evaluation_metrics']={'accuracy': 0.9336, 'crossentropy': 0.42786298828125}
store['active_learning_steps'][176]['acquisition']={'indices': [2330, 53733, 35699, 57243, 32760], 'labels': [-1, -1, -1, 1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][177]['training']={}
store['active_learning_steps'][177]['training']['epochs']=[]
store['active_learning_steps'][177]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6470046639442444})
store['active_learning_steps'][177]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4699207842350006})
store['active_learning_steps'][177]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.45038312673568726})
store['active_learning_steps'][177]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.49226242303848267})
store['active_learning_steps'][177]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4540260434150696})
store['active_learning_steps'][177]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.44395527243614197})
store['active_learning_steps'][177]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4899904727935791})
store['active_learning_steps'][177]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4654132127761841})
store['active_learning_steps'][177]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.44149249792099})
store['active_learning_steps'][177]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5295232534408569})
store['active_learning_steps'][177]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4694877862930298})
store['active_learning_steps'][177]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.5219263434410095})
store['active_learning_steps'][177]['training']['best_epoch']=9
store['active_learning_steps'][177]['evaluation_metrics']={'accuracy': 0.9434, 'crossentropy': 0.43324560546875}
