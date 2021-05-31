store = {}
store['timestamp']=1622115006
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=16']
store['commit']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['github_url']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=16
store['worker_id']=16
store['num_workers']=80
store['config']={'seed': 1251, 'uniform_ood': True, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 16, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('FastFashionMNIST Train (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 3792, 5573, 45567, 10508, 2728, 21423, 396, 49512, 31444]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.2178070545196533})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.31111216545105})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.5687506198883057})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.662446975708008})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.6394803524017334})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.580888271331787})
store['active_learning_steps'][0]['training']['best_epoch']=3
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.7173, 'crossentropy': 2.311590234375}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.3455102443695068})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.4071120023727417})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.422908067703247})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.3989323377609253})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.4214444160461426})
store['active_learning_steps'][0]['eval_training']['best_epoch']=4
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 47889], ['id', 23919], ['id', 17080], ['id', 8680], ['ood', 5413]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [1.0331780183246435, 1.8325662542984142, 2.373435615444734, 2.758217052096189, 2.9786645553392415]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.493780493736267})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.6859087944030762})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.0135397911071777})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.0629491806030273})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.3204708099365234})
store['active_learning_steps'][1]['training']['best_epoch']=2
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7263, 'crossentropy': 1.5189400390625}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.3219879865646362})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.2738583087921143})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.366208791732788})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.373335599899292})
store['active_learning_steps'][1]['eval_training']['best_epoch']=2
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 3653], ['id', 57016], ['id', 55541], ['id', 512], ['id', 45666]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6919075900305365, 1.2451507947332425, 1.7146252539771814, 2.0311712772501096, 2.2386715766492102]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.6719436645507812})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.0812880992889404})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.065338373184204})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.1971826553344727})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.18467116355896})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.677551507949829})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.3515448570251465})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.667919635772705})
store['active_learning_steps'][2]['training']['best_epoch']=5
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7165, 'crossentropy': 1.9151490234375}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.504387378692627})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.291632890701294})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.4531707763671875})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.5249137878417969})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.6476051807403564})
store['active_learning_steps'][2]['eval_training']['best_epoch']=2
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 10876], ['id', 41276], ['id', 29534], ['id', 35946], ['id', 44570]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.7550528652242955, 1.3671607722817116, 1.8835895291285372, 2.2428143647901253, 2.513287725870832]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.8355739116668701})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.04489803314209})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.206791639328003})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.5502681732177734})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.68886137008667})
store['active_learning_steps'][3]['training']['best_epoch']=2
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7079, 'crossentropy': 1.80704921875}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.272264838218689})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.229714274406433})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.3139116764068604})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.278433918952942})
store['active_learning_steps'][3]['eval_training']['best_epoch']=2
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 12355], ['id', 16600], ['id', 36760], ['id', 39915], ['id', 21722]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6132153034549956, 1.1625622703621215, 1.624702164492407, 1.950442098486576, 2.194195895063383]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.2149395942687988})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.5474159717559814})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.5684378147125244})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.6849161386489868})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.6558043956756592})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.8261408805847168})
store['active_learning_steps'][4]['training']['best_epoch']=3
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7893, 'crossentropy': 1.3570912109375}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.2298651933670044})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.2037343978881836})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.150670051574707})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.1429095268249512})
store['active_learning_steps'][4]['eval_training']['best_epoch']=1
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 34789], ['id', 25855], ['id', 12980], ['id', 43143], ['id', 40275]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5730897071896537, 1.0520093351254607, 1.447961874780499, 1.741695394226495, 1.923573727364456]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.4493122100830078})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.8168513774871826})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.9032270908355713})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 2.121455192565918})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 2.0955820083618164})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 2.097903251647949})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 2.285207748413086})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 2.113542079925537})
store['active_learning_steps'][5]['training']['best_epoch']=5
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.756, 'crossentropy': 1.9660583984375}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.2645506858825684})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.365372896194458})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.287808895111084})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.299677848815918})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.2625834941864014})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.2463054656982422})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.3035078048706055})
store['active_learning_steps'][5]['eval_training']['best_epoch']=4
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 36836], ['id', 30704], ['id', 38017], ['id', 54120], ['id', 23588]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.7556968512266177, 1.3840740636458044, 1.9038289190878488, 2.2557361330662653, 2.5053306387117145]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.3620036840438843})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.4119718074798584})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.456939935684204})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.7870838642120361})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.7765536308288574})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7958, 'crossentropy': 1.24324921875}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.1497691869735718})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.0893474817276})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.0793378353118896})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.0585217475891113})
store['active_learning_steps'][6]['eval_training']['best_epoch']=1
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 33397], ['id', 39834], ['id', 11505], ['id', 9581], ['id', 8339]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6694319352450083, 1.1653939900940724, 1.5914571636464458, 1.8672143032270432, 2.0552056951931146]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.1625467538833618})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.1669235229492188})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.2983767986297607})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.5655744075775146})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.644187331199646})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8192, 'crossentropy': 1.069103125}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 0.9370575547218323})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 0.9283461570739746})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 0.8880366683006287})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 0.8685981035232544})
store['active_learning_steps'][7]['eval_training']['best_epoch']=3
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 20641], ['id', 52753], ['id', 51492], ['id', 49880], ['ood', 8892]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.6233255744277706, 1.1244669348821357, 1.5282171490829413, 1.828774359304001, 2.044707245163215]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.1307963132858276})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.214141845703125})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.5205695629119873})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.5106571912765503})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 2.056434392929077})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.7973, 'crossentropy': 1.07686494140625}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.9171445369720459})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.8439934253692627})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.8351911306381226})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 0.8316633701324463})
store['active_learning_steps'][8]['eval_training']['best_epoch']=1
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 44308], ['id', 21471], ['id', 29621], ['id', 52103], ['id', 5000]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.499229624255106, 0.8961417358087531, 1.2390069772324122, 1.5158832548583785, 1.710598627382331]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.0473464727401733})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.121397852897644})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.365067481994629})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.4361696243286133})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.5465261936187744})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8192, 'crossentropy': 1.047997265625}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.0063989162445068})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.9393643140792847})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.837824821472168})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.8304848670959473})
store['active_learning_steps'][9]['eval_training']['best_epoch']=3
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 10446], ['id', 15116], ['id', 14881], ['id', 8516], ['id', 32473]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6261180584960917, 1.1718922630470439, 1.6218732538992917, 1.960031536243541, 2.1826113878732007]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.935970664024353})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.9816255569458008})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.0993672609329224})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.1342661380767822})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.2346370220184326})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8464, 'crossentropy': 0.9068755859375}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.0156517028808594})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.8849291801452637})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.8374379873275757})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.7867887616157532})
store['active_learning_steps'][10]['eval_training']['best_epoch']=4
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 17756], ['id', 4727], ['id', 52294], ['id', 54240], ['id', 31754]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.7311116567778142, 1.2554728402701887, 1.6652749539681464, 1.978805720172378, 2.2046594749598203]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.0203063488006592})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.894730806350708})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.1796294450759888})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.314422845840454})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.2887811660766602})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8294, 'crossentropy': 0.9026681640625}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.9169775247573853})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.758554220199585})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.7435671091079712})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.6927852034568787})
store['active_learning_steps'][11]['eval_training']['best_epoch']=4
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 30401], ['id', 33073], ['id', 31941], ['id', 32352], ['id', 528]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6021295304484751, 1.1796293914413734, 1.589945158263669, 1.9185597926380673, 2.146023360090263]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.0776150226593018})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.0884044170379639})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.3210797309875488})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.3555809259414673})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.5621635913848877})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.4226467609405518})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.5045833587646484})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.7397685050964355})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.6155245304107666})
store['active_learning_steps'][12]['training']['best_epoch']=6
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8291, 'crossentropy': 1.2844458984375}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 0.9673771858215332})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.9512425065040588})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.8899034261703491})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.9612082242965698})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9622455835342407})
store['active_learning_steps'][12]['eval_training']['best_epoch']=2
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 42801], ['id', 23956], ['id', 25946], ['id', 21219], ['id', 38061]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6835114937241544, 1.2288423524100427, 1.6741428082825571, 2.0159412344081185, 2.289350159885244]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 0.9785192012786865})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.0615193843841553})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.1782773733139038})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.206984281539917})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.2282893657684326})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.326117992401123})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.322216510772705})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.4489166736602783})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.449112892150879})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.3747739791870117})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.438920259475708})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.4041495323181152})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.5399168729782104})
store['active_learning_steps'][13]['training']['best_epoch']=10
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8522, 'crossentropy': 1.24281376953125}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.9269463419914246})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.90378737449646})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.938800036907196})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.9035170078277588})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8253288269042969})
store['active_learning_steps'][13]['eval_training']['best_epoch']=2
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 19549], ['id', 31460], ['id', 5188], ['id', 13677], ['id', 18522]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7943332399816353, 1.4249974419635503, 1.9724807237813806, 2.345687961922663, 2.5689127645375756]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.9602214097976685})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.9566293358802795})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.1119847297668457})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.079327940940857})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.1326171159744263})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.2767843008041382})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.2256574630737305})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.1057536602020264})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.3551867008209229})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.3905773162841797})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.2257182598114014})
store['active_learning_steps'][14]['training']['best_epoch']=8
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8725, 'crossentropy': 1.0755814453125}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 0.9786384105682373})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.88875412940979})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.9075659513473511})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8312426805496216})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8393669128417969})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8345057964324951})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8839123249053955})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.7895501255989075})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.767048716545105})
store['active_learning_steps'][14]['eval_training']['best_epoch']=6
store['active_learning_steps'][14]['acquisition']={'indices': [['ood', 16731], ['id', 28914], ['id', 44948], ['id', 22824], ['id', 55269]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.692790273508312, 1.3433094338255107, 1.8764377312857738, 2.242821143198711, 2.4794395554650768]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.9031275510787964})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.835012674331665})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9282345175743103})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.9843181371688843})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9578688740730286})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.02114737033844})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.0230581760406494})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.1308821439743042})
store['active_learning_steps'][15]['training']['best_epoch']=5
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8779, 'crossentropy': 0.81757587890625}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.8976154923439026})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8342381715774536})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.7811156511306763})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8030841946601868})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7641422152519226})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7251355648040771})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7308878302574158})
store['active_learning_steps'][15]['eval_training']['best_epoch']=7
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 34594], ['id', 13614], ['id', 26022], ['id', 21457], ['id', 1634]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7465451309077591, 1.3596686266019118, 1.8408407093915438, 2.132614933047507, 2.3408233977060506]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.9517396688461304})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.9642358422279358})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.9918057918548584})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.173680067062378})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.1170169115066528})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.0489614009857178})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.1086931228637695})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9726670980453491})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.1344949007034302})
store['active_learning_steps'][16]['training']['best_epoch']=6
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8677, 'crossentropy': 0.9547107421875}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.9413326382637024})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7736895680427551})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.7582753896713257})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.6880201697349548})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7869079113006592})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6605568528175354})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.6780871152877808})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6559053659439087})
store['active_learning_steps'][16]['eval_training']['best_epoch']=8
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 51988], ['id', 46329], ['id', 3479], ['id', 6863], ['id', 10820]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.8293240305630829, 1.491753720539069, 2.0156424719043695, 2.3608145449832323, 2.586908077699565]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.9385294914245605})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8058593273162842})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8493584394454956})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9905185699462891})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9348040223121643})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9463784694671631})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.116383671760559})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9942904710769653})
store['active_learning_steps'][17]['training']['best_epoch']=5
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8733, 'crossentropy': 0.8202734375}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.0912392139434814})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.8924325704574585})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.7748844623565674})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.8602198958396912})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.7485386729240417})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.7305629253387451})
store['active_learning_steps'][17]['eval_training']['best_epoch']=3
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 55282], ['id', 48681], ['id', 15769], ['id', 13714], ['id', 38539]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.7057967517517105, 1.2071151441512673, 1.61798402837539, 1.9128645572857703, 2.102036534408959]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.9043539762496948})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8283601999282837})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7066088914871216})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8495525121688843})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8362141847610474})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9034650325775146})
store['active_learning_steps'][18]['training']['best_epoch']=3
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8873, 'crossentropy': 0.706253125}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8875552415847778})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6683237552642822})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5882755517959595})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5384995341300964})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6235239505767822})
store['active_learning_steps'][18]['eval_training']['best_epoch']=4
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 40308], ['id', 33162], ['id', 14329], ['id', 42569], ['id', 50841]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6205108994672142, 1.1775570775476107, 1.6491440884507123, 1.9830353306514863, 2.22920431260607]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.9319102764129639})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8304673433303833})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8656678199768066})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9074351787567139})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8986631035804749})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8692775964736938})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9765973687171936})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.0385767221450806})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 1.0365135669708252})
store['active_learning_steps'][19]['training']['best_epoch']=6
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.885, 'crossentropy': 0.90812529296875}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8997223377227783})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7814671993255615})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7440527677536011})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7226552963256836})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8472895622253418})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6707403659820557})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7216161489486694})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6552010774612427})
store['active_learning_steps'][19]['eval_training']['best_epoch']=6
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 17582], ['id', 52153], ['id', 10910], ['id', 43560], ['id', 43210]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.7037397663536265, 1.2311976694224087, 1.6848855593118803, 2.0225467849782826, 2.255535250175946]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.865923285484314})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.873571515083313})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9211647510528564})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8644371628761292})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9130256175994873})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.0935325622558594})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 1.0638082027435303})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.0203454494476318})
store['active_learning_steps'][20]['training']['best_epoch']=5
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8802, 'crossentropy': 0.8568884765625}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.9250379800796509})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.730846643447876})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6860485076904297})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7008230090141296})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.683017373085022})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6458425521850586})
store['active_learning_steps'][20]['eval_training']['best_epoch']=3
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 9979], ['id', 9180], ['id', 11600], ['id', 9290], ['id', 58050]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.6366237432194992, 1.203008504048026, 1.673293076553974, 1.9939347605683242, 2.192856073395353]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.9585247039794922})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.813630223274231})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8216544985771179})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.9012027978897095})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9805506467819214})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9491469860076904})
store['active_learning_steps'][21]['training']['best_epoch']=3
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.8701, 'crossentropy': 0.80215205078125}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.878624439239502})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.7562441825866699})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6673952341079712})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6247164607048035})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6364337205886841})
store['active_learning_steps'][21]['eval_training']['best_epoch']=3
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 57342], ['id', 9078], ['id', 10005], ['id', 40466], ['id', 23824]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5154880487099847, 0.9863459693524321, 1.3768518082642478, 1.683114274644928, 1.8976690085853178]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.0210121870040894})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6699806451797485})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6638162136077881})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7582796812057495})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6834738850593567})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7974644899368286})
store['active_learning_steps'][22]['training']['best_epoch']=3
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.8949, 'crossentropy': 0.6743572265625}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.9483372569084167})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6541295647621155})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5861863493919373})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.5892050862312317})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.5621521472930908})
store['active_learning_steps'][22]['eval_training']['best_epoch']=3
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 13853], ['id', 51144], ['id', 13078], ['id', 25706], ['id', 27291]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5792945661311968, 1.0662449499443443, 1.489365233592324, 1.8517211661493116, 2.096156607731764]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.0788592100143433})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7139822244644165})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6544628143310547})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6598384976387024})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7346265316009521})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6719330549240112})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7768902778625488})
store['active_learning_steps'][23]['training']['best_epoch']=4
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9012, 'crossentropy': 0.62181396484375}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.9434376955032349})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6267422437667847})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.5662742853164673})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6041248440742493})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.5786932706832886})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.529157280921936})
store['active_learning_steps'][23]['eval_training']['best_epoch']=6
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 32774], ['id', 39208], ['id', 42687], ['id', 7803], ['id', 47870]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.6959660671694072, 1.2786670142105603, 1.7384748337021767, 2.057348478113811, 2.2799192613189376]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.002918004989624})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6558531522750854})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5996346473693848})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.73907071352005})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6977837681770325})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7168680429458618})
store['active_learning_steps'][24]['training']['best_epoch']=3
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.8923, 'crossentropy': 0.63845166015625}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.9111837148666382})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7101464867591858})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6271333694458008})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6055924892425537})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.5465342998504639})
store['active_learning_steps'][24]['eval_training']['best_epoch']=3
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 134], ['id', 42671], ['id', 18573], ['id', 24637], ['ood', 51161]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.5104704320375582, 0.972143011141303, 1.3817082465788886, 1.7235514915546197, 1.9783087058196847]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.9544094204902649})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7444688677787781})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6522982120513916})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6772820949554443})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6770647168159485})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.67711341381073})
store['active_learning_steps'][25]['training']['best_epoch']=3
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9, 'crossentropy': 0.619656494140625}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.9047015905380249})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6160984039306641})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5800427198410034})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5274803638458252})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5383049249649048})
store['active_learning_steps'][25]['eval_training']['best_epoch']=5
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 22139], ['id', 14697], ['id', 54986], ['id', 11074], ['id', 14627]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.5716846609382076, 1.072492564246402, 1.4927605916797528, 1.812682132956395, 2.0267984358116884]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.063614845275879})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7652994394302368})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6201229691505432})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6463562250137329})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6690763235092163})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7573300004005432})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8782689571380615})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7772950530052185})
store['active_learning_steps'][26]['training']['best_epoch']=5
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9078, 'crossentropy': 0.6272404296875}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.025831937789917})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7379274368286133})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7252483367919922})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6212406158447266})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6128581762313843})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6143105626106262})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.5985353589057922})
store['active_learning_steps'][26]['eval_training']['best_epoch']=7
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 39384], ['id', 32926], ['id', 49525], ['id', 11863], ['id', 5314]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6906061457979069, 1.288579830095955, 1.776925840190474, 2.1067858231608074, 2.330933802033562]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.0595505237579346})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6827989816665649})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6644399166107178})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6418704986572266})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7223819494247437})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8281713724136353})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8761091232299805})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9032, 'crossentropy': 0.638794677734375}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.920587420463562})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.614856481552124})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5377121567726135})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.5913372039794922})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5139731764793396})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.47907134890556335})
store['active_learning_steps'][27]['eval_training']['best_epoch']=6
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 55244], ['id', 19108], ['id', 52478], ['id', 10666], ['id', 46363]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.6055619271163128, 1.1589280925428516, 1.601532411064258, 1.9371765418006888, 2.175958985646636]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.0106685161590576})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7121265530586243})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5915877223014832})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6838688254356384})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6867566108703613})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7723463773727417})
store['active_learning_steps'][28]['training']['best_epoch']=3
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9, 'crossentropy': 0.5674359375}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.9215704202651978})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6595511436462402})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5421898365020752})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.5580370426177979})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.528364896774292})
store['active_learning_steps'][28]['eval_training']['best_epoch']=3
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 3795], ['id', 2000], ['id', 21058], ['id', 42201], ['id', 34318]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5816783053631165, 1.1016327434665572, 1.5424642863489098, 1.843413041308299, 2.0434023617818493]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.006643295288086})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8143594264984131})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7094164490699768})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7751258611679077})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7576858997344971})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8822169303894043})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7205502986907959})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7209950685501099})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7522715330123901})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8779698610305786})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7568731307983398})
store['active_learning_steps'][29]['training']['best_epoch']=8
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9084, 'crossentropy': 0.70225400390625}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.0003032684326172})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7440053224563599})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6185956001281738})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5890556573867798})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5306589603424072})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5235332250595093})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5363156795501709})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.49984800815582275})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5068707466125488})
store['active_learning_steps'][29]['eval_training']['best_epoch']=6
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 3419], ['id', 10210], ['id', 20936], ['id', 5633], ['id', 18592]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7249347496689516, 1.3689294114800394, 1.8833774630856692, 2.228766936855991, 2.4580043042845308]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.0275005102157593})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6537573337554932})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6535943746566772})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5939277410507202})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6383464336395264})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6680829524993896})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6426039934158325})
store['active_learning_steps'][30]['training']['best_epoch']=4
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9099, 'crossentropy': 0.570323388671875}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.0592119693756104})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7017416954040527})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5700713396072388})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5365195870399475})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.529816746711731})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.4767192006111145})
store['active_learning_steps'][30]['eval_training']['best_epoch']=6
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 19590], ['id', 8447], ['id', 32977], ['id', 16268], ['id', 29886]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6097823265690991, 1.148677490338292, 1.6121461274052296, 1.9674410829858076, 2.2269307002832726]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.1491326093673706})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7597856521606445})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7014011144638062})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6137244701385498})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.644752562046051})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6121948957443237})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7851792573928833})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7083524465560913})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7635774612426758})
store['active_learning_steps'][31]['training']['best_epoch']=6
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9178, 'crossentropy': 0.583161962890625}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.102442741394043})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7038654685020447})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6550517082214355})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5383046865463257})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5744768381118774})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5047041177749634})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5313622951507568})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.4913490414619446})
store['active_learning_steps'][31]['eval_training']['best_epoch']=6
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 37440], ['id', 56128], ['id', 57307], ['id', 17558], ['ood', 48488]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.7457670217124248, 1.3666738890971697, 1.8588774351318493, 2.2103141994616236, 2.4486001766191494]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.1408910751342773})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8156699538230896})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6486616134643555})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5965154767036438})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6152375936508179})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6970769762992859})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6186597347259521})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.661912739276886})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6173309683799744})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.682691216468811})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6160542964935303})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6461520195007324})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.7214244604110718})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.7226439714431763})
store['active_learning_steps'][32]['training']['best_epoch']=11
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9192, 'crossentropy': 0.6333263671875}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.9897558689117432})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.652229368686676})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5259352326393127})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5034159421920776})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5005068778991699})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5212641954421997})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.48932233452796936})
store['active_learning_steps'][32]['eval_training']['best_epoch']=4
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 21025], ['id', 16749], ['id', 3392], ['id', 33404], ['id', 15352]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6478143199084503, 1.2454939965651377, 1.7343085261535642, 2.1286599394642973, 2.414080483885243]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.1248753070831299})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6743407249450684})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5815846920013428})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5769481658935547})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5815749168395996})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.575670599937439})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5764130353927612})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5902928113937378})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6174626350402832})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6402836441993713})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.678197979927063})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7108429670333862})
store['active_learning_steps'][33]['training']['best_epoch']=9
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9189, 'crossentropy': 0.596329345703125}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.0247554779052734})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6737164855003357})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5445324778556824})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.562849223613739})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5182675123214722})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5132158994674683})
store['active_learning_steps'][33]['eval_training']['best_epoch']=3
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 29839], ['id', 54893], ['id', 42206], ['id', 49282], ['id', 54195]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6853494820284407, 1.291966679605688, 1.7561228880743989, 2.115778743249535, 2.345556053904661]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.1438517570495605})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7789245843887329})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6892023682594299})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7129898071289062})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6589126586914062})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6359027624130249})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6689571738243103})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.741072416305542})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6847817897796631})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6202982664108276})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6479078531265259})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6997215747833252})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8565581440925598})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.8060308694839478})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8376840353012085})
store['active_learning_steps'][34]['training']['best_epoch']=12
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9174, 'crossentropy': 0.658122509765625}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.0344318151474})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6214438080787659})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5616915225982666})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5164471864700317})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.47117021679878235})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.48779332637786865})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4709808826446533})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5037250518798828})
store['active_learning_steps'][34]['eval_training']['best_epoch']=5
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 6336], ['id', 9428], ['id', 31827], ['id', 19044], ['id', 5854]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6428484100011274, 1.2333422269943557, 1.7460850743372127, 2.175387213247941, 2.457148598371098]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.302464246749878})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6882976293563843})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6476866602897644})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6309303045272827})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4997101426124573})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5993523597717285})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5831845998764038})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5706523656845093})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5767852067947388})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5590953826904297})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5695629119873047})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6010092496871948})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6592167615890503})
store['active_learning_steps'][35]['training']['best_epoch']=10
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9218, 'crossentropy': 0.5587498046875}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.1039026975631714})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.627126932144165})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5472189784049988})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5341963171958923})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5533885359764099})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.44955551624298096})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.4871266484260559})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4875805377960205})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.45874443650245667})
store['active_learning_steps'][35]['eval_training']['best_epoch']=6
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 7434], ['id', 36072], ['id', 34765], ['id', 10690], ['id', 37636]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5988874959578193, 1.1423851719196834, 1.5944739225461464, 1.9264804787317087, 2.164365397119534]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.0498754978179932})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6967206001281738})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5822852849960327})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5944638252258301})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5885061025619507})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5114368796348572})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5542358160018921})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6255786418914795})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.548659086227417})
store['active_learning_steps'][36]['training']['best_epoch']=6
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9263, 'crossentropy': 0.48088037109375}
