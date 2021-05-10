store = {}
store['timestamp']=1620295342
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=9']
store['commit']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['github_url']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=9
store['worker_id']=9
store['num_workers']=40
store['config']={'seed': 11, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.BALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.599018096923828})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.039743423461914})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.129556179046631})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.5468454360961914})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6579, 'crossentropy': 2.2578328125}
store['active_learning_steps'][0]['acquisition']={'indices': [56777, 56775, 36475, 542, 9460, 44808, 3720, 12066, 53581, 37973], 'labels': [0, 0, 2, 0, 6, 6, 0, 8, 6, 6], 'scores': [1.1054804921150208, 1.100633144378662, 1.0805630683898926, 1.0640351176261902, 1.0621779561042786, 1.0584089756011963, 1.0580492615699768, 1.0564783811569214, 1.0555649995803833, 1.049207091331482]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.1133906841278076})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.0793027877807617})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.8963894844055176})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.835963726043701})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.656, 'crossentropy': 2.09192421875}
store['active_learning_steps'][1]['acquisition']={'indices': [4606, 5062, 52538, 19942, 36661, 3704, 36492, 48712, 34550, 58437], 'labels': [9, 9, 9, 5, 5, 9, 8, 7, 4, 9], 'scores': [1.1191656589508057, 1.0786522030830383, 1.0753495693206787, 1.072994589805603, 1.0676466226577759, 1.0667533874511719, 1.065949261188507, 1.060628890991211, 1.0506132245063782, 1.0456827282905579]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.8267462253570557})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.0446419715881348})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.2495951652526855})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.18554425239563})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6773, 'crossentropy': 1.6641560546875}
store['active_learning_steps'][2]['acquisition']={'indices': [3370, 28253, 25960, 22083, 22169, 11852, 12327, 12497, 45199, 40766], 'labels': [4, 4, 4, 2, 2, 4, 4, 0, 8, 4], 'scores': [1.0914248824119568, 1.08242267370224, 1.0337038040161133, 1.0213682651519775, 1.0081281065940857, 1.0060235857963562, 1.0039090514183044, 1.0023114681243896, 1.0014033317565918, 0.9996628165245056]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.4739784002304077})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 2.0632448196411133})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.9097051620483398})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 2.017717123031616})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7482, 'crossentropy': 1.3608068359375}
store['active_learning_steps'][3]['acquisition']={'indices': [47322, 14113, 46620, 59447, 4745, 4679, 1861, 18972, 27264, 27972], 'labels': [8, 2, 2, 8, 8, 2, 2, 2, 2, 8], 'scores': [0.9914929866790771, 0.9852344393730164, 0.9742459058761597, 0.9738348722457886, 0.96632981300354, 0.9542650580406189, 0.9534896612167358, 0.9421476125717163, 0.931236982345581, 0.9294438362121582]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.3367743492126465})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.544785976409912})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.7989146709442139})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.9261109828948975})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7339, 'crossentropy': 1.3151529296875}
store['active_learning_steps'][4]['acquisition']={'indices': [20050, 49624, 31090, 24587, 45800, 6175, 55390, 29289, 17010, 27108], 'labels': [9, 6, 4, 8, 9, 3, 6, 3, 3, 2], 'scores': [0.9274281859397888, 0.9033491015434265, 0.8973804712295532, 0.8798990845680237, 0.8782634139060974, 0.8710300922393799, 0.8698515892028809, 0.8687979578971863, 0.8687944412231445, 0.868270993232727]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.3211772441864014})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.57428777217865})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.7699053287506104})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.75227689743042})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7404, 'crossentropy': 1.2395697265625}
store['active_learning_steps'][5]['acquisition']={'indices': [53170, 14749, 6066, 17005, 12957, 25309, 8116, 51570, 8978, 27641], 'labels': [8, 0, 8, 1, 5, 2, 0, 6, 2, 2], 'scores': [0.8326870203018188, 0.8136162757873535, 0.8128117322921753, 0.8049466609954834, 0.7950464487075806, 0.7766791582107544, 0.770216703414917, 0.7669880390167236, 0.763512372970581, 0.7570778131484985]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.1871371269226074})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.5001113414764404})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.569455862045288})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.9447507858276367})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7738, 'crossentropy': 1.12813779296875}
store['active_learning_steps'][6]['acquisition']={'indices': [47787, 40492, 37439, 46727, 19298, 18782, 2571, 2856, 24107, 39103], 'labels': [2, 6, 3, 2, 6, 5, 5, 4, 5, 5], 'scores': [0.8315918445587158, 0.8280717134475708, 0.8071920871734619, 0.7942255139350891, 0.7919896245002747, 0.7914103269577026, 0.7912806868553162, 0.7888516187667847, 0.7869844436645508, 0.7853134870529175]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.2332861423492432})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.0813448429107666})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.3342297077178955})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.303666353225708})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.2617700099945068})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8329, 'crossentropy': 0.98614296875}
store['active_learning_steps'][7]['acquisition']={'indices': [20641, 51986, 37409, 7833, 50320, 35401, 3719, 34429, 58470, 13983], 'labels': [9, 2, 5, 5, 5, 3, 2, 4, 9, 3], 'scores': [1.0631829500198364, 1.046023428440094, 1.0142942070960999, 0.9831182360649109, 0.9773481488227844, 0.9671433568000793, 0.9629303812980652, 0.9566879868507385, 0.9513092041015625, 0.9475055932998657]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.1316092014312744})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.1817033290863037})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.2809324264526367})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.4083185195922852})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.7846, 'crossentropy': 1.01546240234375}
store['active_learning_steps'][8]['acquisition']={'indices': [28102, 49202, 38512, 11616, 47587, 49463, 12391, 56567, 58885, 17710], 'labels': [0, 5, 5, 7, 3, 0, 7, 7, 7, 3], 'scores': [0.7581751346588135, 0.7175825834274292, 0.7071837186813354, 0.7066651582717896, 0.7048709392547607, 0.6947813034057617, 0.6889729499816895, 0.6888260841369629, 0.6848506927490234, 0.6835131645202637]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.0243260860443115})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.086223840713501})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.06715989112854})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.1643753051757812})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.813, 'crossentropy': 0.936939453125}
store['active_learning_steps'][9]['acquisition']={'indices': [25004, 16909, 26434, 2209, 31736, 28366, 32427, 54573, 3524, 21164], 'labels': [2, 2, 2, 5, 6, 2, 0, 2, 6, 2], 'scores': [0.722787082195282, 0.7127537727355957, 0.709648609161377, 0.7077109217643738, 0.6932809948921204, 0.6863123178482056, 0.6861626505851746, 0.6729269027709961, 0.6701700687408447, 0.6588170528411865]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.0080139636993408})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.9253538846969604})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.075594186782837})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.127030611038208})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.2345001697540283})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8556, 'crossentropy': 0.810373095703125}
store['active_learning_steps'][10]['acquisition']={'indices': [56006, 27458, 5474, 44456, 17756, 38130, 16379, 49323, 29132, 30559], 'labels': [3, 2, 8, 3, 8, 3, 7, 8, 8, 8], 'scores': [0.8914812803268433, 0.887052595615387, 0.8792209625244141, 0.869525671005249, 0.8579418063163757, 0.853731632232666, 0.8264475464820862, 0.8230736255645752, 0.820639431476593, 0.819097101688385]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9620531797409058})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8238198757171631})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8330598473548889})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9225902557373047})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.0072083473205566})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8862, 'crossentropy': 0.682426318359375}
store['active_learning_steps'][11]['acquisition']={'indices': [37574, 49784, 39700, 47646, 10044, 49354, 11044, 52083, 31926, 49525], 'labels': [5, 5, 5, 5, 6, 0, 4, 2, 5, 8], 'scores': [0.9346405267715454, 0.893847644329071, 0.8744611740112305, 0.8679723739624023, 0.8627045750617981, 0.8558719158172607, 0.8546839356422424, 0.8485129475593567, 0.8474087715148926, 0.8453680276870728]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.1275867223739624})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8862267136573792})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8994335532188416})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9194598197937012})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.9920512437820435})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8594, 'crossentropy': 0.797269384765625}
store['active_learning_steps'][12]['acquisition']={'indices': [14722, 48102, 58560, 21598, 40308, 33505, 57270, 34765, 37984, 39305], 'labels': [0, 7, 0, 2, 7, 2, 2, 6, 7, 7], 'scores': [0.9563990235328674, 0.9071667194366455, 0.8775011301040649, 0.8636794090270996, 0.8600440621376038, 0.858322024345398, 0.8508580923080444, 0.840800404548645, 0.8405237197875977, 0.83445143699646]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.9614498615264893})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7156566381454468})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7375373244285583})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7602361440658569})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7777572870254517})
store['active_learning_steps'][13]['training']['best_epoch']=2
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8917, 'crossentropy': 0.6657763671875}
store['active_learning_steps'][13]['acquisition']={'indices': [43575, 59983, 3765, 11202, 41489, 59681, 51464, 34771, 18739, 54043], 'labels': [2, 2, 2, 9, 2, 0, 0, 0, 3, 2], 'scores': [0.9261014461517334, 0.8751070499420166, 0.854817271232605, 0.8542225956916809, 0.8446587324142456, 0.8366636037826538, 0.8336774706840515, 0.8256104588508606, 0.8204070925712585, 0.8193273544311523]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.0738555192947388})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7179502844810486})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7704067230224609})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.726875901222229})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8711111545562744})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8916, 'crossentropy': 0.66466474609375}
store['active_learning_steps'][14]['acquisition']={'indices': [34520, 26444, 34684, 4795, 46832, 22561, 31664, 56585, 50975, 1812], 'labels': [6, 1, 3, 3, 7, 6, 3, 3, 3, 4], 'scores': [0.8468130826950073, 0.796941876411438, 0.7880643606185913, 0.7800260186195374, 0.7791635990142822, 0.7692596912384033, 0.7643288373947144, 0.7610791325569153, 0.7567252516746521, 0.7538058757781982]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.9915472269058228})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7079788446426392})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6626244783401489})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7005816698074341})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7210406064987183})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.871324896812439})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9123, 'crossentropy': 0.60595107421875}
store['active_learning_steps'][15]['acquisition']={'indices': [22272, 12986, 17505, 10260, 17043, 59919, 21204, 21532, 49473, 53933], 'labels': [5, 5, 1, 3, 1, 1, 5, 5, 1, 8], 'scores': [0.9709151387214661, 0.9707600474357605, 0.9608365297317505, 0.9567863345146179, 0.9487510919570923, 0.94782555103302, 0.9424631595611572, 0.9419989585876465, 0.9252210259437561, 0.9249106645584106]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.9343349933624268})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6544373631477356})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.610724151134491})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5683293342590332})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5959715843200684})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6647465229034424})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.6076254844665527})
store['active_learning_steps'][16]['training']['best_epoch']=4
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9273, 'crossentropy': 0.550253125}
store['active_learning_steps'][16]['acquisition']={'indices': [39830, 43961, 37154, 2118, 134, 30884, 47936, 20169, 12211, 5129], 'labels': [1, 0, 1, 7, 1, 2, 8, 4, 3, 2], 'scores': [0.9561654329299927, 0.9226824045181274, 0.9129266738891602, 0.9084919691085815, 0.8973808884620667, 0.894495964050293, 0.8839665055274963, 0.8775877356529236, 0.876419723033905, 0.8750677108764648]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8651106357574463})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6372331976890564})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5311177372932434})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5623155236244202})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5443486571311951})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6084638237953186})
store['active_learning_steps'][17]['training']['best_epoch']=3
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9243, 'crossentropy': 0.505243994140625}
store['active_learning_steps'][17]['acquisition']={'indices': [22989, 2284, 2845, 11208, 9428, 52891, 2633, 27085, 59314, 42573], 'labels': [3, 9, 8, 9, 9, 3, 9, 8, 9, 7], 'scores': [0.9066897630691528, 0.8867702484130859, 0.8833452463150024, 0.8739032745361328, 0.862542450428009, 0.8565473556518555, 0.8554657697677612, 0.8387970328330994, 0.8271046280860901, 0.8255919218063354]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.971167802810669})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7193138599395752})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6290030479431152})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5776329040527344})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5871117115020752})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5970550775527954})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6564244031906128})
store['active_learning_steps'][18]['training']['best_epoch']=4
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9177, 'crossentropy': 0.561137646484375}
store['active_learning_steps'][18]['acquisition']={'indices': [44438, 54981, 1674, 12985, 42746, 5979, 424, 14787, 29879, 43000], 'labels': [9, 2, 9, 2, 2, 9, 9, 9, -1, 9], 'scores': [0.9537269473075867, 0.9401278495788574, 0.935687243938446, 0.933159589767456, 0.9319108128547668, 0.9202856421470642, 0.9184749722480774, 0.9116044044494629, 0.9072179198265076, 0.9052165746688843]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.0233352184295654})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6253395080566406})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5638177394866943})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5728851556777954})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5242767333984375})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.595808207988739})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5830922722816467})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6713647246360779})
store['active_learning_steps'][19]['training']['best_epoch']=5
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9141, 'crossentropy': 0.552973193359375}
store['active_learning_steps'][19]['acquisition']={'indices': [27637, 9472, 4185, 41608, 5684, 53155, 1075, 4822, 7207, 8958], 'labels': [-1, 2, 2, -1, 6, 8, 7, 4, 2, 3], 'scores': [0.9969623684883118, 0.9809995889663696, 0.970461368560791, 0.9659996032714844, 0.9441758394241333, 0.9321563243865967, 0.9222077131271362, 0.9180375933647156, 0.9147049188613892, 0.9145286679267883]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.0653858184814453})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6544528007507324})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5588573813438416})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6000651717185974})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5966585874557495})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.525982677936554})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.55443274974823})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5718951225280762})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6699011921882629})
store['active_learning_steps'][20]['training']['best_epoch']=6
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9239, 'crossentropy': 0.532315283203125}
store['active_learning_steps'][20]['acquisition']={'indices': [49890, 1518, 50736, 13524, 7949, 44570, 42415, 50916, 48360, 39208], 'labels': [5, 9, -1, 3, -1, 7, 7, 4, 3, 5], 'scores': [1.0630853772163391, 1.058877408504486, 1.0426397919654846, 1.0204588174819946, 1.0107362866401672, 1.0035039186477661, 1.001076579093933, 0.9915054440498352, 0.9849315285682678, 0.9828268885612488]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.092308759689331})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6943504810333252})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6071563959121704})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.540956974029541})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5945713520050049})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5432003736495972})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5739414691925049})
store['active_learning_steps'][21]['training']['best_epoch']=4
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9275, 'crossentropy': 0.51735830078125}
store['active_learning_steps'][21]['acquisition']={'indices': [51842, 32504, 52697, 31301, 2548, 18654, 52889, 31456, 33426, 43532], 'labels': [9, 9, 3, 5, 4, 4, -1, 9, 4, 8], 'scores': [0.9570397734642029, 0.9122006893157959, 0.8744546175003052, 0.8740020990371704, 0.8574211001396179, 0.8538564443588257, 0.8460884094238281, 0.8435859680175781, 0.8419197201728821, 0.8362006545066833]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.023097276687622})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5573609471321106})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.48074808716773987})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5050128102302551})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5589912533760071})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5055150389671326})
store['active_learning_steps'][22]['training']['best_epoch']=3
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9257, 'crossentropy': 0.481035986328125}
store['active_learning_steps'][22]['acquisition']={'indices': [11708, 32511, 37347, 59747, 37469, 39999, 32519, 29723, 32323, 55442], 'labels': [3, 5, 2, 5, 2, 5, 5, 5, 5, 5], 'scores': [0.8587071895599365, 0.8529300689697266, 0.8477182984352112, 0.8425239324569702, 0.8225460052490234, 0.8201366662979126, 0.8043226599693298, 0.7997262477874756, 0.7950100302696228, 0.7906800508499146]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.0611116886138916})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5969069004058838})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.549669623374939})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.49265632033348083})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5180056095123291})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.478790819644928})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5030142068862915})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5257292985916138})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4953000843524933})
store['active_learning_steps'][23]['training']['best_epoch']=6
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9368, 'crossentropy': 0.470024072265625}
store['active_learning_steps'][23]['acquisition']={'indices': [47140, 46021, 32776, 57714, 7949, 41933, 14878, 50736, 18324, 32880], 'labels': [3, 9, 4, 1, -1, 5, 3, -1, 0, 0], 'scores': [1.0755462050437927, 1.0501831769943237, 1.0297383069992065, 1.0206299424171448, 1.014508068561554, 1.0066276788711548, 1.0043730735778809, 1.0026922821998596, 0.9914419054985046, 0.9857799410820007]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.1044774055480957})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6056384444236755})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6019587516784668})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5660740733146667})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6010228395462036})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5321844816207886})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5678498148918152})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6189258098602295})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5672965049743652})
store['active_learning_steps'][24]['training']['best_epoch']=6
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9312, 'crossentropy': 0.51715}
store['active_learning_steps'][24]['acquisition']={'indices': [670, 59390, 641, 44736, 9778, 42139, 14337, 3676, 39778, 32276], 'labels': [3, 2, 9, 5, 3, 4, 7, 2, 8, 3], 'scores': [1.0589497685432434, 1.003243327140808, 0.9966173768043518, 0.982570469379425, 0.9740477800369263, 0.9649621248245239, 0.9505982398986816, 0.9490666389465332, 0.9479582905769348, 0.9429016709327698]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.007462739944458})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5468015074729919})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4831247329711914})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4643939733505249})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4471832513809204})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.47172990441322327})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.49106448888778687})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.47737202048301697})
store['active_learning_steps'][25]['training']['best_epoch']=5
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9335, 'crossentropy': 0.442939013671875}
store['active_learning_steps'][25]['acquisition']={'indices': [53872, 7768, 23350, 26266, 57383, 43648, 47626, 23112, 43226, 16882], 'labels': [8, 8, 8, 7, 5, 5, -1, 8, 8, 7], 'scores': [0.9623696804046631, 0.9149847030639648, 0.908525288105011, 0.9074306488037109, 0.9043960571289062, 0.8945964574813843, 0.8938028216362, 0.8841751217842102, 0.8839776515960693, 0.8657004833221436]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.0954959392547607})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.599675714969635})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5242396593093872})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.506555438041687})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4689266085624695})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.488877534866333})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.45952439308166504})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.49618130922317505})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5371840000152588})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5524023771286011})
store['active_learning_steps'][26]['training']['best_epoch']=7
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9399, 'crossentropy': 0.442710546875}
store['active_learning_steps'][26]['acquisition']={'indices': [7949, 32668, 37219, 28536, 29899, 50736, 1214, 13942, 45658, 23734], 'labels': [-1, 9, 8, 3, 3, -1, 8, 4, 3, 5], 'scores': [1.07863450050354, 1.0782489776611328, 1.0567044019699097, 1.0286739468574524, 1.028204321861267, 1.0208644270896912, 1.019532322883606, 1.0076653957366943, 1.0042527914047241, 1.0038602948188782]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.216831922531128})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6279913187026978})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4439537525177002})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.447246789932251})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.45010221004486084})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4399232864379883})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.457937091588974})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4328467547893524})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4097132682800293})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4675157070159912})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.45906099677085876})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.45789796113967896})
store['active_learning_steps'][27]['training']['best_epoch']=9
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9469, 'crossentropy': 0.429664599609375}
store['active_learning_steps'][27]['acquisition']={'indices': [7168, 38920, 35246, 15723, 43823, 45666, 54498, 56773, 5789, 53979], 'labels': [8, 7, 8, 8, 8, 1, 8, 9, -1, 8], 'scores': [1.17055743932724, 1.0733410716056824, 1.0518155694007874, 1.0468628406524658, 1.0396742820739746, 1.0330501198768616, 1.0278770327568054, 1.017213761806488, 1.0107543468475342, 1.0099835991859436]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.3023064136505127})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.67402184009552})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4503926634788513})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.42274633049964905})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4472842514514923})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5053998231887817})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.41550570726394653})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4211059510707855})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4311088025569916})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4569351077079773})
store['active_learning_steps'][28]['training']['best_epoch']=7
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9398, 'crossentropy': 0.414782861328125}
store['active_learning_steps'][28]['acquisition']={'indices': [20206, 23494, 45424, 28512, 2381, 2342, 19089, 41119, 2765, 18460], 'labels': [7, 2, 4, 5, 7, 2, 5, -1, 0, 2], 'scores': [1.1230579018592834, 1.0527926683425903, 1.0473602414131165, 1.030620813369751, 0.9995946288108826, 0.9923712015151978, 0.9859859943389893, 0.9778159260749817, 0.977749764919281, 0.9574589729309082]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.1939222812652588})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6273198127746582})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.475349485874176})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.46490567922592163})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.43848222494125366})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.44954201579093933})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4257647395133972})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.43368032574653625})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4330664873123169})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.41064295172691345})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5408357381820679})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4773889183998108})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5130355358123779})
store['active_learning_steps'][29]['training']['best_epoch']=10
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9547, 'crossentropy': 0.402649951171875}
store['active_learning_steps'][29]['acquisition']={'indices': [1477, 18598, 16969, 54195, 36744, 21287, 38275, 4205, 52661, 4955], 'labels': [4, 9, 4, 8, 1, 4, 2, 4, 3, 2], 'scores': [1.081285834312439, 1.0602938532829285, 1.0447184443473816, 1.0434022843837738, 1.0297051072120667, 1.0288966298103333, 1.0176312923431396, 1.0108014941215515, 1.0090696811676025, 1.0032883286476135]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.196587085723877})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6345874071121216})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5353615880012512})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.44908657670021057})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4505777657032013})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.47569072246551514})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4630420207977295})
store['active_learning_steps'][30]['training']['best_epoch']=4
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9404, 'crossentropy': 0.4306876953125}
store['active_learning_steps'][30]['acquisition']={'indices': [1239, 44267, 9180, 1642, 37315, 31293, 40466, 46441, 47401, 57728], 'labels': [8, 8, 3, 6, 6, 8, 8, 6, 8, 9], 'scores': [0.8374543190002441, 0.8138375878334045, 0.8125044703483582, 0.8114567399024963, 0.8032979369163513, 0.7996461391448975, 0.7923712730407715, 0.7897078394889832, 0.7787027359008789, 0.7779322862625122]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.258018970489502})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.684762179851532})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.500660240650177})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4295857548713684})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3991028070449829})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.41538307070732117})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.38737228512763977})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.41451460123062134})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4174327254295349})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.39854446053504944})
store['active_learning_steps'][31]['training']['best_epoch']=7
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9488, 'crossentropy': 0.407379736328125}
store['active_learning_steps'][31]['acquisition']={'indices': [21636, 16286, 34328, 50090, 6269, 48492, 24479, 42438, 20792, 58024], 'labels': [2, 0, 8, 4, 3, 6, 8, 9, 9, 8], 'scores': [1.0302022695541382, 0.9809567332267761, 0.9477594494819641, 0.9435577392578125, 0.9411630034446716, 0.9407286643981934, 0.9184242486953735, 0.9151003360748291, 0.9108779430389404, 0.9084786176681519]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.2653470039367676})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6247646808624268})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5021270513534546})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4359590411186218})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.40243297815322876})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.41418033838272095})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.37862855195999146})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.39451032876968384})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3934211730957031})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.37646037340164185})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.4190003275871277})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4456269145011902})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.44539421796798706})
store['active_learning_steps'][32]['training']['best_epoch']=10
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9584, 'crossentropy': 0.386003857421875}
store['active_learning_steps'][32]['acquisition']={'indices': [33752, 37583, 52889, 56082, 12184, 47286, 28930, 55438, 44698, 53990], 'labels': [1, -1, -1, 8, 0, -1, 7, 8, 1, -1], 'scores': [1.0635443329811096, 1.0569697618484497, 1.0292598009109497, 1.0205859541893005, 1.0199385285377502, 1.0185221433639526, 1.009342908859253, 1.009212613105774, 1.0082489848136902, 1.0053158402442932]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.2965799570083618})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6565366387367249})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.49632370471954346})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3786512017250061})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.35466307401657104})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3722170293331146})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35863369703292847})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.34370511770248413})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.34271615743637085})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3689973056316376})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3313141465187073})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3329489827156067})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3460496664047241})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3941531777381897})
store['active_learning_steps'][33]['training']['best_epoch']=11
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9603, 'crossentropy': 0.3571432861328125}
store['active_learning_steps'][33]['acquisition']={'indices': [29320, 34639, 30897, 49487, 55906, 36704, 59460, 32047, 49242, 15771], 'labels': [1, 0, 3, 8, 2, 2, 1, 9, 7, 5], 'scores': [1.075341820716858, 1.0638036727905273, 1.0233415961265564, 1.0206496119499207, 1.0119336247444153, 1.0113487541675568, 1.0050818920135498, 0.9976636171340942, 0.9962062239646912, 0.9928045868873596]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.2993292808532715})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7240680456161499})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.535240113735199})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.4006868004798889})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3895072340965271})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4230738878250122})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.37013065814971924})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4295671582221985})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4266403317451477})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.38653692603111267})
store['active_learning_steps'][34]['training']['best_epoch']=7
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9479, 'crossentropy': 0.383192138671875}
store['active_learning_steps'][34]['acquisition']={'indices': [20172, 37696, 43176, 22550, 39561, 22053, 48681, 4784, 58832, 3794], 'labels': [4, 2, 2, 6, 2, 5, 2, 7, 3, 6], 'scores': [0.9615360498428345, 0.9496502876281738, 0.9475100040435791, 0.9266743063926697, 0.8845515251159668, 0.8752356171607971, 0.8642261028289795, 0.8577095866203308, 0.8528050780296326, 0.8521752953529358]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.3769629001617432})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7338529825210571})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5032018423080444})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3856915533542633})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.36574506759643555})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3532722592353821})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3528591990470886})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3512018918991089})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3603678345680237})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3826523721218109})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34174174070358276})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3469031751155853})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4244757890701294})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4060555398464203})
store['active_learning_steps'][35]['training']['best_epoch']=11
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9583, 'crossentropy': 0.33703798828125}
store['active_learning_steps'][35]['acquisition']={'indices': [47626, 31014, 49515, 4153, 4564, 31958, 42673, 360, 29185, 50425], 'labels': [-1, -1, 2, 2, -1, -1, -1, -1, 3, -1], 'scores': [0.9895932078361511, 0.9891668558120728, 0.9875534772872925, 0.9843491911888123, 0.9810585975646973, 0.9795100688934326, 0.9745738506317139, 0.9684354066848755, 0.9650727212429047, 0.9608066082000732]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.3103331327438354})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6728463172912598})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4446325898170471})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3529818058013916})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.37871649861335754})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3432387411594391})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31935256719589233})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3371618986129761})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3496299982070923})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.342297226190567})
store['active_learning_steps'][36]['training']['best_epoch']=7
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9619, 'crossentropy': 0.307756494140625}
store['active_learning_steps'][36]['acquisition']={'indices': [4741, 51863, 20005, 9687, 6574, 57026, 17603, 7949, 57718, 34665], 'labels': [6, 9, 6, 0, -1, 4, 0, -1, 7, 9], 'scores': [0.9582836627960205, 0.9106787443161011, 0.8927179872989655, 0.8907490968704224, 0.8889836668968201, 0.8852980136871338, 0.8852081894874573, 0.8658883571624756, 0.8617677092552185, 0.8603208065032959]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.3115581274032593})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6996382474899292})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.534447193145752})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.45137953758239746})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.42414379119873047})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.358634889125824})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33609557151794434})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.37377139925956726})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35804930329322815})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33506083488464355})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.39170414209365845})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.37252217531204224})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3740028142929077})
store['active_learning_steps'][37]['training']['best_epoch']=10
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9629, 'crossentropy': 0.3398847412109375}
store['active_learning_steps'][37]['acquisition']={'indices': [54950, 17712, 43745, 52808, 13969, 635, 26358, 56014, 54030, 12305], 'labels': [8, 3, 8, 8, 3, 5, 3, 5, 8, 9], 'scores': [1.060101866722107, 1.0451598167419434, 1.0346747636795044, 1.0038596391677856, 0.9913430213928223, 0.9744578003883362, 0.966453492641449, 0.9501204490661621, 0.9471074342727661, 0.9451636672019958]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.3667925596237183})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5991652011871338})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.42865967750549316})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4414878785610199})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3441154360771179})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3789854347705841})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.39375609159469604})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3473256230354309})
store['active_learning_steps'][38]['training']['best_epoch']=5
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9641, 'crossentropy': 0.32213505859375}
store['active_learning_steps'][38]['acquisition']={'indices': [52889, 45602, 52294, 43126, 37583, 18003, 1935, 25624, 59980, 22139], 'labels': [-1, 5, 0, 3, -1, 2, 3, -1, 3, 2], 'scores': [0.9728012681007385, 0.9441657066345215, 0.9034340381622314, 0.9002498388290405, 0.8858785629272461, 0.8653401136398315, 0.848443865776062, 0.8454373478889465, 0.8261754512786865, 0.8250173330307007]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.3339189291000366})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.6838891506195068})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.444296658039093})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.363132119178772})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.35737550258636475})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.35488706827163696})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4055992364883423})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3418145179748535})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.26384085416793823})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3162574768066406})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.31011447310447693})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3403521180152893})
store['active_learning_steps'][39]['training']['best_epoch']=9
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9668, 'crossentropy': 0.2997654541015625}
store['active_learning_steps'][39]['acquisition']={'indices': [43206, 42336, 29376, 49910, 42703, 38223, 50250, 32784, 8228, 51236], 'labels': [5, -1, -1, 6, 0, -1, -1, 8, 3, -1], 'scores': [0.9373103380203247, 0.9250863790512085, 0.9226406812667847, 0.920982837677002, 0.9144837260246277, 0.89763343334198, 0.8776018619537354, 0.875917375087738, 0.8752191662788391, 0.8589078187942505]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.3761510848999023})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.7111476063728333})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4868925213813782})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4656258821487427})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3723451495170593})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.34544652700424194})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3315162658691406})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.32483160495758057})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3019028902053833})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.332294762134552})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.34194880723953247})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3320256471633911})
store['active_learning_steps'][40]['training']['best_epoch']=9
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9646, 'crossentropy': 0.3113470947265625}
store['active_learning_steps'][40]['acquisition']={'indices': [17079, 10064, 9118, 20150, 11074, 48382, 40530, 48356, 40654, 37161], 'labels': [6, 8, 9, 3, 9, 8, 2, 2, 5, 3], 'scores': [1.046739101409912, 0.9733999967575073, 0.9532954096794128, 0.9389665126800537, 0.9070963859558105, 0.905402660369873, 0.8957560658454895, 0.8947453498840332, 0.8926393985748291, 0.8884729146957397]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.509312629699707})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.7042769193649292})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.49569791555404663})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4150940775871277})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.42183467745780945})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3500264585018158})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3446526527404785})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.38227543234825134})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.382193386554718})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3541581630706787})
store['active_learning_steps'][41]['training']['best_epoch']=7
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9608, 'crossentropy': 0.355681982421875}
store['active_learning_steps'][41]['acquisition']={'indices': [52358, 48880, 47626, 43626, 7984, 42078, 55490, 10982, 7949, 33614], 'labels': [2, 4, -1, 4, 4, 4, 4, 1, -1, 4], 'scores': [0.9298346042633057, 0.867938756942749, 0.8674726486206055, 0.8582801818847656, 0.8553194999694824, 0.8527994155883789, 0.8499998450279236, 0.8340227007865906, 0.8286890387535095, 0.8168360590934753]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.403583288192749})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7714248895645142})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.5389126539230347})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.390585333108902})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.35874927043914795})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.33914053440093994})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.32643699645996094})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3586932420730591})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35054725408554077})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.32235682010650635})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3306315541267395})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32948756217956543})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.33102279901504517})
store['active_learning_steps'][42]['training']['best_epoch']=10
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9669, 'crossentropy': 0.3149069580078125}
store['active_learning_steps'][42]['acquisition']={'indices': [33812, 49616, 16731, 343, 56196, 48404, 30177, 33010, 38080, 37427], 'labels': [6, 7, -1, -1, -1, -1, 7, -1, 2, 2], 'scores': [1.0524336099624634, 1.0165457725524902, 1.0132701396942139, 0.9792348146438599, 0.9710184335708618, 0.968994677066803, 0.9666079878807068, 0.9649021029472351, 0.9493648409843445, 0.9482776522636414]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.2344837188720703})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.6263696551322937})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.454181045293808})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3983708620071411})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.38439565896987915})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.37487339973449707})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3787868916988373})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34225279092788696})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3263772130012512})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3467245101928711})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3585422933101654})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3222455680370331})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3682401776313782})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3578423857688904})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.33716779947280884})
store['active_learning_steps'][43]['training']['best_epoch']=12
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9661, 'crossentropy': 0.330175927734375}
store['active_learning_steps'][43]['acquisition']={'indices': [54885, 29360, 57507, 49192, 50639, 39877, 5265, 36126, 49563, 2574], 'labels': [6, 8, 0, 2, 8, 7, 4, 5, 8, -1], 'scores': [1.0622571110725403, 1.041037380695343, 1.039560079574585, 1.0325732827186584, 1.0068551301956177, 1.003789484500885, 0.9978578090667725, 0.9934471845626831, 0.9895056486129761, 0.9813729524612427]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.5284855365753174})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.6792349219322205})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.49261605739593506})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4372846484184265})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3613990545272827})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.32339566946029663})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3564015030860901})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3243657946586609})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3095057010650635})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.35376060009002686})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.32145535945892334})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3376542329788208})
store['active_learning_steps'][44]['training']['best_epoch']=9
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.9644, 'crossentropy': 0.311273291015625}
store['active_learning_steps'][44]['acquisition']={'indices': [46368, 16022, 49149, 4379, 53054, 53990, 59081, 36363, 52889, 47110], 'labels': [8, 8, 3, -1, -1, -1, -1, 6, -1, -1], 'scores': [1.030267983675003, 0.9985488653182983, 0.9729116559028625, 0.9675452709197998, 0.9532830715179443, 0.9373294115066528, 0.9305276870727539, 0.9276930689811707, 0.9274091124534607, 0.9142371416091919]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.4721081256866455})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.8246968984603882})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.49545109272003174})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4215031564235687})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.37204670906066895})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.41458651423454285})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.38378095626831055})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3876187205314636})
store['active_learning_steps'][45]['training']['best_epoch']=5
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.9619, 'crossentropy': 0.3544033935546875}
store['active_learning_steps'][45]['acquisition']={'indices': [10555, 32335, 14655, 48645, 57742, 4459, 52928, 53054, 35406, 59344], 'labels': [1, 1, 3, 1, 6, 9, 0, -1, 5, 9], 'scores': [0.8156133890151978, 0.8105470538139343, 0.7988119721412659, 0.7733540534973145, 0.761315107345581, 0.7597709894180298, 0.7548160552978516, 0.7546869516372681, 0.7445083856582642, 0.7442395091056824]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.208503007888794})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6919711828231812})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4512559771537781})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3796736001968384})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.356076180934906})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3172008991241455})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.32846155762672424})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.293939471244812})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.31438231468200684})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.275306761264801})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.31619811058044434})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.3058333098888397})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3087548017501831})
store['active_learning_steps'][46]['training']['best_epoch']=10
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.968, 'crossentropy': 0.3028242431640625}
store['active_learning_steps'][46]['acquisition']={'indices': [53873, 41789, 45944, 23463, 8902, 24860, 42838, 31919, 8932, 50403], 'labels': [4, 0, 9, 9, 9, 9, 9, 9, 0, 3], 'scores': [1.0111863613128662, 0.9967365860939026, 0.9601878523826599, 0.9489787220954895, 0.9418607354164124, 0.9415720105171204, 0.939434289932251, 0.9371161460876465, 0.9367364048957825, 0.9342731833457947]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.4593656063079834})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.7158340215682983})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5209673047065735})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3919903039932251})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32908499240875244})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.27299201488494873})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.294253408908844})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3191007971763611})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.30487799644470215})
store['active_learning_steps'][47]['training']['best_epoch']=6
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.9617, 'crossentropy': 0.309428369140625}
store['active_learning_steps'][47]['acquisition']={'indices': [52889, 52086, 53990, 8940, 35326, 29376, 15402, 36818, 42787, 32419], 'labels': [-1, 5, -1, 6, 5, -1, 5, 7, 4, 4], 'scores': [0.8342872262001038, 0.833473265171051, 0.8029298782348633, 0.8026037812232971, 0.8024855256080627, 0.7902608513832092, 0.7853031754493713, 0.7747660279273987, 0.7685295343399048, 0.759976863861084]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.3387506008148193})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.7711789608001709})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4322690963745117})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3844696283340454})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.35144367814064026})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3493673801422119})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.31957221031188965})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.31750166416168213})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3196636438369751})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3113744854927063})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3025655150413513})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.298240602016449})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.31503936648368835})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3343641459941864})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.34641164541244507})
store['active_learning_steps'][48]['training']['best_epoch']=12
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.9721, 'crossentropy': 0.3064087158203125}
store['active_learning_steps'][48]['acquisition']={'indices': [20578, 21601, 50274, 37583, 10256, 31345, 45443, 8680, 4762, 37450], 'labels': [8, 1, 8, -1, 2, 3, 5, 8, 3, 4], 'scores': [1.0575684309005737, 0.9914514422416687, 0.9891715049743652, 0.982474684715271, 0.973953127861023, 0.9544704556465149, 0.9422511458396912, 0.9388302862644196, 0.938782274723053, 0.921718955039978]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.5649652481079102})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7905497550964355})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4512583613395691})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3953309655189514})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.37222588062286377})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.35923510789871216})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.38948923349380493})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3598704934120178})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.32708993554115295})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3227226734161377})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33644357323646545})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33943045139312744})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.32376012206077576})
store['active_learning_steps'][49]['training']['best_epoch']=10
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.9695, 'crossentropy': 0.2966285888671875}
