store = {}
store['timestamp']=1620258024
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=8']
store['commit']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['github_url']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=8
store['worker_id']=8
store['num_workers']=40
store['config']={'seed': 10, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 50, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.4238171577453613})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.956916570663452})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.213360548019409})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.2559003829956055})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6568, 'crossentropy': 2.223854296875}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 21179], ['id', 865], ['id', 53170], ['id', 8365], ['id', 11546]], 'labels': [3, 8, 8, 8, 8], 'scores': [0.3854817748069763, 0.9375869035720825, 0.9042413234710693, 0.8687103390693665, 0.7878560423851013]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.1635046005249023})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.257805824279785})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.465391159057617})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 3.0824618339538574})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7249, 'crossentropy': 1.891362890625}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 26210], ['id', 48356], ['ood', 59080], ['id', 21399], ['id', 11957]], 'labels': [0, 2, 4, 8, 0], 'scores': [0.8470268249511719, 0.9600033164024353, 0.5641493797302246, 0.8678950071334839, 0.9380927681922913]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.6935917139053345})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.137482166290283})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.465665817260742})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.417635917663574})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6949, 'crossentropy': 1.59673369140625}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 1881], ['id', 18672], ['id', 50111], ['id', 5791], ['id', 23261]], 'labels': [2, 6, 5, 8, 6], 'scores': [0.6618156433105469, 0.7317448854446411, 0.7903085350990295, 0.42026740312576294, 0.745387852191925]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.617330551147461})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.9741477966308594})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.7198086977005005})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.899423599243164})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7257, 'crossentropy': 1.48187822265625}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 55586], ['id', 41580], ['id', 53515], ['id', 43761], ['id', 42821]], 'labels': [8, 4, 9, 1, 2], 'scores': [0.7006638646125793, 0.7622795104980469, 0.6992430090904236, 0.5297017693519592, 0.6786815524101257]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.3469818830490112})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.6172130107879639})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.817425012588501})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.8625341653823853})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7656, 'crossentropy': 1.2347435546875}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 12637], ['id', 40151], ['id', 20312], ['id', 53150], ['id', 2395]], 'labels': [5, 2, 7, 8, 5], 'scores': [0.6129553914070129, 0.5672767758369446, 0.5563309192657471, 0.6180980205535889, 0.8210371136665344]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.413909912109375})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.5431091785430908})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.7660847902297974})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.574774980545044})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7795, 'crossentropy': 1.23074423828125}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 3009], ['id', 35371], ['id', 4666], ['id', 23583], ['id', 18535]], 'labels': [4, 7, 5, 4, 2], 'scores': [0.6308645606040955, 0.6761492490768433, 0.7674664556980133, 0.6222922205924988, 0.7650139927864075]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.4522449970245361})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.4831295013427734})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.5682260990142822})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.8215973377227783})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7772, 'crossentropy': 1.30497451171875}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 45597], ['id', 21993], ['id', 19367], ['id', 55066], ['id', 58270]], 'labels': [3, 3, 8, 6, 5], 'scores': [0.7679145932197571, 0.8124117255210876, 0.7708624601364136, 0.6576001644134521, 0.8168990015983582]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.1835238933563232})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.1928234100341797})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.3799793720245361})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.287419319152832})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7975, 'crossentropy': 1.09056591796875}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 826], ['id', 56669], ['id', 17540], ['id', 28329], ['id', 1222]], 'labels': [9, 5, 1, 9, 5], 'scores': [0.785320520401001, 0.8066675662994385, 0.8205810785293579, 0.5268127918243408, 0.41303157806396484]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.0219272375106812})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.0212432146072388})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.2307854890823364})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.19413423538208})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.4315590858459473})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8553, 'crossentropy': 0.89304033203125}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 52616], ['id', 25891], ['id', 24998], ['id', 49841], ['id', 42898]], 'labels': [1, 5, 9, 3, 3], 'scores': [0.691565752029419, 0.7718647718429565, 0.6119300723075867, 0.8761134743690491, 0.5510662198066711]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.8981392979621887})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9037793874740601})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.005666971206665})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9657936096191406})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8549, 'crossentropy': 0.8279171875}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 24169], ['id', 3490], ['id', 53266], ['id', 7909], ['id', 46546]], 'labels': [4, 0, 2, 8, 2], 'scores': [0.396109402179718, 0.7183979749679565, 0.5127173662185669, 0.5764110684394836, 0.5024300813674927]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.9208768606185913})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.0860908031463623})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.122537612915039})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.0868823528289795})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8459, 'crossentropy': 0.82362314453125}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 19345], ['id', 27419], ['id', 12937], ['id', 7283], ['id', 39034]], 'labels': [2, 3, 5, 3, 9], 'scores': [0.5786677002906799, 0.6264088749885559, 0.484677791595459, 0.5394461154937744, 0.5432142019271851]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8652790784835815})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8696836233139038})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.9149658679962158})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9991267919540405})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8639, 'crossentropy': 0.74646220703125}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 59795], ['id', 47743], ['id', 46888], ['id', 22497], ['id', 3791]], 'labels': [0, 2, 7, 7, 2], 'scores': [0.5425423383712769, 0.5295358896255493, 0.5772430896759033, 0.6811670064926147, 0.8681771755218506]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.877292275428772})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.921453058719635})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8883364200592041})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.963614821434021})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8588, 'crossentropy': 0.772460009765625}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 47211], ['id', 19597], ['id', 4955], ['id', 35718], ['id', 57345]], 'labels': [4, 9, 2, 6, 5], 'scores': [0.43747377395629883, 0.5554842352867126, 0.7260172367095947, 0.48824459314346313, 0.7171425223350525]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.9648610353469849})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8814473152160645})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.0012619495391846})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.0302127599716187})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.1051839590072632})
store['active_learning_steps'][13]['training']['best_epoch']=2
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8756, 'crossentropy': 0.7531498046875}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 15713], ['id', 16550], ['id', 42715], ['ood', 52521], ['id', 29869]], 'labels': [1, 6, 9, 7, 0], 'scores': [0.9471851587295532, 0.7823034524917603, 1.0496017336845398, 0.4157869815826416, 0.7178287506103516]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8348221778869629})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8385634422302246})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8089748024940491})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8587305545806885})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9032775163650513})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9681910276412964})
store['active_learning_steps'][14]['training']['best_epoch']=3
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.894, 'crossentropy': 0.638177099609375}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 25661], ['id', 43518], ['id', 13161], ['id', 29002], ['id', 23430]], 'labels': [8, 6, 3, 7, 7], 'scores': [0.8074166774749756, 0.6899909377098083, 0.6496487259864807, 0.7149505019187927, 0.774150550365448]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8705182671546936})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6565406918525696})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6293555498123169})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.703189492225647})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7230340242385864})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7405052185058594})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9171, 'crossentropy': 0.532746826171875}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 48202], ['id', 15893], ['id', 20283], ['id', 41340], ['id', 6347]], 'labels': [4, 5, 0, 2, 3], 'scores': [0.3759603500366211, 0.8073447346687317, 0.5990653038024902, 0.6087085008621216, 0.6531240344047546]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8376071453094482})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6781632304191589})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7633860111236572})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7928996086120605})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.8174175024032593})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9047, 'crossentropy': 0.57944853515625}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 48880], ['id', 26452], ['id', 39573], ['id', 23861], ['ood', 1426]], 'labels': [4, 6, 5, 5, 5], 'scores': [0.7548273205757141, 0.6014707088470459, 0.7612210512161255, 0.6854848265647888, 0.5503000020980835]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8420905470848083})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6425120830535889})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7179662585258484})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7237249612808228})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7542910575866699})
store['active_learning_steps'][17]['training']['best_epoch']=2
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9076, 'crossentropy': 0.5663890625}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 13256], ['ood', 5293], ['id', 49472], ['id', 50086], ['id', 39546]], 'labels': [5, 7, 7, 6, 1], 'scores': [0.5159764885902405, 0.40989625453948975, 0.7430951595306396, 0.7796120047569275, 0.597288966178894]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.8298025131225586})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6532957553863525})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6512879729270935})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7057419419288635})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7515369653701782})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7595181465148926})
store['active_learning_steps'][18]['training']['best_epoch']=3
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9143, 'crossentropy': 0.548119873046875}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 20606], ['id', 1473], ['id', 4459], ['id', 17079], ['id', 41999]], 'labels': [3, 4, 9, 6, 0], 'scores': [0.7977957725524902, 0.37367701530456543, 0.7577367424964905, 0.8057619333267212, 0.7108844518661499]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7486702799797058})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6236436367034912})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5834695100784302})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.637661337852478})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6777546405792236})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6629147529602051})
store['active_learning_steps'][19]['training']['best_epoch']=3
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.919, 'crossentropy': 0.52859736328125}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 25873], ['id', 49464], ['id', 29667], ['id', 52669], ['id', 13149]], 'labels': [8, 9, 2, 7, 7], 'scores': [0.6851921081542969, 0.5582330822944641, 0.8239559531211853, 0.7485647201538086, 0.7212367057800293]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8167204856872559})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5962203145027161})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6266767382621765})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6814969182014465})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6235904693603516})
store['active_learning_steps'][20]['training']['best_epoch']=2
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9133, 'crossentropy': 0.557330126953125}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 19596], ['id', 49088], ['id', 42963], ['id', 5684], ['id', 33306]], 'labels': [9, 8, 9, 6, 4], 'scores': [0.6626662611961365, 0.7271930575370789, 0.586584210395813, 0.691280722618103, 0.6376701593399048]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7322359085083008})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5528711080551147})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5084893703460693})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6475151777267456})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6393100619316101})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6632410287857056})
store['active_learning_steps'][21]['training']['best_epoch']=3
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9241, 'crossentropy': 0.4927380859375}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 8447], ['id', 18102], ['id', 17057], ['id', 17553], ['id', 52722]], 'labels': [3, 0, 4, 3, 8], 'scores': [0.8165892362594604, 0.7428800463676453, 0.8735587894916534, 0.7071359753608704, 0.5743230581283569]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7588844299316406})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.579514741897583})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.549290120601654})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5268646478652954})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6238474249839783})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6419609189033508})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6220697164535522})
store['active_learning_steps'][22]['training']['best_epoch']=4
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9236, 'crossentropy': 0.502566845703125}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 15013], ['ood', 12710], ['id', 43176], ['id', 13524], ['id', 25116]], 'labels': [2, 1, 2, 3, 3], 'scores': [0.7461996078491211, 0.4815887212753296, 0.7548678815364838, 0.8880525231361389, 0.6749259829521179]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8267437815666199})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5852423906326294})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6195306181907654})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5846784114837646})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6019057035446167})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6312879323959351})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6456534266471863})
store['active_learning_steps'][23]['training']['best_epoch']=4
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9212, 'crossentropy': 0.53193115234375}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 49196], ['id', 54556], ['id', 32348], ['id', 25315], ['id', 29130]], 'labels': [4, 2, 5, 5, 4], 'scores': [0.5797293186187744, 0.9555011987686157, 1.0378535389900208, 0.839743971824646, 0.6381325721740723]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8646059036254883})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.521578311920166})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4869817793369293})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5177161693572998})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5197808146476746})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6024600267410278})
store['active_learning_steps'][24]['training']['best_epoch']=3
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9366, 'crossentropy': 0.45606533203125}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 22903], ['id', 33650], ['id', 11767], ['id', 24613], ['id', 35991]], 'labels': [3, 4, 4, 9, 9], 'scores': [0.6719053685665131, 0.5948201417922974, 0.6986696124076843, 0.5920053720474243, 0.5965932011604309]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8264783024787903})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5542513728141785})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5278191566467285})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5275846719741821})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.553098738193512})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5737869739532471})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5711719989776611})
store['active_learning_steps'][25]['training']['best_epoch']=4
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9349, 'crossentropy': 0.4623375}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 18003], ['id', 54905], ['id', 21550], ['id', 33338], ['id', 3051]], 'labels': [2, 9, 5, 8, 3], 'scores': [0.917707085609436, 0.7196585536003113, 0.6887894868850708, 0.8448431491851807, 0.6925446689128876]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7878891229629517})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.551129937171936})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5256226062774658})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5005173683166504})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4833347201347351})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5683795213699341})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5589584112167358})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5320135354995728})
store['active_learning_steps'][26]['training']['best_epoch']=5
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9383, 'crossentropy': 0.446062890625}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 29294], ['id', 4646], ['id', 8892], ['id', 44586], ['id', 40483]], 'labels': [3, 2, 8, 9, 3], 'scores': [1.058724820613861, 0.6321620941162109, 0.776655375957489, 0.7300071120262146, 0.8380566239356995]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8871074914932251})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5075801610946655})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.48859360814094543})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.47123825550079346})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5140224695205688})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5156236886978149})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5407074093818665})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.94, 'crossentropy': 0.43349150390625}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 1364], ['id', 8954], ['id', 28420], ['id', 19037], ['id', 9543]], 'labels': [9, 7, 1, 6, 8], 'scores': [1.0434412956237793, 0.8200825750827789, 0.6156379580497742, 0.7548795938491821, 0.5227784514427185]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9542397856712341})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5720560550689697})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.48095884919166565})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4929956793785095})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5288487076759338})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.477455735206604})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.49601981043815613})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5101375579833984})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5659785270690918})
store['active_learning_steps'][28]['training']['best_epoch']=6
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9409, 'crossentropy': 0.466081591796875}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 11351], ['id', 56314], ['id', 26166], ['id', 57379], ['id', 57931]], 'labels': [8, 5, 4, 8, 1], 'scores': [0.6886378526687622, 0.7061306238174438, 0.5326305329799652, 0.9786101579666138, 0.6852424144744873]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8927541971206665})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5285696983337402})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.46863025426864624})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4754658341407776})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.46522119641304016})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4703025221824646})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4235847592353821})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5049530863761902})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5227342247962952})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4855891466140747})
store['active_learning_steps'][29]['training']['best_epoch']=7
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9408, 'crossentropy': 0.40882734375}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 39409], ['id', 33804], ['id', 50878], ['id', 29153], ['id', 14333]], 'labels': [5, 2, 7, 3, 3], 'scores': [0.8471351265907288, 0.9958469569683075, 0.9477276802062988, 0.8658257126808167, 0.9541146457195282]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8213318586349487})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.495650053024292})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.455868661403656})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.44248101115226746})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.41362690925598145})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.40671324729919434})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.44592928886413574})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4095023274421692})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.41776764392852783})
store['active_learning_steps'][30]['training']['best_epoch']=6
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9465, 'crossentropy': 0.3649542236328125}
store['active_learning_steps'][30]['acquisition']={'indices': [['ood', 20587], ['id', 49222], ['id', 59786], ['id', 6220], ['id', 29189]], 'labels': [8, 3, 0, 4, 8], 'scores': [0.343194842338562, 0.8882465958595276, 0.8845316767692566, 0.6708922386169434, 0.8614842891693115]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8723959922790527})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4640843868255615})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4125739336013794})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.38125255703926086})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.40398699045181274})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.36018818616867065})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.435386598110199})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4080921411514282})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.42411014437675476})
store['active_learning_steps'][31]['training']['best_epoch']=6
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9537, 'crossentropy': 0.3452447509765625}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 46895], ['id', 34678], ['id', 12972], ['id', 58832], ['id', 38420]], 'labels': [5, 8, 4, 3, 8], 'scores': [0.6789993941783905, 0.7988486289978027, 0.4191606640815735, 0.9833222031593323, 0.8596857190132141]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8956671357154846})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5212585926055908})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.43735435605049133})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4269794523715973})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3972473740577698})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.36796796321868896})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4428326487541199})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4452725946903229})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.42917174100875854})
store['active_learning_steps'][32]['training']['best_epoch']=6
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9527, 'crossentropy': 0.3460598876953125}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 27299], ['id', 12066], ['id', 3254], ['id', 24457], ['id', 14271]], 'labels': [8, 8, 8, 8, 1], 'scores': [0.7283167839050293, 0.832632839679718, 0.9033801853656769, 0.9042717218399048, 0.6817671358585358]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8992359638214111})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5471038818359375})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4813864529132843})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.44952720403671265})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.43756574392318726})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4484702944755554})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.45198357105255127})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5273337960243225})
store['active_learning_steps'][33]['training']['best_epoch']=5
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9443, 'crossentropy': 0.401357275390625}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 26852], ['id', 38920], ['ood', 45919], ['id', 45484], ['id', 40064]], 'labels': [8, 7, 5, 2, 8], 'scores': [0.8993189930915833, 0.9361088275909424, 0.5539017915725708, 0.800663411617279, 0.5850189328193665]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.008487343788147})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5030025243759155})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.48460856080055237})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4719924330711365})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4473723769187927})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.438498318195343})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.47003650665283203})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4508718252182007})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4729953408241272})
store['active_learning_steps'][34]['training']['best_epoch']=6
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.949, 'crossentropy': 0.3848432861328125}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 49658], ['id', 137], ['id', 40654], ['id', 23982], ['id', 59289]], 'labels': [5, 8, 5, 2, 1], 'scores': [0.9728471040725708, 0.6609225273132324, 0.856105625629425, 0.6008756160736084, 1.0199707746505737]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.9603880643844604})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5576010346412659})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4263477921485901})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4671265482902527})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.43073520064353943})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.41684281826019287})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.42587706446647644})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4655860364437103})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.48299556970596313})
store['active_learning_steps'][35]['training']['best_epoch']=6
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9485, 'crossentropy': 0.38048642578125}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 46622], ['id', 49509], ['id', 20388], ['id', 36704], ['id', 45024]], 'labels': [4, 8, 0, 2, 5], 'scores': [0.605840802192688, 0.8460180163383484, 0.8308550715446472, 0.7221234440803528, 0.7100036144256592]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9448699951171875})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4765031933784485})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.37754368782043457})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.39600732922554016})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.39447781443595886})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.36588048934936523})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.41484495997428894})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.42438656091690063})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.40276801586151123})
store['active_learning_steps'][36]['training']['best_epoch']=6
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.947, 'crossentropy': 0.35181455078125}
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 47749], ['id', 46126], ['id', 52814], ['id', 14896], ['id', 34188]], 'labels': [3, 3, 9, 8, 3], 'scores': [0.776383638381958, 1.0897533893585205, 0.6021237373352051, 0.987948477268219, 0.798616886138916]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.9434112310409546})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5189560055732727})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.41471433639526367})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.37620359659194946})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.397638738155365})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3935587704181671})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.41467225551605225})
store['active_learning_steps'][37]['training']['best_epoch']=4
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9459, 'crossentropy': 0.3782189697265625}
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 41738], ['id', 19868], ['id', 54883], ['id', 51582], ['id', 17365]], 'labels': [9, 5, 5, 9, 0], 'scores': [0.5426565408706665, 0.6412052512168884, 0.7517563104629517, 0.53628009557724, 0.7396380305290222]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9303129315376282})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5623350143432617})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4339577555656433})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.39556601643562317})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.36706140637397766})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3980000615119934})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.37626272439956665})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4137895703315735})
store['active_learning_steps'][38]['training']['best_epoch']=5
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9524, 'crossentropy': 0.3500294677734375}
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 17958], ['id', 36047], ['ood', 50747], ['id', 12792], ['id', 48480]], 'labels': [9, 0, 5, 9, 3], 'scores': [0.9567072987556458, 0.5280601978302002, 0.3339838981628418, 0.8493945598602295, 0.7227050065994263]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.073866367340088})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5319377779960632})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4579962491989136})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3998168706893921})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.39978688955307007})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3740742802619934})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.39789775013923645})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3781210482120514})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4075062870979309})
store['active_learning_steps'][39]['training']['best_epoch']=6
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.95, 'crossentropy': 0.3471188232421875}
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 26422], ['id', 44130], ['id', 44013], ['id', 52478], ['ood', 7642]], 'labels': [0, 0, 4, 9, 7], 'scores': [0.8016559481620789, 0.3373231589794159, 0.733849048614502, 0.735007107257843, 0.24949705600738525]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.0287035703659058})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5449934005737305})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.39494645595550537})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4148736596107483})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.384938508272171})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.41823989152908325})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3841056525707245})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3953981399536133})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.42433321475982666})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4617096185684204})
store['active_learning_steps'][40]['training']['best_epoch']=7
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9453, 'crossentropy': 0.3781140380859375}
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 37584], ['id', 47328], ['id', 45917], ['id', 53854], ['id', 23321]], 'labels': [5, 8, 9, 8, 6], 'scores': [0.8488113880157471, 0.7489184737205505, 0.6171773076057434, 0.9996114373207092, 0.637671172618866]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9158880710601807})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5258723497390747})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.42039304971694946})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4164259433746338})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.39743828773498535})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.36659619212150574})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.38473039865493774})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.37522295117378235})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3800811171531677})
store['active_learning_steps'][41]['training']['best_epoch']=6
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.952, 'crossentropy': 0.353060791015625}
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 23008], ['ood', 5073], ['id', 55743], ['ood', 21738], ['id', 57523]], 'labels': [8, 8, 3, 9, 3], 'scores': [0.8018773198127747, 0.49560487270355225, 0.9934723973274231, 0.4806286096572876, 0.7519960403442383]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9274297952651978})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5510810613632202})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.40255916118621826})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3907182812690735})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.37723881006240845})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3782352805137634})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.412792831659317})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.37535497546195984})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3849349021911621})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.38637876510620117})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.45034778118133545})
store['active_learning_steps'][42]['training']['best_epoch']=8
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9492, 'crossentropy': 0.3773563232421875}
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 29886], ['id', 30016], ['id', 36417], ['id', 14695], ['id', 9266]], 'labels': [8, 4, 6, 4, 2], 'scores': [0.5986646413803101, 0.6020697951316833, 0.9830919504165649, 0.7644460797309875, 0.852508008480072]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.0245476961135864})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5762315988540649})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4293500781059265})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.37442445755004883})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.42818939685821533})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.39599454402923584})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.37105828523635864})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.44000914692878723})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.39665302634239197})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.38871967792510986})
store['active_learning_steps'][43]['training']['best_epoch']=7
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.947, 'crossentropy': 0.3821091552734375}
store['active_learning_steps'][43]['acquisition']={'indices': [['id', 26214], ['id', 29899], ['id', 40084], ['id', 52550], ['id', 33198]], 'labels': [9, 3, 2, 2, 8], 'scores': [0.794479250907898, 0.9547035694122314, 0.9531828165054321, 0.8137542307376862, 0.6128761172294617]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.024434208869934})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5315412878990173})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4045107364654541})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4484804570674896})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.39816319942474365})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3874327540397644})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4202460050582886})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.41536810994148254})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.43045344948768616})
store['active_learning_steps'][44]['training']['best_epoch']=6
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.9488, 'crossentropy': 0.3644848876953125}
store['active_learning_steps'][44]['acquisition']={'indices': [['id', 42687], ['id', 52462], ['id', 25748], ['id', 59314], ['id', 24360]], 'labels': [5, 9, 7, 9, 2], 'scores': [0.7329992651939392, 1.1008274555206299, 0.7839629054069519, 1.0057048797607422, 0.7412975430488586]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9858261346817017})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.47257518768310547})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4320252239704132})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.37929052114486694})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3968171775341034})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.36990678310394287})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3510957956314087})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3856106400489807})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.39585942029953003})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.39963313937187195})
store['active_learning_steps'][45]['training']['best_epoch']=7
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.9517, 'crossentropy': 0.3455852783203125}
store['active_learning_steps'][45]['acquisition']={'indices': [['id', 52927], ['id', 53746], ['id', 35232], ['id', 13709], ['id', 18720]], 'labels': [1, 1, 8, 6, 7], 'scores': [0.6660507321357727, 0.6521533131599426, 0.8125500082969666, 0.6762731075286865, 0.5413553714752197]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8995357751846313})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.478492796421051})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.37986069917678833})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3742046356201172})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.35471540689468384})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3608238101005554})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3829069137573242})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3686990737915039})
store['active_learning_steps'][46]['training']['best_epoch']=5
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.947, 'crossentropy': 0.3509068603515625}
store['active_learning_steps'][46]['acquisition']={'indices': [['id', 45944], ['id', 38726], ['id', 57334], ['id', 8435], ['id', 14205]], 'labels': [9, 5, 7, 5, 3], 'scores': [0.8375686407089233, 0.5470064878463745, 0.7679857611656189, 0.702285647392273, 0.43852049112319946]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.9190255403518677})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5693041086196899})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.47782260179519653})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.36174625158309937})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3620530962944031})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.406826376914978})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.38415664434432983})
store['active_learning_steps'][47]['training']['best_epoch']=4
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.9531, 'crossentropy': 0.3292727294921875}
store['active_learning_steps'][47]['acquisition']={'indices': [['id', 31742], ['id', 58871], ['id', 36783], ['id', 20869], ['id', 7793]], 'labels': [7, 5, 0, 3, 8], 'scores': [0.6488009691238403, 0.6462162733078003, 0.6278576254844666, 0.7832834124565125, 0.6296807527542114]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.0536651611328125})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4906688332557678})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.39649003744125366})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3597519099712372})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.369188129901886})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.35809528827667236})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3207305073738098})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3418937921524048})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3517005443572998})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.38151252269744873})
store['active_learning_steps'][48]['training']['best_epoch']=7
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.9576, 'crossentropy': 0.301450390625}
store['active_learning_steps'][48]['acquisition']={'indices': [['id', 23358], ['id', 52219], ['id', 36398], ['id', 50317], ['id', 49728]], 'labels': [6, 8, 7, 3, 5], 'scores': [0.6415485739707947, 0.5562355518341064, 0.7197275161743164, 0.6968104839324951, 0.8249814510345459]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.0124104022979736})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.549801766872406})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4074232578277588})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.38385576009750366})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3512628674507141})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3312368392944336})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.36789512634277344})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3710615634918213})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3559338450431824})
store['active_learning_steps'][49]['training']['best_epoch']=6
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.9547, 'crossentropy': 0.3104775634765625}
store['active_learning_steps'][49]['acquisition']={'indices': [['id', 48380], ['id', 53647], ['id', 41529], ['id', 51568], ['id', 28844]], 'labels': [6, 5, 8, 7, 2], 'scores': [0.7017035186290741, 0.6607510447502136, 0.49021410942077637, 0.5400205254554749, 0.6882023215293884]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.9042272567749023})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.455345094203949})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3603064715862274})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3551645874977112})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3366203010082245})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3220430016517639})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.32803064584732056})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3361288905143738})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3288838863372803})
store['active_learning_steps'][50]['training']['best_epoch']=6
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.9552, 'crossentropy': 0.291729638671875}
store['active_learning_steps'][50]['acquisition']={'indices': [['id', 20005], ['id', 55218], ['id', 31252], ['id', 37070], ['id', 50491]], 'labels': [6, 8, 5, 5, 3], 'scores': [0.6195787489414215, 0.753614604473114, 0.8645902872085571, 0.6509361863136292, 0.4426664113998413]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.9335103034973145})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5845748782157898})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4357043504714966})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3797762393951416})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.35075366497039795})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3660410940647125})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.37545424699783325})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3801936209201813})
store['active_learning_steps'][51]['training']['best_epoch']=5
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.9494, 'crossentropy': 0.342028515625}
store['active_learning_steps'][51]['acquisition']={'indices': [['id', 39668], ['id', 14619], ['id', 43560], ['id', 11240], ['id', 12188]], 'labels': [8, 3, 5, 0, 7], 'scores': [0.6972854733467102, 0.6444973349571228, 0.7879832983016968, 0.6630545258522034, 0.6554523706436157]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.0473110675811768})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5463124513626099})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.40131276845932007})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3487491011619568})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.35359352827072144})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.32330599427223206})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.35195261240005493})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3388664424419403})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33420687913894653})
store['active_learning_steps'][52]['training']['best_epoch']=6
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.9592, 'crossentropy': 0.2955988037109375}
store['active_learning_steps'][52]['acquisition']={'indices': [['ood', 28298], ['id', 17011], ['id', 26842], ['id', 892], ['id', 16678]], 'labels': [3, 6, 5, 6, 3], 'scores': [0.5562498569488525, 0.7411178946495056, 0.5778350830078125, 0.5496537685394287, 0.6036909222602844]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.9167006015777588})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.48098278045654297})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.40399831533432007})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.35408610105514526})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3525846004486084})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3289252519607544})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3677888810634613})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3607551157474518})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.35131311416625977})
store['active_learning_steps'][53]['training']['best_epoch']=6
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.957, 'crossentropy': 0.2895908447265625}
store['active_learning_steps'][53]['acquisition']={'indices': [['id', 17012], ['id', 44234], ['id', 23604], ['id', 8709], ['id', 33974]], 'labels': [1, 9, 1, 3, 9], 'scores': [0.5958424806594849, 0.6853286623954773, 0.5019888877868652, 0.6389466524124146, 0.5271027088165283]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9340921640396118})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4815513491630554})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.412279337644577})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.33065375685691833})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.31402501463890076})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3370780348777771})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2989423871040344})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.321807861328125})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3253524899482727})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3334190249443054})
store['active_learning_steps'][54]['training']['best_epoch']=7
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.9619, 'crossentropy': 0.2741108642578125}
store['active_learning_steps'][54]['acquisition']={'indices': [['ood', 31294], ['id', 36072], ['id', 2622], ['id', 45455], ['ood', 25158]], 'labels': [8, 2, 5, 0, 5], 'scores': [0.540279746055603, 0.8743096590042114, 0.8818619847297668, 0.6123430728912354, 0.4503171443939209]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.1686716079711914})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6539570689201355})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4485883116722107})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4091406464576721})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.37772271037101746})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4031936526298523})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.38033369183540344})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3675234913825989})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3340415954589844})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.37459421157836914})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.43033111095428467})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35546791553497314})
store['active_learning_steps'][55]['training']['best_epoch']=9
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.9559, 'crossentropy': 0.3288219970703125}
store['active_learning_steps'][55]['acquisition']={'indices': [['id', 346], ['id', 21674], ['id', 35420], ['id', 21601], ['id', 7954]], 'labels': [9, 2, 5, 1, 0], 'scores': [0.691646933555603, 0.7176538109779358, 0.7920358777046204, 0.857606053352356, 0.8346596360206604]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 1.0252114534378052})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.536359429359436})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3893158733844757})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.36699768900871277})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3701298236846924})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.38837915658950806})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3465997576713562})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3706926107406616})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3588239550590515})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.38954758644104004})
store['active_learning_steps'][56]['training']['best_epoch']=7
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.9525, 'crossentropy': 0.3341655517578125}
store['active_learning_steps'][56]['acquisition']={'indices': [['id', 20169], ['id', 42973], ['id', 8093], ['id', 31466], ['id', 22094]], 'labels': [4, 4, 0, 0, 7], 'scores': [0.678372859954834, 0.6523557305335999, 0.8071249723434448, 0.8174474835395813, 0.6934028267860413]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.0173084735870361})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5547279119491577})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3849615156650543})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3864845037460327})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.34428870677948})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3331679701805115})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3369162082672119})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3548135757446289})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3471032977104187})
store['active_learning_steps'][57]['training']['best_epoch']=6
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.9606, 'crossentropy': 0.295920556640625}
store['active_learning_steps'][57]['acquisition']={'indices': [['id', 47255], ['id', 35688], ['id', 22824], ['id', 41433], ['id', 30011]], 'labels': [2, 3, 9, 9, 3], 'scores': [0.7934731841087341, 0.7181794047355652, 0.7979743480682373, 0.6500411629676819, 0.7819139361381531]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.0195086002349854})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5331017971038818})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4341779351234436})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.36623626947402954})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3343372344970703})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3090020418167114})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3329554796218872})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3335411548614502})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3342628479003906})
store['active_learning_steps'][58]['training']['best_epoch']=6
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.9626, 'crossentropy': 0.279422412109375}
store['active_learning_steps'][58]['acquisition']={'indices': [['id', 10044], ['id', 22859], ['id', 59747], ['id', 25310], ['id', 34771]], 'labels': [6, 1, 5, 1, 0], 'scores': [0.632780522108078, 0.526069164276123, 0.8237926363945007, 0.5977010726928711, 0.44443321228027344]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.2497813701629639})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6073112487792969})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4424380660057068})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.36108115315437317})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.35805821418762207})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3435620963573456})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31423547863960266})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33088135719299316})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.30022725462913513})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3098103404045105})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32451069355010986})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3395572304725647})
store['active_learning_steps'][59]['training']['best_epoch']=9
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.9624, 'crossentropy': 0.2804699951171875}
store['active_learning_steps'][59]['acquisition']={'indices': [['id', 17486], ['id', 21956], ['id', 47914], ['id', 50840], ['id', 58060]], 'labels': [7, 5, 0, 2, 2], 'scores': [0.793304443359375, 0.7202484011650085, 1.037247359752655, 0.8559143543243408, 0.5892377495765686]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.1043426990509033})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4962528944015503})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4294014573097229})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3435364365577698})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31193816661834717})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31555432081222534})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3220028281211853})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3207288384437561})
store['active_learning_steps'][60]['training']['best_epoch']=5
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.9581, 'crossentropy': 0.2891817626953125}
store['active_learning_steps'][60]['acquisition']={'indices': [['id', 14288], ['id', 32906], ['id', 31301], ['id', 1674], ['id', 22083]], 'labels': [7, 7, 5, 9, 2], 'scores': [0.4922260046005249, 0.5698196887969971, 0.7806105613708496, 0.9063017964363098, 0.7692464590072632]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.0211317539215088})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5704367160797119})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4090615212917328})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.34864431619644165})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3509563207626343})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3533390462398529})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3390814960002899})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.36263224482536316})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3468596339225769})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34576845169067383})
store['active_learning_steps'][61]['training']['best_epoch']=7
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.9618, 'crossentropy': 0.3003392578125}
store['active_learning_steps'][61]['acquisition']={'indices': [['id', 15276], ['id', 48649], ['id', 48154], ['id', 3367], ['id', 45300]], 'labels': [7, 6, 9, 0, 6], 'scores': [0.6924906969070435, 0.712853342294693, 0.6864652633666992, 0.8216434717178345, 0.5676878094673157]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 1.073430061340332})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5409283638000488})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3840259313583374})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.37136250734329224})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3245801329612732})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2823900580406189})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3384453058242798})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.32240554690361023})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2991825342178345})
store['active_learning_steps'][62]['training']['best_epoch']=6
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.9583, 'crossentropy': 0.2861059814453125}
store['active_learning_steps'][62]['acquisition']={'indices': [['id', 24662], ['id', 22561], ['id', 58892], ['ood', 28297], ['id', 43012]], 'labels': [7, 6, 3, 8, 3], 'scores': [0.6146190762519836, 0.6355717182159424, 0.6366474032402039, 0.4974496364593506, 0.6499006152153015]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.0712651014328003})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5174527764320374})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.45178642868995667})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3588023781776428})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.302948534488678})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3408423066139221})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3037160336971283})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3111703395843506})
store['active_learning_steps'][63]['training']['best_epoch']=5
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.9568, 'crossentropy': 0.3103843505859375}
store['active_learning_steps'][63]['acquisition']={'indices': [['id', 3762], ['id', 13590], ['id', 32206], ['id', 45972], ['id', 52650]], 'labels': [8, 1, 8, 2, 5], 'scores': [0.8608917593955994, 0.576789915561676, 0.5310332179069519, 0.5073672235012054, 0.612983763217926]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9743216633796692})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5197147727012634})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.39890214800834656})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3204272389411926})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3083552420139313})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3155944347381592})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.29625794291496277})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3225109577178955})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.27701616287231445})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3185570240020752})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.337482213973999})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3269657790660858})
store['active_learning_steps'][64]['training']['best_epoch']=9
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.9636, 'crossentropy': 0.26767216796875}
store['active_learning_steps'][64]['acquisition']={'indices': [['id', 9396], ['id', 18228], ['id', 31738], ['id', 28512], ['id', 33383]], 'labels': [2, 9, 8, 5, 1], 'scores': [0.7274749279022217, 0.5143536925315857, 0.7202854454517365, 0.7419546544551849, 0.5559499859809875]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.0378246307373047})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5401324033737183})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3965858221054077})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3795642852783203})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.31103992462158203})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32769349217414856})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3078402876853943})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.328934907913208})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33665186166763306})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3347508907318115})
store['active_learning_steps'][65]['training']['best_epoch']=7
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.9622, 'crossentropy': 0.282302783203125}
store['active_learning_steps'][65]['acquisition']={'indices': [['id', 4272], ['id', 49824], ['id', 4935], ['id', 52123], ['id', 6771]], 'labels': [8, 8, 2, 9, 2], 'scores': [0.4613837003707886, 0.6309734582901001, 0.7579504251480103, 0.6731480956077576, 0.616194486618042]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.3350872993469238})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6694755554199219})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.47246992588043213})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3725350499153137})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3685954213142395})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3411343991756439})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3163452744483948})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.29328298568725586})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3370818495750427})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.32398030161857605})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3435633182525635})
store['active_learning_steps'][66]['training']['best_epoch']=8
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.9636, 'crossentropy': 0.2832012939453125}
store['active_learning_steps'][66]['acquisition']={'indices': [['id', 32129], ['id', 1512], ['id', 43998], ['id', 23730], ['id', 228]], 'labels': [1, 0, 7, 3, 3], 'scores': [0.571150541305542, 0.7377549409866333, 0.6344394087791443, 0.5558681190013885, 0.7102466225624084]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.1347460746765137})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5600391626358032})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.40236181020736694})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3409847021102905})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.33501583337783813})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.33728891611099243})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3254029154777527})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29702478647232056})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3017912209033966})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3264387249946594})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32248830795288086})
store['active_learning_steps'][67]['training']['best_epoch']=8
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9627, 'crossentropy': 0.2782617431640625}
store['active_learning_steps'][67]['acquisition']={'indices': [['id', 38969], ['ood', 54813], ['id', 9428], ['id', 59294], ['id', 24424]], 'labels': [9, 8, 9, 8, 1], 'scores': [0.5497567653656006, 0.6276108026504517, 0.9293814897537231, 0.6734870672225952, 0.7258673906326294]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.2921643257141113})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.619462251663208})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4282759428024292})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3789355158805847})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3558536171913147})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35813093185424805})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3076222538948059})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3405947983264923})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.30620476603507996})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3263423442840576})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3555780351161957})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.30854982137680054})
store['active_learning_steps'][68]['training']['best_epoch']=9
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.9676, 'crossentropy': 0.2695468505859375}
store['active_learning_steps'][68]['acquisition']={'indices': [['id', 7984], ['ood', 17057], ['id', 28413], ['id', 24240], ['id', 16456]], 'labels': [4, 0, 5, 8, 2], 'scores': [0.6722645163536072, 0.31956207752227783, 0.5749809145927429, 0.8679502606391907, 0.9583037495613098]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.0303092002868652})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5702491998672485})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3942539095878601})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.35783448815345764})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.31256407499313354})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.30014485120773315})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.32937389612197876})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3138063848018646})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.34437742829322815})
store['active_learning_steps'][69]['training']['best_epoch']=6
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9607, 'crossentropy': 0.2794175048828125}
store['active_learning_steps'][69]['acquisition']={'indices': [['id', 20746], ['id', 50571], ['id', 5474], ['id', 20036], ['id', 25210]], 'labels': [1, 8, 8, 1, 3], 'scores': [0.5925310254096985, 0.644180953502655, 0.8018417954444885, 0.6865391731262207, 0.6407531499862671]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.0603370666503906})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5219129920005798})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4166952967643738})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3973121643066406})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.34841591119766235})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3278224468231201})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30920514464378357})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32615798711776733})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.29901254177093506})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3064233958721161})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3220707178115845})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3045880198478699})
store['active_learning_steps'][70]['training']['best_epoch']=9
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.9676, 'crossentropy': 0.2535281005859375}
store['active_learning_steps'][70]['acquisition']={'indices': [['id', 34785], ['id', 52959], ['id', 32391], ['id', 14210], ['id', 16989]], 'labels': [8, 2, 4, 3, 2], 'scores': [0.8585810661315918, 0.8565168976783752, 0.4999808371067047, 0.8564113974571228, 0.8495014309883118]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.0526056289672852})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.535426139831543})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.42820534110069275})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3433838486671448})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.326210081577301})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28606218099594116})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3154761791229248})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33748236298561096})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.30150306224823})
store['active_learning_steps'][71]['training']['best_epoch']=6
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9657, 'crossentropy': 0.2626124267578125}
store['active_learning_steps'][71]['acquisition']={'indices': [['id', 47220], ['id', 36017], ['id', 1704], ['id', 10674], ['id', 48460]], 'labels': [6, 4, 4, 3, 2], 'scores': [0.6821328997612, 0.5164942741394043, 0.536522388458252, 0.3949441909790039, 0.6469467282295227]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.152461051940918})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6184947490692139})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.43008923530578613})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.36294907331466675})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3287021219730377})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.349626362323761})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3290048837661743})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2882906496524811})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30853399634361267})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3049069046974182})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.28825104236602783})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3022080361843109})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30161619186401367})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.318012535572052})
store['active_learning_steps'][72]['training']['best_epoch']=11
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.9658, 'crossentropy': 0.2738150390625}
store['active_learning_steps'][72]['acquisition']={'indices': [['id', 31016], ['id', 37048], ['id', 19502], ['id', 18487], ['id', 52048]], 'labels': [2, 9, 2, 4, 0], 'scores': [0.45041340589523315, 0.8449205756187439, 0.8263819813728333, 0.9143847823143005, 0.8080745339393616]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.1203410625457764})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5365790128707886})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4113083481788635})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3345189094543457})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.34641265869140625})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32361656427383423})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2617891728878021})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29141664505004883})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2846779525279999})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.314655601978302})
store['active_learning_steps'][73]['training']['best_epoch']=7
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9666, 'crossentropy': 0.264907666015625}
store['active_learning_steps'][73]['acquisition']={'indices': [['id', 27223], ['id', 54181], ['id', 46048], ['id', 15937], ['id', 34802]], 'labels': [2, 9, 7, 3, 3], 'scores': [0.5050413310527802, 0.48723673820495605, 0.43053728342056274, 0.3618575930595398, 0.5130206942558289]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.2940409183502197})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6527221202850342})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.4004809260368347})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.34589195251464844})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.29354190826416016})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3076748251914978})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2998619079589844})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.27033698558807373})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31538236141204834})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2889971137046814})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3024902939796448})
store['active_learning_steps'][74]['training']['best_epoch']=8
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9661, 'crossentropy': 0.2610775146484375}
store['active_learning_steps'][74]['acquisition']={'indices': [['id', 24040], ['id', 19244], ['ood', 766], ['id', 56006], ['id', 57732]], 'labels': [7, 9, 6, 3, 9], 'scores': [0.6978279948234558, 0.7964335680007935, 0.19162726402282715, 0.7758986949920654, 0.6116816401481628]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.166321873664856})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.552528977394104})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4011313319206238})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3298051059246063})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.29178333282470703})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2911958694458008})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.27055710554122925})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2933726906776428})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.29451680183410645})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3011971712112427})
store['active_learning_steps'][75]['training']['best_epoch']=7
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9679, 'crossentropy': 0.2357984130859375}
store['active_learning_steps'][75]['acquisition']={'indices': [['id', 24062], ['id', 29440], ['id', 22259], ['id', 42209], ['id', 36421]], 'labels': [9, 7, 7, 9, 3], 'scores': [0.6397757530212402, 0.7851965427398682, 0.4818125367164612, 0.4308406114578247, 0.596707284450531]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.0331376791000366})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.494962215423584})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.42993277311325073})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.347558856010437})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.305133581161499})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.29112446308135986})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28786733746528625})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3179152309894562})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.27576422691345215})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32136034965515137})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31541234254837036})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29303765296936035})
store['active_learning_steps'][76]['training']['best_epoch']=9
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9694, 'crossentropy': 0.2464085693359375}
store['active_learning_steps'][76]['acquisition']={'indices': [['id', 17382], ['id', 52086], ['id', 34847], ['id', 57628], ['id', 51759]], 'labels': [6, 5, 0, 2, 3], 'scores': [0.8542720675468445, 0.7396330237388611, 0.7290368676185608, 0.8177967667579651, 0.7889978885650635]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.1230841875076294})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.6081457138061523})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.42220839858055115})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34827128052711487})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.31539130210876465})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3104163706302643})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30823004245758057})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3352435231208801})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32865065336227417})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28182852268218994})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32887566089630127})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3103073239326477})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3277026414871216})
store['active_learning_steps'][77]['training']['best_epoch']=10
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9705, 'crossentropy': 0.245013427734375}
store['active_learning_steps'][77]['acquisition']={'indices': [['id', 12630], ['id', 6606], ['id', 56842], ['id', 7833], ['id', 36744]], 'labels': [8, 8, 8, 5, 1], 'scores': [0.6763095259666443, 0.7321078181266785, 0.691311240196228, 0.622820258140564, 0.9385309815406799]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 1.0840356349945068})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5170004367828369})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.44541680812835693})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3521259129047394})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2988755702972412})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2712453603744507})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3117446303367615})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.30536192655563354})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3016374409198761})
store['active_learning_steps'][78]['training']['best_epoch']=6
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9704, 'crossentropy': 0.2480136474609375}
store['active_learning_steps'][78]['acquisition']={'indices': [['id', 36337], ['id', 40364], ['id', 18042], ['id', 38195], ['id', 14649]], 'labels': [3, 8, 0, 2, 0], 'scores': [0.734396755695343, 0.693474292755127, 0.7039053440093994, 0.6781318187713623, 0.8331552147865295]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.1224892139434814})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5486195683479309})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4011284112930298})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3847457766532898})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32545268535614014})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3147215247154236})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2861870527267456})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3247249722480774})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29878681898117065})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.29602378606796265})
store['active_learning_steps'][79]['training']['best_epoch']=7
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9656, 'crossentropy': 0.26236884765625}
store['active_learning_steps'][79]['acquisition']={'indices': [['id', 59664], ['id', 5600], ['id', 23578], ['ood', 16638], ['id', 41540]], 'labels': [7, 6, 2, 5, 2], 'scores': [0.6877046823501587, 0.6356668472290039, 0.7389971017837524, 0.4303826093673706, 0.7752901017665863]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.2478195428848267})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6847507953643799})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4240584969520569})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3736584186553955})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.33301112055778503})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.30011677742004395})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3384086489677429})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2890620231628418})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2761286199092865})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2923843562602997})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3096798062324524})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2901364862918854})
store['active_learning_steps'][80]['training']['best_epoch']=9
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.9679, 'crossentropy': 0.258930419921875}
store['active_learning_steps'][80]['acquisition']={'indices': [['id', 8202], ['id', 31934], ['id', 42472], ['id', 52566], ['id', 37489]], 'labels': [2, 9, 2, 4, 2], 'scores': [0.8741708397865295, 0.7667768001556396, 0.7561860680580139, 0.7414968013763428, 0.6455258131027222]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.1660058498382568})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5299957990646362})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.39128267765045166})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3570323884487152})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.28738126158714294})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2779415249824524})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.268804132938385})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.26687079668045044})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2870396375656128})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.27856460213661194})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2881155014038086})
store['active_learning_steps'][81]['training']['best_epoch']=8
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9655, 'crossentropy': 0.2530531005859375}
store['active_learning_steps'][81]['acquisition']={'indices': [['id', 6348], ['id', 47383], ['id', 46524], ['id', 19702], ['id', 49624]], 'labels': [2, 6, 6, 5, 6], 'scores': [0.6876466870307922, 0.8563200235366821, 0.6871498227119446, 0.9271711111068726, 0.9006838202476501]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.0897554159164429})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5777239799499512})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4083143472671509})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3378581404685974})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.33071428537368774})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3023207187652588})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.29152727127075195})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2569792568683624})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29162949323654175})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2591991424560547})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2669760286808014})
store['active_learning_steps'][82]['training']['best_epoch']=8
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9687, 'crossentropy': 0.235099755859375}
store['active_learning_steps'][82]['acquisition']={'indices': [['id', 38960], ['id', 27732], ['id', 44737], ['id', 32507], ['id', 45099]], 'labels': [4, 9, 7, 5, 2], 'scores': [0.667559027671814, 0.5386325716972351, 0.7029550075531006, 0.6192596256732941, 0.5387099981307983]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.1560230255126953})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5572545528411865})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.43597397208213806})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3494754135608673})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29830390214920044})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.282447874546051})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.29349076747894287})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26492634415626526})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.26558738946914673})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27727818489074707})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26905161142349243})
store['active_learning_steps'][83]['training']['best_epoch']=8
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9678, 'crossentropy': 0.243586669921875}
store['active_learning_steps'][83]['acquisition']={'indices': [['id', 57985], ['id', 39778], ['id', 11292], ['id', 27358], ['id', 24728]], 'labels': [4, 8, 1, 8, 2], 'scores': [0.6178369522094727, 0.8594377040863037, 0.903158962726593, 0.6618175506591797, 0.7518589496612549]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.2914800643920898})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6532981395721436})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4453394114971161})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.35671311616897583})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3225829005241394})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2949868440628052})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3047071099281311})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27346980571746826})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2895318269729614})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2639046609401703})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28116458654403687})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2867610454559326})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32491323351860046})
store['active_learning_steps'][84]['training']['best_epoch']=10
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9727, 'crossentropy': 0.24103447265625}
store['active_learning_steps'][84]['acquisition']={'indices': [['id', 36822], ['id', 39899], ['id', 57054], ['id', 53930], ['id', 26376]], 'labels': [1, 2, 8, 1, 1], 'scores': [0.8326696753501892, 0.698013186454773, 0.7196044325828552, 0.49541378021240234, 0.7501435279846191]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.9786484241485596})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.5034854412078857})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.39630669355392456})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3471965789794922})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2872963547706604})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27875208854675293})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.289225310087204})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.27638864517211914})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2606106400489807})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.26980826258659363})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.26415860652923584})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2669873833656311})
store['active_learning_steps'][85]['training']['best_epoch']=9
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9709, 'crossentropy': 0.2251644775390625}
store['active_learning_steps'][85]['acquisition']={'indices': [['id', 30159], ['id', 54371], ['id', 4185], ['id', 47283], ['id', 25034]], 'labels': [3, 0, 2, 8, 3], 'scores': [0.6585625410079956, 0.720777153968811, 0.7064160108566284, 0.6968815624713898, 0.6066167652606964]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.2654531002044678})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.6378544569015503})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.40153247117996216})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3497977554798126})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30585044622421265})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2665887475013733})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.26383817195892334})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2622515559196472})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.25897642970085144})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2847755551338196})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2426372766494751})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2727716565132141})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2689363956451416})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2730565071105957})
store['active_learning_steps'][86]['training']['best_epoch']=11
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.9693, 'crossentropy': 0.245711474609375}
